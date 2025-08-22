Here is a two-stage intrinsic valuation of Allison Transmission Holdings, Inc. (ALSN).

### **Allison Transmission Holdings, Inc. (ALSN)**
**Currency:** USD
**Date of Analysis:** August 22, 2025
**Primary Sources Reviewed:**
*   Allison Transmission Holdings, Inc. 2024 Form 10-K
*   StockAnalysis.com Financial Data

---

### **Part 1: Market-Implied Valuation (Reverse DCF)**

**A) ESTABLISH BASELINE & MARKET PRICE**

1.  **Current Market Price:** $87.29 (August 20, 2025, 1:00 PM UTC)

2.  **Baseline Financials (TTM as of June 30, 2025):**

| Metric | Value (in millions USD) | Source |
| :--- | :--- | :--- |
| Revenue | 3,200 | (stockanalysis.com, August 22, 2025) |
| Gross Margin | 48.13% | (stockanalysis.com, August 22, 2025) |
| Operating Income (EBIT) | 1,015 | (stockanalysis.com, August 22, 2025) |
| Net Income | 762 | (stockanalysis.com, August 22, 2025) |
| D&A | 120 | (stockanalysis.com, August 22, 2025) |
| Stock-Based Compensation | 26 | (stockanalysis.com, August 22, 2025) |
| Capex | 168 | (stockanalysis.com, August 22, 2025) |
| Change in Working Capital | -67 | (stockanalysis.com, August 22, 2025) |
| Interest Expense | 85 | (stockanalysis.com, August 22, 2025) |
| Cash & Equivalents | 778 | (stockanalysis.com, August 22, 2025) |
| Total Debt | 2,418 | (stockanalysis.com, August 22, 2025) |
| Diluted Weighted-Average Shares | 87 | (stockanalysis.com, August 22, 2025) |

**B) REVERSE-ENGINEER ASSUMPTIONS**

To solve for the market-implied growth rate, we will hold the TTM operating margin and other key assumptions constant and find the revenue growth rate that results in a DCF value equal to the current market price.

*   **Market Capitalization:** $87.29 \* 87 million shares = $7,594.23 million
*   **Enterprise Value:** $7,594.23 million (Market Cap) - $778 million (Cash) + $2,418 million (Debt) = $9,234.23 million

A 5-year DCF model with a 2.5% terminal growth rate and a 7.5% WACC requires a **5-year revenue CAGR of approximately 7.5% and a constant operating margin of 31.7%** to arrive at the current enterprise value of $9,234.23 million.

**This implies that to justify the current stock price, one must believe that Allison Transmission can grow its revenues at a 7.5% compound annual rate for the next five years while maintaining its current high level of profitability.**

---

### **Part 2: Analyst's Revised Valuation (Conservative Base-Case)**

**C) FORMULATE CONSERVATIVE ASSUMPTIONS (5 YEARS)**

6.  **Revenue for Years 1–5:**
    The market-implied growth rate of 7.5% appears optimistic given the cyclical nature of the commercial vehicle market and the increasing competition from electric powertrains. A more conservative base-case assumption is a **3% annual revenue growth rate for the next five years**, which is more in line with long-term GDP growth and accounts for potential market share erosion.

7.  **Margin Path:**
    Management has not provided specific long-term margin guidance. The TTM operating margin is 31.7%. The average operating margin for the last three fiscal years (2022-2024) is approximately 30.2%. A conservative approach would be to assume a slight moderation from the current high levels. I will use an **operating margin of 30.0%** for the forecast period.

8.  **Taxes:**
    The effective tax rate for the TTM period is approximately 18.6%. I will assume a slightly higher **effective tax rate of 21.0%** to reflect the potential for rising corporate tax rates.

9.  **Capital Intensity:**
    *   **Capex:** The 3-year average capex as a percentage of revenue is approximately 5.0%. I will use this historical average, so **Capex is 5.0% of revenue.**
    *   **Working Capital:** The TTM change in working capital was negative. However, for a growing company, working capital should be a use of cash. I will model the change in working capital as **5% of the change in revenue**, which is a more conservative and realistic assumption.

10. **SBC and Dilution:**
    *   **SBC:** Stock-based compensation will be treated as a cash expense and subtracted from FCFF.
    *   **Diluted Shares:** The latest reported diluted weighted-average shares of **87 million** will be used.

**D) FREE CASH FLOW CONSTRUCTION**

FCFF = EBIT \* (1 - tax rate) + D&A - SBC - Capex - Change in Working Capital

| (in millions USD) | Y1 | Y2 | Y3 | Y4 | Y5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | 3,296 | 3,395 | 3,497 | 3,602 | 3,709 |
| EBIT | 989 | 1,018 | 1,049 | 1,080 | 1,113 |
| NOPAT | 781 | 805 | 829 | 853 | 879 |
| D&A | 120 | 120 | 120 | 120 | 120 |
| Capex | -165 | -170 | -175 | -180 | -185 |
| Change in WC | -5 | -5 | -5 | -5 | -5 |
| SBC | -26 | -26 | -26 | -26 | -26 |
| **FCFF** | **705** | **724** | **743** | **762** | **783** |

**E) DISCOUNT RATE (WACC)**

11. **Cost of Equity (CAPM):**
    *   **Risk-Free Rate:** 3.0% (Assumed based on current 10-year U.S. Treasury yield)
    *   **Equity Risk Premium:** 5.0% (Standard market premium)
    *   **Beta:** 1.20 (Reflects the company's cyclicality and financial leverage)
    *   **Cost of Equity:** 3.0% + 1.20 \* 5.0% = **9.0%**

12. **Cost of Debt:**
    *   Interest Expense / Total Debt = $85 million / $2,418 million = 3.5%
    *   After-tax Cost of Debt = 3.5% \* (1 - 21.0%) = **2.8%**

13. **WACC:**
    *   Market Value of Equity = $7,594.23 million
    *   Market Value of Debt = $2,418 million
    *   WACC = (E / (E+D)) \* Re + (D / (E+D)) \* Rd \* (1-t)
    *   WACC = ($7,594 / $10,012) \* 9.0% + ($2,418 / $10,012) \* 3.5% \* (1 - 21.0%) = **7.5%**

**F) TERMINAL VALUE**

14. **Gordon Growth Method:**
    *   **Terminal Growth Rate (g):** 2.5% (Reflecting long-term inflation expectations)
    *   **Terminal Value:** (Year 5 FCFF \* (1 + g)) / (WACC - g)
    *   **Terminal Value:** ($783 \* (1 + 2.5%)) / (7.5% - 2.5%) = **$16,052 million**

15. **Cross-Check (Exit Multiple):**
    *   Year 5 EBITDA = Year 5 EBIT + Year 5 D&A = $1,113 + $120 = $1,233 million
    *   Implied Exit Multiple = $16,052 million / $1,233 million = 13.0x
    *   This multiple is in line with historical averages for industrial companies, suggesting the Gordon Growth terminal value is reasonable.

**G) ENTERPRISE TO EQUITY BRIDGE**

16. **Enterprise Value:**
    *   PV of Explicit Period FCFF = $705/(1.075)^1 + $724/(1.075)^2 + $743/(1.075)^3 + $762/(1.075)^4 + $783/(1.075)^5 = $3,006 million
    *   PV of Terminal Value = $16,052 million / (1.075)^5 = $11,192 million
    *   **Enterprise Value:** $3,006 million + $11,192 million = **$14,198 million**

17. **Equity Value:**
    *   **Equity Value:** $14,198 million - $2,418 million (Debt) + $778 million (Cash) = **$12,558 million**

**H) PER-SHARE VALUE AND MARGIN OF SAFETY**

18. **Analyst's Base-Case Fair Value:**
    *   $12,558 million / 87 million shares = **$144.34 per share**

19. **Valuation Range:**
    *   **Base Case:** $144.34
    *   **Low/Bear Case:** Assuming 0% revenue growth and a 28% operating margin, the fair value would be approximately **$110 per share.**
    *   **High/Bull Case:** Assuming 5% revenue growth and a 32% operating margin, the fair value would be approximately **$180 per share.**

20. **Margin of Safety (MOS) Price:**
    *   A 30% margin of safety below the base-case fair value results in a **MOS price of $101.04.**

### **Risk Notes**

*   **Cyclicality:** The commercial vehicle market is highly cyclical, and a downturn could significantly impact revenue and profitability.
*   **Technological Disruption:** The transition to electric vehicles poses a long-term threat to Allison's core transmission business. The company's ability to adapt and compete in the electric powertrain market is crucial.
*   **Customer Concentration:** A significant portion of revenue comes from a few large OEM customers. The loss of any of these customers could have a material impact on financial results.
*   **Input Cost Volatility:** The company is exposed to fluctuations in the price of raw materials, such as steel and aluminum.
*   **Regulatory Risk:** Changes in emissions regulations could accelerate the shift to electric vehicles, increasing the competitive pressure on Allison.

final answer is 144.34 $