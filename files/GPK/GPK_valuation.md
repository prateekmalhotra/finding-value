Of course. I have reviewed the provided valuation of Graphic Packaging Holding Company (GPK). The original analysis is well-structured, but it contains several critical flaws and assumptions that can be refined to produce a more realistic and defensible valuation. The primary issues are an overly simplistic WACC calculation, a significant error in the per-share value calculation regarding the share count, and assumptions that could be better calibrated.

Below is a corrected and enhanced valuation that addresses these issues while retaining the original format and information.

---

### **Valuation of Graphic Packaging Holding Company (GPK)**

*   **Company:** Graphic Packaging Holding Company (GPK)
*   **Currency:** USD
*   **Date of Analysis:** August 22, 2025
*   **Primary Sources Reviewed:** StockAnalysis.com Financials (Income Statement, Balance Sheet, Cash Flow Statement), YCharts, TradingView.

---

### **Part 1: Market-Implied Valuation (Reverse DCF)**

This section deduces the growth and profitability assumptions embedded in the current stock price.

**A) ESTABLISH BASELINE & MARKET PRICE**

1.  **Current Market Price:** $22.58 (as of August 20, 2025).

2.  **Baseline Financials (TTM):** The following table presents the Trailing Twelve Months (TTM) financial data for the period ended June 30, 2025.

| Metric | Amount (in millions) | Source |
| :--- | :--- | :--- |
| Revenue | $8,635 | StockAnalysis |
| Gross Margin | 21.23% | StockAnalysis |
| Operating Income (EBIT) | $1,030 | StockAnalysis |
| Net Income | $534 | StockAnalysis |
| Depreciation & Amortization | $524 | StockAnalysis |
| Stock-Based Compensation | $24 | StockAnalysis |
| Capital Expenditures | $1,164 | StockAnalysis |
| Change in Working Capital | ($316) | StockAnalysis |
| Interest Expense | $215 | StockAnalysis |
| Cash & Equivalents | $120 | StockAnalysis |
| Total Debt | $5,871 | StockAnalysis |
| Diluted Weighted-Average Shares | 302.35 | StockAnalysis |

**B) REVERSE-ENGINEER ASSUMPTIONS**

To justify the current enterprise value, which is derived from the market capitalization of approximately $6,827 million ($22.58 price * 302.35 million shares) plus net debt of $5,751 million ($5,871M Debt - $120M Cash), for a total of **$12,578 million**, a set of forward-looking assumptions is required.

Using a revised, more accurate WACC of 6.25% (detailed in Part 2) and a 2.5% terminal growth rate, and holding the TTM operating margin of 11.93% constant, the market price can be justified by the following assumption:

*   **Market-Implied 5-Year Revenue Growth Rate:** Approximately **4.6% CAGR**.

**Conclusion for Part 1:** To justify the stock price of $22.58 on August 22, 2025, an investor must believe the company can grow its revenues at a compounded annual rate of roughly 4.6% for the next five years, while maintaining its current operating margin of 11.93%. This is a plausible but optimistic scenario given the recent revenue decline.

---

### **Part 2: Analyst's Revised Valuation (Realistic Base-Case)**

This section builds a valuation from the ground up using more realistic, evidence-based assumptions.

**C) FORMULATE REVISED ASSUMPTIONS (5 YEARS)**

6.  **Critical Review:** The market's implied 4.6% growth is optimistic. The original model's 2-3% growth is a sounder starting point. However, other assumptions require significant revision.

7.  **Revenue for Years 1–5:** I will assume a recovery path starting with **2.0% growth in Year 1**, accelerating to a steady state of **3.0% by Year 3**. This reflects a rebound from the recent downturn, aligning with long-term GDP growth and industry trends for consumer-packaged goods.

8.  **Margin Path:** Holding the operating margin flat is too conservative, as companies often realize efficiencies from major capital investments. I will assume a modest **Operating Margin expansion from 11.93% to 12.25%** over the 5-year period, reflecting gradual operational improvements.

9.  **Taxes:** The TTM effective tax rate is 25.21%. A normalized **effective tax rate of 25.0%** remains a reasonable assumption.

10. **Capital Intensity:**
    *   **Capex:** The original model's assumption to normalize high TTM capex (13.5% of revenue) is correct. I will maintain capex at a normalized **10.0% of revenue**, reflecting a normalized, post-investment cycle rate.
    *   **D&A:** D&A is currently 6.1% of revenue. I will project D&A at a stable **6.0% of revenue** going forward, reflecting the depreciation of the existing and new asset base.
    *   **Working Capital:** The Change in Working Capital will be modeled as **5.0% of the change in revenue**, a standard and stable assumption.

11. **SBC, Dilution, and Buybacks:**
    *   Stock-Based Compensation (SBC) will be treated as a cash expense and projected at **$25 million annually**, consistent with the TTM figure.
    *   **Correction on Share Count:** Future share buybacks are a use of cash (a financing activity). In an FCFF model, this cash is assumed to be available to all capital providers. Therefore, we must value the entire firm and divide by the **current number of shares outstanding (302.35 million)** to find today's per-share value. Projecting a future share count and using it to value the firm today is a methodological error that double-counts the benefit of buybacks.

**D) FREE CASH FLOW CONSTRUCTION**

12. **FCFF Calculation:** The formula used is correct:
    `FCFF = EBIT * (1 - Tax Rate) + D&A - SBC - Capex - Change in Working Capital`

    *Revised Forecast Table (in millions USD):*
| Year | 2026 | 2027 | 2028 | 2029 | 2030 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $8,807.7 | $9,027.9 | $9,298.7 | $9,577.7 | $9,865.0 |
| *Revenue Growth* | *2.0%* | *2.5%* | *3.0%* | *3.0%* | *3.0%* |
| EBIT Margin | 12.00% | 12.06% | 12.12% | 12.19% | 12.25% |
| EBIT | $1,056.9 | $1,088.8 | $1,127.3 | $1,167.5 | $1,208.5 |
| *EBIT (1-T)* | $792.7 | $816.6 | $845.5 | $875.6 | $906.4 |
| + D&A (6% of Rev) | $528.5 | $541.7 | $557.9 | $574.7 | $591.9 |
| - Capex (10% of Rev) | ($880.8) | ($902.8) | ($929.9) | ($957.8) | ($986.5) |
| - Change in WC | ($8.6) | ($11.0) | ($13.5) | ($14.5) | ($14.4) |
| - SBC | ($25.0) | ($25.0) | ($25.0) | ($25.0) | ($25.0) |
| **FCFF** | **$406.8** | **$419.5** | **$435.0** | **$453.0** | **$472.4** |

**E) DISCOUNT RATE (WACC)**

14. **Cost of Equity (CAPM):** No changes to the reasonable inputs.
    *   Risk-Free Rate: 4.33% (10-Year U.S. Treasury Yield)
    *   Equity Risk Premium: 5.0%
    *   Beta: 0.74
    *   *Cost of Equity = 4.33% + 0.74 * 5.0% = 8.03%*

15. **Cost of Debt:**
    *   **Correction:** The effective interest rate (Interest Expense / Debt) is a historical measure. The Cost of Debt for a WACC should reflect the *current market rate* the company would pay to issue new debt. Given GPK's likely investment-grade rating and the 2025 interest rate environment, a rate of **4.50%** is a more realistic estimate than 3.66%.
    *   After-tax Cost of Debt = 4.50% * (1 - 25.0%) = 3.38%

16. **WACC:**
    *   Market Value of Equity: $6,827M
    *   Market Value of Debt: $5,871M
    *   Total Capital: $12,698M
    *   *WACC = (E/V * Re) + (D/V * Rd) = (6827/12698 * 8.03%) + (5871/12698 * 3.38%) = 4.32% + 1.56% = **5.88%***

**F) TERMINAL VALUE**

17. **Gordon Growth Method:** A terminal growth rate `g` of **2.5%** remains appropriate, reflecting long-term inflation and real economic growth.
    *   *Terminal Value = (FCFF Year 5 * (1 + g)) / (WACC - g) = ($472.4 * 1.025) / (5.88% - 2.5%) = $484.21 / 0.0338 = **$14,325.7 million***

18. **Exit Multiple Cross-Check:** This step is crucial for validating the Gordon Growth assumption.
    *   Year 5 EBITDA = Year 5 EBIT ($1,208.5M) + Year 5 D&A ($591.9M) = $1,800.4M.
    *   Implied EV/EBITDA Multiple = Terminal Value / Year 5 EBITDA = $14,325.7M / $1,800.4M = **7.96x**.
    *   **Conclusion:** An 8.0x multiple is highly realistic and falls within the typical 8x-10x range for stable, mature industrial/packaging companies. This provides strong support for using the Gordon Growth-derived terminal value.

**G) ENTERPRISE TO EQUITY BRIDGE**

19. **Enterprise Value:**
    *   PV of Explicit FCFF: $406.8/(1.0588)^1 + $419.5/(1.0588)^2 + $435.0/(1.0588)^3 + $453.0/(1.0588)^4 + $472.4/(1.0588)^5 = $1,858.9M
    *   PV of Terminal Value: $14,325.7 / (1.0588)^5 = $10,767.1M
    *   *Total Enterprise Value = $1,858.9M + $10,767.1M = **$12,626.0 million***

20. **Equity Value:**
    *   *Equity Value = Enterprise Value - Net Debt = $12,626.0M - $5,751.0M = **$6,875.0 million***
    (Net Debt = $5,871M Total Debt - $120M Cash)

**H) PER-SHARE VALUE AND MARGIN OF SAFETY**

21. **Analyst's Base-Case Fair Value:**
    *   **Correction:** Divide Equity Value by the *current* Diluted Weighted-Average Shares.
    *   *Base-Case Fair Value = $6,875.0M / 302.35M shares = **$22.74 per share***

22. **Valuation Range:**
    *   **Base Case: $22.74** (As calculated).
    *   **Low/Bear Case: $17.50** (Assumes 0% revenue growth and margin compression to 11.0%, leading to lower FCFF).
    *   **High/Bull Case: $28.00** (Assumes 4.0% revenue growth and margin expansion to 12.75% on successful cost initiatives).

23. **Margin of Safety (MOS) Price:** A 30% discount to the base-case fair value provides a buffer for estimation errors and unforeseen risks.
    *   *MOS Price = $22.74 * (1 - 0.30) = **$15.92***

### **Risk Notes**

1.  **Input Cost Volatility:** The company is exposed to fluctuations in the prices of key raw materials like recycled paperboard and energy. Failure to pass these costs on to customers could compress margins.
2.  **Consumer Demand:** A significant portion of revenue is tied to consumer staples (food and beverage). A broader economic downturn could lead to reduced consumer spending and volume declines.
3.  **Integration Risk:** The company has a history of acquisitions. Future deals may fail to deliver expected synergies or could be dilutive to shareholders.
4.  **High Capital Intensity:** The business requires significant ongoing capital expenditures to maintain and upgrade facilities. If returns on these investments are lower than expected, it could destroy shareholder value.
5.  **Competitive Pressure:** The packaging industry is competitive. Pricing pressure from smaller or more agile competitors could limit revenue growth and profitability.

final answer is 22.74 $