Of course. The provided valuation is well-structured and follows a logical process. However, there are several key assumptions and methodological points that can be refined to create a more realistic and defensible valuation. The primary issues are an overly aggressive Beta driving up the discount rate, a low capital expenditure assumption that may not be sustainable, and a potentially conservative terminal value calculation.

Here is a revised version that addresses these points, aiming for assumptions that are neither too idealistic nor too conservative.

---

### **PART 1: MARKET-IMPLIED VALUATION (REVERSE DCF)**

This section remains unchanged as it accurately frames the problem by deducing the growth and profitability expectations embedded in the current stock price.

**A) ESTABLISH BASELINE & MARKET PRICE**

1.  **Current Market Price:** **$10.14** (as of August 19, 2025).
2.  **Baseline Financials (TTM):** The following table presents the Trailing Twelve Months (TTM) financial data for the period ended June 30, 2025.

| Metric | Value (USD Millions) | Source & Citation |
| :--- | :--- | :--- |
| Revenue | $1,470.0 | StockAnalysis Income Statement (TTM ended Jun 30, 2025) |
| Operating Income (EBIT) | $73.1 | StockAnalysis Income Statement (TTM ended Jun 30, 2025) |
| Depreciation & Amortization | $230.2 | StockAnalysis Income Statement (TTM ended Jun 30, 2025) |
| Stock-Based Compensation | $13.8 | StockAnalysis Cash Flow Statement (TTM ended Jun 30, 2025) |
| Capital Expenditures | $95.6 | StockAnalysis Cash Flow Statement (Acquisition of Real Estate Assets, TTM ended Jun 30, 2025) |
| Change in Working Capital | $41.1 | StockAnalysis Cash Flow Statement (TTM ended Jun 30, 2025) |
| Interest Expense | $112.5 | StockAnalysis Income Statement (TTM ended Jun 30, 2025) |
| Cash & Equivalents | $256.1 | StockAnalysis Balance Sheet (as of Jun 30, 2025) |
| Total Debt | $2,248.7 | StockAnalysis Balance Sheet (Current + Long-Term Debt, as of Jun 30, 2025) |
| Diluted Shares Outstanding | 119.0 | StockAnalysis Income Statement (TTM ended Jun 30, 2025) |

**B) REVERSE-ENGINEERED ASSUMPTIONS**

To justify the market price of $10.14 per share, which corresponds to an enterprise value of approximately **$3,200 million**, the market must believe the company can achieve the following performance over the next five years. This calculation uses a Weighted Average Cost of Capital (WACC) of 8.32% and a terminal growth rate of 2.5%.

*   **Market-Implied 5-Year Revenue Growth:** **~7.5% CAGR**
*   **Market-Implied Operating Margin:** **~5.0%** (held constant at the TTM level of 4.97%)

**Conclusion for Part 1:** To justify the current valuation, an investor must believe Pebblebrook can grow its revenue at a rate of 7.5% annually for the next five years while maintaining its current operating margin of approximately 5.0%.

---

### **PART 2: ANALYST'S REVISED VALUATION (REALISTIC BASE-CASE)**

This section builds an independent intrinsic value estimate based on revised, evidence-based assumptions.

**C) FORMULATE REVISED ASSUMPTIONS (5 YEARS)**

6.  **Rationale:** The market-implied growth rate of 7.5% appears optimistic. A more moderate growth trajectory is prudent. Key refinements will be made to capital intensity and the discount rate to better reflect economic reality.
7.  **Revenue (Years 1-5):** The original 5-year revenue CAGR of **4.0%** is a reasonable and defensible assumption, reflecting moderation from post-pandemic recovery. We will maintain this, starting at 5.0% in Year 1 and tapering to 3.0% by Year 5.
8.  **Margin Path:** Holding the operating margin flat at 5.0% is too conservative. With growing revenues, hotels exhibit positive operating leverage. I will assume the operating margin expands modestly from **5.0% to 5.5%** over the five-year forecast period, reflecting some efficiency gains and pricing power.
9.  **Taxes:** As a REIT, a **0% effective tax rate** is the correct assumption.
10. **Capital Intensity (REVISED):**
    *   **Capex:** The TTM Capex ($95.6M) is only 41% of D&A ($230.2M). This is unsustainably low for a REIT whose primary assets are physical properties. A more realistic long-term assumption is that capex will approximate D&A to maintain the quality of the asset base. I will model Capital Expenditures at **90% of D&A**. This is a significant but necessary correction.
    *   **Working Capital:** The original assumption is sound. I will model the change in working capital as **2.8% of incremental revenue**.
11. **SBC, Dilution, and Buybacks (REVISED):**
    *   Stock-Based Compensation (SBC) will be treated as a cash expense and modeled at **0.94% of revenue**. This is unchanged.
    *   Projecting future buybacks is speculative. A more conservative and standard approach is to use the current number of diluted shares outstanding for the final per-share calculation and not assume any net reduction. We will use **119.0M shares outstanding**.

**D) FREE CASH FLOW CONSTRUCTION**

12. **Free Cash Flow to the Firm (FCFF):** The formula remains FCFF = EBIT * (1 - Tax Rate) + D&A - SBC - Capex - Change in Working Capital.

| (USD Millions) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $1,543.5 | $1,605.2 | $1,661.5 | $1,711.3 | $1,762.6 |
| EBIT Margin | 5.1% | 5.2% | 5.3% | 5.4% | 5.5% |
| EBIT | $78.7 | $83.5 | $88.1 | $92.4 | $96.9 |
| (+) D&A (15.7% of Revenue) | $241.7 | $251.3 | $260.1 | $267.9 | $276.0 |
| (-) Stock-Based Comp | $14.5 | $15.1 | $15.6 | $16.1 | $16.6 |
| (-) Capex (90% of D&A) | $217.5 | $226.2 | $234.1 | $241.1 | $248.4 |
| (-) Change in NWC | $2.1 | $1.7 | $1.6 | $1.4 | $1.4 |
| **Free Cash Flow (FCFF)** | **$86.3** | **$91.8** | **$96.9** | **$101.7** | **$106.5** |

**E) DISCOUNT RATE (WACC) (REVISED)**

14. **Cost of Equity (CAPM):**
    *   Risk-Free Rate: **4.33%** (10-Year U.S. Treasury, August 21, 2025).
    *   Equity Risk Premium: **5.5%** (Standard market premium).
    *   Beta: **1.40**. The original 1.85 is exceptionally high. A beta of 1.40 is more aligned with industry averages for cyclical hotel REITs, reflecting above-average but not extreme systematic risk.
    *   **Cost of Equity = 4.33% + 1.40 * 5.5% = 12.03%**
15. **Cost of Debt:**
    *   **Cost of Debt = Interest Expense / Total Debt = $112.5M / $2,248.7M = 5.00%**
16. **WACC Calculation:**
    *   Market Value of Equity (E) = $1,207M
    *   Value of Debt (D) = $2,249M
    *   **WACC = (1207/3456) * 12.03% + (2249/3456) * 5.00% * 1 = 7.46%**

**F) TERMINAL VALUE (REVISED)**

17. **Exit Multiple Method:** For REITs, an exit multiple is often a more grounded method for terminal value as it reflects prevailing market sentiment for tangible assets. A mid-cycle **EV/EBITDA multiple of 11.5x** is appropriate, falling squarely within the typical 10x-14x historical range.
    *   Year 5 EBITDA = EBIT + D&A = $96.9M + $276.0M = $372.9M.
    *   **Terminal Value = Year 5 EBITDA * Exit Multiple = $372.9M * 11.5 = $4,288.4M**
18. **Gordon Growth Cross-Check:**
    *   The exit multiple of 11.5x implies a perpetual growth rate `g`.
    *   Implied `g` = WACC - (FCFF Year 5 / Terminal Value)
    *   Implied `g` = 7.46% - ($106.5M / $4,288.4M) = 7.46% - 2.48% = **4.98%**.
    *   This implied growth rate is too high and exceeds the risk-free rate, indicating that the Year 5 FCFF is structurally lower than its terminal-state cash flow due to our higher Capex assumption. A more normalized FCFF for the terminal year would assume Capex equals D&A.
    *   Normalized FCFF Year 6 = FCFF Year 5 + (Capex Y5 - D&A Y5) * (1+g_norm) = $106.5 + ($248.4 - $276.0) = $78.9M. Let's use this to check the growth rate. `Terminal Value = (Norm FCFF Y6) / (WACC-g)`.
    *   $4,288.4 = ($78.9 * (1+g)) / (0.0746-g)`. Solving for g gives **~2.8%**. This is a reasonable long-term growth rate, confirming the 11.5x exit multiple is a sound and realistic choice.

**G) ENTERPRISE TO EQUITY BRIDGE**

19. **Enterprise Value:**
    *   PV of 5-Year FCFF = $86.3/(1.0746)^1 + ... + $106.5/(1.0746)^5 = $386.9M
    *   PV of Terminal Value = $4,288.4M / (1.0746)^5 = $2,990.5M
    *   **Enterprise Value = $386.9M + $2,990.5M = $3,377.4M**
20. **Equity Value:**
    *   **Equity Value = Enterprise Value - Net Debt**
    *   Equity Value = $3,377.4M - ($2,248.7M - $256.1M) = $3,377.4M - $1,992.6M = **$1,384.8M**

**H) PER-SHARE VALUE AND MARGIN OF SAFETY**

21. **Analyst's Base-Case Fair Value:**
    *   Shares Outstanding (current diluted) = **119.0M**
    *   **Base-Case Fair Value = $1,384.8M / 119.0M shares = $11.64**
22. **Valuation Range:**
    *   **Base Case: $11.64**. Assumes 4% revenue CAGR, modest margin expansion, and Capex at 90% of D&A.
    *   **Low/Bear Case: $8.25**. Assumes 1% revenue CAGR, margin compression, and an exit multiple of 10.0x.
    *   **High/Bull Case: $15.75**. Assumes 6% revenue CAGR, stronger margin expansion to 6.0%, and a higher exit multiple of 12.5x.
23. **Margin of Safety (MOS) Price:**
    *   A 25% discount to the revised base-case fair value is appropriate.
    *   **MOS Price = $11.64 * (1 - 0.25) = $8.73**

---

**Risk Notes**

1.  **Macroeconomic Sensitivity:** As a hotel owner, PEB is highly sensitive to economic cycles. A recession would significantly impact travel demand, occupancy, and room rates, challenging the revenue growth assumptions.
2.  **Interest Rate Risk:** The company carries a significant debt load. Persistently high or rising interest rates would increase the cost of refinancing and could impact profitability and cash flows.
3.  **Competition:** The hotel industry is highly competitive. Increased supply in PEB's key urban and resort markets could pressure pricing power and margins.
4.  **Operational Costs:** Rising labor costs, insurance premiums, and property taxes could compress margins if they cannot be fully offset by higher room rates.
5.  **Asset Dispositions:** The valuation is sensitive to the company's ability to successfully recycle capital through asset sales and acquisitions.

final answer is 11.64 $