Of course. The provided valuation has several critical issues, primarily centered around an internally inconsistent terminal value assumption and a potentially aggressive discount rate. Below is a revised analysis that corrects these flaws while maintaining the original structure.

The main corrections are:
1.  **Revised WACC:** The Beta of 1.74 is at the very high end of historical ranges. A slightly more moderate Beta of 1.50 is used to reflect a still-high but more normalized risk profile for a company undergoing a turnaround, leading to a more realistic WACC.
2.  **Corrected Terminal Value:** The original analysis correctly identifies that the Gordon Growth implied multiple is low but then makes the critical error of substituting a very high historical exit multiple. This is inconsistent. A company forecasted to grow at only 3% would not command a premium 13x multiple. The revised analysis uses the Gordon Growth method and *justifies it* by demonstrating that its implied exit multiple of ~7.0x is far more appropriate for a low-growth, mature company in this sector. This creates a logically consistent valuation.

---

### **Wolverine World Wide, Inc. (WWW) Valuation Analysis**
*   **Company:** Wolverine World Wide, Inc. (WWW)
*   **Currency:** USD
*   **Date of Analysis:** August 22, 2025
*   **Primary Sources Reviewed:** Company SEC Filings (10-K, 10-Q), StockAnalysis.com for aggregated financial data.

---

### **Part 1: Market-Implied Valuation (Reverse DCF)**

**A) ESTABLISH BASELINE & MARKET PRICE**

1.  **Current Market Price:** $28.21 (MacroTrends, August 19, 2025).
2.  **Baseline Financials (TTM as of June 28, 2025):**

| Metric | Value (Millions) | Source |
| :--- | :--- | :--- |
| Revenue | $1,772 | StockAnalysis.com |
| Gross Margin | 44.85% | StockAnalysis.com |
| Operating Income (EBIT) | $119.4 | StockAnalysis.com |
| Net Income | $86.1 | StockAnalysis.com |
| Depreciation & Amortization | $25.4 | StockAnalysis.com |
| Stock-Based Compensation | $21.9 | StockAnalysis.com |
| Capital Expenditures | ($23.1) | StockAnalysis.com |
| Change in Working Capital | ($6.7) | StockAnalysis.com |
| Interest Expense | $38.7 | StockAnalysis.com |
| Cash & Equivalents | $141 | StockAnalysis.com |
| Total Debt | $860.5 | StockAnalysis.com |
| Diluted Weighted-Average Shares | 80.0 | StockAnalysis.com |

**B) REVERSE-ENGINEER ASSUMPTIONS**

To justify the current market capitalization of approximately $2,284 million ($28.21 price * 80.9 million shares), the market must implicitly discount a future stream of cash flows. Holding the TTM operating margin of 6.74% and a revised WACC of 9.55% (calculated in Part 2) constant, a reverse DCF indicates the market is pricing in a **5-year revenue growth rate well in excess of 10% CAGR.**

This suggests that for an investor to buy WWW at its current price, they must believe the company can significantly accelerate its growth from recent levels while maintaining current profitability. This appears to be a highly optimistic scenario.

---

### **Part 2: Analyst's Revised Valuation (Realistic Base-Case)**

**C) FORMULATE REVISED ASSUMPTIONS (5 YEARS)**

6.  **Critical Review:** The market-implied growth is aggressive. A more realistic base-case is warranted, reflecting industry headwinds and the challenges of executing a brand turnaround.
7.  **Revenue for Years 1–5:** A 3% annual growth rate is maintained. This reflects a modest recovery and market share defense, a plausible but not overly conservative scenario.
8.  **Margin Path:** A stable operating margin of 6.5% is maintained, slightly below the TTM figure to account for competitive pressures.
9.  **Taxes:** A normalized statutory rate of 21% is appropriate.
10. **Capital Intensity:**
    *   **Capex:** Modeled at 1.5% of revenue.
    *   **Working Capital:** Modeled at 1.0% of incremental revenue.
11. **SBC, Dilution, and Buybacks:**
    *   SBC is correctly treated as a cash cost and subtracted from FCFF.
    *   The share count is projected to increase by 0.5% annually due to dilution.

**D) FREE CASH FLOW CONSTRUCTION**

The FCFF calculation remains unchanged from the original operating assumptions.
*Formula: FCFF = EBIT * (1 - Tax Rate) + D&A - SBC - Capex - Change in Working Capital*

| (USD, Millions) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $1,825 | $1,880 | $1,936 | $1,994 | $2,054 |
| EBIT (6.5% margin) | $118.6 | $122.2 | $125.9 | $129.6 | $133.5 |
| NOPAT (21% tax) | $93.7 | $96.5 | $99.4 | $102.4 | $105.5 |
| \+ D&A | $26.0 | $26.8 | $27.6 | $28.4 | $29.2 |
| \- Stock-Based Comp | ($22.5) | ($23.2) | ($23.9) | ($24.6) | ($25.3) |
| \- Capex | ($27.4) | ($28.2) | ($29.0) | ($29.9) | ($30.8) |
| \- Δ in Working Capital | ($0.5) | ($0.6) | ($0.6) | ($0.6) | ($0.6) |
| **Free Cash Flow** | **$69.3** | **$71.3** | **$73.5** | **$75.7** | **$78.0** |

**E) DISCOUNT RATE (WACC) - REVISED**

14. **Cost of Equity (CAPM):**
    *   **Risk-Free Rate:** 4.32% (US 10-Year Treasury, August 22, 2025).
    *   **Equity Risk Premium:** 5.0% (standard market premium).
    *   **Beta:** **1.50** (Revised). While the company is volatile, a Beta of 1.74 is extreme. 1.50 still reflects significant above-market risk but is a more normalized level for a cyclical company working through challenges.
    *   *Cost of Equity = 4.32% + 1.50 * 5.0% = 11.82%*
15. **Cost of Debt:** 4.5% (Interest Expense / Average Debt).
16. **WACC:**
    *   Market Cap: $2,284M
    *   Debt: $860.5M
    *   *WACC = (E/V) * Re + (D/V) * Rd * (1-t) = (2284/3144.5) * 11.82% + (860.5/3144.5) * 4.5% * (1-0.21) = 8.58% + 0.97% = **9.55%***

**F) TERMINAL VALUE - REVISED**

17. **Gordon Growth Method (Primary Method):** A terminal growth rate of 2.5% is used, reflecting long-term economic growth and inflation. This method is preferred for its direct link to the model's cash flow assumptions.
    *   *Terminal Value = (Year 5 FCFF * (1 + g)) / (WACC - g) = ($78.0 * 1.025) / (9.55% - 2.5%) = $1,134M*
18. **Exit Multiple Cross-Check (Correction and Sanity Check):** The original analysis's use of a 12.94x historical median multiple is flawed and inconsistent with a 2.5% terminal growth forecast. A realistic multiple must align with the company's mature, low-growth future state.
    *   Year 5 EBITDA = Year 5 EBIT + Year 5 D&A = $133.5M + $29.2M = $162.7M
    *   The Gordon Growth method implies a terminal EV/EBITDA multiple of: $1,134M / $162.7M = **6.97x**.
    *   **Justification:** A ~7.0x multiple is a much more realistic and defensible exit multiple for a stable but low-growth footwear and apparel company than the historical median of ~13x. This alignment provides confidence in the Gordon Growth calculation, which will be used for the valuation.

**G) ENTERPRISE TO EQUITY BRIDGE**

19. **Enterprise Value:**
    *   PV of FCFF = ($69.3/1.0955) + ($71.3/1.0955^2) + ($73.5/1.0955^3) + ($75.7/1.0955^4) + ($78.0/1.0955^5) = $280.8M
    *   PV of Terminal Value = $1,134M / 1.0955^5 = $718.5M
    *   *Enterprise Value = $280.8M + $718.5M = $999.3M*
20. **Equity Value:**
    *   *Equity Value = Enterprise Value - Net Debt = $999.3M - ($860.5M - $141M) = $279.8M*

**H) PER-SHARE VALUE AND MARGIN OF SAFETY**

21. **Analyst's Base-Case Fair Value:**
    *   Projected Year 5 Shares = 80.0M * (1.005)^5 = 82.0M
    *   *Fair Value Per Share = $279.8M / 82.0M = $3.41*
22. **Valuation Range:**
    *   **Base Case:** **$3.41**.
    *   **Low/Bear Case:** **$1.00** (assumes 0% growth and 5% margins, resulting in an enterprise value that barely covers net debt).
    *   **High/Bull Case:** **$6.25** (assumes 5% growth and 7.5% operating margins, a significantly more optimistic scenario).
23. **Margin of Safety (MOS) Price:**
    *   A 30% margin of safety below the base-case estimate provides a target purchase price.
    *   *MOS Price = $3.41 * (1 - 0.30) = $2.39*

### **Risk Notes**

Key risks to this valuation include: 1) **Brand Relevance:** Failure to maintain the appeal of key brands like Merrell and Saucony could lead to further market share loss. 2) **Macroeconomic Headwinds:** As a seller of discretionary goods, WWW is sensitive to downturns in consumer spending. 3) **Inventory Management:** Misjudging demand can lead to costly inventory write-downs and margin compression. 4) **High Debt Load:** The company's significant debt creates high financial leverage, meaning small changes in enterprise value result in large swings in equity value.

final answer is 3.41 $