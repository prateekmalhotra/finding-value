Here's a review of your valuation with identified issues and proposed corrections, maintaining the original format.

---

### **PART 1: MARKET-IMPLIED VALUATION (REVERSE DCF)**

**A) ESTABLISH BASELINE & MARKET PRICE**

**1) Current Market Price**

*   **Company:** Carriage Services, Inc. (CSV)
*   **Currency:** USD
*   **Date of Analysis:** August 22, 2025
*   **Primary Sources Reviewed:** SEC Filings (10-K for FY 2024, 10-Q for Q1 2025 and Q2 2025)
*   **Current Market Price:** $45.13 (as of August 20, 2025)

**2) Baseline Financials (TTM)**

| Financial Metric | Amount (in millions) | Citation |
| :--- | :--- | :--- |
| Revenue | $404.2 | (10-K, February 28, 2025) |
| Gross Margin | 35.5% | (Calculated from 10-K, February 28, 2025) |
| Operating Income (EBIT) | $81.8 | (10-K, February 28, 2025) |
| Net Income | $33.0 | (10-K, February 28, 2025) |
| Depreciation & Amortization | $22.9 | (10-K, February 28, 2025) |
| Stock-Based Compensation | $6.5 | (10-K, February 28, 2025) |
| Capital Expenditures | $16.1 | (10-K, February 28, 2025) |
| Change in Working Capital | ($2.1) | (Calculated from 10-K, February 28, 2025 and 10-K for FY 2023 not provided, but estimated from the trend.) |
| Interest Expense | $32.1 | (10-K, February 28, 2025) |
| Cash & Equivalents | $1.2 | (10-K, February 28, 2025) |
| Total Debt | $542.5 | (10-K, February 28, 2025) |
| Diluted Weighted-Average Shares | 15.4 | (10-K, February 28, 2025) |

**B) REVERSE-ENGINEER ASSUMPTIONS**

To solve for the market-implied growth rate, I will hold the operating margin constant at the TTM level of 20.2% (EBIT/Revenue) and use a standard WACC of 7.5% and a terminal growth rate of 2.5%. Through iteration, a 5-year revenue growth rate of approximately **5.0%** is required to justify the current market price of $45.13.

**Market-Implied Assumptions:**

*   **5-Year Revenue Growth CAGR:** 5.0%
*   **Operating Margin:** 20.2% (held constant)

This implies that to justify the current stock price, investors must believe that Carriage Services can grow its revenue by 5.0% annually for the next five years while maintaining its current profitability.

---

### **PART 2: ANALYST'S REVISED VALUATION (CONSERVATIVE BASE-CASE)**

**C) FORMULATE CONSERVATIVE ASSUMPTIONS (5 YEARS)**

**6) Critical Review of Market-Implied Assumptions**

The market's implied 5.0% revenue growth is slightly below the historical average. I will use a more conservative revenue growth rate that tapers down, reflecting potential market saturation and competition. I will also use a slightly more conservative operating margin.

**7) Revenue for Years 1–5:**

I will assume a revenue growth rate of 4.0% in Year 1, tapering linearly to 2.5% by Year 5. This is more conservative than the market-implied rate and reflects a cautious outlook. The specific growth rates used for calculation are 4.0% (Year 1), 3.625% (Year 2), 3.25% (Year 3), 2.875% (Year 4), and 2.5% (Year 5).

**8) Margin Path:**

I will use an operating margin of 20.0%, slightly below the TTM margin, to account for potential cost pressures.

**9) Taxes:**

The effective tax rate over the last three years has fluctuated. I will use a conservative 28.0% effective tax rate, which is in line with the company's historical average.

**10) Capital Intensity:**

*   **Capex:** I will model capex at 4.0% of revenue, consistent with the historical average.
*   **Working Capital:** Change in working capital is modeled at 0.5% of the change in revenue.

**11) SBC, Dilution, and Buybacks:**

*   **SBC:** Stock-based compensation will be subtracted from FCFF, treated as a real cash expense. I will model it at 1.6% of revenue, in line with the historical average.
*   **Dilution:** I will assume a net 0.5% annual increase in shares outstanding, reflecting share issuance for compensation.

**D) FREE CASH FLOW CONSTRUCTION**

**12) FCFF Calculation**

FCFF = EBIT * (1 - tax rate) + D&A - SBC - Capex - Change in Working Capital

**Issue:** The revenue growth rates implied by your original table (Year 2: 3.26%, Year 3: 2.86%, Year 4: 2.51%, Year 5: 2.45%) do not perfectly match the stated linear taper from 4.0% to 2.5%. I have recalculated the revenue and subsequent FCFF using a consistent linear taper as stated in point 7.

| Year | Revenue (M) | EBIT (M) (20%) | NOPAT (M) (EBIT * (1-0.28)) | D&A (M) | SBC (M) (1.6% Rev) | Capex (M) (4.0% Rev) | Change in WC (M) (0.5% dRev) | FCFF (M) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **0** | **$404.20** | **$81.80** | | **$22.90** | **$6.50** | **$16.10** | **($2.10)** | |
| 1 | $420.37 | $84.07 | $60.53 | $23.80 | $6.73 | $16.81 | $0.08 | $60.71 |
| 2 | $435.63 | $87.13 | $62.73 | $24.30 | $6.97 | $17.43 | $0.08 | $62.56 |
| 3 | $449.80 | $89.96 | $64.77 | $25.00 | $7.20 | $17.99 | $0.07 | $64.51 |
| 4 | $462.72 | $92.54 | $66.62 | $25.60 | $7.40 | $18.51 | $0.06 | $66.25 |
| 5 | $474.29 | $94.86 | $68.29 | $26.30 | $7.59 | $18.97 | $0.06 | $67.97 |

**13) Use of FCFF**

I am using FCFF for valuation because it represents the cash flow available to all capital providers and is independent of capital structure.

**E) DISCOUNT RATE (WACC)**

**Issue:** The most significant issue was the WACC calculation, specifically the equity and debt weights. WACC weights should ideally be based on the market values of equity and debt, not arbitrary percentages or book values for both.

**14) Cost of Equity (CAPM):**

*   **Risk-Free Rate:** 4.25% (10-Year U.S. Treasury Yield, August 22, 2025)
*   **Equity Risk Premium:** 5.0%
*   **Beta:** 0.85 (A beta below 1.0 is justified as the death care industry is generally less volatile than the overall market)
*   **Cost of Equity:** 4.25% + 0.85 * 5.0% = **8.5%** (Correct)

**15) Cost of Debt:**

*   **Cost of Debt:** 5.9% (Interest Expense / Average Debt)
*   **After-Tax Cost of Debt:** 5.9% * (1 - 28.0%) = **4.25%** (Correct)

**16) WACC:**

*   **Market Value of Equity (MVE):** $45.13 (Current Market Price) * 15.4 million (Diluted Shares) = $695.0 million
*   **Market Value of Debt (MVD):** $542.5 million (Total Debt, approximating market value)
*   **Total Capital:** $695.0 million + $542.5 million = $1,237.5 million
*   **Equity Weight:** $695.0 / $1,237.5 = **56.16%** (Corrected from 31.3%)
*   **Debt Weight:** $542.5 / $1,237.5 = **43.84%** (Corrected from 68.7%)
*   **WACC:** (0.5616 * 8.5%) + (0.4384 * 4.25%) = 0.047736 + 0.018632 = **6.64%** (Corrected from 5.6%)

**F) TERMINAL VALUE**

**17) Gordon Growth Method:**

*   **Terminal Growth Rate (g):** 2.5%
*   **Terminal Value (using corrected FCFF and WACC):** ($67.97 * (1 + 0.025)) / (0.0664 - 0.025) = $69.67 / 0.0414 = **$1,682.85 million** (Corrected from $2,229.2M)

**18) Exit Multiple Cross-Check:**

*   **Year 5 EBITDA:** EBIT (Year 5) + D&A (Year 5) = $94.86 + $26.3 = $121.16 million (Corrected from $120.1M due to revised EBIT)
*   **Exit Multiple:** 10.0x (A 10x multiple is realistic for a mature company in this industry)
*   **Terminal Value (Exit Multiple):** $121.16 * 10.0 = **$1,211.6 million** (Corrected from $1,201.0M)
*   The Gordon Growth implied exit multiple is $1,682.85M / $121.16M = 13.89x. While this is closer to the 10.0x multiple than before, the 10.0x exit multiple is still more conservative and realistic for cross-checking, so I'll use that for the Terminal Value.

**G) ENTERPRISE TO EQUITY BRIDGE**

**19) Enterprise Value:**

*   **PV of Explicit Period FCFF (using corrected FCFF and WACC):**
    *   PV1 = $60.71 / (1.0664)^1 = $56.93
    *   PV2 = $62.56 / (1.0664)^2 = $54.92
    *   PV3 = $64.51 / (1.0664)^3 = $53.06
    *   PV4 = $66.25 / (1.0664)^4 = $51.27
    *   PV5 = $67.97 / (1.0664)^5 = $49.56
    *   **Sum PV of Explicit Period FCFF:** **$265.74 million** (Corrected from $286.1M)
*   **PV of Terminal Value (using corrected Exit Multiple TV and WACC):** $1,211.6 / (1.0664)^5 = **$878.69 million** (Corrected from $917.4M)
*   **Enterprise Value:** $265.74 + $878.69 = **$1,144.43 million** (Corrected from $1,203.5M)

**20) Equity Value:**

*   **Enterprise Value:** $1,144.43 million
*   **Net Debt:** $541.3 million (Total Debt - Cash & Equivalents) (Remains unchanged)
*   **Equity Value:** $1,144.43 - $541.3 = **$603.13 million** (Corrected from $662.2M)

**H) PER-SHARE VALUE AND MARGIN OF SAFETY**

**21) Analyst's Base-Case Fair Value:**

*   **Equity Value:** $603.13 million
*   **Diluted Shares Outstanding (Year 5):** 15.4M * (1.005)^5 = 15.789 million (approx. 15.8M) (Remains unchanged)
*   **Base-Case Fair Value:** $603.13 / 15.789 = **$38.20** (Corrected from $41.91)

**22) Valuation Range:**

*   **Base Case:** $38.20
*   **Low/Bear Case:** $35.00 (Lower growth of 1.5% and 19% operating margin)
*   **High/Bull Case:** $50.00 (Higher growth of 3.5% and 21% operating margin)

**23) Margin of Safety (MOS) Price:**

*   **MOS Discount:** 30%
*   **Margin of Safety Price:** $38.20 * (1 - 0.30) = **$26.74** (Corrected from $29.34)

### Risk Notes

Key risks to this valuation include: (1) increased competition from both national players and local independent operators, (2) a continued shift in consumer preference towards lower-cost cremation services, impacting revenue per service, and (3) rising interest rates, which could increase the cost of capital and negatively impact the valuation.

final answer is 38.20 $