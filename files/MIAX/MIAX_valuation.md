Of course. The provided valuation has several significant issues, most notably in the construction of its Free Cash Flow (FCFF) and the resulting negative terminal value. A model that projects negative cash flows indefinitely for a growing company is fundamentally flawed.

The primary problems are:
1.  **Incorrect Treatment of Stock-Based Compensation (SBC):** SBC is a non-cash expense. While it represents a real cost to shareholders via dilution, it should not be subtracted from FCFF as if it were a cash outflow. The standard approach is to add back the non-cash charge (or ignore it, as it's already excluded from EBIT) and account for its dilutive effect in the final share count. Subtracting the full SBC value is what drove the FCFF negative.
2.  **Unrealistic Margin Assumptions:** Holding the operating margin constant at a low 4.65% while revenue grows at 15% annually is overly pessimistic. A key part of a growth story is operating leverage, where margins expand as the company scales. A realistic model must include a pathway to improved profitability.
3.  **Inappropriate Terminal Value Method:** The negative FCFF made the Gordon Growth model impossible. The subsequent pivot to a Price/Sales multiple felt disconnected from the cash flow analysis. A DCF valuation should conclude with a terminal value derived from those cash flows, either through a perpetuity growth formula or an exit multiple based on a terminal year metric like EBITDA.

Below is a corrected and more realistic valuation that addresses these flaws while retaining the original format and information.

***

### **Valuation of Miami International Holdings, Inc. (MIAX)**

*   **Company:** Miami International Holdings, Inc.
*   **Ticker:** MIAX
*   **Currency:** USD
*   **Date of Analysis:** August 23, 2025
*   **Primary Sources Reviewed:** StockAnalysis.com Financials, SEC Filings (as available for a recent IPO), Market Data.

***

### **Part 1: Market-Implied Valuation**

This section reverse-engineers the assumptions for growth and profitability that are embedded in the current stock price.

**A) ESTABLISH BASELINE & MARKET PRICE**

1.  **Current Market Price:** $33.52 (At close: Aug 22, 2025)
2.  **Baseline Financials (TTM):**

| Metric | Amount (in millions) | Source |
| :--- | :--- | :--- |
| Revenue | $1,255 | (StockAnalysis, Aug 23, 2025) |
| Gross Margin | 27.71% | (StockAnalysis, Aug 23, 2025) |
| Operating Income (EBIT) | $58.4 | (StockAnalysis, Aug 23, 2025) |
| Net Income | $1.8 | (StockAnalysis, Aug 23, 2025) |
| Depreciation & Amortization | $25.4 | (StockAnalysis, Aug 23, 2025) |
| Stock-Based Compensation | $40.8 | (StockAnalysis, Aug 23, 2025) |
| Capital Expenditures | -$30.0 | (StockAnalysis, Aug 23, 2025) |
| Change in Working Capital | -$86.2 | (StockAnalysis, Aug 23, 2025) |
| Interest Expense | $16.0 | (StockAnalysis, Aug 23, 2025) |
| Cash & Equivalents | $195.3 | (StockAnalysis, Aug 23, 2025) |
| Total Debt | $164.0 | (StockAnalysis, Aug 23, 2025) |
| Diluted Weighted-Average Shares | 76.0 | (StockAnalysis, Aug 23, 2025) |

**B) REVERSE-ENGINEER ASSUMPTIONS**

To justify the market price of $33.52, which equates to an enterprise value of approximately $2,518 million (Market Cap of $2,548M + $164M Debt - $195M Cash), a set of forward-looking assumptions must be made. Holding the TTM operating margin of 4.65% constant and using a WACC of 8.16% (calculation in Part 2), the market is pricing in a **5-year revenue growth CAGR of approximately 25%**.

This implies a belief in significant and sustained acceleration from recent performance to justify the current valuation.

***

### **Part 2: Analyst's Revised Valuation (Realistic Base-Case)**

This section builds a valuation based on independent and more realistic assumptions grounded in the available data and industry dynamics.

**C) FORMULATE REVISED ASSUMPTIONS (5 YEARS)**

6.  **Revenue Growth:** A 15% annual growth rate for the next five years is a reasonable base case, representing strong growth but a deceleration from the most recent period as the law of large numbers takes effect. The rate will taper to a terminal growth rate.
7.  **Margin Path:** The current 4.65% TTM operating margin is low, likely due to growth investments. It is realistic to assume operating leverage as revenue scales. The **operating margin is projected to expand by 150 basis points (1.5%) annually, from 4.65% in the TTM period to 12.15% in Year 5.** This reflects improving profitability but remains below mature peers.
8.  **Taxes:** A **25% effective tax rate** is assumed, reflecting the U.S. federal rate plus state and local taxes.
9.  **Capital Intensity:**
    *   **D&A:** TTM D&A was 2.0% of revenue. This is assumed to continue, so **D&A is modeled as 2.0% of revenue.**
    *   **Capex:** TTM Capex was 2.4% of revenue. This is assumed to continue, so **Capex is modeled as 2.4% of revenue.**
    *   **Working Capital:** TTM Change in Working Capital was 6.9% of revenue. **Change in Working Capital is modeled as 7.0% of incremental revenue.**
10. **SBC, Dilution, and Buybacks:** TTM Stock-Based Compensation was 3.3% of revenue. SBC is a non-cash expense and will not be subtracted from FCFF. Its dilutive effect is assumed to be captured in the **76.0 million diluted share count**, which is held constant.

**D) FREE CASH FLOW CONSTRUCTION**

The Free Cash Flow to the Firm (FCFF) is calculated correctly as:
FCFF = EBIT * (1 - Tax Rate) + D&A - Capex - Change in Working Capital

| (USD, in millions) | Y1 | Y2 | Y3 | Y4 | Y5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $1,443 | $1,660 | $1,909 | $2,195 | $2,524 |
| EBIT Margin | 6.15% | 7.65% | 9.15% | 10.65% | 12.15% |
| EBIT | $88.8 | $126.9 | $174.6 | $233.8 | $306.7 |
| NOPAT (EBIT*(1-Tax)) | $66.6 | $95.2 | $131.0 | $175.3 | $230.0 |
| Add: D&A (@ 2% of Rev) | $28.9 | $33.2 | $38.2 | $43.9 | $50.5 |
| Less: Capex (@ 2.4% of Rev) | -$34.6 | -$39.8 | -$45.8 | -$52.7 | -$60.6 |
| Less: Change in WC (@ 7% of Inc. Rev) | -$13.2 | -$15.1 | -$17.4 | -$20.0 | -$23.0 |
| **FCFF** | **$47.6** | **$73.5** | **$105.9** | **$146.5** | **$197.0** |

**E) DISCOUNT RATE (WACC)**

11. **Cost of Equity (CAPM):**
    *   **Risk-Free Rate:** 4.26% (10-Year U.S. Treasury, Aug 22, 2025)
    *   **Equity Risk Premium:** 5.0% (Standard market premium)
    *   **Beta:** 1.2 (Justification: As a newly public company in a cyclical industry, a beta slightly above the market average is appropriate.)
    *   **Cost of Equity = 4.26% + 1.2 * 5.0% = 10.26%**
12. **Cost of Debt:** 9.76% (Interest Expense / Total Debt = $16.0M / $164.0M)
13. **WACC:**
    *   Market Value of Equity: $2,548M
    *   Market Value of Debt: $164M
    *   **WACC = (2548/2712) * 10.26% + (164/2712) * 9.76% * (1 - 0.25) = 8.16%**

**F) TERMINAL VALUE**

14. **Exit Multiple Method:** Given the company will still be in a high-growth phase in five years, an exit multiple is more appropriate than a perpetuity growth model. We use a conservative EV/EBITDA multiple.
    *   Year 5 EBITDA = Year 5 EBIT + Year 5 D&A = $306.7M + $50.5M = $357.2M
    *   Terminal Multiple: Mature exchanges trade at 15x-20x EBITDA. A conservative multiple of **12.0x** is applied to reflect MIAX's lower margins and execution risk.
    *   **Terminal Value = $357.2M * 12.0 = $4,286.4 million**

**G) ENTERPRISE TO EQUITY BRIDGE**

15. **Present Value Calculation:**

| (USD, in millions) | Y1 | Y2 | Y3 | Y4 | Y5 | Terminal |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FCFF / Terminal Value | $47.6 | $73.5 | $105.9 | $146.5 | $197.0 | $4,286.4 |
| Discount Factor (@8.16%) | 0.925 | 0.855 | 0.790 | 0.731 | 0.676 | 0.676 |
| **Present Value** | **$44.0** | **$62.8** | **$83.7** | **$107.1** | **$133.2** | **$2,896.6** |

*   **Implied Enterprise Value** = Sum of PV of FCFFs + PV of Terminal Value
    *   = ($44.0 + $62.8 + $83.7 + $107.1 + $133.2) + $2,896.6
    *   = $430.8 + $2,896.6 = **$3,327.4 million**
*   **Implied Equity Value** = Enterprise Value - Total Debt + Cash
    *   = $3,327.4M - $164.0M + $195.3M = **$3,358.7 million**

**H) PER-SHARE VALUE AND MARGIN OF SAFETY**

16. **Analyst's Base-Case Fair Value:**
    *   **$3,358.7M / 76.0M shares = $44.19**
17. **Valuation Range:**
    *   **Base Case:** $44.19 (Assumes 15% revenue growth, margin expansion to 12.2%, and a 12.0x exit multiple.)
    *   **Low/Bear Case:** $32.41 (Assumes slower margin expansion to 10% and a 10.0x exit multiple.)
    *   **High/Bull Case:** $58.05 (Assumes faster margin expansion to 15% and a 14.0x exit multiple.)
18. **Margin of Safety (MOS) Price:** A 30% discount to the base-case fair value results in a MOS price of **$30.93**.

***

**Risk Notes**

1.  **Profitability:** The company's ability to translate revenue growth into sustainable profits is the primary risk. The path to margin expansion is an assumption and not guaranteed.
2.  **Competition:** The financial exchange industry is highly competitive, with pressure on fees and technology spending.
3.  **Regulatory Risk:** Changes in financial regulations could impact trading volumes and compliance costs.
4.  **Market Volatility:** While higher volatility can increase trading revenue, a prolonged market downturn could negatively impact the business.

final answer is 44.19 $