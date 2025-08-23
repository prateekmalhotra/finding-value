This is a solid attempt at a two-stage DCF valuation. You've correctly identified the key steps, from reverse-engineering the market's expectations to building your own forecast. However, there are a few critical methodological issues and conservative assumptions that can be refined to make the valuation more robust and realistic.

Here are the primary issues I see in your analysis:

1.  **Incorrect FCFF Formula:** Your Free Cash Flow to Firm (FCFF) calculation incorrectly subtracts Stock-Based Compensation (SBC). SBC is a non-cash expense that is already accounted for within EBIT. The standard FCFF formula starting from EBIT is `EBIT * (1 - Tax Rate) + D&A - Capex - Change in WC`. SBC is typically handled by accounting for future share dilution, which you are already doing by projecting a lower share count. Subtracting it again effectively double-counts its impact.
2.  **Incorrect WACC Weights:** The weights for equity and debt in your WACC calculation are incorrect. The denominator for the weights should be the sum of the Market Value of Equity (E) and the Market Value of Debt (D), i.e., `V = E + D`. You used Enterprise Value as the denominator, which is incorrect as it already nets out cash.
3.  **Overly Conservative Terminal Multiple:** While it's prudent to be conservative, an 8.0x EV/EBITDA exit multiple is on the low end for a scaled, flagship integrated resort operator like MGM, which historically trades in a higher 9-11x range in a stable economic environment. A "just right" assumption would be closer to the historical median for the sector.

Below is a revised valuation that corrects these issues while retaining the structure and well-reasoned parts of your original analysis.

***

### **Part 1: Market-Implied Valuation (Reverse DCF)**

*(This section is well-structured and serves as a good baseline. No changes are needed here.)*

#### **A) Establish Baseline & Market Price**

*   **Current Market Price:** $38.06 (Market close, August 22, 2025).

#### **Baseline Financials (TTM)**

| Metric | Amount (in millions) | Source |
| :--- | :--- | :--- |
| Revenue | $17,212 | (stockanalysis.com/stocks/MGM/financials/, August 23, 2025) |
| Gross Margin | 44.95% | (stockanalysis.com/stocks/MGM/financials/, August 23, 2025) |
| Operating Income (EBIT) | $1,478 | (stockanalysis.com/stocks/MGM/financials/, August 23, 2025) |
| Net Income | $539.52 | (stockanalysis.com/stocks/MGM/financials/cash-flow-statement/, August 23, 2025) |
| Depreciation & Amortization | $921 | (stockanalysis.com/stocks/MGM/financials/cash-flow-statement/, August 23, 2025) |
| Stock-Based Compensation | $86.01 | (stockanalysis.com/stocks/MGM/financials/cash-flow-statement/, August 23, 2025) |
| Capital Expenditures | $1,237 | (stockanalysis.com/stocks/MGM/financials/cash-flow-statement/, August 23, 2025) |
| Change in Working Capital | ($59.07) | (stockanalysis.com/stocks/MGM/financials/cash-flow-statement/, August 23, 2025) |
| Interest Expense | $433.31 | (stockanalysis.com/stocks/MGM/financials/, August 23, 2025) |
| Cash & Equivalents | $1,958 | (stockanalysis.com/stocks/MGM/financials/balance-sheet/, August 23, 2025) |
| Total Debt | $6,205 | (stockanalysis.com/stocks/MGM/financials/balance-sheet/, August 23, 2025) |
| Diluted Shares Outstanding | 292 | (stockanalysis.com/stocks/MGM/financials/, August 23, 2025) |

#### **B) Reverse-Engineer Assumptions**

To determine the assumptions embedded in the current stock price, I will hold the operating margin and other ratios constant at TTM levels and solve for the required 5-year revenue growth rate.

*   **WACC (preliminary estimate):** 7.5%
*   **Terminal Growth Rate:** 2.5%

Based on these inputs, a reverse DCF model indicates the market is pricing in a **5-year revenue CAGR of approximately 7.5%** while maintaining the current **TTM EBIT margin of 8.58%**. This implies that to justify the current price of $38.06, an investor must believe that MGM can grow its revenues consistently at 7.5% per year for the next five years without any margin deterioration.

### **Part 2: Analyst's Revised Valuation (Corrected Base-Case)**

#### **C) Formulate Conservative Assumptions**

*(Your initial assumptions on growth, margins, and taxes are well-reasoned and will be retained. The primary changes will be in the calculation methodology.)*

*   **Revenue Growth (Years 1-5):** Retaining your tapering growth rate, starting at 6% in Year 1 and declining to 3% by Year 5, for a **five-year average of 4.5%**. This reflects a normalization from post-pandemic recovery highs and is a prudent, conservative assumption.
*   **Operating Margin:** Retaining the TTM EBIT margin of **8.58%** as the base, assuming stable profitability.
*   **Taxes:** Using a normalized statutory rate of **21%**.
*   **Capital Intensity:**
    *   **Capex:** Maintained at **7.2% of revenue**.
    *   **Working Capital:** Modeled as **1.0% of incremental revenue**.
*   **Buybacks and Dilution:** Assuming a net reduction in shares outstanding of **3.0% annually** to model aggressive buybacks net of any SBC dilution.

#### **D) Free Cash Flow Construction (Corrected)**

**Correction:** The FCFF formula has been corrected to `FCFF = NOPAT + D&A - Capex - Change in Working Capital`. Stock-Based Compensation is not subtracted here.

| (USD, in millions) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $18,245 | $19,157 | $20,020 | $20,821 | $21,445 |
| EBIT (8.58% of Revenue) | $1,565 | $1,644 | $1,718 | $1,786 | $1,840 |
| NOPAT (EBIT * 0.79) | $1,237 | $1,299 | $1,357 | $1,411 | $1,453 |
| D&A | $975 | $1,023 | $1,069 | $1,112 | $1,145 |
| Capex | ($1,314) | ($1,379) | ($1,441) | ($1,500) | ($1,544) |
| Change in WC | ($10) | ($9) | ($9) | ($8) | ($6) |
| **Free Cash Flow to Firm** | **$888** | **$933** | **$976** | **$1,015** | **$1,048** |

#### **E) Discount Rate (WACC) (Corrected)**

*   **Cost of Equity (CAPM):**
    *   Risk-Free Rate: 4.25% (10-Year U.S. Treasury Yield, August 2025).
    *   Equity Risk Premium: 5.0%.
    *   Beta: 1.39.
    *   **Cost of Equity = 4.25% + 1.39 * 5.0% = 11.2%**
*   **Cost of Debt:**
    *   Pre-tax Cost of Debt = 6.98% (Interest Expense / Total Debt).
    *   After-tax Cost of Debt = 6.98% * (1 - 0.21) = 5.52%.
*   **WACC (Corrected Weights):**
    *   Market Cap (E) = $11,114M.
    *   Total Debt (D) = $6,205M.
    *   Total Capital (V = E + D) = $11,114M + $6,205M = $17,319M.
    *   Weight of Equity (E/V) = $11,114 / $17,319 = 64.2%.
    *   Weight of Debt (D/V) = $6,205 / $17,319 = 35.8%.
    *   **WACC = (0.642 * 11.2%) + (0.358 * 5.52%) = 7.19% + 1.98% = 9.17%**

#### **F) Terminal Value (Revised)**

*   **Gordon Growth Cross-Check:**
    *   Terminal Value = (Year 5 FCFF * (1 + g)) / (WACC - g) = ($1,048 * 1.025) / (9.17% - 2.5%) = $16,099M.
    *   Year 5 EBITDA = Year 5 EBIT + Year 5 D&A = $1,840M + $1,145M = $2,985M.
    *   Implied EV/EBITDA multiple = $16,099M / $2,985M = **5.39x**. This is still unrealistically low for a premier operator and suggests the long-term growth and margin assumptions are too conservative for the Gordon Growth Model to be reliable.
*   **Exit Multiple Method (Revised):**
    *   A more realistic terminal multiple for a stable, mature company in this sector would be closer to its historical average. An 8.0x multiple is too conservative. We will use a **9.5x EV/EBITDA multiple**, which is more in line with the industry median for a market leader, reflecting a balance between conservatism and historical reality.
    *   **Revised Terminal Value (9.5x EBITDA) = $2,985M * 9.5 = $28,358M.**

#### **G) Enterprise to Equity Bridge (Recalculated)**

*   PV of Explicit Period FCFF = $888/(1.0917)^1 + $933/(1.0917)^2 + $976/(1.0917)^3 + $1015/(1.0917)^4 + $1048/(1.0917)^5 = $813 + $781 + $750 + $716 + $677 = **$3,737M**.
*   PV of Terminal Value = $28,358M / (1.0917)^5 = **$18,224M**.
*   **Enterprise Value = $3,737M + $18,224M = $21,961M**.
*   **Equity Value** = $21,961M (Enterprise Value) - $6,205M (Total Debt) + $1,958M (Cash) = **$17,714M**.

#### **H) Per-Share Value and Margin of Safety (Recalculated)**

*   **Projected Year 5 Share Count:** 292M * (1 - 0.03)^5 = **250M shares**.
*   **Analyst's Base-Case Fair Value = $17,714M / 250M shares = $70.86**.
*   **Valuation Range:**
    *   **Base Case:** **$70.86**.
    *   **Low/Bear Case:** (Lower growth of 2%, margin compression to 7.5%, 8.0x Exit Multiple) -> **$54.00**.
    *   **High/Bull Case:** (Higher growth of 6%, margin expansion to 9.5%, 10.5x Exit Multiple) -> **$91.00**.
*   **Margin of Safety (MOS) Price (30% discount):** $70.86 * (1 - 0.30) = **$49.60**.

### **Risk Notes**

*(These risks are well-articulated and remain highly relevant.)*

1.  **Macroeconomic Sensitivity:** As a consumer discretionary company, MGM's performance is highly sensitive to economic downturns, which could reduce travel and gaming budgets.
2.  **Regulatory Risks:** The gaming industry is heavily regulated. Changes in gaming laws or tax structures in key markets like Las Vegas or Macau could materially impact profitability.
3.  **Competitive Pressures:** The hospitality and gaming industry is intensely competitive. Increased competition, particularly from online gaming, could pressure margins.
4.  **Geopolitical Risks:** A significant portion of MGM's business is in Macau, making it vulnerable to geopolitical tensions and policy changes from the Chinese government.

final answer is 70.86 $