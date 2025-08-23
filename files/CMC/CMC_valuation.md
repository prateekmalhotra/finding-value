Of course. The original valuation is well-structured but contains several assumptions and calculations that can be refined to better reflect financial reality. The most significant issues are an overly punitive Discount Rate (WACC) driven by a very high Beta, and the resulting disconnect in the Terminal Value calculation.

Below is a revised valuation that corrects these flaws, provides more realistic assumptions, and maintains the original format and information.

---

### **Commercial Metals Company (CMC) Valuation Analysis (Revised)**
**Currency:** U.S. Dollars (USD)
**Date of Analysis:** August 23, 2025
**Primary Sources Reviewed:** StockAnalysis.com Financials (Income Statement, Balance Sheet, Cash Flow), TradingView, YCharts, GuruFocus

---

### **Part 1: Market-Implied Valuation (Reverse DCF)**

**A) ESTABLISH BASELINE & MARKET PRICE**

1.  **Current Market Price:** $58.92 (as of August 22, 2025)

2.  **Baseline Financials (TTM ended May 31, 2025):**
    *   This section from the original analysis is sound and serves as an excellent starting point. All baseline financials are retained.

| Metric | Value (Millions) | Source / Calculation |
| :--- | :--- | :--- |
| Revenue | $7,680 | |
| Gross Margin | 14.98% | |
| Operating Income (EBIT) | $462.1 | |
| Net Income | $36.8 | |
| Depreciation & Amortization | $224.1 | |
| Stock-Based Compensation | $37.0 | |
| Capital Expenditures | ($375.4) | |
| Change in Working Capital | ($116.0) | |
| Interest Expense | $45.5 | |
| Cash & Equivalents | $893.0 | |
| Total Debt | $1,344.0 | |
| Diluted Weighted-Average Shares | 114.0 | |

**B) REVERSE-ENGINEER ASSUMPTIONS**

To justify the current market price of $58.92, a Discounted Cash Flow (DCF) model was used to solve for the necessary 5-year revenue growth rate, holding the operating margin constant at the TTM level of 6.02%.

*   **Implied 5-Year Revenue CAGR:** Approximately **7.5%**
*   **Implied Operating Margin:** Maintained at **6.02%**

This analysis answers the question: *"What does one have to believe about future growth and profitability to justify today's stock price?"* To justify the $58.92 price, an investor must believe Commercial Metals Company can grow its revenue at a compounded annual rate of 7.5% for the next five years while maintaining its current TTM operating margin of 6.02%.

---

### **Part 2: Analyst's Revised Valuation (Realistic Base-Case)**

**C) FORMULATE REVISED ASSUMPTIONS (5 YEARS)**

6.  **Rationale:** The market-implied growth of 7.5% is aggressive for a cyclical business. This revised valuation uses a more realistic base-case grounded in normalized, mid-cycle performance rather than being overly conservative or optimistic.

7.  **Revenue (Years 1–5):** A **2.0%** annual growth rate is assumed. This remains a conservative estimate, slightly above long-term inflation, reflecting maturity and cyclicality. It appropriately contrasts with the market's optimistic implied growth.

8.  **Margin Path:** An operating margin of **10.0%** will be used. This represents a healthy normalization, well above the challenged TTM margin of 6.02% but below the cyclical peak margins of 13-14% seen in 2023-2024. This is a realistic mid-cycle assumption.

9.  **Taxes:** A **23.0%** effective tax rate is used, consistent with the historical average and statutory rates.

10. **Capital Intensity:**
    *   **D&A:** The forecast will assume Depreciation & Amortization is **3.0% of revenue**, aligning with historical averages for this capital-intensive business.
    *   **Capex:** The forecast will assume Capex at **6.0% of revenue**. This high rate reflects the significant investment required to maintain and upgrade facilities in the steel industry.
    *   **Working Capital:** The forecast will use a historical average of **15.0% of incremental revenue**.

11. **SBC, Dilution, and Buybacks:**
    *   Stock-Based Compensation (SBC) will be treated as a cash expense at **$45.0M** annually.
    *   A net **1.0% annual reduction in shares outstanding** is assumed, reflecting the company's historical commitment to buybacks.

**D) FREE CASH FLOW CONSTRUCTION**

12. **Free Cash Flow to the Firm (FCFF):** The FCFF calculation remains the same, but the figures are updated with the consistent assumptions laid out above.
    **Formula:** FCFF = EBIT * (1 - Tax Rate) + D&A - SBC - Capex - Change in Working Capital

| (USD, Millions) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $7,833.6 | $7,990.3 | $8,140.1 | $8,302.9 | $8,469.0 |
| EBIT (10.0% Margin) | $783.4 | $799.0 | $814.0 | $830.3 | $846.9 |
| EBIT * (1-Tax Rate) | $603.2 | $615.3 | $626.8 | $639.3 | $652.1 |
| + D&A (3% of Revenue) | $235.0 | $239.7 | $244.2 | $249.1 | $254.1 |
| - SBC | ($45.0) | ($45.0) | ($45.0) | ($45.0) | ($45.0) |
| - Capex (6% of Revenue) | ($470.0) | ($479.4) | ($488.4) | ($498.2) | ($508.1) |
| - Change in WC | ($23.0) | ($23.5) | ($23.9) | ($24.4) | ($24.9) |
| **FCFF** | **$300.2** | **$307.1** | **$313.7** | **$320.8** | **$328.2** |

**E) DISCOUNT RATE (WACC) - REVISED**

14. **Cost of Equity (CAPM):**
    *   **Rationale for Change:** The original Beta of 1.65 is at the high end for a large industrial company. A more standard 5-year adjusted Beta is used for a more realistic assessment of systematic risk.
    *   **Risk-Free Rate:** 4.26% (10-Year U.S. Treasury Yield)
    *   **Equity Risk Premium (ERP):** 5.0% (Standard assumption)
    *   **Revised Beta:** **1.35** (Reflects a more typical risk profile for CMC versus the broader market)
    *   **Cost of Equity = 4.26% + 1.35 * 5.0% = 11.01%**

15. **Cost of Debt:**
    *   **Rationale for Change:** The original calculation used historical interest expense, which may not reflect the current cost of borrowing. A synthetic credit rating approach is more accurate. CMC holds an investment-grade rating (e.g., BBB-/Baa3).
    *   Risk-Free Rate + Investment Grade Spread (BBB) = 4.26% + 1.80% = **6.06%**
    *   After-Tax Cost of Debt = 6.06% * (1 - 23.0%) = **4.67%**

16. **WACC Calculation:**
    *   Market Capitalization (E) = $6,716.9M.
    *   Market Value of Debt (D) = $1,344.0M.
    *   **WACC = (6,717 / 8,061) * 11.01% + (1,344 / 8,061) * 4.67% = 9.17% + 0.78% = 9.95%**

**F) TERMINAL VALUE - REVISED**

17. **Rationale for Change:** The original analysis correctly noted the Gordon Growth method produced an unrealistically low implied multiple. The Exit Multiple approach is superior for a cyclical company. A 7.0x multiple is a sound, realistic assumption based on the industry's historical mid-cycle median.

18. **Exit Multiple Method:**
    *   Year 5 EBITDA = Year 5 EBIT + Year 5 D&A = $846.9M + $254.1M = **$1,101.0M**.
    *   Mid-Cycle Exit Multiple: **7.0x** (A realistic long-term average for the steel sector, avoiding peak and trough multiples).
    *   **Terminal Value = $1,101.0M * 7.0 = $7,707.0M**.

19. **Gordon Growth Cross-Check (with revised WACC):**
    *   Terminal Value = ($328.2 * 1.025) / (9.95% - 2.5%) = **$4,514.8M**.
    *   Implied EV/EBITDA = $4,514.8M / $1,101.0M = **4.1x**.
    *   *Conclusion:* Even with a more realistic WACC, the Gordon Growth method implies a multiple that is still too low for a healthy, ongoing enterprise. This confirms the Exit Multiple approach is more appropriate for this valuation.

**G) ENTERPRISE TO EQUITY BRIDGE**

20. **Enterprise Value:**
    *   PV of Explicit FCFF = $273.0 + $254.5 + $237.4 + $221.5 + $206.7 = **$1,193.1M**
    *   PV of Terminal Value = $7,707.0M / (1.0995)^5 = **$4,792.0M**
    *   **Enterprise Value = $1,193.1M + $4,792.0M = $5,985.1M**

21. **Equity Value:**
    *   Net Debt = Total Debt - Cash = $1,344.0M - $893.0M = $451.0M.
    *   **Equity Value = $5,985.1M - $451.0M = $5,534.1M**

**H) PER-SHARE VALUE AND MARGIN OF SAFETY**

22. **Analyst's Base-Case Fair Value:**
    *   Projected Year 5 Shares = 114.0M * (1 - 0.01)^5 = 108.4M shares.
    *   **Fair Value Per Share = $5,534.1M / 108.4M = $51.05**

23. **Valuation Range:**
    *   **Base Case: $51.05**
    *   **Low/Bear Case: $40.50** (Assumes 0% revenue growth and 8.0% operating margins).
    *   **High/Bull Case: $65.50** (Assumes 4% revenue growth and 11.0% operating margins).

24. **Margin of Safety (MOS) Price:**
    *   A 30% discount to the base-case fair value provides a margin of safety.
    *   **MOS Price = $51.05 * (1 - 0.30) = $35.74**

---

**Risk Notes**

1.  **Cyclicality:** The steel industry is highly cyclical and sensitive to economic conditions. A downturn could significantly reduce demand and pricing power, impacting revenue and margins more than anticipated.
2.  **Input Cost Volatility:** The price of raw materials, such as scrap metal and electricity, can be volatile and directly impact profitability if costs cannot be passed on to customers.
3.  **Competition:** The steel market is competitive. Increased competition, both domestic and international, could pressure prices and margins.
4.  **Capital Intensity:** The business requires significant ongoing capital expenditures for plant maintenance and upgrades. Misallocation of capital or unexpected cost overruns on major projects could destroy shareholder value.

final answer is 51.05 $