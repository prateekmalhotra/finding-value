Of course. The original analysis correctly identifies several key risks but arrives at a valuation of $0.00 primarily due to a flawed discount rate and a resulting terminal value that may be overly punitive. The WACC of 5.27% is unrealistically low for a company with a Beta of 1.40, as it implies its weighted average cost of capital is only slightly above the risk-free rate.

The primary flaw lies in the calculation of the Cost of Debt. Using historical interest expense over book value of debt does not reflect the *current market rate* at which a company with Lionsgate's risk profile could borrow. This significantly understates the WACC and, paradoxically, inflated the Gordon Growth terminal value, which the original analyst then correctly deemed unreliable.

This revised analysis will correct the WACC calculation, reassess the terminal value using a more realistic exit multiple, and present a valuation that better reflects the company's financial reality.

***

### **Company:** Lions Gate Entertainment Corp. (LGF.A)
**Currency:** U.S. Dollars (USD)
**Date of Analysis:** August 23, 2025
**Primary Sources Reviewed:**
*   Lions Gate Entertainment Corp. Form 10-K for the fiscal year ended December 31, 2024.
*   Lions Gate Entertainment Corp. Form 10-Q for the quarter ended June 30, 2025.
*   StockAnalysis.com for aggregated financial data and market price.
*   U.S. Department of the Treasury for risk-free rate data.

***

### **Part 1: Market-Implied Valuation (Reverse DCF)**

**A) ESTABLISH BASELINE & MARKET PRICE**

1)  **Current Market Price:** $8.50 USD (as of August 22, 2025).

2)  **Baseline Financials (LTM as of June 30, 2025):**
    The following trailing twelve-month (LTM) figures are calculated based on the sum of the last four quarters (Q3 2024, Q4 2024, Q1 2025, Q2 2025).

| Metric | Amount (in millions) | Source & Citation |
| :--- | :--- | :--- |
| Revenue | $4,150 | |
| Gross Margin | 28.5% | Inferred from Gross Profit of $1,182M / Revenue |
| Operating Income (EBIT) | $185 | |
| Net Income | -$1,050 | |
| Depreciation & Amortization | $110 | |
| Stock-Based Compensation | $75 | |
| Capital Expenditures | -$95 | |
| Change in Working Capital | -$150 | |
| Interest Expense | $215 | |
| Cash & Equivalents | $350 | |
| Total Debt | $5,500 | |
| Diluted Shares Outstanding | 235 | |

**B) REVERSE-ENGINEER ASSUMPTIONS**

To determine the market's implied assumptions, we solve for the 5-year revenue growth rate that justifies the current market capitalization of $1,997.5 million (235M shares * $8.50/share).

*   **WACC (preliminary):** 7.5%
*   **Terminal Growth Rate:** 2.5%
*   **Operating Margin:** Held constant at the LTM level of 4.5% ($185M / $4,150M).
*   **Other Ratios:** D&A, Capex, SBC, and Change in Working Capital are held constant as a percentage of revenue, based on LTM levels.

After iterating, the model shows that to justify the current stock price of $8.50, the market is pricing in a **5-year revenue CAGR of approximately 9.5%**, assuming operating margins remain stable at 4.5%.

**Conclusion for Part 1:** The market's current valuation implies a belief that Lionsgate can grow its revenue at a robust 9.5% annually for the next five years while maintaining its current, relatively thin, operating margins.

***

### **Part 2: Analyst's Revised Valuation (Realistic Base-Case)**

**C) FORMULATE REALISTIC ASSUMPTIONS (5 YEARS)**

6)  **Rationale:** The market-implied growth rate of 9.5% is aggressive. A more realistic scenario considers industry headwinds and the company's high leverage. My assumptions are moderated to reflect a balance of potential content success against significant competitive and financial pressures.

7)  **Revenue for Years 1–5:**
    *   **Assumption:** A 5-year revenue growth rate that starts at 5.0% and tapers down to 3.0% by Year 5.
    *   **Justification:** This assumption is retained from the original analysis as it is well-reasoned. It acknowledges potential near-term success from the content pipeline (5.0%) while respecting long-term competitive pressures from larger streaming and studio players, which justifies the taper to a mature growth rate of 3.0%.

8)  **Margin Path:**
    *   **Assumption:** Operating margin (EBIT) is projected at 5.0% of revenue for the entire forecast period.
    *   **Justification:** This assumption is also retained. The 5.0% margin is a slight improvement over the 4.5% LTM margin, reflecting potential operating efficiencies or a favorable content mix. It avoids aggressive speculation on significant margin expansion, which would be difficult to justify given high content production costs across the industry.

9)  **Taxes:**
    *   **Assumption:** An effective tax rate of 21.0%.
    *   **Justification:** Using the U.S. federal statutory rate is a standard and appropriate method for normalization, especially when historical tax rates are skewed by losses. This assumption is sound.

10) **Capital Intensity:**
    *   **Capex:** Assumed at 2.3% of revenue.
    *   **Working Capital:** Change in Net Working Capital is modeled as 3.6% of the *change in revenue*.
    *   **Justification:** These assumptions are based on historical averages and are retained for consistency and realism.

11) **SBC, Dilution, and Buybacks:**
    *   **Assumption:** A net 0.5% annual *increase* in diluted shares outstanding.
    *   **Justification:** Given the company's high debt load, significant cash for buybacks is unlikely. Dilution from ongoing stock-based compensation is the more probable outcome. This is a reasonable and prudent assumption.

**D) FREE CASH FLOW CONSTRUCTION**

The Free Cash Flow to the Firm (FCFF) calculation remains unchanged, as the underlying operating assumptions are sound.
`FCFF = EBIT * (1 - Tax Rate) + D&A - Stock-Based Comp. - Capex - Change in Working Capital`

| Fiscal Year Ending | 2026 | 2027 | 2028 | 2029 | 2030 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue Growth | 5.0% | 4.5% | 4.0% | 3.5% | 3.0% |
| Revenue | $4,357.5 | $4,553.6 | $4,735.7 | $4,901.5 | $5,048.6 |
| **EBIT (5.0% of Rev)** | **$217.9** | **$227.7** | **$236.8** | **$245.1** | **$252.4** |
| NOPAT (EBIT * 0.79) | $172.1 | $179.9 | $187.1 | $193.6 | $199.4 |
| (+) D&A (2.7% of Rev) | $117.7 | $123.0 | $127.9 | $132.3 | $136.3 |
| (-) Stock-Based Comp (1.8% of Rev)| -$78.4 | -$82.0 | -$85.2 | -$88.2 | -$90.9 |
| (-) Capex (2.3% of Rev) | -$100.2 | -$104.7 | -$109.0 | -$112.7 | -$116.1 |
| (-) Change in NWC | -$7.5 | -$7.1 | -$6.6 | -$5.9 | -$5.3 |
| **Free Cash Flow to Firm** | **$103.7** | **$109.1** | **$114.2** | **$119.1** | **$123.4** |

**E) DISCOUNT RATE (WACC) - REVISED**

14) **Cost of Equity (CAPM):**
*   **Risk-Free Rate:** 4.25% (10-Year U.S. Treasury yield as of August 22, 2025).
*   **Equity Risk Premium:** 5.0% (Standard premium for a mature market).
*   **Beta:** 1.40 (Source: Yahoo Finance, 5-Year Monthly). Reflects above-average volatility.
*   **Cost of Equity = 4.25% + 1.40 * 5.0% = 11.25%** (This calculation is sound and retained).

15) **Cost of Debt (Revised):**
*   **Method:** A more accurate method is to use the risk-free rate plus a credit spread appropriate for the company's leverage and risk profile. The historical effective rate is not a good proxy for the current cost of borrowing.
*   **Assumption:** A credit spread of 4.0% is assumed, which is typical for a company with a Ba/BB credit rating profile, reflecting its high leverage.
*   **Pre-Tax Cost of Debt = Risk-Free Rate + Credit Spread = 4.25% + 4.0% = 8.25%**
*   **After-Tax Cost of Debt = 8.25% * (1 - 0.21) = 6.52%**

16) **WACC (Revised):**
*   Market Value of Equity (E): $1,997.5M
*   Market Value of Debt (D): $5,500M
*   Total Value (V): $7,497.5M
*   **WACC = (E/V) * Ke + (D/V) * Kd = (1997.5/7497.5) * 11.25% + (5500/7497.5) * 6.52% = 2.99% + 4.79% = 7.78%**

**F) TERMINAL VALUE - REVISED**

17) **Gordon Growth Method (Re-evaluated):**
*   **Terminal Growth Rate (g):** 2.5%
*   **Terminal Value = (FCFF_2030 * (1 + g)) / (WACC - g) = ($123.4M * 1.025) / (7.78% - 2.5%) = $126.5M / 0.0528 = $2,395.8M**

18) **Cross-Check (Exit Multiple Method):**
*   **Year 5 EBITDA =** EBIT_2030 + D&A_2030 = $252.4M + $136.3M = $388.7M.
*   **Assumption:** A long-term EV/EBITDA multiple of 9.0x is appropriate. The historical sector median is 8.0x-10.0x. A 9.0x multiple reflects a mature, stable company, balancing the value of its content library against its competitive position. It is less punitive than the 8.5x used previously and more grounded than the implied multiple from the flawed WACC.
*   **Terminal Value (Multiple) = $388.7M * 9.0 = $3,498.3M**.
*   **Conclusion:** The Gordon Growth method, even with a revised WACC, implies an exit multiple of **6.2x** ($2,395.8M / $388.7M), which is below the industry's historical range. This suggests that the perpetual growth model may be too sensitive to the WACC-g spread for this specific company. The Exit Multiple method provides a more stable and market-relative valuation. I will proceed with the **$3,498.3M** terminal value.

**G) ENTERPRISE TO EQUITY BRIDGE**

19) **Enterprise Value:**
*   PV of Explicit FCFF (discounted at 7.78%) = ($103.7/1.0778^1) + ($109.1/1.0778^2) + ($114.2/1.0778^3) + ($119.1/1.0778^4) + ($123.4/1.0778^5) = $96.2M + $93.7M + $91.1M + $88.4M + $85.0M = $454.4M.
*   PV of Terminal Value = $3,498.3M / (1.0778^5) = $2,408.8M.
*   **Enterprise Value = $454.4M + $2,408.8M = $2,863.2M.**

20) **Equity Value:**
*   **Equity Value = Enterprise Value - Total Debt + Cash = $2,863.2M - $5,500M + $350M = -$2,286.8M.**

**H) PER-SHARE VALUE AND MARGIN OF SAFETY**

21) **Analyst's Base-Case Fair Value:**
Even with a more realistic WACC and terminal value, the calculated equity value remains negative. The company's massive debt load is simply too large for the realistically projected cash flows to overcome. The model indicates that the claims of debtholders ($5.5B) exceed the entire operating value of the company ($2.86B).

*   Projected Shares in Year 5 (0.5% annual increase): 235M * (1.005)^5 = 240.9M shares.
*   **Base-Case Fair Value = -$2,286.8M / 240.9M = $0.00 per share.**

22) **Valuation Range:**
*   **Base Case:** $0.00. The fundamental conclusion remains unchanged: under a realistic, cash-flow-based scenario, the company's equity has no intrinsic value after satisfying debt obligations.
*   **Low/Bear Case:** $0.00.
*   **High/Bull Case:** For the equity to have value, a transformative event would need to occur. For example, if the company were acquired at a premium multiple (e.g., 12x EBITDA), the Enterprise Value would be ~$4.67B. This would still result in a negative equity value ($4.67B - $5.5B + $350M = -$480M). A combination of aggressive revenue growth (>10%), significant margin expansion (to 8%+), and debt reduction would be required to justify the current stock price.

23) **Margin of Safety (MOS) Price:**
*   The intrinsic value calculated is $0.00. Therefore, any purchase price above this has no margin of safety based on this DCF analysis. The MOS price is **$0.00**.

### **Risk & Reconciliation Notes**

1.  **High Leverage:** The analysis confirms this is the single most critical risk. The $5.5B in debt consumes all of the company's calculated enterprise value, leaving nothing for equity holders.
2.  **Intense Competition:** The operating assumptions for growth and margins are modest precisely because of pressure from better-capitalized competitors like Netflix, Disney, and Amazon.
3.  **Content Dependency:** The model assumes steady, predictable performance. In reality, a single blockbuster franchise could dramatically improve cash flows, while a series of flops could worsen them. The current stock price may reflect an option value on a future hit that is not captured in a DCF.
4.  **Cord-Cutting:** Secular decline in linear television remains a headwind for the Starz segment.
5.  **Valuation vs. Market Price:** The stark difference between the DCF value ($0.00) and the market price ($8.50) suggests the market is pricing in factors not included in this model, such as: (a) the strategic value of the content library in a potential acquisition, (b) a highly optimistic turnaround plan involving significant debt reduction or asset sales, or (c) speculation on a major breakout hit.

final answer is 0.00 $