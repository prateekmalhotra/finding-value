import argparse
import gspread
import yfinance as yf
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
import os.path
import re
import time
import random
import google.generativeai as genai
from dotenv import load_dotenv
from io import BytesIO

# Import for GitHub
from github import Github, UnknownObjectException
import os

# Make sure these functions are correctly defined in your local package
from finding_value.valuation import analyze_stock_valuation, analyze_qualitative_aspects, analyze_catalysts, analyze_fisher_qs

SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
SPREADSHEET_NAME = "bullpen-2.0"
MARGIN_OF_SAFETY = 0.30
MAX_RETRIES = 3
RETRY_DELAY = 5

def save_text_to_github(repo, ticker, file_type, text_content):
    """Saves text content to a file in the specified GitHub repo."""
    filename = f"{ticker}_{file_type}.md"
    path = f"files/{ticker}/{filename}"
    commit_message = f"Add/Update {file_type} analysis for {ticker}"

    try:
        # Check if file exists
        contents = repo.get_contents(path)
        # If content is the same, skip update
        if contents.decoded_content.decode('utf-8') == text_content:
            print(f"    ↪ '{filename}' content unchanged. Skipping update.")
            return contents.html_url

        repo.update_file(contents.path, commit_message, text_content, contents.sha)
        print(f"    ↪ Updated '{filename}' in GitHub.")
        return contents.html_url
    except UnknownObjectException:
        # File does not exist, create it
        try:
            repo.create_file(path, commit_message, text_content)
            print(f"    ↪ Created '{filename}' in GitHub.")
            # Need to fetch the URL after creation
            new_contents = repo.get_contents(path)
            return new_contents.html_url
        except Exception as e:
            print(f"    ❌ Error creating file {path} in GitHub: {e}")
            raise
    except Exception as e:
        print(f"    ❌ Error interacting with GitHub for {path}: {e}")
        raise

def get_company_name(ticker: str) -> str | None:
    """Fetches the long name of a company as a string."""
    try:
        stock = yf.Ticker(ticker)
        name = stock.info.get('longName')
        return name if name else None
    except Exception as e:
        raise IOError(f"Could not fetch name for {ticker}: {e}") from e

def authenticate_google_sheets():
    """Handles user authentication for Google Sheets and returns credentials."""
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds

def get_current_price(ticker) -> float | None:
    """Fetches the current stock price as a numeric float."""
    try:
        stock = yf.Ticker(ticker)
        price = stock.info.get('regularMarketPrice', stock.info.get('previousClose'))
        return float(price) if price else None
    except Exception as e:
        raise IOError(f"Could not fetch price for {ticker}: {e}") from e

def parse_price_from_string(price_str: str) -> float | None:
    """Extracts a float value from a string (e.g., "-25 $" -> -25.0)."""
    if not price_str: return None
    match = re.search(r'(-?\d+\.?\d*)', price_str)
    return float(match.group(1)) if match else None

def set_conditional_formatting(worksheet):
    """
    Sets conditional formatting rules for the sheet ONLY if no rules already exist.
    """
    print("Checking for existing formatting rules...")
    try:
        sheet_metadata = worksheet.spreadsheet.fetch_sheet_metadata()
        for s in sheet_metadata.get('sheets', []):
            if s.get('properties', {}).get('sheetId') == worksheet.id:
                num_rules = len(s.get('conditionalFormats', []))
                if num_rules > 0:
                    print(f"✅ Found {num_rules} existing rules. Skipping format setup.")
                    return
                break
    except Exception as e:
        print(f"Warning: Could not fetch sheet metadata. Proceeding to add rules anyway. Error: {e}")

    print("No existing rules found. Adding new formatting rules...")
    add_requests = [
        {"addConditionalFormatRule": {"rule": {"ranges": [{"sheetId": worksheet.id, "startRowIndex": 1, "endRowIndex": 1000, "startColumnIndex": 0, "endColumnIndex": 11}], "booleanRule": {"condition": {"type": "CUSTOM_FORMULA", "values": [{"userEnteredValue": "=AND(ISNUMBER($B2), ISNUMBER($C2), $B2 > $C2 * 1.3)"}]}, "format": {"backgroundColor": {"red": 0.95, "green": 0.81, "blue": 0.81}}}}, "index": 0}},
        {"addConditionalFormatRule": {"rule": {"ranges": [{"sheetId": worksheet.id, "startRowIndex": 1, "endRowIndex": 1000, "startColumnIndex": 0, "endColumnIndex": 11}], "booleanRule": {"condition": {"type": "CUSTOM_FORMULA", "values": [{"userEnteredValue": "=AND(ISNUMBER($B2), ISNUMBER($D2), $B2 < $D2)"}]}, "format": {"backgroundColor": {"red": 0.81, "green": 0.92, "blue": 0.79}}}}, "index": 1}},
        {"addConditionalFormatRule": {"rule": {"ranges": [{"sheetId": worksheet.id, "startRowIndex": 1, "endRowIndex": 1000, "startColumnIndex": 0, "endColumnIndex": 11}], "booleanRule": {"condition": {"type": "CUSTOM_FORMULA", "values": [{"userEnteredValue": "=ISNUMBER($B2)"}]}, "format": {"backgroundColor": {"red": 1, "green": 0.94, "blue": 0.8}}}}, "index": 2}}
    ]
    body = {"requests": add_requests}
    worksheet.spreadsheet.batch_update(body)
    print("✅ New formatting rules added.")

def main():
    """Main function to run the valuation for multiple stocks and update the sheet."""
    parser = argparse.ArgumentParser(description="Analyze stocks from a file and write the results to a Google Sheet.")
    parser.add_argument("filename", type=str, help="The path to a text file containing stock tickers, one per line.")
    args = parser.parse_args()

    try:
        with open(args.filename, 'r') as f:
            tickers = [line.strip().upper() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"❌ Error: The file '{args.filename}' was not found.")
        return

    if not tickers:
        print("The file is empty. No stocks to process.")
        return

    random.shuffle(tickers)
    print(f"Found {len(tickers)} stocks to process: {', '.join(tickers)}")

    # Load GitHub credentials
    GITHUB_PAT = os.environ.get("GITHUB_PAT")
    GITHUB_REPO_NAME = os.environ.get("GITHUB_REPO_NAME")

    if not GITHUB_PAT:
        print("❌ Error: GITHUB_PAT environment variable not set.")
        return
    if not GITHUB_REPO_NAME:
        print("❌ Error: GITHUB_REPO_NAME environment variable not set (e.g., 'username/repo-name').")
        return

    print("\nConnecting to Google Sheets...")
    try:
        creds = authenticate_google_sheets()
        gc = gspread.authorize(creds)

        try:
            spreadsheet = gc.open(SPREADSHEET_NAME)
        except gspread.exceptions.SpreadsheetNotFound:
            print(f"Spreadsheet '{SPREADSHEET_NAME}' not found. Creating a new one...")
            spreadsheet = gc.create(SPREADSHEET_NAME)
            worksheet = spreadsheet.sheet1
            headers = ["Ticker", "Current Value", "Fair Value", "Entry Point", "Moat Rating", "Catalyst Rating", "Fisher Rating", "Valuation Reasoning", "Moat Reasoning", "Catalyst Reasoning", "Fisher Reasoning"]
            worksheet.append_row(headers)
            print("New sheet created with headers.")

        worksheet = spreadsheet.sheet1
        set_conditional_formatting(worksheet)

        print("\nConnecting to GitHub...")
        g = Github(GITHUB_PAT)
        repo = g.get_user().get_repo(GITHUB_REPO_NAME.split('/')[1])
        print(f"✅ Successfully connected to GitHub repo: {GITHUB_REPO_NAME}")

        all_tickers_in_sheet = worksheet.col_values(1)

        for ticker in tickers:
            if ticker in all_tickers_in_sheet:
                print(f"--- Skipping {ticker}, as it is already in the sheet. ---")
                continue

            try:
                print(f"\n--- Processing {ticker} ---")

                # Step 0: Get company name
                company_name = None
                for attempt in range(MAX_RETRIES):
                    try:
                        name = get_company_name(ticker)
                        if name:
                            company_name = name
                            break
                        raise ValueError("Fetched company name is empty.")
                    except Exception as e:
                        print(f"    ↪ Attempt {attempt + 1}/{MAX_RETRIES} to get company name failed: {e}")
                        if attempt < MAX_RETRIES - 1: time.sleep(RETRY_DELAY)
                if not company_name: raise ValueError("All attempts to get company name failed.")

                # Analysis Steps with retries (Valuation, Moat, Catalysts, Fisher)
                analysis_functions = {
                    "Valuation": analyze_stock_valuation,
                    "Moat": analyze_qualitative_aspects,
                    "Catalyst": analyze_catalysts,
                    "Fisher": analyze_fisher_qs,
                }
                results = {}
                for analysis_type, func in analysis_functions.items():
                    print(f"Analyzing {analysis_type} for {ticker}...")
                    result = None
                    for attempt in range(MAX_RETRIES):
                        try:
                            res = func(ticker, company_name)
                            if res.get("final_answer") and res.get("reasoning") != "NO RESPONSE" and res.get("final_answer") != "N/A":
                                result = res
                                break
                            raise ValueError(f"{analysis_type} analysis returned incomplete data.")
                        except Exception as e:
                            print(f"    ↪ Attempt {attempt + 1}/{MAX_RETRIES} for {analysis_type} failed: {e}")
                            if attempt < MAX_RETRIES - 1: time.sleep(RETRY_DELAY)
                    if not result: raise ValueError(f"All {analysis_type} attempts failed for {ticker}.")
                    results[analysis_type] = result
                    time.sleep(1) # Sleep between different analysis types

                # Step 5: Price
                current_price_val = None
                for attempt in range(MAX_RETRIES):
                    try:
                        price = get_current_price(ticker)
                        if price is not None:
                            current_price_val = price
                            break
                        raise ValueError("Fetched price is None.")
                    except Exception as e:
                        print(f"    ↪ Attempt {attempt + 1}/{MAX_RETRIES} for price failed: {e}")
                        if attempt < MAX_RETRIES - 1: time.sleep(RETRY_DELAY)
                if current_price_val is None: raise ValueError("All price fetching attempts failed.")

                # --- All steps succeeded ---
                fair_value_val = parse_price_from_string(results["Valuation"].get("final_answer"))
                moat_rating = results["Moat"].get("final_answer")
                catalyst_rating = results["Catalyst"].get("final_answer")
                fisher_rating = results["Fisher"].get("final_answer")

                print("    Uploading reasoning files to GitHub...")
                valuation_reasoning_url = save_text_to_github(repo, ticker, "valuation", results["Valuation"].get("reasoning"))
                moat_reasoning_url = save_text_to_github(repo, ticker, "moat", results["Moat"].get("reasoning"))
                catalyst_reasoning_url = save_text_to_github(repo, ticker, "catalyst", results["Catalyst"].get("reasoning"))
                fisher_reasoning_url = save_text_to_github(repo, ticker, "fisher", results["Fisher"].get("reasoning"))

                entry_point_val = fair_value_val * (1 - MARGIN_OF_SAFETY) if fair_value_val is not None else None

                new_row = [
                    ticker, current_price_val, fair_value_val, entry_point_val,
                    moat_rating, catalyst_rating, fisher_rating,
                    valuation_reasoning_url, moat_reasoning_url,
                    catalyst_reasoning_url, fisher_reasoning_url
                ]

                worksheet.append_row(new_row, value_input_option='USER_ENTERED')
                all_tickers_in_sheet.append(ticker)
                print(f"✅ Successfully added new entry for {ticker}.")
                time.sleep(2) # Sleep to avoid hitting API limits and allow GitHub to process

            except Exception as e:
                print(f"❌ Failed processing {ticker}: {e}. Skipping to next stock.")
                continue

        print(f"\n🎉 All stocks have been processed and updated in '{SPREADSHEET_NAME}'.")

    except Exception as e:
        print(f"\n❌ A critical error occurred during setup or sheet/GitHub interaction: {e}")

if __name__ == "__main__":
    load_dotenv()
    api_key = os.environ.get("GOOGLE_API_KEY")
    if api_key:
        genai.configure(api_key=api_key)
    else:
        print("Warning: GOOGLE_API_KEY not found in environment variables.")
    main()