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
SPREADSHEET_NAME = "bullpen"
MARGIN_OF_SAFETY = 0.30

def get_company_name(ticker: str) -> str | None:
    """Fetches the long name of a company as a string."""
    try:
        stock = yf.Ticker(ticker)
        # Access the 'longName' key from the info dictionary
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
    # FIX: The regex now looks for an optional hyphen '-?' at the beginning.
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
    
    # --- FIX 1: Changed endColumnIndex from 7 to 9 ---
    # This will apply the formatting to all 9 columns (A through I).
    add_requests = [
        # Rule 1 (Index 0): RED for overvalued (Current Value > 30% above Fair Value)
        {"addConditionalFormatRule": {"rule": {"ranges": [{"sheetId": worksheet.id, "startRowIndex": 1, "endRowIndex": 1000, "startColumnIndex": 0, "endColumnIndex": 11}], "booleanRule": {"condition": {"type": "CUSTOM_FORMULA", "values": [{"userEnteredValue": "=AND(ISNUMBER($B2), ISNUMBER($C2), $B2 > $C2 * 1.3)"}]}, "format": {"backgroundColor": {"red": 0.95, "green": 0.81, "blue": 0.81}}}}, "index": 0}},
        
        # Rule 2 (Index 1): GREEN for good value (Current Value < Entry Point)
        {"addConditionalFormatRule": {"rule": {"ranges": [{"sheetId": worksheet.id, "startRowIndex": 1, "endRowIndex": 1000, "startColumnIndex": 0, "endColumnIndex": 11}], "booleanRule": {"condition": {"type": "CUSTOM_FORMULA", "values": [{"userEnteredValue": "=AND(ISNUMBER($B2), ISNUMBER($D2), $B2 < $D2)"}]}, "format": {"backgroundColor": {"red": 0.81, "green": 0.92, "blue": 0.79}}}}, "index": 1}},
        
        # Rule 3 (Index 2): YELLOW for neutral/fair price (catches everything not red or green)
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

            print(f"\n--- Processing {ticker} ---")
            company_name = get_company_name(ticker)
            
            print(f"Analyzing valuation for {ticker}...")
            analysis_result = analyze_stock_valuation(ticker, company_name)
            valuation_reasoning = analysis_result.get("reasoning", "No reasoning provided.")
            
            print(f"Analyzing moat for {ticker}...")
            qualitative_result = analyze_qualitative_aspects(ticker, company_name)
            moat_rating = qualitative_result.get("final_answer", "N/A")
            moat_reasoning = qualitative_result.get("reasoning", "No reasoning provided.")

            print(f"Analyzing catalyst for {ticker}...")
            catalyst_result = analyze_catalysts(ticker, company_name)
            catalyst_rating = catalyst_result.get("final_answer", "N/A")
            catalyst_reasoning = catalyst_result.get("reasoning", "No reasoning provided.")

            print(f"Analyzing fisher qualitiative checklist for {ticker}...")
            fisher_result = analyze_fisher_qs(ticker, company_name)
            fisher_rating = fisher_result.get("final_answer", "N/A")
            fisher_reasoning = fisher_result.get("reasoning", "No reasoning provided.")

            print(f"Fetching current price for {ticker}...")
            current_price_val = get_current_price(ticker)
            
            fair_value_val = parse_price_from_string(analysis_result.get("final_answer"))
            
            entry_point_val = None
            if fair_value_val is not None:
                entry_point_val = fair_value_val * (1 - MARGIN_OF_SAFETY)

            new_row = [
                ticker, 
                current_price_val, 
                fair_value_val,    
                entry_point_val,
                moat_rating,
                catalyst_rating,
                fisher_rating
                valuation_reasoning,
                moat_reasoning,
                catalyst_reasoning,
                fisher_reasoning
            ]
            
            value_input_option = 'USER_ENTERED'
            
            try:
                row_index = all_tickers_in_sheet.index(ticker) + 1
                # --- FIX 2: Changed update range from G to I ---
                # This ensures all 9 columns are updated for existing rows.
                worksheet.update(f'A{row_index}:I{row_index}', [new_row], value_input_option=value_input_option)
                print(f"✅ Successfully updated row for {ticker}.")
            except ValueError:
                worksheet.append_row(new_row, value_input_option=value_input_option)
                all_tickers_in_sheet.append(ticker)
                print(f"✅ Successfully added new entry for {ticker}.")
            
            time.sleep(1) 

        print(f"\n🎉 All stocks have been processed and updated in '{SPREADSHEET_NAME}'.")

    except Exception as e:
        print(f"\n❌ An error occurred: {e}")


if __name__ == "__main__":
    load_dotenv()
    api_key = os.environ.get("GOOGLE_API_KEY")
    if api_key:
        genai.configure(api_key=api_key)
    main()