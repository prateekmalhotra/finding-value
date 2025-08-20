import gspread
import yfinance as yf
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
import os.path
import time

# --- Configuration ---
# These scopes are required to read/write sheet data and metadata.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file"]
# The name of the Google Sheet file to update.
SPREADSHEET_NAME = "bullpen"

def authenticate_google_sheets():
    """Handles user authentication for Google Sheets."""
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    
    return gspread.authorize(creds)

def get_current_price(ticker: str) -> float | None:
    """Fetches the current stock price using yfinance as a numeric float."""
    if not ticker:
        return None
    try:
        stock = yf.Ticker(ticker)
        # Use 'regularMarketPrice' for live price, with a fallback to 'previousClose'
        price = stock.info.get('regularMarketPrice', stock.info.get('previousClose'))
        return float(price) if price else None
    except Exception as e:
        print(f"❌ Could not fetch price for {ticker}: {e}")
        return None

def main():
    """Main function to update stock prices in the Google Sheet."""
    print("Connecting to Google Sheets...")
    try:
        gc = authenticate_google_sheets()
        
        # Try to open the spreadsheet; exit if it doesn't exist.
        try:
            spreadsheet = gc.open(SPREADSHEET_NAME)
        except gspread.exceptions.SpreadsheetNotFound:
            print(f"❌ Error: The sheet '{SPREADSHEET_NAME}' was not found. Please run the main analysis script first to create it.")
            return

        worksheet = spreadsheet.sheet1
        print(f"Successfully connected to '{SPREADSHEET_NAME}'.")

        # Get all tickers from the first column (A)
        tickers_in_sheet = worksheet.col_values(1)

        if len(tickers_in_sheet) <= 1:
            print("No tickers found in the sheet to update.")
            return

        print(f"Found {len(tickers_in_sheet) - 1} stocks to update.")

        # Iterate through each ticker, skipping the header row (index 0)
        for index, ticker in enumerate(tickers_in_sheet[1:]):
            row_num = index + 2  # Sheet rows are 1-indexed, and we skip the header
            
            if not ticker.strip(): # Skip empty rows
                continue

            print(f"\n--- Processing {ticker} (Row {row_num}) ---")
            
            current_price = get_current_price(ticker)
            
            if current_price is not None:
                # Update the 'Current Value' column (B, which is the 2nd column)
                worksheet.update_cell(row_num, 2, current_price)
                print(f"✅ Updated {ticker} price to ${current_price:.2f}")
            else:
                print(f"⚠️  Skipping update for {ticker} due to fetch error.")

            # Add a small delay to avoid hitting API rate limits
            time.sleep(1)

        print(f"\n🎉 Price update complete for '{SPREADSHEET_NAME}'.")

    except gspread.exceptions.APIError as e:
        print(f"\n❌ A Google Sheets API error occurred: {e}")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()