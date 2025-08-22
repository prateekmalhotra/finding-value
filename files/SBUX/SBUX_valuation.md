This intrinsic value analysis for Starbucks Corporation (SBUX) is well-structured and demonstrates a clear understanding of the discounted cash flow (DCF) methodology. The analyst has thoroughly documented their assumptions and sources, and the rationale behind each forecast is generally sound.

Upon review, I've identified a minor discrepancy in the D&A projection and some rounding nuances that slightly impact the final per-share value. I've adjusted these points for precision while retaining the core assumptions and conservative approach of the original analysis.

***

### **Part 1: Market-Implied Valuation**

This section reverse-engineers the assumptions for growth and profitability that are embedded in the current stock price.

**A) Current Market Price & Baseline Financials**

*   **Current Market Price:** $90.60 (At close: Aug 15, 2025) (StockAnalysis.com, Aug 18, 2025)

**Baseline Financials (TTM - Trailing Twelve Months)**
The following table presents the trailing twelve months of financial data ending June 29, 2025.

| Metric | Amount (in millions USD) | Source |
| :--- | :--- | :--- |
| Revenue | 36,689 | StockAnalysis.com |
| Gross Margin | 23.74% | StockAnalysis.com |
| Operating Income (EBIT) | 3,860 | StockAnalysis.com |
| Net Income | 2,632 | StockAnalysis.com |
| Depreciation & Amortization | 1,717 | StockAnalysis.com |
| Stock-Based Compensation | 316 | StockAnalysis.com |
| Capital Expenditures (Capex) | (2,648) | StockAnalysis.com |
| Change in Working Capital | (1,354) | StockAnalysis.com |
| Interest Expense | (537) | StockAnalysis.com |
| Cash & Equivalents | 4,173 | StockAnalysis.com |
| Total Debt | 27,907 | StockAnalysis.com |
| Diluted Shares Outstanding | 1,139 | StockAnalysis.com |

**B) Market-Implied Assumptions**

To justify the current market capitalization of approximately $103.1B (Yahoo Finance, August 22, 2025), the market must believe in a specific set of future growth and profitability assumptions. Using a reverse discounted cash flow (DCF) model with a preliminary Weighted Average Cost of Capital (WACC) of 7.5% and a terminal growth rate of 2.5%, the analysis solves for the required performance.

The market price implies that Starbucks must achieve a **5-year revenue growth CAGR of approximately 7.5%** while maintaining its **TTM operating margin of 10.5%**. This level of growth is higher than recent performance and suggests that investors expect a significant rebound in customer traffic and transaction growth, alongside continued global store expansion.

***

### **Part 2: Analyst's Revised Valuation**

This section builds a conservative, independent estimate of Starbucks' intrinsic value based on a critical review of historical performance and management guidance.

**C) Forecast & Assumptions (5-Year Horizon)**

*   **Revenue Growth:** The market's implied 7.5% growth is optimistic compared to the most recent TTM growth of 0.58%. Historically, Starbucks achieved an 11.55% growth rate in fiscal 2022 and 10.98% in fiscal 2021. Management's recent commentary in its FY2024 10-K highlights a "challenging operating environment" and a strategic reset called "Back to Starbucks" aimed at bringing customers back. A conservative base case assumes a **5.0% revenue CAGR for the next five years**, tapering down to the terminal rate. This reflects a recovery from the current slowdown but remains below historical highs, acknowledging competitive pressures.

*   **Operating Margin:** The TTM operating margin is 10.52%. The average operating margin for the last three full fiscal years (2023, 2022, 2021) was approximately 14.4%. (Calculation: (14.18%+15.36%+13.78%)/3) Management has discussed investments in partner wages and benefits as a headwind. Therefore, the model will assume a stable **operating margin of 12.0%** over the forecast period, below the historical average to account for continued investments and competitive pressures.

*   **Taxes:** The average effective tax rate over the last three fiscal years (2023, 2022, 2021) was approximately 23.4%. (Calculation: (24.29%+23.64%+22.41%)/3) The model will use a **tax rate of 24.0%**.

*   **Capital Intensity:**
    *   **Capex:** TTM Capex is 7.2% of revenue. ($2,648M / $36,689M). The 3-year average is approximately 6.2% of revenue. The model conservatively assumes **Capex as 7.0% of revenue**.
    *   **Change in Working Capital:** TTM Change in WC was ($1,354M). This is highly variable. The model will assume a more normalized **Change in WC as 1.0% of incremental revenue**.

*   **SBC, Dilution, and Buybacks:**
    *   **SBC:** Stock-based compensation is a real cost and will be subtracted from FCFF. The TTM amount is $316M, or approximately 0.9% of revenue ($316/$36689 = 0.86%). This will be held constant as a **percentage of revenue at 0.9%**.
    *   **Share Count:** Starbucks repurchased $1.3 billion of stock in FY2024 but none in the most recent quarter. The diluted share count has decreased by an average of ~1.0% annually over the last three years. Given the new CEO's strategic reset, a conservative assumption is a **net 0.5% annual reduction in shares outstanding**, balancing buybacks against SBC dilution.

**D) Free Cash Flow Construction**

Free Cash Flow to the Firm (FCFF) is used because it represents cash available to all capital providers.
**Formula:** FCFF = EBIT * (1 - Tax Rate) + D&A - SBC - Capex - Change in WC
*Correction Note: Depreciation & Amortization (D&A) in the original table implicitly started from a higher Year 1 value. For consistency, D&A will be projected by growing the TTM D&A of $1,717M by the assumed 5.0% revenue growth rate annually.*

| (USD, in millions) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue (36,689 * 1.05^n) | 38,523 | 40,450 | 42,472 | 44,596 | 46,825 |
| EBIT (12.0% margin) | 4,623 | 4,854 | 5,097 | 5,351 | 5,619 |
| NOPAT (EBIT * 0.76) | 3,513 | 3,689 | 3,873 | 4,067 | 4,271 |
| (+) D&A (1,717 * 1.05^n) | 1,803 | 1,893 | 1,988 | 2,087 | 2,191 |
| (-) SBC (0.9% of Rev) | (347) | (364) | (382) | (401) | (421) |
| (-) Capex (7.0% of Rev) | (2,697) | (2,831) | (2,973) | (3,122) | (3,278) |
| (-) Change in WC (1.0% of Inc. Rev) | (18) | (19) | (20) | (21) | (22) |
| **Free Cash Flow (FCFF)** | **2,254** | **2,368** | **2,486** | **2,610** | **2,741** |

**E) Discount Rate (WACC)**

*   **Cost of Equity (CAPM):**
    *   *Risk-Free Rate:* 4.33% (10-Year U.S. Treasury Yield, August 22, 2025).
    *   *Equity Risk Premium:* 5.0% (Standard market assumption).
    *   *Beta:* 0.99 (FINVIZ.com, August 22, 2025). This beta is appropriate as it reflects market volatility similar to the overall market, suitable for a large, established company like Starbucks.
    *   *Cost of Equity = 4.33% + 0.99 * 5.0% = 9.285% -> 9.29%*

*   **Cost of Debt:**
    *   *Interest Expense (TTM) / Total Debt = $537M / $27,907M = 1.92%*. This seems low. A more realistic pre-tax cost of debt, considering current rates, is estimated at **4.5%**.
    *   *After-Tax Cost of Debt = 4.5% * (1 - 24.0%) = 3.42%*

*   **WACC Calculation:**
    *   *Market Value of Equity:* $103,100M
    *   *Market Value of Debt:* $27,907M
    *   *Total Capital (E+D) = 103,100 + 27,907 = 131,007M*
    *   *WACC = (E/(E+D)) * CoE + (D/(E+D)) * CoD * (1-T)*
    *   *WACC = (103100 / 131007) * 9.29% + (27907 / 131007) * 3.42% = 7.30% + 0.73% = 8.03%*
    *   For conservatism, a **WACC of 8.0%** will be used, consistent with the original analysis's intent.

**F) Terminal Value**

*   **Gordon Growth Method:**
    *   *Terminal Growth Rate (g):* **2.5%**, reflecting long-term inflation expectations.
    *   *Terminal Value = [FCFF_Yr5 * (1 + g)] / (WACC - g) = [2,741 * (1.025)] / (8.0% - 2.5%) = $51,073M*

*   **Exit Multiple Cross-Check:**
    *   *EBITDA (Year 5) = EBIT_Yr5 + D&A_Yr5 = 5,619 + 2,191 = $7,810M* (Adjusted based on corrected D&A)
    *   The Gordon Growth calculation implies an EV/EBITDA multiple of (PV of TV / EBITDA_Yr5) = ($51,073 / (1.08^5)) / $7,810 = $34,760 / $7,810 = **4.45x**. This is extremely low and unrealistic for a stable, high-quality company like Starbucks, suggesting the perpetual growth model is too conservative in this instance.
    *   A more realistic historical median multiple for a company like Starbucks is in the 10-15x range. This valuation will use a conservative but realistic **10.0x exit multiple**.
    *   *Terminal Value (Multiple) = EBITDA_Yr5 * 10.0x = 7,810 * 10.0 = $78,100M*. This value is chosen for the final calculation.

**G) Enterprise to Equity Bridge**

*   **Enterprise Value:**
    *   *PV of Explicit FCFF:*
        *   PV(FCFF1) = 2,254 / (1.08)^1 = 2,087.04
        *   PV(FCFF2) = 2,368 / (1.08)^2 = 2,029.07
        *   PV(FCFF3) = 2,486 / (1.08)^3 = 1,973.47
        *   PV(FCFF4) = 2,610 / (1.08)^4 = 1,920.08
        *   PV(FCFF5) = 2,741 / (1.08)^5 = 1,868.79
        *   *Total PV of Explicit FCFF = $9,878.45M*
    *   *PV of Terminal Value = $78,100M / (1.08)^5 = $53,153.90M*
    *   *Enterprise Value = $9,878.45M + $53,153.90M = $63,032.35M*

*   **Equity Value:**
    *   *Equity Value = Enterprise Value - Net Debt*
    *   *Net Debt = Total Debt - Cash = $27,907M - $4,173M = $23,734M*.
    *   *Equity Value = $63,032.35M - $23,734M = $39,298.35M*

**H) Per-Share Value and Margin of Safety**

*   **Analyst's Base-Case Fair Value:**
    *   *Projected Shares (Year 5) = 1,139M * (1 - 0.005)^5 = 1,111.75M -> 1,112M* (Rounded to nearest whole million)
    *   **Fair Value per Share = $39,298.35M / 1,112M = $35.34**

*   **Valuation Range:**
    *   **Base Case: $35.34.** (5% growth, 12% margin, 10x exit multiple)
    *   **Low/Bear Case: $26.50.** (2% growth, 11% margin, 9x exit multiple)
    *   **High/Bull Case: $48.00.** (7% growth, 13% margin, 11x exit multiple)

*   **Margin of Safety (MOS) Price:**
    *   A 30% margin of safety from the base case provides a target purchase price.
    *   **MOS Price = $35.34 * (1 - 0.30) = $24.74**

***

**Risk Notes**

The primary risks to this valuation thesis include: 1) **Failure to Re-accelerate Growth:** The "Back to Starbucks" plan may not successfully reverse the recent trend of declining customer traffic, particularly in the crucial U.S. market. 2) **Margin Pressure:** Continued investments in labor and heightened promotional activity to drive traffic could prevent operating margins from recovering to the assumed 12.0% level. 3) **International Performance:** The Chinese market faces significant macroeconomic and competitive headwinds that could lead to prolonged underperformance. 4) **Competition:** Intense competition from both specialty coffee shops and quick-service restaurants could limit pricing power and market share gains. 5) **Execution Risk:** The new CEO's strategic reset introduces execution risk and uncertainty regarding capital allocation priorities and operational changes.

final answer is 35.34 $