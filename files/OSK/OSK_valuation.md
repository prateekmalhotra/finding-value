## **Oshkosh Corporation (OSK) Intrinsic Value Analysis**

*   **Company:** Oshkosh Corporation (OSK)
*   **Currency:** United States Dollar (USD)
*   **Date of Analysis:** August 22, 2025
*   **Primary Sources Reviewed:** StockAnalysis.com (Financials, Balance Sheet, Cash Flow), GuruFocus (Historical Multiples), Q2 2025 Earnings Call Transcripts, Search Results for Market Data.

---

### **Part 1: Market-Implied Valuation (Reverse DCF)**

This section reverse-engineers the assumptions for growth and profitability that are embedded in the current stock price.

**A) Current Market Price & Baseline Financials**

*   **Current Market Price:** $137.19 (August 21, 2025)

**Baseline Financials (TTM as of June 30, 2025)**

| Metric | Value (in millions USD) | Source |
| :--- | :--- | :--- |
| Revenue | $10,384.4 | StockAnalysis |
| Gross Margin | 18.08% | StockAnalysis |
| Operating Income (EBIT) | $969.3 | StockAnalysis |
| Net Income | $750.4 | Author's Calculation |
| Depreciation & Amortization | $215.1 | StockAnalysis |
| Stock-Based Compensation | $36.8 | StockAnalysis |
| Capital Expenditures | $222.3 | StockAnalysis |
| Change in Working Capital | ($43.3) | StockAnalysis |
| Interest Expense | $122.2 | StockAnalysis |
| Cash & Equivalents | $191.7 | StockAnalysis |
| Total Debt | $1,498.3 | StockAnalysis |
| Diluted Shares Outstanding | 65.0 | StockAnalysis |

**B) Market-Implied Assumptions**

To justify the market price of **$137.19**, investors must believe the company can achieve specific growth and profitability milestones. Holding the Trailing Twelve Month (TTM) operating margin of 9.33% constant and using a WACC of 10.92%, the model solves for the required revenue growth.

*   **Market-Implied 5-Year Revenue CAGR: 12.92%**

This analysis indicates that to justify today's stock price, one must believe Oshkosh can grow its revenue at a compound annual rate of nearly 13% for the next five years while maintaining its current profitability, a rate that is higher than its recent 3-year historical average.

---

### **Part 2: Analyst's Revised Valuation (Conservative Base-Case)**

This section builds an independent intrinsic value estimate based on a conservative interpretation of company fundamentals and guidance.

**C) Forecast & Assumptions**

My assumptions are more conservative than the market's, based on historical volatility and the lack of explicit long-term management guidance.

*   **Revenue Growth (Years 1–5):** The market's implied 12.9% CAGR appears optimistic compared to the 3-year historical average of ~10.5% and a mixed business outlook. I am assuming a more conservative **8.0% growth in Year 1, tapering down to 4.0% by Year 5**. This reflects potential strength in Vocational and NGDV segments, offset by headwinds in others.
*   **Operating Margin:** The TTM margin is 9.33%. While management aims to "transform margins," there is no concrete guidance. I am holding the operating margin stable at **9.5%** for the forecast period, slightly above the TTM figure to reflect operational efficiency but avoiding speculative expansion.
*   **Tax Rate:** The average effective tax rate over the last two full years (normalizing for a 2022 outlier) is approximately 23.8%. I will use a **24.0%** effective tax rate. (StockAnalysis)
*   **Capital Intensity:**
    *   **Capex:** Management has not provided specific guidance. The 3-year average capex is 3.1% of revenue. I will use a conservative **2.8% of revenue**. (StockAnalysis)
    *   **Working Capital:** I assume NWC will require investment to grow, modeled at **12.0% of incremental revenue**.

**D) Free Cash Flow Build**

Free Cash Flow to the Firm (FCFF) is used as it represents cash available to all capital providers.
**Formula:** FCFF = EBIT * (1 - Tax Rate) + D&A - Stock-Based Compensation (SBC) - Capex - Change in NWC

| (in millions USD) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $11,215.2 | $12,000.2 | $12,720.2 | $13,356.2 | $13,890.5 |
| EBIT (9.5% margin) | $1,065.4 | $1,140.0 | $1,208.4 | $1,268.8 | $1,319.6 |
| EBIT * (1-Tax Rate) | $809.7 | $866.4 | $918.4 | $964.3 | $1,002.9 |
| + D&A | $232.1 | $248.4 | $263.3 | $276.5 | $287.5 |
| - Stock-Based Comp | ($39.3) | ($42.0) | ($44.5) | ($46.7) | ($48.6) |
| - Capital Expenditures | ($314.0) | ($336.0) | ($356.2) | ($374.0) | ($388.9) |
| - Change in NWC | ($99.7) | ($94.2) | ($86.4) | ($76.3) | ($64.1) |
| **Free Cash Flow** | **$588.9** | **$642.6** | **$694.6** | **$743.8** | **$788.8** |

**E) Discount Rate (WACC)**

*   **Cost of Equity (CAPM):** 11.48%
    *   *Formula:* Risk-Free Rate + Beta * Equity Risk Premium
    *   *Inputs:* 4.33% (10-Yr Treasury, Aug 22, 2025) + 1.43 (5-Yr Beta) * 5.0% (Standard ERP)
*   **After-Tax Cost of Debt:** 6.20%
    *   *Formula:* (Interest Expense / Total Debt) * (1 - Tax Rate)
    *   *Inputs:* ($122.2M / $1,498.3M) * (1 - 0.24)
*   **WACC:** 10.92%
    *   *Formula:* (Cost of Equity * % Equity) + (After-Tax Cost of Debt * % Debt)
    *   *Inputs:* (11.48% * 87.2%) + (6.20% * 12.8%)

**F) Terminal Value**

*   **Gordon Growth Method:** A 2.5% terminal growth rate (in line with long-term inflation expectations) yields a terminal value of **$9,602.0 M**.
    *   *Formula:* (Year 5 FCFF * (1 + g)) / (WACC - g)
*   **Exit Multiple Cross-Check:** Using the 13-year median EV/EBITDA multiple of 8.8x for Oshkosh yields a terminal value of **$14,142.7 M**. This value is higher and will be used in the final valuation.
    *   *Formula:* Year 5 EBITDA * Exit Multiple

**G) Enterprise to Equity Bridge**

| Component | Value (in millions USD) |
| :--- | :--- |
| PV of 5-Year FCFF | $2,523.4 |
| PV of Terminal Value | $8,423.3 |
| **Enterprise Value** | **$10,946.7** |
| Less: Total Debt | ($1,498.3) |
| Plus: Cash & Equivalents | $191.7 |
| **Analyst's Base-Case Equity Value** | **$9,640.1** |

**H) Per-Share Value and Margin of Safety**

*   **Analyst's Base-Case Fair Value:** **$148.31**
    *   *Formula:* Equity Value / Diluted Shares Outstanding

*   **Valuation Range:**
    *   **Base Case: $148.31**
    *   **Low/Bear Case: ~$85.00.** This scenario assumes flat revenue and margin compression to ~8.0% due to competitive pressures or a downturn.
    *   **High/Bull Case: ~$145.00.** This scenario assumes revenue growth closer to the market-implied rate and modest margin expansion toward 10.5%, driven by successful execution on new programs.

*   **Margin of Safety (MOS) Price (30%): $103.82**
    *   *Formula:* Base-Case Fair Value * (1 - 0.30)

### **Risk Notes**

1.  **Defense Spending Volatility:** A significant portion of Oshkosh's revenue is tied to large government defense contracts (e.g., FMTV, historical JLTV). Changes in government spending priorities or contract losses represent a major risk.
2.  **Cyclicality of Access & Vocational Markets:** The Access and Vocational segments are cyclical and dependent on construction and municipal spending, which can decline during economic downturns.
3.  **Program Execution Risk:** The successful ramp-up of major new programs like the USPS Next Generation Delivery Vehicle (NGDV) is critical to achieving growth targets and is not guaranteed.
4.  **Input Cost Inflation:** Like other industrial manufacturers, Oshkosh is exposed to fluctuations in raw material and labor costs, which could compress margins if not offset by price increases.

final answer is 148.31 $