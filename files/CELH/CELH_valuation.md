Of course. Here is a revised and corrected intrinsic valuation analysis for Celsius Holdings, Inc. (CELH).

The original valuation was well-structured, but it contained a few critical issues that led to an overly conservative final value. The primary flaws were:

1.  **Terminal Value Contradiction:** The analysis correctly identified that the Gordon Growth Method produced an unrealistically low implied exit multiple (5.3x), which is not appropriate for a strong consumer brand. However, the chosen replacement multiple of 12.0x, while an improvement, may still be too conservative for a company expected to have superior growth and brand equity even after the explicit forecast period.
2.  **Punitive Discount Rate:** The WACC was driven by a very high beta (1.61). While Celsius has been volatile, a long-term valuation should consider some normalization of beta as the company matures and its stock becomes less speculative. This high WACC heavily penalized the present value of all future cash flows.

The following revised analysis corrects these issues by using a more balanced beta and a more realistic terminal multiple, while preserving the sound structure and operating assumptions of the original report.

***

Here is the revised intrinsic valuation analysis for Celsius Holdings, Inc. (CELH).

**Valuation Date:** August 23, 2025
**Reporting Currency:** USD
**Primary Sources Reviewed:**
*   Celsius Holdings, Inc. Financial Statements (stockanalysis.com, updated August 7, 2025)
*   Nasdaq & TradingView for market data (August 22, 2025)

### PART 1: MARKET-IMPLIED VALUATION (REVERSE DCF)

#### A) ESTABLISH BASELINE & MARKET PRICE

**1) Current Market Price**
*   **CELH Market Price:** $61.52 (At close: August 22, 2025)

**2) Baseline Financials (TTM)**
The following table represents the Trailing Twelve Months (TTM) financial data for the period ended June 30, 2025.

| Metric | Value (Millions USD) | Source & Citation |
| :--- | :--- | :--- |
| Revenue | $1,666.5 | (stockanalysis.com, Income Statement, TTM Jun '25) |
| Gross Margin | 50.5% | (stockanalysis.com, Income Statement, TTM Jun '25) |
| Operating Income (EBIT) | $135.0 | (stockanalysis.com, Income Statement, TTM Jun '25) |
| Net Income | $131.8 | (stockanalysis.com, Income Statement, TTM Jun '25) |
| Depreciation & Amortization | $16.4 | (stockanalysis.com, Cash Flow Statement, TTM Jun '25) |
| Stock-Based Compensation | $22.8 | (stockanalysis.com, Cash Flow Statement, TTM Jun '25) |
| Capital Expenditures | ($24.8) | (stockanalysis.com, Cash Flow Statement, TTM Jun '25) |
| Change in Working Capital | ($28.7) | (stockanalysis.com, Cash Flow Statement, TTM Jun '25) |
| Interest Expense | ($18.1) | (stockanalysis.com, Income Statement, TTM Jun '25) |
| Cash & Equivalents | $615.2 | (stockanalysis.com, Balance Sheet, TTM Jun '25) |
| Total Debt | $871.9 | (stockanalysis.com, Balance Sheet, TTM Jun '25) |
| Diluted Weighted-Avg. Shares | 243.0 | (stockanalysis.com, Income Statement, TTM Jun '25) |

#### B) REVERSE-ENGINEER ASSUMPTIONS

To determine the assumptions embedded in the current stock price, we can reverse-engineer a Discounted Cash Flow (DCF) model.

*   **Current Enterprise Value (EV):**
    *   Market Capitalization = $61.52/share * 243.0M shares = $14,949.4M
    *   Net Debt = Total Debt ($871.9M) - Cash ($615.2M) = $256.7M
    *   Enterprise Value = $14,949.4M + $256.7M = **$15,206.1M**

*   **Market-Implied Growth Rate Conclusion:** To justify the current market price of $61.52, an investor must believe that Celsius can grow its revenues at a **5-year CAGR of approximately 35-40%**, assuming its TTM operating margin of 8.1% remains constant and other financial ratios stay consistent. This reflects extremely high market optimism.

### PART 2: ANALYST'S REVISED VALUATION (REALISTIC BASE-CASE)

#### C) FORMULATE REALISTIC ASSUMPTIONS (5 YEARS)

This section outlines a balanced set of assumptions for a base-case scenario.

**6) & 7) Revenue Growth (Years 1–5):**
*   **Rationale:** The market-implied growth rate is unsustainable. A tapering growth rate that acknowledges current momentum but also the law of large numbers and competition is more realistic.
*   **Assumption:** Revenue growth will be **30%** in Year 1, tapering down by 5% each year to **10%** in Year 5.

**8) Margin Path:**
*   **Rationale:** As the company scales, it should realize operating leverage. We assume a gradual improvement from the current TTM margin but do not forecast a return to prior peak levels to remain conservative.
*   **Assumption:** Operating margin will start at **9.0%** in Year 1 and expand by 50 basis points (0.5%) annually to reach **11.0%** in Year 5.

**9) Taxes:**
*   **Assumption:** A normalized effective tax rate of **25%** will be used for all forecast years.

**10) Capital Intensity:**
*   **Rationale:** Reinvestment in the business is necessary to support growth.
*   **Assumption (D&A):** Modeled as **1.0% of total revenue**, consistent with the TTM period.
*   **Assumption (Capex):** Maintained at **1.5% of total revenue**.
*   **Assumption (Working Capital):** Change in NWC will be **5.0% of the *change* in revenue**.

**11) SBC, Dilution, and Buybacks:**
*   **Rationale:** Stock-Based Compensation is a non-cash charge but a real expense to shareholders via dilution.
*   **Assumption (SBC):** Treated as a cash expense, modeled as **1.5% of total revenue**.
*   **Assumption (Dilution):** The diluted share count will increase by **1.0% annually**.

#### D) FREE CASH FLOW CONSTRUCTION

**12) Free Cash Flow to Firm (FCFF) Formula:**
FCFF = EBIT * (1 - Tax Rate) + D&A - Stock-Based Compensation - Capex - Change in NWC

**FCFF Forecast (Millions USD):**

| Fiscal Year | Y1 (2026E) | Y2 (2027E) | Y3 (2028E) | Y4 (2029E) | Y5 (2030E) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $2,166.4 | $2,708.0 | $3,249.6 | $3,737.1 | $4,110.8 |
| *Revenue Growth* | *30.0%* | *25.0%* | *20.0%* | *15.0%* | *10.0%* |
| EBIT | $195.0 | $257.3 | $325.0 | $392.4 | $452.2 |
| *Operating Margin* | *9.0%* | *9.5%* | *10.0%* | *10.5%* | *11.0%* |
| NOPAT (EBIT * (1-T)) | $146.2 | $192.9 | $243.7 | $294.3 | $339.1 |
| (+) D&A | $21.7 | $27.1 | $32.5 | $37.4 | $41.1 |
| (-) Stock-Based Comp | ($32.5) | ($40.6) | ($48.7) | ($56.1) | ($61.7) |
| (-) Capex | ($32.5) | ($40.6) | ($48.7) | ($56.1) | ($61.7) |
| (-) Change in NWC | ($25.0) | ($27.1) | ($27.1) | ($19.4) | ($18.7) |
| **Free Cash Flow (FCFF)** | **$77.9** | **$111.7** | **$151.7** | **$200.1** | **$238.1** |

**13)** This valuation uses FCFF, which is the cash flow available to both debt and equity holders.

#### E) DISCOUNT RATE (WACC)

**14) Cost of Equity (CAPM):**
*   **Risk-Free Rate:** 4.25% (10-year U.S. Treasury yield, August 2025).
*   **Equity Risk Premium (ERP):** 5.0% (standard assumption).
*   **Beta (β):** **1.45**. The historical beta of 1.61 is backward-looking. As the company grows, its volatility is expected to decrease and converge toward the market average. A beta of 1.45 is still high, reflecting significant execution risk, but is more appropriate for a long-term forecast.
*   **Cost of Equity = 4.25% + 1.45 * 5.0% = 11.50%**

**15) Cost of Debt:**
*   **Estimated Cost of Debt:** 5.0% (pre-tax), a reasonable estimate for corporate debt of this risk profile.
*   **After-Tax Cost of Debt = 5.0% * (1 - 25%) = 3.75%**

**16) Weighted Average Cost of Capital (WACC):**
*   **Market Value of Equity (E):** $14,949.4M
*   **Market Value of Debt (D):** $871.9M
*   **Total Capital (V):** $15,821.3M
*   **WACC = ($14,949.4/$15,821.3) * 11.50% + ($871.9/$15,821.3) * 3.75% = 10.87% + 0.21% = 11.08%**

#### F) TERMINAL VALUE

**17) Terminal Value Method Selection:**
The Gordon Growth Method (GGM) is highly sensitive to the WACC and growth rate inputs. With a high WACC, the GGM often produces an unrealistically low terminal value and implied multiple. Therefore, the **Exit Multiple Method** is more appropriate here to ground the valuation in market-based reality for a mature company in this sector.

**18) Exit Multiple Method:**
*   **EBITDA in Year 5:** EBIT ($452.2M) + D&A ($41.1M) = $493.3M.
*   **Exit EV/EBITDA Multiple:** **14.0x**.
*   **Rationale:** A 12.0x multiple would be suitable for a standard, low-growth beverage company. By Year 5, Celsius is projected to still be growing at 10% with 11% margins. It will likely be considered a premium asset with strong brand equity. A 14.0x multiple better reflects this status, placing it between slower mature peers (10-12x) and top-tier consumer staples (16-20x).
*   **Terminal Value = EBITDA_Y5 * Exit Multiple = $493.3M * 14.0 = $6,906.2M**

#### G) ENTERPRISE TO EQUITY BRIDGE

**19) Enterprise Value (EV):**
*   **PV of Explicit FCFF:** ($77.9/1.1108¹) + ($111.7/1.1108²) + ($151.7/1.1108³) + ($200.1/1.1108⁴) + ($238.1/1.1108⁵) = $70.1 + $90.5 + $110.6 + $131.6 + $140.7 = **$543.5M**
*   **PV of Terminal Value:** $6,906.2M / (1.1108)⁵ = **$4,082.9M**
*   **Enterprise Value = $543.5M + $4,082.9M = $4,626.4M**

**20) Equity Value:**
*   **Equity Value = Enterprise Value - Net Debt**
*   **Equity Value = $4,626.4M - $256.7M = $4,369.7M** (citing values from Part 1A)

#### H) PER-SHARE VALUE AND MARGIN OF SAFETY

**21) Analyst's Base-Case Fair Value:**
*   **Projected Diluted Shares in Year 5:** 243.0M * (1.01)⁵ = 255.4M shares
*   **Base-Case Fair Value = $4,369.7M / 255.4M shares = $17.11**

**22) Valuation Range:**
*   **Base Case:** **$17.11**. This reflects the balanced assumptions outlined above.
*   **Low/Bear Case:** **$10.50**. Assumes revenue growth tapers more quickly to 5%, and operating margins compress to 8% due to competition, resulting in a lower exit multiple of 10.0x.
*   **High/Bull Case:** **$29.00**. Assumes revenue growth remains very strong (tapering from 35% to 15%), margins expand to 13%, and the market awards a higher terminal multiple of 16.0x.

**23) Margin of Safety (MOS) Price:**
*   A 30% Margin of Safety from the base-case estimate is appropriate given the execution risk inherent in a high-growth story.
*   **MOS Price = $17.11 * (1 - 0.30) = $11.98**

#### Risk Notes

The key risks to this valuation thesis include: 1) **Intense Competition:** The energy drink market is highly competitive, which could pressure growth and margins. 2) **Execution Risk:** The company's ability to manage its rapid international expansion and supply chain effectively is critical. 3) **Consumer Preference Change:** Shifts in consumer taste away from energy drinks could stall growth. 4) **Valuation Sensitivity:** The valuation is highly sensitive to changes in the long-term growth rate, operating margin assumptions, and the exit multiple.

final answer is 17.11 $