import argparse
# Note the relative import '.' which means "from the same package"
from .valuation import analyze_stock_valuation

def main():
    parser = argparse.ArgumentParser(description="Perform a stock valuation using the Gemini API.")
    parser.add_argument("ticker", type=str, help="The stock ticker symbol to analyze.")
    args = parser.parse_args()
    
    ticker_to_analyze = args.ticker

    print("--- Running Stock Valuation Analysis ---")
    print(f"\nAnalyzing {ticker_to_analyze.upper()}...")
    
    result = analyze_stock_valuation(ticker_to_analyze)

    if result:
        print("\n--- Full Reasoning ---")
        print(result.get("reasoning"))
        print("\n----------------------")
        
        final_answer = result.get("final_answer")
        if final_answer is not None:
            print(f"✅ Final Estimated Value: {final_answer.upper()}")
        else:
            print("⚠️ Final answer could not be extracted.")

    print("\n--- Analysis complete ---")

if __name__ == "__main__":
    main()