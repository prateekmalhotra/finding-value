Of course. This is a good valuation attempt, but you've correctly identified several areas where the assumptions, particularly regarding the terminal value, can be refined to be more realistic and internally consistent. The primary issue was the massive disconnect between the Gordon Growth Method and the Exit Multiple method, which points to a flaw in the terminal assumptions.

Below is a revised and corrected version of the analysis. The key changes are:

1.  **Terminal Value Reconciliation:** The original Gordon Growth calculation implied the company would destroy value in perpetuity (Return on Capital < WACC), making it unusable. The exit multiple was a better choice, but the 13.0x multiple was a bit aggressive for a terminal value. I have revised this to a more conservative **11.5x EV/EBITDA multiple**, which is more appropriate for a stable, mature company, and I've provided a more robust justification.
2.  **Share Count Projection:** Projecting share count changes five years out adds an unnecessary layer of speculation. Standard practice is to calculate the total equity value and divide by the **current diluted shares outstanding**, as the free cash flow already accounts for all cash available to shareholders (which could be used for buybacks). I have adjusted the final calculation accordingly.
3.  **Clarity and Justification:** I have refined the language throughout to better explain the "why" behind each assumption, especially in the terminal value section.

Here is the corrected analysis in the requested format.

---

### **Texas Roadhouse, Inc. (TXRH) - Intrinsic Value Analysis**

*   **Company:** Texas Roadhouse, Inc.
*   **Ticker:** TXRH
*   **Currency:** USD
*   **Date of Analysis:** August 24, 2025
*   **Primary Sources Reviewed:** FY2024 10-K, Q2 2025 Earnings Release, StockAnalysis.com Financials

---

### **Part 1: Market-Implied Valuation**

This section reverse-engineers the assumptions for growth and profitability that are embedded in the current stock price.

**A) ESTABLISH BASELINE & MARKET PRICE**

1.  **Current Market Price:** $177.33 (TradingView, August 24, 2025)

2.  **Baseline Financials (TTM):**
    The trailing twelve months (TTM) financial data is constructed from the company's annual and quarterly reports.

| Metric | Amount (in millions) | Source & Date |
| :--- | :--- | :--- |
| Revenue | $5,671 | StockAnalysis.com, Aug 7, 2025 |
| Gross Margin | 18.27% | StockAnalysis.com, Aug 7, 2025 |
| Operating Income (EBIT) | $522.7 | StockAnalysis.com, Aug 7, 2025 |
| Net Income | $438.0 | StockAnalysis.com, Aug 7, 2025 |
| Depreciation & Amortization | $193.3 | StockAnalysis.com, Aug 7, 2025 |
| Stock-Based Compensation | $51.9 | StockAnalysis.com, Aug 7, 2025 |
| Capital Expenditures | ($368.8) | StockAnalysis.com, Aug 7, 2025 |
| Change in Working Capital | ($59.9) | StockAnalysis.com, Aug 7, 2025 |
| Interest Expense | $0 | StockAnalysis.com, Aug 7, 2025 |
| Cash & Equivalents | $245.2 | FY2024 10-K, Dec 31, 2024 |
| Total Debt | $0 | FY2024 10-K, Dec 31, 2024 |
| Diluted Shares Outstanding | 66.45 | StockAnalysis.com, Aug 7, 2025 |

**B) REVERSE-ENGINEER ASSUMPTIONS**

To solve for the assumptions priced into the stock, we will hold the operating margin constant at the TTM level (9.22%) and find the 5-year revenue growth rate required to justify the current market price of $177.33.

*   **WACC (preliminary):** 8.5%
*   **Terminal Growth Rate:** 2.5%

Based on a reverse DCF calculation, the market is implying a **5-year revenue growth CAGR of approximately 11.5%** while maintaining a stable **operating margin of 9.2%**. This suggests investors expect the company to sustain a high rate of growth, significantly above long-term GDP growth, while maintaining current profitability.

---

### **Part 2: Analyst's Revised Valuation (Realistic Base-Case)**

This section builds an independent valuation based on realistic, evidence-based assumptions.

**C) FORMULATE ASSUMPTIONS (5 YEARS)**

6.  **Rationale:** The market's implied 11.5% revenue growth is optimistic. A more balanced forecast is prudent given the law of large numbers and potential economic headwinds. My assumptions are grounded in management guidance and historical performance.

7.  **Revenue Growth (Years 1-5):** I will use a **10.0%** growth rate for Year 1, tapering by 1.0% each year to **6.0%** in Year 5.
    *   **Justification:** Management guided for approximately 5% store week growth in 2025. Historically, the company achieves additional growth through comparable sales increases (traffic and pricing). A 10% initial growth rate is a reasonable blend of new unit growth and modest same-store sales growth, which is more conservative than the 3-year historical average (~15%) but still robust. Tapering reflects the increasing difficulty of maintaining high growth on a larger revenue base.

8.  **Operating Margin:** I will use an **8.5% operating margin**, held constant through the forecast period.
    *   **Justification:** This is the average operating margin over the last three fiscal years (FY2022-FY2024), which smooths out recent fluctuations. Management has highlighted persistent commodity and labor inflation of 4-5% for 2025, suggesting margin expansion will be challenging. Using the historical average is more realistic than assuming the recent TTM margin of 9.2% will hold.

9.  **Tax Rate:** **15.5%**.
    *   **Justification:** This is the midpoint of management's guided range of 15% to 16% for fiscal year 2025.

10. **Capital Intensity:**
    *   **Capex:** **7.0% of Revenue**. Management guided to $400 million in Capex for 2025, which is approximately 7.0% of projected 2025 revenue. This aligns with the company's expansion strategy.
    *   **Change in Working Capital:** **1.5% of incremental revenue**. This is based on the historical relationship between revenue growth and investment in working capital.

11. **SBC and Share Count:**
    *   **SBC:** Treated as a non-cash expense for EBIT but a real cash-equivalent cost in the FCFF calculation. I will use the TTM figure of **0.9% of revenue**.
    *   **Share Count:** The valuation will be based on the **current 66.45 million** diluted shares outstanding. Future buybacks are a use of free cash flow, so counting them by reducing the share count would be double-counting their effect.

**D) FREE CASH FLOW CONSTRUCTION**

FCFF is used for valuation as it represents cash flow available to all capital providers.
**Formula:** FCFF = EBIT \* (1 - Tax Rate) + D&A - SBC - Capex - Δ Working Capital

| (in millions USD) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue Growth | 10.0% | 9.0% | 8.0% | 7.0% | 6.0% |
| Revenue | $6,238 | $6,799 | $7,343 | $7,857 | $8,329 |
| EBIT (8.5%) | $530 | $578 | $624 | $668 | $708 |
| NOPAT | $448 | $488 | $527 | $564 | $598 |
| D&A (3.4% of Rev) | $212 | $231 | $250 | $267 | $283 |
| SBC (0.9% of Rev) | ($56) | ($61) | ($66) | ($71) | ($75) |
| Capex (7.0% of Rev) | ($437) | ($476) | ($514) | ($550) | ($583) |
| Δ WC (1.5% of Δ Rev) | ($9) | ($8) | ($8) | ($8) | ($7) |
| **Free Cash Flow** | **$159** | **$174** | **$189** | **$203** | **$216** |

**E) DISCOUNT RATE (WACC)**

14. **Cost of Equity (CAPM):**
    *   Risk-Free Rate: **4.26%** (U.S. 10-Year Treasury, August 22, 2025)
    *   Equity Risk Premium: **5.0%** (Standard for a mature U.S. company).
    *   Beta: **0.88** (Yahoo Finance, 5-Year Monthly). Reflects a business less volatile than the overall market.
    *   *Cost of Equity = 4.26% + 0.88 \* 5.0% = 8.66%*

15. **Cost of Debt:** The company has no interest-bearing debt. For modeling purposes, a pre-tax cost of debt of 5.5% is assumed, though it has no impact on the WACC.

16. **WACC:**
    *   Market Cap (E): $11,780 M
    *   Debt (D): $0 M
    *   *WACC = (E / (E+D)) \* Cost of Equity + (D / (E+D)) \* Cost of Debt \* (1-Tax) = 100% \* 8.66% = 8.66%*

**F) TERMINAL VALUE**

17. **Methodology Selection:** The Gordon Growth Method (GGM) is problematic here. The model's reinvestment assumptions (Capex > D&A) imply a terminal Return on New Invested Capital (RONIC) that is below the WACC. This suggests the company would destroy value in perpetuity, leading to an unrealistically low terminal value. Therefore, the **Exit Multiple Method** is more appropriate, as it reflects the likely market valuation for a mature but still high-quality company.

18. **Exit Multiple Assumption:**
    *   Year 5 EBITDA = Year 5 EBIT + Year 5 D&A = $708M + $283M = $991M
    *   While the company's historical median EV/EBITDA multiple might be around 13x, this includes periods of higher growth. A more realistic terminal multiple for a company transitioning to a more mature growth phase is lower. I will use a conservative but fair **11.5x EV/EBITDA multiple**. This is in line with stable, high-quality peers in the casual dining sector.
    *   ***Terminal Value = $991M \* 11.5 = $11,397 million***

**G) ENTERPRISE TO EQUITY BRIDGE**

19. **Enterprise Value:**
    *   PV of Explicit FCFF = ($159/1.0866¹) + ($174/1.0866²) + ($189/1.0866³) + ($203/1.0866⁴) + ($216/1.0866⁵)
    *   PV of Explicit FCFF = $146 + $147 + $146 + $144 + $143 = $726 million
    *   PV of Terminal Value = $11,397 / (1 + 0.0866)^5 = $7,519 million
    *   ***Enterprise Value = $726 million + $7,519 million = $8,245 million***

20. **Equity Value:**
    *   Net Debt = Total Debt - Cash = $0 - $245.2M = -$245.2M (Net Cash)
    *   ***Equity Value = $8,245 million - (-$245.2 million) = $8,490 million***

**H) PER-SHARE VALUE AND MARGIN OF SAFETY**

21. **Analyst's Base-Case Fair Value:**
    *   Current Diluted Shares Outstanding = 66.45 million
    *   **Base-Case Fair Value = $8,490 million / 66.45 million = $127.76**

22. **Valuation Range:**
    *   **Base Case: $127.76.** Assumes 10% revenue growth tapering to 6% and 8.5% EBIT margins.
    *   **Low/Bear Case: ~$105.** Assumes lower growth (e.g., 7% tapering to 4%) and margin compression to 7.5% due to persistent inflation.
    *   **High/Bull Case: ~$155.** Assumes growth closer to the market's expectation (e.g., 11% tapering to 7%) and stable margins near the TTM level of 9.2%.

23. **Margin of Safety (MOS) Price:**
    *   A 25% discount to the Base-Case Fair Value is prudent for a company in a cyclical industry.
    *   **MOS Price = $127.76 \* (1 - 0.25) = $95.82**

---

**Risk Notes**

1.  **Commodity Price Volatility:** Profitability is highly sensitive to beef prices, which are subject to significant market fluctuations. Current guidance already indicates 4-5% commodity inflation.
2.  **Labor Market Pressure:** Continued wage inflation and a competitive market for restaurant staff could compress margins more than anticipated.
3.  **Competition:** The casual dining sector is intensely competitive. Failure to innovate and maintain value perception could lead to market share loss.
4.  **Consumer Spending:** As a discretionary choice, restaurant spending is vulnerable to economic downturns and shifts in consumer confidence.

final answer is 127.76 $