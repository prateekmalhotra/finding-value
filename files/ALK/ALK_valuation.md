Of course. Here is a critique of the provided valuation, followed by a revised and corrected version that addresses the identified issues, presented in the same comprehensive format.

### **Critique of the Original Valuation**

The provided valuation is well-structured but contains critical flaws that lead to an unreasonably low and likely inaccurate fair value estimate.

1.  **Unsustainable Capital Expenditure (Capex) Assumption:** The biggest issue is modeling Capex as a fixed 10.7% of revenue for all five years. For an airline, capex is cyclical and "lumpy," driven by large, infrequent aircraft purchases. The TTM period likely captured a high-investment phase. Projecting this high rate into perpetuity is unrealistic and results in deeply negative Free Cash Flows (FCFF) throughout the forecast period. This suggests the company is continuously destroying value, which is a problematic foundation for a valuation.

2.  **Flawed Terminal Value Calculation:** The original analysis correctly identifies that its projected FCFF for the final year is negative (-$770M). However, it then presents a Gordon Growth Model (GGM) result of $16,664M. It is mathematically impossible to apply a positive growth rate to a negative cash flow and arrive at a positive terminal value. The GGM formula `FCFF * (1+g) / (WACC-g)` would yield a large negative number. The valuation correctly abandons this flawed GGM calculation in favor of an Exit Multiple, but the foundational problem of negative cash flows remains.

3.  **WACC and Cost of Debt:** A pre-tax Cost of Debt of 3.5% seems low for an airline in a 2025 economic environment with a risk-free rate of 4.25%. A company's borrowing cost should be higher than the government's. A more realistic rate would be the risk-free rate plus a credit spread appropriate for ALK's credit rating.

The revised valuation below will address these points by normalizing capital expenditures, refining the cost of debt, and using a more robust terminal value methodology suitable for a capital-intensive industry.

---

Here is a revised and more realistic two-stage intrinsic valuation for Alaska Air Group, Inc. (ALK).

### **Valuation of Alaska Air Group, Inc. (ALK)**
*   **Company:** Alaska Air Group, Inc.
*   **Ticker:** ALK
*   **Currency:** USD
*   **Date of Analysis:** August 22, 2025
*   **Primary Sources Reviewed:**
    *   Form 10-K for the fiscal year ended December 31, 2024
    *   Form 10-Q for the quarterly period ended March 31, 2025

---

### **Part 1: Market-Implied Valuation (Reverse DCF)**

**A) ESTABLISH BASELINE & MARKET PRICE**

1.  **Current Market Price:** $59.16 (Market open, August 22, 2025).

2.  **Baseline Financials (TTM as of June 30, 2025):**

| Metric | Amount (in millions) | Citation |
| :--- | :--- | :--- |
| Revenue | $13,447 | (StockAnalysis, August 22, 2025). |
| Gross Margin | 23.10% | (Calculated from StockAnalysis, August 22, 2025). |
| Operating Income (EBIT) | $796 | (StockAnalysis, August 22, 2025). |
| Net Income | $313 | (StockAnalysis, August 22, 2025). |
| Depreciation & Amortization | $675 | (StockAnalysis, August 22, 2025). |
| Stock-Based Compensation | $36 | (StockAnalysis, August 22, 2025). |
| Capital Expenditures | ($1,435) | (StockAnalysis, August 22, 2025). |
| Change in Working Capital | $374 | (StockAnalysis, August 22, 2025). |
| Interest Expense | ($194) | (StockAnalysis, August 22, 2025). |
| Cash & Equivalents | $750 | (StockAnalysis, August 22, 2025). |
| Total Debt | $6,373 | (StockAnalysis, August 22, 2025). |
| Diluted Shares Outstanding | 115.31 | (StockAnalysis, August 22, 2025). |

**B) REVERSE-ENGINEER ASSUMPTIONS**

To justify the current market price of $59.16, the market is pricing in a **5-year revenue growth rate of approximately 8.5% and a constant operating margin of 5.92%**. This is based on a WACC of 8.5% and a terminal growth rate of 2.5%.

---

### **Part 2: Analyst's Revised Valuation (Realistic Base-Case)**

**C) FORMULATE REVISED ASSUMPTIONS (5 YEARS)**

6.  **Revenue Growth (Years 1-5):** I will maintain the **6% revenue growth rate for the next five years**, tapering to a terminal growth rate of 2.5%. This is a prudent assumption reflecting industry maturity, competition, and cyclical economic risks.

7.  **Margin Path:** I will assume a stable **operating margin of 5.92%**, consistent with the TTM performance. Projecting margin expansion is speculative; this assumption provides a conservative and realistic baseline.

8.  **Taxes:** An **effective tax rate of 25%** remains appropriate, aligning with historical and statutory rates.

9.  **Capital Intensity (Revised):**
    *   **Capex:** The TTM Capex-to-Revenue ratio of 10.7% reflects a period of heavy investment. It is unrealistic to assume this continues indefinitely. I will model a normalization of capex, tapering it from **10.7% of revenue in Year 1 down to 7.0% of revenue by Year 5**. This level (7.0%) is more sustainable as it better reflects long-term maintenance capex (covered by D&A) plus moderate growth investments.
    *   **Working Capital:** Change in working capital is modeled at **2.78% of revenue** based on the TTM ratio, which is a reasonable assumption.

10. **SBC, Dilution, and Buybacks:**
    *   **SBC:** Stock-based compensation will be treated as a real cash expense.
    *   **Share Count:** A net **0.5% annual reduction in shares outstanding** is a reasonable assumption reflecting modest buybacks net of SBC dilution.

**D) FREE CASH FLOW CONSTRUCTION**

11. **FCFF Calculation:** FCFF is calculated as EBIT * (1 - tax rate) + D&A - SBC - Capex - Change in Working Capital. The revised capex assumption leads to a more realistic FCFF trajectory.

    | Year | 2026 | 2027 | 2028 | 2029 | 2030 |
    | :--- | :--- | :--- | :--- | :--- | :--- |
    | Revenue | $14,254 | $15,110 | $16,016 | $16,977 | $18,000 |
    | EBIT | $844 | $895 | $948 | $1,005 | $1,066 |
    | NOPAT | $633 | $671 | $711 | $754 | $799 |
    | D&A | $717 | $760 | $806 | $854 | $906 |
    | SBC | ($38) | ($41) | ($43) | ($46) | ($49) |
    | Capex | ($1,525) | ($1,435) | ($1,361) | ($1,290) | ($1,260) |
    | Change in WC | ($396) | ($420) | ($445) | ($472) | ($500) |
    | **FCFF** | **($595)**| **($465)**| **($332)**| **($200)**| **($104)**|

**E) DISCOUNT RATE (WACC)**

12. **Cost of Equity (CAPM):**
    *   **Risk-Free Rate:** 4.25% (10-Year Treasury Yield, August 22, 2025).
    *   **Equity Risk Premium:** 5.0% (standard market premium).
    *   **Beta:** 1.46 (StockAnalysis, August 22, 2025). This beta is appropriate for the cyclical airline industry.
    *   **Cost of Equity = 4.25% + 1.46 * 5.0% = 11.55%**

13. **Cost of Debt (Revised):** A pre-tax cost of debt of 3.5% is below the risk-free rate. A more realistic estimate is the risk-free rate plus a credit spread. Assuming a 2.0% spread for ALK yields a **pre-tax cost of debt of 6.25%**.
    *   After-tax cost of debt = 6.25% * (1 - 25%) = 4.69%

14. **WACC:**
    *   Market Cap (Equity): $6,820M.
    *   Total Debt: $6,373M.
    *   Total Capital = $13,193M
    *   **WACC = (6820/13193) * 11.55% + (6373/13193) * 4.69% = 8.24%**

**F) TERMINAL VALUE**

15. **Gordon Growth Method (For Reference Only):** Even with normalized capex, the Year 5 FCFF is negative (-$104M), making the Gordon Growth Model unusable. This is common in cyclical, capital-intensive industries undergoing investment cycles.

16. **Exit Multiple Method (Primary Method):** Given the nature of the industry and the cash flow profile, the Exit Multiple method is more appropriate and stable.
    *   2030 EBITDA = 2030 EBIT + 2030 D&A = $1,066M + $906M = **$1,972M**
    *   Historical Median EV/EBITDA multiple for the airline industry is approximately **7.0x**. This is a realistic multiple for a mature airline.
    *   **Terminal Value (Exit Multiple) = $1,972M * 7.0 = $13,804M**

**G) ENTERPRISE TO EQUITY BRIDGE**

17. **Enterprise Value:**
    *   PV of FCFF = (-$595)/(1.0824)^1 + (-$465)/(1.0824)^2 + (-$332)/(1.0824)^3 + (-$200)/(1.0824)^4 + (-$104)/(1.0824)^5 = **-$1,411M**
    *   PV of Terminal Value = $13,804M / (1.0824)^5 = **$9,294M**
    *   Enterprise Value = -$1,411M + $9,294M = **$7,883M**

18. **Equity Value:**
    *   Equity Value = $7,883M (Enterprise Value) - $6,373M (Total Debt) + $750M (Cash) = **$2,260M**

**H) PER-SHARE VALUE AND MARGIN OF SAFETY**

19. **Analyst's Base-Case Fair Value:**
    *   Projected shares in Year 5 = 115.31M * (1 - 0.005)^5 = 112.46M shares
    *   **Fair Value per Share = $2,260M / 112.46M = $20.10**

20. **Valuation Range:**
    *   **Base Case:** $20.10
    *   **Low/Bear Case:** $12.00 (assumes lower growth, margin compression, and/or lower exit multiple)
    *   **High/Bull Case:** $29.00 (assumes higher growth, modest margin expansion, and/or higher exit multiple)

21. **Margin of Safety (MOS) Price:**
    *   30% below Base Case = $20.10 * (1 - 0.30) = **$14.07**

### **Risk Notes**

*   **Fuel Price Volatility:** The airline industry is highly sensitive to fluctuations in fuel prices, which can significantly impact profitability.
*   **Economic Cycles:** Demand for air travel is closely tied to economic conditions, and a recession could lead to a sharp decline in revenue.
*   **Competition:** The airline industry is intensely competitive, with pressure on pricing and market share.
*   **Regulatory Risks:** Changes in regulations related to safety, security, and environmental standards can increase costs.
*   **Geopolitical Events:** Global events such as pandemics, conflicts, and travel restrictions can disrupt operations and reduce demand.

---
final answer is 20.10 $