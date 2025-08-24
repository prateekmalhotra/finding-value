Of course. This is a well-structured valuation model, but you've correctly identified several areas where the assumptions could be refined to better reflect financial reality. The key issues in the original analysis are an overly punitive treatment of Stock-Based Compensation (SBC), a potentially high WACC driven by a reactive Beta, and the resulting disconnect in the terminal value calculation.

Below is a revised valuation that addresses these points, aiming for assumptions that are neither too idealistic nor overly conservative. Changes and justifications are noted throughout.

***

### **Abercrombie & Fitch Co. (ANF) – Revised Valuation**
*   **Currency:** U.S. Dollars (USD)
*   **Date of Analysis:** August 24, 2025
*   **Primary Sources Reviewed:** SEC Filings (10-K, 10-Q), StockAnalysis.com for aggregated financial data, and public data for market inputs.

---

### **PART 1: MARKET-IMPLIED VALUATION (REVERSE DCF)**

This section is unchanged as it correctly reflects the market's perspective based on the given stock price. It serves as a solid benchmark.

**A) ESTABLISH BASELINE & MARKET PRICE**

1.  **Current Market Price:** As of August 22, 2025, the closing market price for ANF was **$175.79**.
    *   **Source:** Google Finance (accessed August 24, 2025).

2.  **Baseline Financials (LTM):** The following table represents the company's financial performance for the trailing twelve months ended May 3, 2025.

| Metric | Value (USD Millions) | Source & Derivation |
| :--- | :--- | :--- |
| Revenue | $4,475.2 | StockAnalysis.com, Sum of 4 quarters ending 2025-05-03 |
| Gross Margin | 64.1% | StockAnalysis.com, ($2,868.8M / $4,475.2M) |
| Operating Income (EBIT) | $614.9 | StockAnalysis.com, Sum of 4 quarters ending 2025-05-03 |
| *Operating Margin* | *13.7%* | *Inferred ($614.9M / $4,475.2M)* |
| Net Income | $471.1 | StockAnalysis.com, Sum of 4 quarters ending 2025-05-03 |
| Depreciation & Amortization | $119.0 | StockAnalysis.com, Sum of 4 quarters ending 2025-05-03 |
| Stock-Based Compensation | $54.8 | StockAnalysis.com, Sum of 4 quarters ending 2025-05-03 |
| Capital Expenditures | ($186.2) | StockAnalysis.com, Sum of 4 quarters ending 2025-05-03 |
| Change in Working Capital | ($128.9) | StockAnalysis.com, Sum of 4 quarters ending 2025-05-03 |
| Interest Expense | $19.9 | StockAnalysis.com, Sum of 4 quarters ending 2025-05-03 |
| Cash & Equivalents | $903.0 | StockAnalysis.com, As of 2025-05-03 |
| Total Debt | $202.9 | StockAnalysis.com, As of 2025-05-03 |
| Diluted Shares | 51.5 | StockAnalysis.com, For the quarter ended 2025-05-03 |

**B) REVERSE-ENGINEER ASSUMPTIONS**

*   **Market Capitalization:** $175.79/share * 51.5M shares = **$9,052.2M**
*   **Net Debt:** $202.9M Total Debt - $903.0M Cash = **-$700.1M** (Net Cash)
*   **Enterprise Value (EV):** $9,052.2M - $700.1M = **$8,352.1M**

*   **Conclusion on Market-Implied Assumptions:** To justify the current enterprise value of **$8,352.1M**, the market must believe that Abercrombie & Fitch Co. can achieve a **5-year revenue CAGR of approximately 11.5%** while maintaining its impressive LTM **operating margin of 13.7%**. This implies revenues reaching approximately $7,700M by the end of fiscal 2030, a significant increase from the current $4,475M.

---

### **PART 2: ANALYST'S REVISED VALUATION (REALISTIC BASE-CASE)**

This section builds a valuation using revised, evidence-based assumptions.

**C) FORMULATE REALISTIC ASSUMPTIONS (5 YEARS)**

6.  **Critical Review:** The market's implied 11.5% CAGR is aggressive. The original analyst's tapering growth and moderating margin assumptions are prudent. The primary areas for refinement are the treatment of SBC, the discount rate, and the terminal value, which appeared overly conservative.

7.  **Revenue (Years 1–5):** The assumption of tapering growth is realistic and maintained.
    *   **Assumption:** Revenue growth of **10% in Year 1, tapering down by 1.5% each year to 4% in Year 5.**

8.  **Margin Path:** The assumption of a 12.5% operating margin is a solid, realistic choice. It's below the recent peak but well above historical levels, reflecting sustained operational improvements.
    *   **Assumption:** Operating margin remains at **12.5%** for the entire 5-year forecast period.

9.  **Taxes:** Assumption maintained.
    *   **Assumption:** A long-term effective tax rate of **26%**.

10. **Capital Intensity:** Assumptions maintained.
    *   **Capex:** Assumed at **4.1% of annual revenue.**
    *   **Working Capital:** Change in Non-Cash Working Capital assumed at **3.0% of the change in revenue.**

11. **SBC, Dilution, and Buybacks:**
    *   **SBC Treatment:** Stock-based compensation is a non-cash expense. Subtracting it from FCFF while also forecasting share count reduction double-counts its impact. The correct treatment is to add it back to NOPAT (as it was subtracted to get to EBIT) and then account for its dilutive effect in the final share count. **This is a key modeling change.**
    *   **Share Count:** The 2.0% annual net reduction is a reasonable assumption, implying that the company's buyback program will more than offset the dilution caused by issuing new shares for stock-based compensation.
        *   **Assumption:** A net reduction in diluted shares outstanding of **2.0% annually**.

**D) FREE CASH FLOW CONSTRUCTION (REVISED)**

12. **FCFF Calculation:** The Free Cash Flow to the Firm (FCFF) is calculated as:
    `FCFF = EBIT * (1 - Tax Rate) + D&A - Capex - Change in Working Capital`

    *Note: SBC is a non-cash charge and is not subtracted from the cash flow calculation itself. Its economic cost is captured through the dilution side of the per-share value calculation.*

| (USD Millions) | **Year 1** | **Year 2** | **Year 3** | **Year 4** | **Year 5** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $4,922.7 | $5,341.3 | $5,715.2 | $6,029.9 | $6,271.1 |
| *Growth Rate* | *10.0%* | *8.5%* | *7.0%* | *5.5%* | *4.0%* |
| EBIT | $615.3 | $667.7 | $714.4 | $753.7 | $783.9 |
| *Operating Margin* | *12.5%* | *12.5%* | *12.5%* | *12.5%* | *12.5%* |
| NOPAT (EBIT * (1-T)) | $455.4 | $494.1 | $528.7 | $557.8 | $579.9 |
| \+ D&A (Assumed 2.5% of Rev) | $123.1 | $133.5 | $142.9 | $150.7 | $156.8 |
| \- Capex (4.1% of Rev) | ($201.8) | ($219.0) | ($234.3) | ($247.2) | ($257.1) |
| \- Change in WC | ($13.4) | ($12.6) | ($11.2) | ($9.4) | ($7.2) |
| **Free Cash Flow to Firm** | **$363.2** | **$396.1** | **$426.1** | **$451.8** | **$472.3** |

**E) DISCOUNT RATE (WACC) (REVISED)**

14. **Cost of Equity (CAPM):** `Ke = Rf + Beta * ERP`
    *   **Risk-Free Rate (Rf):** 4.25% (U.S. 10-Year Treasury Yield, August 2025).
    *   **Equity Risk Premium (ERP):** 5.0% (Standard assumption for a mature market).
    *   **Beta (β):** The 5-year beta of 1.55 reflects a period of massive turnaround volatility. For a long-term valuation, it is more appropriate to use a beta that reflects a more stable, successful company. A forward-looking beta closer to the industry average is more realistic. **We will adjust Beta to 1.35.**
    *   **Cost of Equity = 4.25% + 1.35 * 5.0% = 11.00%**

15. **Cost of Debt:** Assumption maintained.
    *   **Pre-Tax Cost of Debt:** 5.5%
    *   **After-Tax Cost of Debt = 5.5% * (1 - 26%) = 4.07%**

16. **WACC Calculation:**
    *   E (Market Value of Equity) = $9,052.2M
    *   D (Market Value of Debt) = $202.9M
    *   V (Total Value) = $9,255.1M
    *   **WACC = ($9,052.2 / $9,255.1 * 11.00%) + ($202.9 / $9,255.1 * 4.07%) = 10.76% + 0.09% = 10.85%**

**F) TERMINAL VALUE (REVISED)**

17. **Method Selection:** The original analysis correctly noted that the Gordon Growth model produced an unrealistically low implied multiple, primarily due to the high WACC. While our revised WACC of 10.85% is more reasonable, the Exit Multiple method remains a more pragmatic and common approach for specialty retailers, grounding the terminal value in market-based multiples.

18. **Exit Multiple Method:**
    *   **Year 5 EBITDA:** $783.9M (EBIT) + $156.8M (D&A) = **$940.7M**.
    *   **Exit Multiple:** A 7.5x multiple is reasonable. However, given ANF's brand strength and superior margins compared to peers, a slightly higher multiple is justifiable for a base case. A mature, well-managed specialty apparel retailer could trade in the 7x-9x range. We will use an **8.0x EV/EBITDA** multiple, reflecting confidence in the brand's long-term positioning.
    *   **Revised Terminal Value:** $940.7M * 8.0 = **$7,525.6M**.

**G) ENTERPRISE TO EQUITY BRIDGE (REVISED)**

19. **Enterprise Value:**
    *   **PV of Explicit FCFF:** ($363.2/1.1085^1) + ($396.1/1.1085^2) + ($426.1/1.1085^3) + ($451.8/1.1085^4) + ($472.3/1.1085^5) = $327.7 + $321.3 + $311.9 + $300.2 + $281.3 = **$1,542.4M**
    *   **PV of Terminal Value:** $7,525.6M / (1.1085^5) = **$4,482.5M**
    *   **Total Enterprise Value = $1,542.4M + $4,482.5M = $6,024.9M**

20. **Equity Value:**
    *   **Equity Value = Enterprise Value - Net Debt**
    *   Equity Value = $6,024.9M - (-$700.1M) = **$6,725.0M**

**H) PER-SHARE VALUE AND MARGIN OF SAFETY (REVISED)**

21. **Analyst's Base-Case Fair Value:**
    *   **Initial Diluted Shares:** 51.5M
    *   **Projected Year 5 Shares (after 2.0% annual reduction):** 51.5M * (1 - 0.02)^5 = **46.6M shares**
    *   **Base-Case Fair Value = $6,725.0M / 46.6M shares = $144.31**

22. **Valuation Range:**
    *   **Base Case: $144.31.** This assumes tapering growth, stable 12.5% margins, and an 8.0x terminal multiple.
    *   **Low/Bear Case: ~$95.** Assumes revenue growth stalls (0-2% annually), margins compress to 9.5%, and the market assigns a lower 6.5x exit multiple.
    *   **High/Bull Case: ~$190.** Assumes the company sustains higher growth for longer (8-10% annually), margins expand toward 14.0%, justifying a higher exit multiple of 9.0x.

23. **Margin of Safety (MOS) Price:** A 30% discount to the base-case fair value is prudent.
    *   **MOS Price = $144.31 * (1 - 0.30) = $101.02**

### **Risk Notes**
(These risks are well-stated and remain relevant to the revised valuation.)
1.  **Fashion/Execution Risk:** The company's success is highly dependent on anticipating fashion trends and executing its brand strategy. A misstep could quickly lead to deteriorating sales and margins.
2.  **Macroeconomic Headwinds:** As a seller of discretionary goods, ANF is vulnerable to economic downturns that reduce consumer spending on apparel.
3.  **Margin Sustainability:** The current high operating margins may not be sustainable if promotional activity increases across the industry or if input costs rise.
4.  **Competitive Pressure:** The apparel industry is intensely competitive, with pressure from fast-fashion players, online retailers, and other established brands.

final answer is 144.31 $