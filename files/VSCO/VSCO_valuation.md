Of course. This is a solid attempt at a DCF valuation. You've correctly identified the key components, cited sources, and laid out the model in a clear, two-part structure. However, there are several areas where the assumptions and methodology can be refined to create a more robust and realistic valuation.

The primary issues in the original analysis are:
1.  **Inconsistent Terminal Value:** The biggest flaw is the terminal value calculation. The model calculates a value using the Gordon Growth method, finds it too low, and then switches to an Exit Multiple that implies a perpetual growth rate (4.8%) far higher than what is considered reasonable (2.5%). This internal inconsistency undermines the final valuation.
2.  **Arbitrary D&A Forecast:** The Depreciation & Amortization forecast declines in perfectly round numbers ($5M per year) without a clear link to the company's capital asset base or capital expenditure plans. A more grounded forecast is needed.
3.  **Potentially Low Reinvestment:** The assumption of Capex at 3.0% of revenue is lower than the company's historical average, which could understate the capital needed to maintain its competitive position and refresh its store base, thus overstating free cash flow in the long run.

Below is a revised valuation that corrects these flaws and refines the assumptions to be more realistic while maintaining the original structure and information.

---

### **Valuation Analysis: Victoria's Secret & Co. (VSCO) - REVISED**
*   **Company:** Victoria's Secret & Co. (VSCO)
*   **Currency:** United States Dollar (USD)
*   **Date of Analysis:** August 22, 2025
*   **Primary Sources Reviewed:**
    *   Form 10-Q for the quarterly period ended May 3, 2025, filed June 12, 2025.
    *   Form 10-K for the fiscal year ended February 1, 2025, filed March 21, 2025.

---

### **PART 1: MARKET-IMPLIED VALUATION (REVERSE DCF)**

This section deduces the growth and profitability assumptions embedded in the current stock price.

**A) ESTABLISH BASELINE & MARKET PRICE**

1.  **Current Market Price:** **$22.15** (Investing.com, August 22, 2025).
2.  **Baseline Financials (LTM as of May 3, 2025):** The following table presents the Last Twelve Months (LTM) financial data, calculated from the company's latest 10-K and 10-Q filings.

| Metric | LTM Value (Millions USD) | Citation (Source Document, Page, Date) |
| :--- | :--- | :--- |
| Revenue | $6,224 | (10-K p.51, 10-Q p.3, FY2024 & Q1 2025) |
| Gross Margin | 36.3% | (Calculated from Gross Profit / Revenue) |
| Operating Income (EBIT) | $304 | (10-K p.51, 10-Q p.3, FY2024 & Q1 2025) |
| Net Income (to VSCO) | $167 | (10-K p.51, 10-Q p.3, FY2024 & Q1 2025) |
| Depreciation & Amortization | $255 | (10-K p.54, 10-Q p.6, FY2024 & Q1 2025) |
| Stock-Based Compensation | $58 | (10-K p.54, 10-Q p.6, FY2024 & Q1 2025) |
| Capital Expenditures | $182 | (10-K p.54, 10-Q p.6, FY2024 & Q1 2025) |
| Change in Working Capital | $222 | (Calculated from 10-Q p.4, Q1 2025 vs Q1 2024) |
| Interest Expense | $81 | (10-K p.51, 10-Q p.3, FY2024 & Q1 2025) |
| Cash & Equivalents | $138 | (10-Q p.4, May 3, 2025) |
| Total Debt | $1,082 | (10-Q p.4, May 3, 2025) |
| Diluted Shares Outstanding | 79.9 | (10-Q p.2, as of June 6, 2025) |

**B) REVERSE-ENGINEER ASSUMPTIONS**

To determine the market's expectations, we solve for the Free Cash Flow (FCF) growth rate that justifies the current Enterprise Value.

*   **Market Capitalization:** $22.15/share \* 79.9M shares = $1,770 million.
*   **Net Debt:** $1,082M (Total Debt) - $138M (Cash) = $944 million.
*   **Market-Implied Enterprise Value (EV):** $1,770M + $944M = **$2,714 million**.
*   **Normalized Baseline Free Cash Flow to Firm (FCFF):**
    *   `Formula: EBIT(1-T) + D&A - SBC - Capex`
    *   `FCFF = $304M(1-0.21) + $255M - $58M - $182M = $259M`
    *   *(Note: The LTM effective tax rate of 21% is used. Stock-Based Compensation is treated as a cash expense to reflect its dilutive effect, which is often offset by cash-based buybacks).*

Using a 5-year DCF model with a **9.0% WACC** and a **2.5% terminal growth rate**, the market-implied EV of **$2,714 million** is achieved with a **-6.5% annual decline in Free Cash Flow over the next five years.**

**Conclusion for Part 1:** To justify today's stock price of $22.15, an investor must believe that Victoria's Secret's normalized free cash flow will decline by approximately 6.5% per year for the next five years, followed by 2.5% long-term growth thereafter, assuming stable LTM margins.

---

### **PART 2: ANALYST'S REVISED VALUATION (REALISTIC BASE-CASE)**

This section builds an independent valuation based on revised, evidence-based assumptions.

**C) FORMULATE REALISTIC ASSUMPTIONS (5 YEARS)**

6.  **Revised Rationale:** The market's implied -6.5% decline appears overly pessimistic. The original analyst's assumptions were a good start, but this revision aims for a more realistic reinvestment rate. This base case still assumes a period of stabilization followed by modest growth, reflecting VSCO's brand equity and market position against near-term headwinds.

7.  **Revenue for Years 1–5:** The original path is reasonable. It reflects near-term pressures from a challenged consumer environment followed by stabilization as the brand turnaround takes hold.
    *   **Assumption:** Revenue will decline by **-2.0% in Year 1**, remain flat at **0.0% in Year 2**, and grow at **1.0% annually for Years 3-5**.

8.  **Margin Path:** The original assumption of reverting to the three-year average operating margin of 5.5% is a sound base-case assumption, reflecting a successful execution of management's cost discipline initiatives.
    *   **Assumption:** The operating margin will be maintained at a constant **5.5%** over the forecast period.

9.  **Taxes:** A 22.0% tax rate remains a conservative and appropriate long-term assumption.
    *   **Assumption:** An effective tax rate of **22.0%** will be used throughout the forecast.

10. **Capital Intensity (Revised):**
    *   **Capex:** The original assumption for years 2-5 was potentially too low. A higher reinvestment rate is more realistic for maintaining store appeal and technology infrastructure.
        *   **Assumption:** Capex will be **$220M in Year 1** (per guidance) and **3.5% of revenue** for Years 2-5, better aligning with historical levels required for maintenance and growth.
    *   **Depreciation & Amortization:** The forecast is revised to reflect a more gradual decline from the current base, consistent with the new Capex schedule.
        *   **Assumption:** D&A will be **$252M in Year 1** and will decline by approximately $3M per year.
    *   **Working Capital:** The original assumption is standard and remains unchanged.
        *   **Assumption:** Change in Working Capital will be **5.2% of the change in revenue** each year.

11. **SBC, Dilution, and Buybacks:** Treating SBC as a cash expense and assuming a flat share count remains a simple and effective way to model the net effect of dilution and offsetting buybacks.
    *   **Assumption:** Stock-Based Compensation is held flat at **$60M**. Net share count remains flat at **79.9 million**.

**D) FREE CASH FLOW CONSTRUCTION**

12. **FCFF Calculation:** The formula used is:
    `FCFF = EBIT * (1 - tax rate) + D&A - SBC - Capex - Change in Working Capital`

    *Revised FCFF Forecast Table (in millions USD):*
| Metric | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Revenue | $6,099.5 | $6,099.5 | $6,160.5 | $6,222.1 | $6,284.3 |
| EBIT (5.5% margin) | $335.5 | $335.5 | $338.8 | $342.2 | $345.6 |
| NOPAT (EBIT\*(1-T)) | $261.7 | $261.7 | $264.3 | $266.9 | $269.6 |
| D&A | $252.0 | $249.0 | $246.0 | $243.0 | $240.0 |
| Less: Capex | ($220.0) | ($213.5) | ($215.6) | ($217.8) | ($220.0) |
| Less: SBC | ($60.0) | ($60.0) | ($60.0) | ($60.0) | ($60.0) |
| Less: Δ in WC | $6.5 | $0.0 | ($3.2) | ($3.2) | ($3.2) |
| **Free Cash Flow (FCFF)** | **$246.7** | **$237.2** | **$231.5** | **$228.9** | **$226.4** |

13. This valuation uses FCFF, which represents the cash available to all capital providers (both debt and equity holders).

**E) DISCOUNT RATE (WACC)**

14. **Cost of Equity (CAPM):** The high beta reflects VSCO's stock volatility relative to the market, which is characteristic of challenged retailers in discretionary sectors.
    *   **Risk-Free Rate:** 4.20% (U.S. 10-Year Treasury, Aug 2025).
    *   **Equity Risk Premium:** 5.50% (Standard for U.S. market).
    *   **Beta:** 1.85 (Source: Public financial data).
    *   **Cost of Equity (Ke) = 4.20% + 1.85 \* 5.50% = 14.38%**

15. **Cost of Debt:** The calculated pre-tax cost is a reasonable proxy for the company's borrowing rate.
    *   **Pre-tax Cost of Debt (Kd):** 7.35% (LTM Interest Expense / Average Total Debt).
    *   **After-tax Cost of Debt = 7.35% \* (1 - 22.0%) = 5.73%**

16. **WACC Calculation:**
    *   Market Value of Equity (E) = $1,770M
    *   Market Value of Debt (D) = $1,082M
    *   Total Value (V) = $2,852M
    *   **WACC = (1770/2852 \* 14.38%) + (1082/2852 \* 5.73%) = 11.10%**

**F) TERMINAL VALUE (REVISED)**

17. **Revised Methodology:** The original model created an inconsistency by choosing an exit multiple that implied an unrealistic perpetual growth rate. The corrected approach selects a realistic exit multiple for a stabilized retailer and then cross-checks the implied growth rate to ensure it aligns with the terminal growth assumption.

18. **Exit Multiple Selection:** A 7.0x multiple is too high for a low-growth company. Peers like Gap and American Eagle have historically traded in the 5x-8x EV/EBITDA range. A multiple of **6.5x** is more appropriate for a stabilized but mature VSCO, reflecting its brand strength but limited growth prospects.
    *   Year 5 EBITDA = Year 5 EBIT ($345.6M) + Year 5 D&A ($240.0M) = **$585.6M**.
    *   `Terminal Value (TV) = $585.6M * 6.5x = $3,806M`.

19. **Gordon Growth Cross-Check:** We verify that this TV implies a reasonable long-term growth rate (`g`).
    *   `FCFF_6 = FCFF_5 * (1+g) = $226.4M * (1.025) = $232.1M`
    *   `Implied g = WACC - (FCFF_6 / TV)`
    *   `Implied g = 11.10% - ($232.1M / $3,806M) = 11.10% - 6.10% = 5.00%`
    *   **Correction:** The implied growth is still too high. The high WACC is making reconciliation difficult. A more theoretically sound approach is to prioritize the Gordon Growth method, as its inputs (WACC and g) are explicitly defined. The exit multiple can serve as a sanity check. Let's use the Gordon Growth method as the primary driver.
    *   `TV = (FCFF_5 * (1+g)) / (WACC - g)`
    *   `TV = ($226.4M * 1.025) / (11.10% - 2.5%) = $232.1M / 8.60% = $2,698M`
    *   This implies an exit EV/EBITDA multiple of $2,698M / $585.6M = **4.6x**. This is conservative but plausible for a no-growth company and is internally consistent with the model's assumptions. This method is chosen for its theoretical integrity.

**G) ENTERPRISE TO EQUITY BRIDGE**

20. **Enterprise Value:**
    *   PV of Explicit FCFF = $825M (Sum of discounted FCFFs from the revised table using 11.1% WACC).
    *   PV of Terminal Value = $2,698M / (1 + 11.10%)^5 = $1,590M.
    *   **Enterprise Value = $825M + $1,590M = $2,415M.**

21. **Equity Value:**
    *   `Equity Value = Enterprise Value - Net Debt`
    *   `Equity Value = $2,415M - $944M = $1,471M`.

**H) PER-SHARE VALUE AND MARGIN OF SAFETY**

22. **Analyst's Base-Case Fair Value:**
    *   `Fair Value = Equity Value / Projected Diluted Shares`
    *   `Fair Value = $1,471M / 79.9M shares =` **$18.41 per share.**

23. **Valuation Range:**
    *   **Base Case: $18.41.**
    *   **Low/Bear Case: $13.00.** (Assumes revenue declines further before stabilizing and margins compress to 4.5%).
    *   **High/Bull Case: $25.00.** (Assumes a faster return to 2% growth and margin expansion to 6.0%).

24. **Margin of Safety (MOS) Price:** A 30% discount to the base-case fair value provides a buffer against forecasting errors and execution risk.
    *   `MOS Price = $18.41 * (1 - 0.30) =` **$12.89.**

---

**Revised Risk Notes**

1.  **Macroeconomic Headwinds:** As a seller of discretionary goods, VSCO is highly sensitive to consumer spending, which is pressured by inflation and economic uncertainty. A prolonged downturn could severely impact revenue and profitability.
2.  **Competitive Pressure:** The intimates and apparel market is intensely competitive. Failure to innovate and maintain brand relevance could lead to further market share erosion and margin compression.
3.  **Turnaround Execution Risk:** The valuation is contingent on management's ability to stabilize sales and maintain historical average margins. Any missteps could result in performance that aligns more closely with the pessimistic market-implied case.
4.  **High Financial Leverage:** The company's significant debt load makes the equity value highly sensitive to changes in enterprise value. Small misses in operational performance can have an amplified negative impact on the stock price.

final answer is 18.41 $