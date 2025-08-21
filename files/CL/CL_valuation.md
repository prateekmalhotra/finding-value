### **Colgate-Palmolive Company (CL) Intrinsic Value Estimation**

*   **Company:** Colgate-Palmolive Company (CL)
*   **Currency:** United States Dollars (USD)
*   **Date of Analysis:** August 21, 2025
*   **Primary Sources Reviewed:** Q2 2025 Earnings Release, stockanalysis.com financial data, public market data.

### **A) Baseline Financials (TTM)**

The following table represents the Trailing Twelve Months (TTM) financial data for the period ended June 30, 2025.

| Metric | Value (in millions USD) | Source |
| :--- | :--- | :--- |
| Revenue | $19,998 | (stockanalysis.com, Aug 21, 2025) |
| Gross Margin | 60.6% | ($12,123M / $19,998M) (stockanalysis.com, Aug 21, 2025) |
| Operating Income (EBIT) | $4,227 | (stockanalysis.com, Aug 21, 2025) |
| Net Income | $2,908 | (stockanalysis.com, Aug 21, 2025) |
| Depreciation & Amortization (D&A) | $597 | (stockanalysis.com, Aug 21, 2025) |
| Stock-Based Compensation (SBC) | $147 | (stockanalysis.com, Aug 21, 2025) |
| Capital Expenditures (Capex) | $550 | (stockanalysis.com, Aug 21, 2025) |
| Change in Working Capital | $70 | (stockanalysis.com, Aug 21, 2025) |
| Interest Expense | $278 | (stockanalysis.com, Aug 21, 2025) |
| Cash & Equivalents | $1,215 | (stockanalysis.com, Aug 21, 2025) |
| Total Debt | $8,758 | (stockanalysis.com, Aug 21, 2025) |
| Diluted Weighted-Average Shares | 818 | (stockanalysis.com, Aug 21, 2025) |

### **B) Management Guidance Extraction**

Key guidance extracted from the company's Q2 2025 earnings release:

*   **Net Sales Growth:** "The Company still expects net sales to be up low single digits..." (Q2 2025 Earnings Release, Aug 1, 2025).
*   **Organic Sales Growth:** "The Company now expects organic sales growth to be at the low end of 2% to 4%..." (Q2 2025 Earnings Release, Aug 1, 2025).
*   **Gross Margin:** "...the Company still expects...gross profit margin...to be roughly flat as a percentage of net sales..." (Q2 2025 Earnings Release, Aug 1, 2025).

### **C) Forecast Horizon and Base-Case Assumptions (5 Years)**

*   **Revenue Growth:** The midpoint of the organic sales growth guidance of 2% to 4% is 3%. Therefore, a **3.0%** annual growth rate is assumed for the next 5 years, which is in line with the "low single digits" guidance.
*   **Operating Margin:** Based on management's guidance of "roughly flat" gross margin and the historical stability of the business, the TTM operating margin of **21.1%** ($4,227M / $19,998M) is held constant.
*   **Taxes:** The TTM effective tax rate is 22.5% ($885M / $3,938M). We will use a normalized rate of **23.0%**.
*   **Capital Intensity:**
    *   **Capex:** TTM Capex is 2.75% of revenue. This is assumed to continue.
    *   **Working Capital:** TTM Change in WC is 0.35% of revenue. This is assumed to continue.
*   **SBC and Dilution:**
    *   SBC is projected as a percentage of revenue, consistent with the TTM level of **0.74%**.
    *   The latest diluted share count of **818 million** is used for the final per-share calculation.

### **D) Free Cash Flow Construction**

Free Cash Flow to the Firm (FCFF) is used for valuation as it represents cash flow available to all capital providers. The formula is:
**FCFF = EBIT * (1 - Tax Rate) + D&A - SBC - Capex - Change in Working Capital**

| (in millions USD) | Y1 (2026) | Y2 (2027) | Y3 (2028) | Y4 (2029) | Y5 (2030) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $20,598 | $21,216 | $21,852 | $22,508 | $23,183 |
| EBIT (21.1%) | $4,346 | $4,477 | $4,611 | $4,749 | $4,892 |
| EBIT * (1-Tax Rate) | $3,347 | $3,447 | $3,550 | $3,657 | $3,767 |
| + D&A | $612 | $630 | $649 | $669 | $689 |
| - SBC | $152 | $157 | $162 | $166 | $171 |
| - Capex | $567 | $584 | $601 | $619 | $638 |
| - Change in WC | $72 | $74 | $76 | $79 | $81 |
| **FCFF** | **$3,168** | **$3,262** | **$3,360** | **$3,462** | **$3,566** |

### **E) Discount Rate (WACC)**

*   **Cost of Equity (CAPM):**
    *   **Risk-Free Rate:** 4.29% (10-Year U.S. Treasury Yield, Aug 21, 2025)
    *   **Equity Risk Premium:** 5.0% (Standard market assumption)
    *   **Beta:** 0.40 (5-Year Beta). This reflects the company's low volatility and defensive characteristics.
    *   **Cost of Equity = 4.29% + 0.40 * 5.0% = 6.29%**
*   **Cost of Debt:**
    *   Interest Expense / Average Debt = $278M / $8,758M = 3.17%
    *   After-tax Cost of Debt = 3.17% * (1 - 23.0%) = 2.44%
*   **WACC:**
    *   Market Value of Equity: $69.55B (Forbes, Aug 21, 2025)
    *   Market Value of Debt: $8.76B
    *   Total Value: $78.31B
    *   **WACC = (69.55/78.31) * 6.29% + (8.76/78.31) * 2.44% = 5.86%**

### **F) Terminal Value**

*   **Gordon Growth Method:**
    *   A terminal growth rate (g) of **2.5%** is used, reflecting long-term inflation expectations.
    *   **Terminal Value = (FCFF Year 5 * (1 + g)) / (WACC - g) = ($3,566 * 1.025) / (5.86% - 2.5%) = $108,719M**
*   **Exit Multiple Cross-Check:**
    *   Year 5 EBITDA = $5,581M ($4,892M EBIT + $689M D&A)
    *   Current EV/EBITDA multiple is 15.8x (Finbox, Aug 21, 2025).
    *   **Terminal Value (Multiple) = $5,581M * 15.8 = $88,180M**
*   **Conclusion:** The lower, more conservative exit multiple method is chosen. **Terminal Value = $88,180M**.

### **G) Enterprise to Equity Bridge**

*   PV of Explicit FCFF = $3,168/(1.0586)^1 + $3,262/(1.0586)^2 + $3,360/(1.0586)^3 + $3,462/(1.0586)^4 + $3,566/(1.0586)^5 = $14,582M
*   PV of Terminal Value = $88,180M / (1.0586)^5 = $66,419M
*   **Enterprise Value = $14,582M + $66,419M = $81,001M**
*   **Equity Value = $81,001M - $8,758M (Total Debt) + $1,215M (Cash) = $73,458M**

### **H) Per-Share Value and Margin of Safety**

*   **Base-Case Fair Value = $73,458M / 818M shares = $89.80 per share**
*   **Valuation Range:**
    *   **Base Case: $89.80**
    *   **Low/Bear Case:** With revenue growth at 1.5% and margin compression, the value would likely be in the **$70-$75** range.
    *   **High/Bull Case:** With revenue growth at 4.0% and modest margin expansion, the value could approach the **$105-$110** range.
*   **Margin of Safety (MOS) Price (30%): $89.80 * (1 - 0.30) = $62.86**

### **Risk Notes**

1.  **Input Cost Volatility:** The business is exposed to fluctuations in raw material and packaging costs, which could compress margins if not offset by pricing.
2.  **Foreign Exchange Risk:** As a global company, unfavorable currency movements can negatively impact reported sales and profits.
3.  **Competitive Pressures:** The consumer staples market is highly competitive, with pressure from both branded and private-label competitors that could limit pricing power.
4.  **Slowing Category Growth:** The company faces cautious consumer environments in key markets like North America, potentially leading to lower-than-expected volume growth.

final answer is 89.80 $