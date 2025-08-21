Here is a base-case intrinsic value analysis for Sprouts Farmers Market, Inc. (SFM).

### **Sprouts Farmers Market, Inc. (SFM)**
*   **Currency:** USD
*   **Date of Analysis:** August 21, 2025
*   **Primary Sources Reviewed:**
    *   StockAnalysis.com Financial Data (as of TTM period ended June 29, 2025)
    *   Q2 2025 Earnings Call Transcript (dated July 30, 2025)
    *   YCharts & Trading Economics for 10-Year Treasury Yield (dated August 20, 2025)
    *   GuruFocus for historical valuation multiples.

---

### **A) Baseline Financials (TTM)**
The following table represents the Trailing Twelve Months (TTM) financial data for the period ended June 29, 2025. All figures are in millions of USD.

| Metric | TTM Value | Source & Citation |
| :--- | :--- | :--- |
| Revenue | $8,399.0 | StockAnalysis, Income Statement, August 21, 2025 |
| Gross Margin | 38.9% | StockAnalysis, Income Statement, August 21, 2025 |
| Operating Income (EBIT) | $635.0 | StockAnalysis, Income Statement, August 21, 2025 |
| Net Income | $484.9 | StockAnalysis, Income Statement, August 21, 2025 |
| Depreciation & Amortization | $286.7 | StockAnalysis, Cash Flow Statement, August 21, 2025 |
| Stock-Based Compensation | $29.6 | StockAnalysis, Cash Flow Statement, August 21, 2025 |
| Capital Expenditures | $241.8 | StockAnalysis, Cash Flow Statement, August 21, 2025 |
| Change in Working Capital | ($77.5) | StockAnalysis, Cash Flow Statement, August 21, 2025 |
| Interest Expense | ($2.3) | StockAnalysis, Income Statement, August 21, 2025 |
| Cash & Equivalents | $261.4 | StockAnalysis, Balance Sheet, August 21, 2025 |
| Total Debt | $1,756.0 | StockAnalysis, Balance Sheet, August 21, 2025 |
| Diluted Shares | 100.2 | StockAnalysis, Income Statement, August 21, 2025 |

---

### **B) Management Guidance Extraction**
The following guidance was extracted for the full fiscal year 2025 from the Q2 2025 earnings call on July 30, 2025.

*   **Total Sales Growth:** "For 2025, we expect total sales growth to be 14.5% to 16%."
*   **Comparable Store Sales:** "...and comp sales in the range of 7.5% to 9%."

*No explicit guidance was provided for margins or capital expenditures.*

---

### **C) Forecast & Assumptions (5-Year Horizon)**

*   **Revenue Growth:**
    *   **Year 1:** 15.25%, the midpoint of management's guidance.
    *   **Years 2-5:** Growth rate is assumed to decline steadily from 12.75% to 5.25% as the company scales, representing a normalization of growth.
*   **Operating Margin:**
    *   **Forecast Period:** 7.75%. This is a slight expansion from the TTM margin of 7.56%, reflecting operating leverage from strong sales growth mentioned by management.
*   **Taxes:**
    *   **Effective Tax Rate:** 25.0%. This is based on the normalized average effective tax rate from the past three full fiscal years (2022-2024).
*   **Capital Intensity:**
    *   **Capex:** 2.74% of revenue. This is based on the average capex as a percentage of revenue over the last three full fiscal years (2022-2024), as no guidance was provided.
    *   **Change in Working Capital:** -1.0% of incremental revenue. This is a conservative estimate, reflecting historical efficiency but normalizing for the volatility of prior periods.
*   **Other:**
    *   **D&A and SBC:** Forecasted as a percentage of revenue, based on TTM levels: 3.41% for D&A and 0.35% for SBC.

---

### **D) Free Cash Flow Construction**
Free Cash Flow to the Firm (FCFF) is used as it represents cash flow available to all capital providers.
**Formula:** `FCFF = EBIT * (1 - Tax Rate) + D&A - SBC - Capex - Change in Working Capital`

| ($ in millions) | Year 1 (2026E) | Year 2 (2027E) | Year 3 (2028E) | Year 4 (2029E) | Year 5 (2030E) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $9,680 | $10,914 | $12,033 | $12,966 | $13,647 |
| *Revenue Growth* | *15.25%* | *12.75%* | *10.25%* | *7.75%* | *5.25%* |
| EBIT | $750 | $846 | $933 | $1,005 | $1,058 |
| NOPAT (EBIT \* 0.75) | $562 | $635 | $700 | $754 | $793 |
| (+) D&A | $330 | $372 | $410 | $442 | $465 |
| (-) Stock-Based Comp | $34 | $38 | $42 | $45 | $48 |
| (-) Capex | $265 | $299 | $330 | $355 | $374 |
| (-) Change in WC | ($13) | ($12) | ($11) | ($9) | ($7) |
| **Free Cash Flow (FCFF)** | **$606** | **$682** | **$749** | **$805** | **$843** |

---

### **E) Discount Rate (WACC)**
The Weighted Average Cost of Capital (WACC) is calculated to discount future cash flows.

*   **Cost of Equity (CAPM):**
    *   **Formula:** `Risk-Free Rate + Beta * Equity Risk Premium`
    *   **Risk-Free Rate:** 4.30% (based on the 10-Year U.S. Treasury yield on August 20, 2025).
    *   **Beta (β):** 0.78. This reflects a lower systematic risk profile than the broader market, which is typical for a grocery retailer.
    *   **Equity Risk Premium:** 5.0% (a standard assumption for the U.S. market).
    *   **Calculation:** `4.30% + 0.78 * 5.0% = 8.20%`
*   **Cost of Debt:**
    *   **Pre-Tax Cost of Debt:** 6.0%. This is an estimate assuming a reasonable credit spread over the risk-free rate, used because net interest expense is not representative.
*   **WACC Calculation:**
    *   **Formula:** `(E/V * Cost of Equity) + (D/V * Cost of Debt * (1 - Tax Rate))`
    *   **Market Value of Equity (E):** $14,760M
    *   **Market Value of Debt (D):** $1,756M
    *   **Total Value (V):** $16,516M
    *   **Calculation:** `(89.4% * 8.20%) + (10.6% * 6.0% * 0.75) = 7.33% + 0.48% =` **7.81%**

---

### **F) Terminal Value**

*   **Method:** Gordon Growth Model.
*   **Formula:** `(Year 5 FCFF * (1 + g)) / (WACC - g)`
*   **Terminal Growth Rate (g):** 2.5%. This rate is selected to be in line with long-term expected inflation and economic growth, representing a stable, mature state.
*   **Calculation:** `($843M * 1.025) / (7.81% - 2.50%) = $864M / 5.31% =` **$16,273M**
*   **Exit Multiple Cross-Check:**
    *   Year 5 EBITDA is projected to be $1,523M.
    *   The company's 13-year median EV/EBITDA multiple is 10.3x.
    *   `$1,523M * 10.3 = $15,687M`. This result is proximate to the Gordon Growth value, providing confidence in the terminal assumption.

---

### **G) Enterprise to Equity Bridge**

*   **Present Value of Explicit FCFF:** Sum of discounted FCFF from Years 1-5 = **$2,920M**
*   **Present Value of Terminal Value:** `$16,273M / (1.0781)^5 =` **$11,190M**
*   **Enterprise Value:** `$2,920M + $11,190M =` **$14,110M**
*   **Less: Net Debt:**
    *   Total Debt: $1,756M
    *   Cash & Equivalents: ($261M)
    *   Net Debt: **$1,495M**
*   **Equity Value:** `$14,110M - $1,495M =` **$12,615M**

---

### **H) Per-Share Valuation and Margin of Safety**

*   **Base-Case Fair Value:** `$12,615M / 100.2M shares =` **$125.92**
*   **Valuation Range:**
    *   **Base Case:** **$125.92**. Assumes successful execution of growth plans and modest margin expansion.
    *   **Low/Bear Case:** **~$100**. Assumes lower revenue growth (fading to 3%), margin compression to 7.25%, and a lower 2.0% terminal growth rate.
    *   **High/Bull Case:** **~$150**. Assumes stronger sustained growth, margin expansion to 8.25%, and a higher 2.75% terminal growth rate.
*   **Margin of Safety (MOS) Price (30% Discount):** `$125.92 * (1 - 0.30) =` **$88.14**

---

### **Risk Notes**
1.  **Competition:** The grocery industry is intensely competitive, with pressure from conventional supermarkets, other natural/organic retailers, and mass merchandisers, which could impact pricing power and margins.
2.  **Execution Risk:** The valuation is dependent on the successful execution of an ambitious store growth strategy. Any delays, cost overruns, or underperformance of new stores could negatively impact future cash flows.
3.  **Consumer Spending:** As a specialty retailer, Sprouts is exposed to shifts in consumer discretionary spending. An economic downturn could lead to customers trading down to lower-priced conventional grocers.
4.  **Input Cost Volatility:** The company is subject to fluctuations in food commodity prices, transportation costs, and labor costs, which could compress margins if not fully passed on to consumers.

final answer is 125.92 $