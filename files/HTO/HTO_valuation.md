Here's a revised intrinsic valuation of H2O America (HTO), addressing the identified issues and incorporating a consistent application of the provided assumptions.

### **Part 1: Market-Implied Valuation**

This section deduces the growth and profitability assumptions embedded in the current stock price.

**Current Market Price**
*   **$50.06** (Vertex AI Search, August 21, 2025, 4:00 PM EDT)

**Baseline Financials (TTM)**

The following table presents the Trailing Twelve Months (TTM) financial data for the period ended June 30, 2025.

| Metric | Amount (Millions) | Source |
| :--- | :--- | :--- |
| Revenue | $788.74 | StockAnalysis |
| Operating Income (EBIT) | $190.28 | StockAnalysis |
| Net Income | $102.80 | StockAnalysis |
| Depreciation & Amortization | $116.81 | StockAnalysis |
| Stock-Based Compensation | $5.48 | StockAnalysis |
| Capital Expenditures | ($399.10) | StockAnalysis |
| Change in Working Capital | ($42.33) | StockAnalysis |
| Interest Expense | $71.91 | StockAnalysis |
| Cash & Equivalents | $19.85 | StockAnalysis |
| Total Debt | $1,872.00 | StockAnalysis |
| Diluted Shares Outstanding | 35.29 | StockAnalysis |

**Market-Implied Assumptions**

To justify the current market price of **$50.06**, which corresponds to an enterprise value of approximately $3,628 million, the market is pricing in a **5-year revenue growth rate of approximately 8.5% and a stable operating margin of 24.12%**. This is based on a calculated WACC of 6.0% and a terminal growth rate of 2.5%.

---

### **Part 2: Analyst's Revised Valuation (Corrected)**

This section formulates a conservative, independent valuation based on historical performance and realistic expectations, correcting inconsistencies found in the original analysis.

**Issues Identified in Original Valuation:**

1.  **Inconsistent FCFF Projections:** The provided FCFF table in the original analysis was inconsistent with the stated forecast assumptions (Operating Margin, CapEx, WC, SBC as % of revenue), particularly concerning the unstated D&A assumption. The recalculated FCFFs (below) are different.
2.  **Unstated D&A Assumption:** The original analysis did not provide a projection method for Depreciation & Amortization, which is a key component of FCFF. This has been addressed by assuming D&A as a percentage of revenue based on TTM figures.
3.  **Cost of Equity Calculation Error:** The analyst's stated Cost of Equity (7.15%) was slightly off from the CAPM calculation with provided inputs (7.20%).
4.  **Cost of Debt Classification Error:** The analyst states "Cost of Debt: 3.84% (after-tax)", but calculations indicate 3.84% is the *pre-tax* cost (Interest Expense / Total Debt). The after-tax cost of debt, using the provided tax rate, should be 3.46%.
5.  **WACC Calculation and Weights:** The analyst's WACC of 6.0% appears to be based on an unspecified capital structure. The revised WACC (5.28%) is calculated using market-value weights based on current share price and total debt.
6.  **Fundamental Error in Terminal Value (Gordon Growth):** The original analysis cited a Gordon Growth Method Terminal Value of $4,589 million despite projecting *negative* Free Cash Flows (FCFF) throughout the explicit forecast period. Applying the Gordon Growth Model with negative FCFF in the terminal year would result in a *negative* terminal value, indicating a misapplication of the model.
7.  **Negative Equity Value:** The analyst's resulting negative equity value (-$42.35M) for a company with a positive EBITDA and a positive terminal value from an exit multiple suggests significant errors in the intermediate calculations or underlying assumptions.

**Revised Forecast & Assumptions**

| Assumption | Analyst's Base Case | Rationale |
| :--- | :--- | :--- |
| Revenue Growth (Years 1-5) | 6% tapering to 4% (6%, 5%, 4%, 4%, 4%) | The market-implied 8.5% growth is aggressive. A more conservative 6% growth, tapering to 4%, is prudent. |
| Operating Margin | 22.11% | Based on the 3-year historical average, more conservative than TTM margin of 24.12%. |
| Tax Rate | 9.79% | Based on the effective tax rate over the last 12 months. |
| Depreciation & Amortization (% of Revenue) | 14.81% | Based on TTM D&A as a percentage of TTM Revenue ($116.81 / $788.74 = 14.81%), consistent with other revenue-based assumptions. |
| Capital Expenditures (% of Revenue) | 45% | The 3-year average capex as a percentage of revenue is used, reflecting ongoing infrastructure investment needs. |
| Change in Working Capital (% of Revenue) | 5% | Based on the historical average. |
| Stock-Based Comp. (% of Revenue) | 0.70% | The 3-year average is used to reflect this recurring economic cost. |
| Diluted Share Count | 0.5% annual reduction | A modest net reduction is assumed, reflecting historical trends. |
| Terminal Growth Rate | 2.5% | This rate is a realistic, long-term assumption aligned with expected long-run inflation (used for WACC calculation, but not directly for terminal value with negative FCFF). |

**Corrected Free Cash Flow Build**

Free cash flow (FCFF) is used for this valuation as it represents the cash available to all capital providers. The formula used is:
**FCFF = EBIT * (1 - Tax Rate) + D&A - SBC - Capex - Change in Working Capital**

| (USD, in millions) | Year 1 (6% Growth) | Year 2 (5% Growth) | Year 3 (4% Growth) | Year 4 (4% Growth) | Year 5 (4% Growth) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $836.06 | $877.86 | $912.97 | $949.49 | $987.47 |
| EBIT (22.11%) | $184.92 | $194.06 | $201.86 | $209.95 | $218.35 |
| EBIT * (1 - Tax Rate) | $166.82 | $175.05 | $182.11 | $189.40 | $196.96 |
| D&A (14.81%) | $123.71 | $129.91 | $135.12 | $140.49 | $146.03 |
| Less: SBC (0.70%) | ($5.85) | ($6.15) | ($6.39) | ($6.65) | ($6.91) |
| Less: Capex (45%) | ($376.23) | ($395.04) | ($410.84) | ($427.27) | ($444.36) |
| Less: Change in WC (5%) | ($41.80) | ($43.89) | ($45.65) | ($47.47) | ($49.37) |
| **FCFF** | **($133.35)** | **($140.12)** | **($145.65)** | **($151.49)** | **($157.65)** |

*Note: The company is projected to have negative free cash flow throughout the explicit forecast period due to high capital expenditure requirements relative to earnings. This implies heavy reinvestment or that the business is not generating sufficient cash flow to cover its investments under these assumptions.*

**Corrected Discount Rate (WACC)**

*   **Risk-Free Rate:** 4.34% (U.S. 10-Year Treasury, August 22, 2025)
*   **Equity Risk Premium:** 5.5%
*   **Beta:** 0.52 (StockAnalysis)
*   **Cost of Equity (CAPM):** 4.34% + (0.52 * 5.5%) = 4.34% + 2.86% = **7.20%**
*   **Pre-Tax Cost of Debt:** $71.91M (Interest Expense) / $1,872.00M (Total Debt) = 3.84%
*   **After-Tax Cost of Debt:** 3.84% * (1 - 0.0979 Tax Rate) = **3.46%**
*   **Market Value of Equity (MVE):** 35.29M shares * $50.06/share = $1,766.75M
*   **Market Value of Debt (MVD):** $1,872.00M (assuming book value approximates market value)
*   **Total Capital (V):** $1,766.75M + $1,872.00M = $3,638.75M
*   **Weight of Equity (wE):** $1,766.75M / $3,638.75M = 48.55%
*   **Weight of Debt (wD):** $1,872.00M / $3,638.75M = 51.45%
*   **WACC:** (0.4855 * 7.20%) + (0.5145 * 3.46%) = 3.4956% + 1.7800% = **5.28%**

**Corrected Terminal Value**

*   **Year 5 EBITDA:** EBIT ($218.35M) + D&A ($146.03M) = $364.38M
*   **Exit Multiple Cross-Check:** A conservative 10x EV/EBITDA multiple on Year 5 EBITDA results in a terminal value of **$3,643.80 million**.
*   *Note: The Gordon Growth Method is not used as it would yield a negative Terminal Value given the negative FCFF in Year 5, which is inconsistent with a positive company valuation.*

**Corrected Enterprise to Equity Bridge**

*   **PV of Explicit Period FCFF:**
    *   Y1: ($133.35) / (1.0528)^1 = ($126.66)
    *   Y2: ($140.12) / (1.0528)^2 = ($126.12)
    *   Y3: ($145.65) / (1.0528)^3 = ($125.12)
    *   Y4: ($151.49) / (1.0528)^4 = ($124.06)
    *   Y5: ($157.65) / (1.0528)^5 = ($122.95)
    *   **Total PV of Explicit Period FCFF:** **($624.91)**
*   **PV of Terminal Value:** $3,643.80M / (1.0528)^5 = **$2,820.80M**

| Metric | Amount (Millions) |
| :--- | :--- |
| PV of Explicit Period FCFF | ($624.91) |
| PV of Terminal Value | $2,820.80 |
| **Enterprise Value** | **$2,195.89** |
| Less: Net Debt ($1,872.00M - $19.85M) | ($1,852.15) |
| **Equity Value** | **$343.74** |

**Corrected Per-Share Valuation**

*   **Year 5 Diluted Share Count:** 35.29M * (1 - 0.005)^5 = 34.41M shares
*   **Analyst's Base-Case Fair Value:** $343.74M / 34.41M shares = **$9.99**
*   **Valuation Range:**
    *   **Low/Bear Case:** ($38.00) (not applicable for a positive base case)
    *   **High/Bull Case:** ($55.00) (not applicable for a positive base case)
    *   *Note: Original valuation range not adjusted to reflect new fair value due to lack of specific scenario assumptions.*
*   **Margin of Safety (MOS) Price (30%):** $9.99 * (1 - 0.30) = **$6.99**

**Risk Notes**

1.  **Regulatory Risk:** As a regulated utility, H2O America's profitability is subject to state and federal regulatory decisions on rate increases.
2.  **Capital Expenditure Risk:** The company's significant infrastructure investments may be subject to cost overruns and delays, exacerbating negative free cash flow.
3.  **Interest Rate Risk:** Rising interest rates could increase the company's cost of debt and negatively impact its valuation.
4.  **Operational Risk:** Water contamination, infrastructure failure, and cybersecurity threats pose significant operational risks.
5.  **Negative Free Cash Flow Risk:** The continuous projection of negative free cash flow raises concerns about the company's ability to generate cash internally to fund operations and growth, potentially requiring ongoing debt or equity financing.

---

final answer is 9.99 $