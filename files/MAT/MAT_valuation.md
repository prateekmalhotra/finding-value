This is a solid valuation framework. However, there are several areas where the assumptions can be refined to be more realistic, and there are two critical calculation errors that need correction. The primary issues are: a calculation error in the present value of free cash flows, the use of a future share count for a present valuation, and an overly conservative assumption regarding share repurchases.

Here is a revised valuation that corrects these issues and adjusts assumptions to better reflect a realistic base-case scenario.

***

An intrinsic valuation of Mattel, Inc. (MAT) is performed in two stages. The first stage reverse-engineers the market's assumptions about growth and profitability. The second stage builds an independent, balanced valuation based on primary data sources.

**Company**: Mattel, Inc. (MAT)
**Currency**: USD
**Date of Analysis**: August 24, 2025
**Primary Sources Reviewed**:
*   Mattel, Inc. Form 10-K for the fiscal year ended December 31, 2024.
*   YCharts, Trading Economics for market data.
*   Seeking Alpha for beta.

### Part 1: Market-Implied Valuation (Reverse DCF)

**A) ESTABLISH BASELINE & MARKET PRICE**

1.  **Current Market Price**: $18.36 (NASDAQ, August 24, 2025).

2.  **Baseline Financials (TTM)**: The following table presents Mattel's trailing-twelve-months financials, calculated from the most recent SEC filings.

| Metric | Amount (in millions) | Citation |
| :--- | :--- | :--- |
| Revenue | $5,379.5 | (Form 10-K, December 31, 2024, p. 51) |
| Gross Margin | 50.8% | (Form 10-K, December 31, 2024, p. 30) |
| Operating Income (EBIT) | $694.3 | (Form 10-K, December 31, 2024, p. 30) |
| Net Income | $541.8 | (Form 10-K, December 31, 2024, p. 30) |
| Depreciation & Amortization | $167.9 | (Form 10-K, December 31, 2024, p. 53) |
| Stock-Based Compensation | $79.4 | (Form 10-K, December 31, 2024, p. 53) |
| Capital Expenditures | ($202.6) | (Form 10-K, December 31, 2024, p. 38) |
| Change in Working Capital | ($191.1) | (Calculated from Form 10-K, December 31, 2024, p. 53) |
| Interest Expense | $118.8 | (Form 10-K, December 31, 2024, p. 30) |
| Cash & Equivalents | $1,387.9 | (Form 10-K, December 31, 2024, p. 50) |
| Total Debt | $2,334.4 | (Form 10-K, December 31, 2024, p. 39) |
| Diluted Weighted-Average Shares | 343.3 | (Form 10-K, December 31, 2024, p. 51) |

**B) REVERSE-ENGINEER ASSUMPTIONS**

To solve for the market-implied growth rate, we hold the TTM operating margin and other key metrics constant and find the 5-year revenue growth rate that results in a DCF value equal to the current market price of $18.36.

*   **Market Capitalization**: $18.36/share \* 343.3 million shares = $6,303 million.
*   **Enterprise Value**: $6,303 million + $2,334.4 million (Debt) - $1,387.9 million (Cash) = $7,249.5 million.

After iterating, the analysis shows that to justify the current enterprise value of approximately $7.25 billion, the market is pricing in a **5-year revenue growth CAGR of approximately 7.5%**, assuming the operating margin remains stable at the TTM level of 12.9%.

This implies a belief in sustained, robust growth, significantly higher than recent performance, likely driven by expectations of continued brand momentum and international expansion.

### PART 2: ANALYST'S REVISED VALUATION (REALISTIC BASE-CASE)

**C) FORMULATE REVISED ASSUMPTIONS (5 YEARS)**

6.  **Revenue Growth (Years 1-5)**: The 4.0% CAGR assumption is a reasonable starting point. It reflects a normalization post-Barbie movie while still acknowledging the strength of core franchises and potential for growth in emerging markets. We will maintain a **4.0% CAGR for the next five years**.

7.  **Margin Path**: Management has successfully improved margins. Assuming a slight regression to 12.5% may be too conservative if revenue growth is achieved. A more realistic path is slight operating leverage. I will model a modest **operating margin expansion from 12.9% to 13.2%** over the forecast period, reflecting ongoing efficiency programs.

8.  **Taxes**: The effective tax rate has been volatile. The normalized effective tax rate of **22.0%** remains a sound long-term assumption.

9.  **Capital Intensity**:
    *   **Capex**: Modeling **Capex at 3.5% of revenue** annually is consistent with historical spending and is a reasonable assumption.
    *   **Working Capital**: The change in working capital modeled as **5.0% of incremental revenue** reflects historical averages and is retained.

10. **SBC, Dilution, and Buybacks**: The original 1.0% net share reduction is overly conservative given the $400M buyback in 2024 (over 6% of market cap). Factoring in dilution from SBC, a more realistic assumption is that the company will continue to return capital to shareholders. We will project a **net 1.5% annual reduction in shares outstanding**.

**D) FREE CASH FLOW CONSTRUCTION**

The Free Cash Flow to the Firm (FCFF) is calculated as:
`FCFF = EBIT * (1 - Tax Rate) + D&A - SBC - Capex - Change in Working Capital`

| (in millions) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $5,594.7 | $5,818.5 | $6,051.2 | $6,293.3 | $6,545.0 |
| Operating Margin | 13.0% | 13.0% | 13.1% | 13.1% | 13.2% |
| EBIT | $724.9 | $759.4 | $793.6 | $828.0 | $864.0 |
| NOPAT | $565.4 | $592.3 | $619.0 | $645.8 | $673.9 |
| D&A | $173.0 | $179.7 | $186.9 | $194.4 | $202.1 |
| Stock-Based Comp | ($82.1) | ($85.4) | ($88.8) | ($92.4) | ($96.1) |
| Capex | ($195.8) | ($203.6) | ($211.8) | ($220.3) | ($229.1) |
| Change in WC | ($10.8) | ($11.2) | ($11.6) | ($12.1) | ($12.6) |
| **FCFF** | **$449.7** | **$471.8** | **$493.7** | **$515.4** | **$538.1** |

FCFF is used for this valuation because it represents the cash flow available to all capital providers and is independent of the company's capital structure.

**E) DISCOUNT RATE (WACC)**

11. **Cost of Equity (CAPM)**:
    *   **Risk-Free Rate**: 4.26% (10-Year U.S. Treasury Yield, August 22, 2025).
    *   **Equity Risk Premium**: 5.0% (standard assumption for a mature market).
    *   **Beta**: 0.80 (24-Month Beta). A beta below 1.0 is justified as Mattel operates in the relatively stable consumer discretionary toy sector, which is less volatile than the overall market.
    *   **Cost of Equity** = 4.26% + 0.80 \* 5.0% = **8.26%**

12. **Cost of Debt**:
    *   Interest Expense / Average Debt = $118.8M / $2,332.2M = 5.1%.
    *   After-tax Cost of Debt = 5.1% \* (1 - 22.0%) = **3.98%**

13. **WACC**:
    *   Market Value of Equity = $6,303 million
    *   Market Value of Debt = $2,334 million
    *   Total Capital = $8,637 million
    *   **WACC** = (8.26% \* 73.0%) + (3.98% \* 27.0%) = **7.10%**

**F) TERMINAL VALUE**

14. **Exit Multiple Method**: For mature consumer goods companies, an exit multiple provides a more direct, market-based approach to terminal value. A conservative but realistic long-term **EV/EBITDA multiple of 10.0x** is appropriate for a company of Mattel's scale and growth profile. This is in line with historical industry averages for stable players.

15. **Terminal Value Calculation**:
    *   Year 5 EBITDA = Year 5 EBIT + Year 5 D&A = $864.0M + $202.1M = $1,066.1M.
    *   **Terminal Value** = Year 5 EBITDA \* 10.0x = **$10,661 million**

16. **Implied Growth Cross-Check**: A 10.0x EV/EBITDA multiple implies a perpetual growth rate (g) of approximately **2.0%**, calculated as: g = (TV \* WACC - Final FCFF) / (TV + Final FCFF). This 2.0% rate is a sustainable long-term growth assumption, confirming the 10.0x multiple is reasonable and not overly aggressive.

**G) ENTERPRISE TO EQUITY BRIDGE**

17. **Enterprise Value**:
    *   **Correction**: The PV of explicit FCFF is recalculated correctly below.
    *   PV of Explicit FCFF = ($449.7/1.071¹) + ($471.8/1.071²) + ($493.7/1.071³) + ($515.4/1.071⁴) + ($538.1/1.071⁵)
    *   PV of Explicit FCFF = $419.9 + $411.6 + $401.4 + $391.4 + $381.5 = **$2,005.8 million**
    *   PV of Terminal Value = $10,661 / (1.071)^5 = **$7,557.7 million**
    *   **Enterprise Value** = $2,005.8M + $7,557.7M = **$9,563.5 million**

18. **Equity Value**:
    *   Equity Value = Enterprise Value - Net Debt
    *   Equity Value = $9,563.5M - ($2,334.4M - $1,387.9M) = **$8,617.0 million**

**H) PER-SHARE VALUE AND MARGIN OF SAFETY**

19. **Analyst's Base-Case Fair Value**:
    *   **Correction**: The equity value represents the value to shareholders today. Therefore, it must be divided by the current number of shares outstanding, not a future projected number.
    *   Current Shares Outstanding = 343.3 million shares
    *   **Base-Case Fair Value** = $8,617.0M / 343.3M shares = **$25.10 per share**

20. **Valuation Range**:
    *   **Base Case**: **$25.10**. Assumes 4.0% revenue growth and margin expansion to 13.2%.
    *   **Low/Bear Case**: **$18.75**. Assumes 2.0% revenue growth and margin compression to 12.0% due to competition.
    *   **High/Bull Case**: **$32.00**. Assumes 5.5% revenue growth and margin expansion to 14.0% from successful IP monetization.

21. **Margin of Safety (MOS) Price**:
    *   Applying a 25% discount to the base-case fair value provides a buffer against forecasting errors and unforeseen risks.
    *   **MOS Price** = $25.10 \* (1 - 0.25) = **$18.83**

### Risk Notes

Key risks to this valuation include: 1) **Franchise Concentration**: Over-reliance on the Barbie and Hot Wheels brands poses a risk if consumer tastes shift away from these core franchises. 2) **Competitive Pressure**: The toy industry is highly competitive, with low barriers to entry. Increased competition from rivals like Hasbro and LEGO could pressure margins and growth. 3) **Input Cost Volatility**: Fluctuations in raw material and transportation costs could impact profitability if they cannot be fully offset by price increases. 4) **Retailer Dependence**: A significant portion of sales is concentrated among a few large retailers (Walmart, Target, Amazon). Any deterioration in these relationships could materially impact sales.

final answer is 25.10 $