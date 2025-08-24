Of course. This is a well-structured DCF, but there are several critical flaws and areas for refinement to make the valuation more realistic.

Here is a critique of the original valuation, followed by a corrected and refined version in the same format.

### **Critique of the Original Valuation**

This is a good attempt at a DCF, but it contains a few significant issues that materially impact the final price target:

1.  **Incorrect Free Cash Flow Formula:** The most significant error is in the FCFF calculation. Stock-Based Compensation (SBC) is a non-cash expense that is deducted to arrive at EBIT. Therefore, like Depreciation & Amortization (D&A), it should be **added back**, not subtracted, when calculating Free Cash Flow. The original model incorrectly subtracts it, penalizing the company's cash flow by double-counting the expense.
2.  **Inconsistent WACC Calculation:** The stated WACC of 8.5% appears too low based on the model's own inputs (Cost of Equity of 9.55%). A more rigorous calculation using the provided market data results in a higher WACC, which is more appropriate for the current interest rate environment and the company's risk profile. A lower WACC inflates the present value of future cash flows, leading to a higher valuation.
3.  **Terminal Value Methodology:** While the Gordon Growth method is standard, relying solely on a perpetual growth rate can be arbitrary. A more robust approach is to use an Exit Multiple (e.g., EV/EBITDA) based on industry comparables and use the Gordon Growth method as a cross-check to ensure the implied assumptions are reasonable. The original model's cross-check showed a 10.4x multiple, which is reasonable, but the valuation is highly sensitive to the WACC used in the denominator.
4.  **Static Share Count in Final Calculation:** The model correctly assumes a 0.5% annual reduction in shares but appears to use the starting share count to calculate the final per-share value. The final equity value should be divided by the projected share count at the end of the forecast period to accurately reflect the impact of buybacks.
5.  **Static Operating Margin:** Assuming a perfectly flat operating margin is safe but may not be realistic. A growing company often gains some operating leverage. A slight, modest margin expansion would be a more nuanced and realistic "base-case" assumption.

---

Here is the corrected and refined valuation.

### **Intrinsic Valuation: MSA Safety Incorporated (MSA) - Revised**

**Date of Analysis:** August 24, 2025

**Reporting Currency:** USD

**Primary Sources Reviewed:**
*   MSA Safety Incorporated Form 10-Q for the quarter ended March 31, 2025
*   StockAnalysis.com for TTM financial data

---

### **Part 1: Market-Implied Valuation (Reverse DCF)**

**A) Establish Baseline & Market Price**

1.  **Current Market Price:** $175.96 (August 22, 2025)

2.  **Baseline Financials (TTM as of June 30, 2025):**

| Metric | Value (in millions USD) | Source & Date |
| --- | --- | --- |
| Revenue | 1,828 | StockAnalysis.com, Aug 4, 2025. |
| Gross Margin | 46.83% | StockAnalysis.com, Aug 4, 2025. |
| Operating Income (EBIT) | 416.04 | StockAnalysis.com, Aug 4, 2025. |
| Net Income | 276.97 | StockAnalysis.com, Aug 4, 2025. |
| Depreciation & Amortization | 66.58 | StockAnalysis.com, Aug 4, 2025. |
| Stock-Based Compensation | 16.96 | StockAnalysis.com, Aug 4, 2025. |
| Capital Expenditures | -68.78 | StockAnalysis.com, Aug 4, 2025. |
| Change in Working Capital | -32.84 | StockAnalysis.com, Aug 4, 2025. |
| Interest Expense | 31.44 | StockAnalysis.com, Aug 4, 2025. |
| Cash & Equivalents | 170.62 | Form 10-Q, March 31, 2025 |
| Total Debt | 502.06 | Form 10-Q, March 31, 2025 |
| Diluted Weighted-Average Shares | 39.48 | StockAnalysis.com, Aug 4, 2025. |

**B) Reverse-Engineer Assumptions**

To justify the current market price of $175.96, the market is implying a **5-year revenue growth rate of approximately 7.5% and a stable operating margin of 22.76%**. This is based on a DCF model with the following assumptions:

*   **WACC:** 8.5%
*   **Terminal Growth Rate:** 2.5%

This suggests that investors expect steady, moderate growth and consistent profitability from MSA Safety over the next five years.

---

### **Part 2: Analyst's Revised Valuation (Realistic Base-Case)**

**C) Formulate Realistic Assumptions (5 Years)**

My assumptions are grounded in the company's historical performance while incorporating modest improvements and correcting methodological errors.

*   **Revenue for Years 1–5:** A 5-year revenue CAGR of 6.0%, starting at 7.0% and tapering to 5.0%. This aligns with a realistic outlook for a mature industrial leader.
*   **Margin Path:** Operating margin expands modestly from 22.76% to 23.25% over 5 years, reflecting minor operating leverage and efficiency gains as the company grows.
*   **Taxes:** Effective tax rate of 24.0%, in line with recent historical rates.
*   **Capital Intensity:**
    *   **Capex:** 3.8% of revenue, consistent with the historical average.
    *   **Working Capital:** 1.8% of incremental revenue, based on the TTM relationship.
*   **SBC, Dilution, and Buybacks:** A net 0.5% annual reduction in shares outstanding, reflecting a balance between share repurchases and dilution from stock-based compensation.

**D) Free Cash Flow Construction**

**Corrected FCFF Formula:** FCFF = EBIT * (1 - Tax Rate) + D&A **+ SBC** - Capex - Change in Working Capital

| (in millions USD) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Revenue** | **$1,955.96** | **$2,082.91** | **$2,207.89** | **$2,328.28** | **$2,444.70** |
| *Growth* | *7.0%* | *6.5%* | *6.0%* | *5.5%* | *5.0%* |
| **EBIT** | **$447.38** | **$478.02** | **$508.92** | **$538.93** | **$568.39** |
| *Margin* | *22.88%* | *22.95%* | *23.05%* | *23.15%* | *23.25%* |
| Taxes | $107.37 | $114.72 | $122.14 | $129.34 | $136.41 |
| **EBIAT** | **$340.01** | **$363.29** | **$386.78** | **$409.59** | **$431.98** |
| D&A | $70.41 | $74.98 | $79.48 | $83.82 | $88.01 |
| SBC (Added Back) | $17.60 | $18.75 | $19.87 | $20.95 | $22.00 |
| Capex | $74.33 | $79.15 | $83.90 | $88.47 | $92.90 |
| Change in WC | $2.31 | $2.29 | $2.25 | $2.17 | $2.09 |
| **FCFF** | **$351.40** | **$375.59** | **$399.98** | **$423.71** | **$447.00** |

**E) Discount Rate (WACC)**

*   **Cost of Equity (CAPM):**
    *   **Risk-Free Rate:** 4.25% (10-Year US Treasury Yield, August 2025)
    *   **Equity Risk Premium:** 5.0%
    *   **Beta:** 1.06
    *   **Cost of Equity = 4.25% + 1.06 \* 5.0% = 9.55%**
*   **Cost of Debt:** 6.26% (Interest Expense / Total Debt)
*   **Market Value of Equity:** $6,946.9 M ($175.96 * 39.48 M shares)
*   **Market Value of Debt:** $502.1 M
*   **WACC = (E/V \* CoE) + (D/V \* CoD \* (1-T))**
    *   WACC = (93.3% \* 9.55%) + (6.7% \* 6.26% \* (1 - 0.24)) = 8.91% + 0.32% = **9.23%**

**F) Terminal Value**

Using an **Exit Multiple Method** for a more realistic, market-based terminal value.

*   **Year 5 EBITDA:** EBIT_5 + D&A_5 = $568.39 M + $88.01 M = **$656.40 million**
*   **Exit Multiple:** **11.0x**. This is a reasonable multiple for a high-quality, stable industrial technology company, reflecting its market leadership and consistent cash flows.
*   **Terminal Value (EV):** $656.40 M * 11.0 = **$7,220.40 million**
*   **Gordon Growth Cross-Check:** An 11.0x EV/EBITDA multiple implies a perpetual growth rate of **3.1%** `(g = (WACC * TV - FCFF_6) / (TV + FCFF_6))`, which is a reasonable long-term growth assumption for a market leader.

**G) Enterprise to Equity Bridge**

*   **PV of Explicit FCFF:** $1,617.51 million (Using 9.23% WACC)
*   **PV of Terminal Value:** $4,639.45 million
*   **Enterprise Value:** $1,617.51 + $4,639.45 = **$6,256.96 million**
*   **Net Debt:** $331.44 million (Total Debt - Cash)
*   **Equity Value:** $6,256.96 - $331.44 = **$5,925.52 million**

**H) Per-Share Value and Margin of Safety**

*   **Projected Year 5 Shares:** 39.48 M * (1 - 0.005)^5 = **38.50 million**
*   **Analyst's Base-Case Fair Value:** $5,925.52 / 38.50 = **$153.91 per share**
*   **Valuation Range:**
    *   **Low/Bear Case:** $125 (Lower growth, 10x exit multiple)
    *   **High/Bull Case:** $180 (Higher growth, 12x exit multiple)
*   **Margin of Safety (MOS) Price (30%):** **$107.74**

---

**Risk Notes**

1.  **Industrial Cyclicality:** A significant portion of MSA's revenue is tied to industrial end markets, which can be cyclical and impact demand.
2.  **Competition:** The safety products market is competitive, and MSA faces pressure from both large, diversified industrial companies and smaller, specialized competitors.
3.  **Product Liability:** As a manufacturer of safety equipment, MSA is exposed to product liability claims.

final answer is 153.91 $