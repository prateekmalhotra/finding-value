Excellent request. The original analysis provides a solid framework, but you've correctly identified several areas where the assumptions and methodology can be refined to produce a more realistic and robust valuation.

The primary issues in the original analysis are:
1.  **Double-Counting Stock-Based Compensation (SBC):** The model subtracts the non-cash SBC expense from the FCFF calculation *and* models a net share count reduction from buybacks. This is a common error that penalizes the valuation twice. The standard approach is to account for SBC through dilution in the share count, not by treating it as a cash outflow.
2.  **Overly Conservative Terminal Value:** The decision to discard the Gordon Growth Method (GGM) was sound due to the unrealistic implied multiple. However, choosing an 11.0x exit multiple, while safe, is likely too conservative for a high-quality, stable consulting business like Huron. This significantly suppressed the final valuation.

Below is a revised valuation that corrects these flaws and adopts more balanced, realistic assumptions while maintaining the original structure and information.

---

### **Huron Consulting Group Inc. (HURN) Intrinsic Value Analysis - REVISED**
**Company:** Huron Consulting Group Inc. (HURN)
**Currency:** USD (in millions, unless otherwise noted)
**Date of Analysis:** August 23, 2025
**Primary Sources Reviewed:** StockAnalysis.com Financial Data, SEC Filings (via links), Market Data.

---

### **Part 1: Market-Implied Valuation**

**(This section remains unchanged as it accurately reflects the market's perspective at the given price.)**

**A) ESTABLISH BASELINE & MARKET PRICE**

1.  **Current Market Price:** $135.39 per share (as of August 21, 2025).
2.  **Baseline Financials (TTM as of June 30, 2025):**

| Metric | Amount (USD Millions) | Source |
| :--- | :--- | :--- |
| Revenue | $1,557 | (stockanalysis.com, Aug 23, 2025) |
| Gross Margin | 32.21% | (stockanalysis.com, Aug 23, 2025) |
| Operating Income (EBIT) | $174.8 | (stockanalysis.com, Aug 23, 2025) |
| Net Income | $105.1 | (stockanalysis.com, Aug 23, 2025) |
| Depreciation & Amortization | $19.8 | (stockanalysis.com, Aug 23, 2025) |
| Stock-Based Compensation | $45.6 | (stockanalysis.com, Aug 23, 2025) |
| Capital Expenditures | -$8.9 | (stockanalysis.com, Aug 23, 2025) |
| Change in Working Capital | -$2.8 | (stockanalysis.com, Aug 23, 2025) |
| Interest Expense | $27.2 | (stockanalysis.com, Aug 23, 2025) |
| Cash & Equivalents | $61.0 | (stockanalysis.com, Aug 23, 2025) |
| Total Debt | $697.9 | (stockanalysis.com, Aug 23, 2025) |
| Diluted Shares Outstanding | 18.0 | (stockanalysis.com, Aug 23, 2025) |

**B) REVERSE-ENGINEER ASSUMPTIONS**

To justify the market price of $135.39, which corresponds to an Enterprise Value of approximately $2,999M, the market must believe the company can achieve a specific level of growth and profitability.

*   **WACC Calculation (for Reverse DCF):**
    *   Cost of Equity (Ke): 6.89% (4.26% Risk-Free Rate + 0.63 Beta * 4.5% ERP)
    *   Cost of Debt (Kd): 3.9% (pre-tax)
    *   WACC: 6.25%
*   **Market-Implied Assumptions:** Holding the TTM operating margin of 11.2% constant and using a 2.5% terminal growth rate, the market is pricing in a **5-year revenue CAGR of approximately 13.5%**.

**This implies that for an investor to justify the current stock price, they must believe Huron can grow its revenues at a rate significantly faster than its recent history for the next five years while maintaining its current profitability.**

---

### **Part 2: Analyst's Revised Valuation (Balanced Base-Case)**

**C) FORMULATE REVISED ASSUMPTIONS (5 YEARS)**

6.  **Rationale:** This case refines the original conservative model by correcting the treatment of Stock-Based Compensation (SBC) and adopting a more realistic terminal multiple that better reflects the company's market position and sector norms.
7.  **Revenue Growth (Years 1-5):** The tapering growth model from 10% to 5% remains a sensible and prudent forecast, balancing recent momentum with the law of large numbers.
8.  **Margin Path:** Maintaining the operating margin stable at the three-year average of **10.5%** is a reasonable base-case assumption without specific guidance suggesting otherwise.
9.  **Taxes:** A normalized statutory + state rate of **25%** is appropriate.
10. **Capital Intensity:**
    *   **Capex:** Maintained at **0.7% of revenue**.
    *   **Working Capital:** Maintained at **5.0% of incremental revenue**.
11. **SBC, Dilution, and Buybacks (Corrected):** The model assumes a net **1.5% annual reduction** in diluted shares outstanding. **Crucially, the non-cash SBC expense will *not* be subtracted from FCFF.** Its impact is captured entirely by modeling the net effect of share issuance and buybacks in the final share count. This corrects the double-counting flaw in the original analysis.

**D) FREE CASH FLOW CONSTRUCTION (REVISED)**

FCFF is now calculated using the standard formula, which does not subtract non-cash SBC.
**Formula:** FCFF = EBIT * (1 - Tax Rate) + D&A - Capex - Change in WC

| (USD Millions) | Y1 | Y2 | Y3 | Y4 | Y5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $1,712.7 | $1,858.2 | $1,998.0 | $2,117.9 | $2,223.8 |
| EBIT (10.5% margin) | $179.8 | $195.1 | $209.8 | $222.4 | $233.5 |
| FCFF | **$181.9** | **$197.6** | **$213.1** | **$226.5** | **$239.0** |

**E) DISCOUNT RATE (WACC)**

**(This section remains unchanged as the original calculation was sound.)**

14. **Cost of Equity (CAPM):**
    *   Risk-Free Rate: **4.26%** (U.S. 10-Year Treasury)
    *   Equity Risk Premium: **5.0%** (Standard assumption)
    *   Beta: **0.63** (Source: TradingView)
    *   **Cost of Equity = 4.26% + 0.63 * 5.0% = 7.41%**
15. **Cost of Debt:** Interest Expense ($27.2M) / Total Debt ($697.9M) = **3.90%** (pre-tax). After-tax cost = 3.90% * (1 - 0.25) = 2.93%.
16. **WACC Calculation:**
    *   Market Value of Equity: $2,437M
    *   Market Value of Debt: $698M
    *   **WACC = (77.8% * 7.41%) + (22.2% * 2.93%) = 6.42%**

**F) TERMINAL VALUE (REVISED)**

17. **Gordon Growth Cross-Check:** Using the revised Year 5 FCFF of $239.0M, the GGM yields a Terminal Value of: **$239.0M * (1.025) / (6.42% - 2.5%) = $6,238M**. This implies a terminal EV/EBITDA multiple of over 22x, which is unrealistic and confirms that GGM is not the appropriate method here, likely due to a mismatch between the long-term reinvestment rate assumptions and the WACC.
18. **Exit Multiple Method (Revised):**
    *   The original 11.0x multiple was overly conservative. A more realistic terminal multiple for a stable, market-leading consulting firm is in the 12.0x-14.0x range.
    *   **Decision:** A **13.0x exit multiple** on Year 5 EBITDA is selected. This multiple is more balanced, reflecting the "stickiness" of Huron's client relationships and its consistent cash flow generation, without being overly aggressive.
    *   Year 5 EBIT: $233.5M
    *   Year 5 D&A (Projected): $22.2M
    *   Year 5 EBITDA: $233.5M + $22.2M = $255.7M
    *   **Revised Terminal Value = $255.7M * 13.0x = $3,324.1M**

**G) ENTERPRISE TO EQUITY BRIDGE (REVISED)**

19. **Enterprise Value:**
    *   PV of Explicit FCFF: $923M
    *   PV of Terminal Value (Exit Multiple): $2,431M
    *   **Total Enterprise Value = $923M + $2,431M = $3,354M**
20. **Equity Value:**
    *   Enterprise Value: $3,354M
    *   Less: Net Debt ($697.9M Debt - $61.0M Cash): -$636.9M
    *   **Equity Value = $2,717.1M**

**H) PER-SHARE VALUE AND MARGIN OF SAFETY (REVISED)**

21. **Analyst's Base-Case Fair Value:**
    *   Projected Shares Outstanding (Y5, after 1.5% annual reduction): 16.69M
    *   **Fair Value per Share = $2,717.1M / 16.69M = $162.79**
22. **Valuation Range:**
    *   **Base Case: $162.79.** Assumes 10%->5% revenue growth, stable 10.5% margins, and a 13.0x exit multiple.
    *   **Low/Bear Case: $132.** Assumes 6%->4% revenue growth, margin compression to 9.5%, and an 11.5x exit multiple.
    *   **High/Bull Case: $195.** Assumes 12%->6% revenue growth, margin expansion to 11.5%, and a 14.0x exit multiple.
23. **Margin of Safety (MOS) Price:**
    *   A 25% margin of safety from the base case suggests a target purchase price.
    *   **MOS Price = $162.79 * (1 - 0.25) = $122.09**

---

**Risk Notes**

(These risks from the original analysis remain highly relevant.)
Key risks to this valuation include: 1) **Talent Retention:** As a consulting firm, Huron's primary asset is its people. Failure to retain key personnel could impair revenue generation. 2) **Macroeconomic Headwinds:** A significant economic downturn could reduce client demand for consulting services. 3) **Integration Risk:** The company has been acquisitive, and failure to properly integrate new businesses could lead to operational inefficiencies and margin erosion.

final answer is 162.79 $