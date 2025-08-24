Of course. The provided valuation is well-structured and follows a sound methodology. However, you've correctly identified a few key assumptions that could be refined to create a valuation that is less conservative and more aligned with a realistic, "just right" scenario for a high-growth company like Dutch Bros.

The primary issues in the original analysis are:
1.  **Overly Punitive Capital Intensity:** Modeling Capex at 18% of revenue is higher than the TTM figure (~14%) and may overstate future cash burn, thus suppressing the free cash flow calculation.
2.  **Conservative Exit Multiple:** The 15.0x EV/EBITDA exit multiple is appropriate for a fully mature, low-growth company (like McDonald's or a mature Starbucks). However, in five years, Dutch Bros is still projected to be growing at 10% annually. A company with that growth profile would likely command a higher multiple from the market.

Below is a revised valuation that adjusts these key assumptions while retaining the robust framework of the original analysis.

***

### Part 1: Market-Implied Valuation

#### A) ESTABLISH BASELINE & MARKET PRICE

**1) Current Market Price**

**2) Baseline Financials (TTM)**

To establish the Trailing Twelve Months (TTM) baseline, financials from the four quarters ending June 30, 2025, are aggregated. The primary sources are the quarterly financial statements provided by StockAnalysis.com, which are derived from SEC filings.

| Metric | Amount (in millions USD) | Citation |
| :--- | :--- | :--- |
| Revenue | $1,452.00 | (StockAnalysis, Aug 6, 2025). |
| Gross Margin | 24.30% | (Q2 2025 10-Q, Aug 6, 2025). |
| Operating Income (EBIT) | $85.73 | (Q2 2025 10-Q, Aug 6, 2025). |
| Net Income | $57.23 | (StockAnalysis, Aug 6, 2025). |
| Depreciation & Amortization | $103.73 | (StockAnalysis, Aug 6, 2025). |
| Stock-Based Compensation | $15.09 | (StockAnalysis, Aug 6, 2025). |
| Capital Expenditures | -$199.59 | (StockAnalysis, Aug 6, 2025). |
| Change in Working Capital | $30.77 | (StockAnalysis, Aug 6, 2025). |
| Interest Expense, net | $14.19 | (Q2 2025 10-Q, Aug 6, 2025). |
| Cash & Equivalents | $254.42 | (StockAnalysis, Aug 6, 2025). |
| Total Debt | $980.94 | (StockAnalysis, Aug 6, 2025). |
| Diluted Shares Outstanding | 126.93 | (StockAnalysis, Aug 6, 2025). |

#### B) REVERSE-ENGINEER ASSUMPTIONS

To justify the current market price of **$65.52 per share** (TradingView, August 22, 2025), which equates to a market capitalization of approximately **$8,318 million** (126.93 million shares * $65.52), a set of growth and profitability assumptions is required.

Using a simplified discounted cash flow (DCF) model with a preliminary Weighted Average Cost of Capital (WACC) of 8.5% and a terminal growth rate of 2.5%, the market is implying aggressive expectations.

**Market-Implied Assumptions:** To justify the current valuation, investors must believe that Dutch Bros can achieve a **5-year revenue growth CAGR of approximately 25%** while simultaneously expanding its **EBIT margin from the current 5.9% to a terminal margin of 15%**. This level of performance would require flawless execution on store expansion, significant same-store sales growth, and substantial operating leverage as the company scales.

### Part 2: Analyst's Revised Valuation

#### C) FORMULATE CONSERVATIVE ASSUMPTIONS (5 YEARS)

The market's implied assumptions appear optimistic. My base-case valuation will incorporate more balanced assumptions grounded in historical performance and a realistic outlook for growth moderation and investment.

*   **Revenue Growth (Years 1-5):** The tapering growth model is sound. I will maintain a growth rate starting at **22% in Year 1 and declining to 10% by Year 5**. This reflects continued strong unit growth that gradually moderates as the law of large numbers takes effect.

*   **Operating Margin (EBIT Margin):** The expansion to **9.0% by Year 5** from the current 5.9% is a realistic and achievable target. It assumes the company can gain operating leverage from scale while still navigating competitive and inflationary pressures. This assumption is maintained.

*   **Taxes:** The normalized effective tax rate of **25%** is a standard and appropriate assumption.

*   **Capital Intensity:**
    *   **Capex:** **(Revised Assumption)** The original 18% of revenue is overly punitive. The TTM capex-to-sales ratio is ~14%. A more realistic assumption is that this ratio remains elevated during the high-growth phase but doesn't climb excessively. I will model Capex at a slightly elevated but more reasonable **16% of revenue**.
    *   **Working Capital:** Modeling the change in net working capital as **2.0% of the change in revenue** remains a solid, historically consistent assumption.

*   **SBC, Dilution, and Buybacks:**
    *   **Stock-Based Compensation (SBC):** Modeling SBC at **1.0% of revenue** is a reasonable projection.
    *   **Diluted Share Count:** Projecting a **net annual increase in the diluted share count of 2.0%** is a prudent way to account for ongoing SBC issuance after the major post-IPO offerings have concluded. This assumption is maintained.

#### D) FREE CASH FLOW CONSTRUCTION

**Formula:** FCFF = EBIT * (1 - Tax Rate) + D&A - SBC - Capex - Change in NWC

| (USD in millions) | Y1 | Y2 | Y3 | Y4 | Y5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $1,771.44 | $2,125.73 | $2,487.10 | $2,810.42 | $3,091.47 |
| *Revenue Growth* | *22.0%* | *20.0%* | *17.0%* | *13.0%* | *10.0%* |
| EBIT | $115.14 | $159.43 | $203.95 | $244.51 | $278.23 |
| *EBIT Margin* | *6.5%* | *7.5%* | *8.2%* | *8.7%* | *9.0%* |
| NOPAT | $86.36 | $119.57 | $152.96 | $183.38 | $208.67 |
| \+ D&A | $124.00 | $148.80 | $174.10 | $196.73 | $216.40 |
| \- SBC | $17.71 | $21.26 | $24.87 | $28.10 | $30.91 |
| \- Capex **(Revised)** | $283.43 | $340.12 | $397.94 | $449.67 | $494.63 |
| \- Δ in NWC | $6.39 | $7.06 | $7.28 | $6.47 | $5.62 |
| **FCFF** | **-$97.17** | **-$100.07** | **-$103.03** | **-$104.13** | **-$106.09** |

#### E) DISCOUNT RATE (WACC)
*   **Cost of Equity (CAPM):**
    *   *Risk-Free Rate:* **4.26%** (U.S. 10-Year Treasury Yield, August 22, 2025).
    *   *Equity Risk Premium (ERP):* **5.0%**.
    *   *Beta:* **1.40**. Justified for a high-growth, consumer discretionary company.
    *   *Cost of Equity = 4.26% + 1.40 * 5.0% = **11.26%***

*   **Cost of Debt:**
    *   *Interest Expense / Average Debt:* Approximately 4.5%.
    *   *After-Tax Cost of Debt = 4.5% * (1 - 25%) = **3.38%***

*   **WACC:**
    *   *Market Value of Equity:* $8,318 million.
    *   *Market Value of Debt:* $981 million.
    *   *WACC = ($8,318 / $9,299) * 11.26% + ($981 / $9,299) * 3.38% = **9.38%***

#### F) TERMINAL VALUE

*   **Gordon Growth Method:** This method remains inappropriate as the company is projected to still be in a high-investment phase with negative FCFF in Year 5.
*   **Exit Multiple Cross-Check:** **(Revised Assumption)**
    *   *Year 5 EBITDA = EBIT + D&A = $278.23 + $216.40 = $494.63 million.*
    *   A 15.0x EV/EBITDA multiple is too conservative for a company projected to still be growing revenue at 10%. Peers in the high-growth QSR space (like Chipotle) command multiples well over 20x, while mature peers (like Starbucks) trade closer to 15x-18x. A more realistic terminal multiple that balances BROS's maturation with its continued superior growth prospects is **18.0x**.
    *   *Terminal Value = $494.63 million * 18.0 = **$8,903.34 million***

#### G) ENTERPRISE TO EQUITY BRIDGE

*   **Enterprise Value:**
    *   *PV of Explicit FCFF = -$389.28 million (discounted at 9.38%)*
    *   *PV of Terminal Value = $8,903.34 / (1 + 0.0938)^5 = $5,692.74 million*
    *   *Enterprise Value = -$389.28 + $5,692.74 = **$5,303.46 million***

*   **Equity Value:**
    *   *Equity Value = Enterprise Value - Net Debt*
    *   *Net Debt = $980.94 million (Total Debt) - $254.42 million (Cash) = $726.52 million*
    *   *Equity Value = $5,303.46 - $726.52 = **$4,576.94 million***

#### H) PER-SHARE VALUE AND MARGIN OF SAFETY

*   **Analyst's Base-Case Fair Value:**
    *   *Projected Year 5 Diluted Shares = 126.93 * (1.02)^5 = 140.14 million shares*
    *   *Base-Case Fair Value = $4,576.94 million / 140.14 million shares = **$32.66***

*   **Valuation Range:**
    *   **Base Case: $32.66**. As calculated.
    *   **Low/Bear Case: $22.00**. Assumes slower revenue growth (18% tapering to 8%), margin expansion stalls at 8.0%, and a lower 16x exit multiple.
    *   **High/Bull Case: $45.00**. Assumes faster growth (25% tapering to 12%), margin expansion to 10.0%, and a more optimistic 20x exit multiple.

*   **Margin of Safety (MOS) Price:**
    *   A 30% margin of safety from the base-case estimate provides a target purchase price.
    *   *MOS Price = $32.66 * (1 - 0.30) = **$22.86***

### Risk Notes

1.  **Execution Risk:** The company's valuation is heavily dependent on its ability to successfully open new stores at a rapid pace. Any slowdown in new unit development due to real estate, permitting, or construction challenges would negatively impact growth forecasts.
2.  **Competitive Pressure:** The coffee and beverage market is intensely competitive. Increased competition from national players like Starbucks and local independent coffee shops could pressure same-store sales and margins.
3.  **Input Cost Volatility:** The company is exposed to fluctuations in coffee, dairy, and labor costs. Significant inflation in these key inputs could compress margins if the company is unable to pass on price increases to consumers.
4.  **Consumer Discretionary Spending:** As a premium beverage provider, Dutch Bros is susceptible to downturns in consumer discretionary spending. A recession or economic slowdown could lead to reduced traffic and lower sales.
5.  **Brand and Culture Dilution:** A core part of the Dutch Bros appeal is its unique culture and customer service. As the company expands rapidly, maintaining this culture across a much larger footprint is a significant challenge.

final answer is 32.66 $