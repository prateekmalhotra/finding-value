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

# Make sure these functions are correctly defined in your local package
from finding_value.valuation import analyze_stock_valuation, analyze_qualitative_aspects, analyze_catalysts, analyze_fisher_qs

SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file"]
SPREADSHEET_NAME = "bullpen-2.0"
MARGIN_OF_SAFETY = 0.30

def get_company_name(ticker: str) -> str | None:
    """Fetches the long name of a company as a string."""
    try:
        stock = yf.Ticker(ticker)
        name = stock.info.get('longName')
        return name if name else None
    except Exception as e:
        print(f"Could not fetch name for {ticker}: {e}")
        return None

def authenticate_google_sheets():
    """Handles user authentication for Google Sheets."""
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
    
    return gspread.authorize(creds)

def get_current_price(ticker) -> float | None:
    """Fetches the current stock price as a numeric float."""
    try:
        stock = yf.Ticker(ticker)
        price = stock.info.get('regularMarketPrice', stock.info.get('previousClose'))
        return float(price) if price else None
    except Exception as e:
        print(f"Could not fetch price for {ticker}: {e}")
        return None

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
    
    # Adjusted endColumnIndex to 11 to cover all columns A through K
    add_requests = [
        {"addConditionalFormatRule": {"rule": {"ranges": [{"sheetId": worksheet.id, "startRowIndex": 1, "endRowIndex": 1000, "startColumnIndex": 0, "endColumnIndex": 14}], "booleanRule": {"condition": {"type": "CUSTOM_FORMULA", "values": [{"userEnteredValue": "=AND(ISNUMBER($B2), ISNUMBER($C2), $B2 > $C2 * 1.3)"}]}, "format": {"backgroundColor": {"red": 0.95, "green": 0.81, "blue": 0.81}}}}, "index": 0}},
        {"addConditionalFormatRule": {"rule": {"ranges": [{"sheetId": worksheet.id, "startRowIndex": 1, "endRowIndex": 1000, "startColumnIndex": 0, "endColumnIndex": 14}], "booleanRule": {"condition": {"type": "CUSTOM_FORMULA", "values": [{"userEnteredValue": "=AND(ISNUMBER($B2), ISNUMBER($D2), $B2 < $D2)"}]}, "format": {"backgroundColor": {"red": 0.81, "green": 0.92, "blue": 0.79}}}}, "index": 1}},
        {"addConditionalFormatRule": {"rule": {"ranges": [{"sheetId": worksheet.id, "startRowIndex": 1, "endRowIndex": 1000, "startColumnIndex": 0, "endColumnIndex": 14}], "booleanRule": {"condition": {"type": "CUSTOM_FORMULA", "values": [{"userEnteredValue": "=ISNUMBER($B2)"}]}, "format": {"backgroundColor": {"red": 1, "green": 0.94, "blue": 0.8}}}}, "index": 2}}
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

    print("\nConnecting to Google Sheets...")
    try:
        gc = authenticate_google_sheets()
        
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
        
        all_tickers_in_sheet = worksheet.col_values(1)

        for ticker in tickers:
            if ticker in all_tickers_in_sheet:
                print(f"--- Skipping {ticker}, as it is already in the sheet. ---")
                continue
            
            # **MODIFICATION**: This entire block handles one ticker. If any step fails,
            # it raises an exception, which is caught below, and we `continue` to the next ticker.
            try:
                print(f"\n--- Processing {ticker} ---")
                company_name = get_company_name(ticker)
                if not company_name:
                    raise ValueError("Could not fetch company name.")

                # --- Step 1: Valuation ---
                print(f"Analyzing valuation for {ticker}...")
                analysis_result = analyze_stock_valuation(ticker, company_name)
                fair_value_val = parse_price_from_string(analysis_result.get("final_answer"))
                valuation_reasoning = analysis_result.get("reasoning", "No reasoning provided.")
                if fair_value_val is None or valuation_reasoning == "NO RESPONSE":
                    raise ValueError("Valuation analysis failed or returned incomplete data.")

                # --- Step 2: Moat ---
                print(f"Analyzing moat for {ticker}...")
                qualitative_result = analyze_qualitative_aspects(ticker, company_name)
                moat_rating = qualitative_result.get("final_answer", "N/A")
                moat_reasoning = qualitative_result.get("reasoning", "No reasoning provided.")
                if moat_rating == "N/A" or moat_reasoning == "NO RESPONSE":
                    raise ValueError("Moat analysis failed or returned incomplete data.")

                # --- Step 3: Catalysts ---
                print(f"Analyzing catalyst for {ticker}...")
                catalyst_result = analyze_catalysts(ticker, company_name)
                catalyst_rating = catalyst_result.get("final_answer", "N/A")
                catalyst_reasoning = catalyst_result.get("reasoning", "No reasoning provided.")
                if catalyst_rating == "N/A" or catalyst_reasoning == "NO RESPONSE":
                    raise ValueError("Catalyst analysis failed or returned incomplete data.")
                
                # --- Step 4: Fisher Checklist ---
                print(f"Analyzing fisher qualitative checklist for {ticker}...")
                fisher_result = analyze_fisher_qs(ticker, company_name)
                fisher_rating = fisher_result.get("final_answer", "N/A")
                fisher_reasoning = fisher_result.get("reasoning", "No reasoning provided.")
                if fisher_rating == "N/A" or fisher_reasoning == "NO RESPONSE":
                    raise ValueError("Fisher analysis failed or returned incomplete data.")

                # --- Step 5: Price & Final Calculations ---
                print(f"Fetching current price for {ticker}...")
                current_price_val = get_current_price(ticker)
                if current_price_val is None:
                    raise ValueError("Could not fetch current price.")
                
                entry_point_val = fair_value_val * (1 - MARGIN_OF_SAFETY)

                # --- All checks passed, prepare and write the row ---
                new_row = [
                    ticker, 
                    current_price_val, 
                    fair_value_val,    
                    entry_point_val,
                    moat_rating,
                    catalyst_rating,
                    fisher_rating,
                    valuation_reasoning,
                    moat_reasoning,
                    catalyst_reasoning,
                    fisher_reasoning
                ]
                
                value_input_option = 'USER_ENTERED'
                
                worksheet.append_row(new_row, value_input_option=value_input_option)
                all_tickers_in_sheet.append(ticker)
                print(f"✅ Successfully added new entry for {ticker}.")
                
                time.sleep(1) 

            except Exception as e:
                # This block catches ANY failure from the 'try' block above.
                print(f"❌ Failed processing {ticker}: {e}. Skipping to next stock.")
                continue # Move to the next ticker in the list

        print(f"\n🎉 All stocks have been processed and updated in '{SPREADSHEET_NAME}'.")

    except Exception as e:
        print(f"\n❌ A critical error occurred: {e}")


if __name__ == "__main__":
    load_dotenv()
    api_key = os.environ.get("GOOGLE_API_KEY")
    if api_key:
        genai.configure(api_key=api_key)
    main()