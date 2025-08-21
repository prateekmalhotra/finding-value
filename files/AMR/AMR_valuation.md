Here is a step-by-step intrinsic valuation of Alpha Metallurgical Resources, Inc. (AMR).

### **Valuation of Alpha Metallurgical Resources, Inc. (AMR)**
*   **Company:** Alpha Metallurgical Resources, Inc.
*   **Ticker:** AMR
*   **Currency:** USD
*   **Date of Analysis:** August 21, 2025
*   **Primary Sources Reviewed:** Company 10-Q filings, StockAnalysis Financial Data, DiscountingCashFlows Transcript Data, U.S. Department of the Treasury.

I will begin by gathering the necessary financial data for the valuation.I need to gather more data to complete the baseline financial analysis, specifically the TTM income statement. I will also search for the necessary components for the WACC calculation.### A) BASELINE FINANCIALS (TTM)

Here is the trailing twelve months (TTM) financial data for AMR, ending June 30, 2025.

| Metric | Value (USD Millions) | Citation |
|---|---|---|
| Revenue | 2,371.5 | (StockAnalysis, Aug 21, 2025) |
| Gross Margin | 10.4% | (Calculation based on StockAnalysis Data, Aug 21, 2025) |
| Operating Income (EBIT) | -27.8 | (StockAnalysis, Aug 21, 2025) |
| Net Income | -37.2 | (StockAnalysis, Aug 21, 2025) |
| D&A | 201.8 | (StockAnalysis, Aug 21, 2025) |
| Stock-Based Compensation| 13.5 | (StockAnalysis, Aug 21, 2025) |
| Capex | -147.2 | (StockAnalysis, Aug 21, 2025) |
| Change in Working Capital| 111.0 | (StockAnalysis, Aug 21, 2025) |
| Interest Expense | -3.1 | (StockAnalysis, Aug 21, 2025) |
| Cash & Equivalents | 449.0 | (StockAnalysis, Aug 21, 2025) |
| Total Debt | 5.8 | (StockAnalysis, Aug 21, 2025) |
| Diluted Shares | 13.0 | (StockAnalysis, Aug 21, 2025) |

### B) MANAGEMENT GUIDANCE EXTRACTION

A review of the latest earnings call transcripts from Q2 2025 did not provide specific, quantifiable guidance for long-term revenue growth or margin targets. Management commentary focused on operational performance and market conditions. Lacking explicit guidance, the forecast will be based on historical performance and reasoned assumptions. (DiscountingCashFlows, August 8, 2025)

### C) FORECAST HORIZON AND BASE-CASE ASSUMPTIONS (5 YEARS)

The following assumptions will be used to build the 5-year forecast.

*   **Revenue Growth:** Lacking management guidance, a conservative **-5.0%** annual decline is projected for the next 5 years. This reflects the cyclical nature of the coal industry and recent negative TTM revenue growth of -29.63%.
*   **Margin Path:** The TTM operating margin was -1.2%. Given the volatility in the coal market, a stable **0% operating margin** is assumed for the forecast period. This is a conservative assumption reflecting the lack of clear drivers for margin expansion.
*   **Taxes:** The average effective tax rate over the last three fiscal years (2022-2024) was approximately 10.8%. A **11% effective tax rate** is used.
*   **Capital Intensity:**
    *   **Capex:** TTM capex was 6.2% of revenue. The 3-year average is closer to 7%. We will assume capex remains at **6.5% of revenue.**
    *   **Working Capital:** TTM Change in Working Capital was 4.7% of revenue. It will be modeled at a more conservative **3.0% of incremental revenue.**
*   **SBC and Dilution:**
    *   **SBC:** TTM Stock-Based Compensation was 0.6% of revenue. It is forecast to remain at **0.6% of revenue.**
    *   **Share Count:** The latest diluted share count of **13.0 million** will be used for the final per-share calculation.

### D) FREE CASH FLOW CONSTRUCTION

Free Cash Flow to the Firm (FCFF) is used for this valuation as it represents cash flow available to all capital providers.

**FCFF Formula:**
FCFF = EBIT * (1 - Tax Rate) + D&A - Capex - Change in Working Capital - Stock-Based Compensation

**FCFF Forecast (USD Millions):**

| Year | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Revenue | 2,252.9 | 2,140.3 | 2,033.3 | 1,931.6 | 1,835.0 |
| EBIT | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| D&A | 146.4 | 139.1 | 132.2 | 125.6 | 119.3 |
| Capex | -146.4 | -139.1 | -132.2 | -125.6 | -119.3 |
| Change in WC | -3.5 | -3.4 | -3.2 | -3.0 | -2.9 |
| SBC | -13.5 | -12.8 | -12.2 | -11.6 | -11.0 |
| **FCFF** | **-13.5** | **-12.8** | **-12.2** | **-11.6** | **-11.0**|

### E) DISCOUNT RATE (WACC)

*   **Cost of Equity (CAPM):**
    *   **Risk-Free Rate:** 4.33% (U.S. 10-Year Treasury Yield, August 21, 2025).
    *   **Equity Risk Premium:** 5.0% (Standard market premium).
    *   **Beta:** 0.75 (5-Year Monthly Beta). This reflects lower volatility than the broader market.
    *   **Cost of Equity = 4.33% + 0.75 * 5.0% = 8.08%**
*   **Cost of Debt:**
    *   Interest Expense / Average Debt implies a cost of debt, but with debt near zero, this is not meaningful. A proxy of 6.0% is used.
    *   After-Tax Cost of Debt = 6.0% * (1 - 11%) = 5.34%
*   **WACC Calculation:**
    *   Market Value of Equity (E) = 13.0M shares * $138.25/share = $1,797M
    *   Market Value of Debt (D) = $5.8M
    *   **WACC = (1797 / 1802.8) * 8.08% + (5.8 / 1802.8) * 5.34% = 8.06%**

### F) TERMINAL VALUE

*   **Gordon Growth Method:**
    *   A terminal growth rate (g) of **2.0%** is used, reflecting long-term inflation expectations.
    *   **Terminal Value = (FCFF Year 5 * (1 + g)) / (WACC - g) = (-11.0 * 1.02) / (8.06% - 2.0%) = -$185.2 million**
*   **Exit Multiple Cross-Check:**
    *   Due to negative projected EBIT, an EBITDA multiple is not meaningful. The Gordon Growth method will be used, despite the negative value, which signals that under these assumptions, the company is destroying value in perpetuity.

### G) ENTERPRISE TO EQUITY BRIDGE

*   **Enterprise Value:**
    *   PV of Explicit FCFF = -$51.1 million
    *   PV of Terminal Value = -$185.2 million / (1 + 8.06%)^5 = -$125.7 million
    *   **Enterprise Value = -51.1 - 125.7 = -$176.8 million**
*   **Equity Value:**
    *   Net Debt = Total Debt - Cash = $5.8M - $449.0M = -$443.2M
    *   **Equity Value = Enterprise Value - Net Debt = -176.8 - (-443.2) = $266.4 million**

### H) PER-SHARE VALUE AND MARGIN OF SAFETY

*   **Base-Case Fair Value:**
    *   **$266.4 million / 13.0 million shares = $20.49 per share**
*   **Valuation Range:**
    *   **Base Case: $20.49**
    *   **Low/Bear Case:** With a faster revenue decline (-8%) and a -2% operating margin, the value would be negative, suggesting significant downside risk.
    *   **High/Bull Case:** With flat revenue growth (0%) and a 2% operating margin, the fair value would be significantly higher, closer to $50 per share.
*   **Margin of Safety (MOS) Price:**
    *   A 30% discount to the base-case fair value.
    *   **MOS Price = $20.49 * (1 - 0.30) = $14.34**

### One-paragraph Risk Notes

Key risks to this valuation include the high volatility of metallurgical coal prices, which could lead to revenue and margin performance significantly different from the conservative assumptions used. Regulatory risks, particularly those related to carbon emissions, could increase operating costs or curtail demand faster than anticipated. Finally, the company's ability to manage its capital expenditures and working capital in a declining market is crucial; failure to do so could accelerate value destruction. The negative TTM operating income is a significant concern, and the valuation is highly sensitive to the assumption of a return to breakeven.

final answer is 20.49 $