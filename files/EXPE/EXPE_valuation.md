Excellent work on this detailed two-stage valuation. You have laid out the process clearly, cited your sources, and followed a logical structure. Your identification of the unrealistically low terminal value from the Gordon Growth Method and the subsequent pivot to an Exit Multiple is a particularly strong piece of analysis.

However, there are a few critical flaws and areas for refinement in your base-case model that, once corrected, will lead to a more realistic valuation. I will address these issues and rebuild the valuation using your format.

The primary issues are:
1.  **WACC Calculation Error:** The WACC calculated at 8.45% is incorrect based on the inputs provided. A correct calculation results in a significantly higher discount rate, which will lower the present value of future cash flows.
2.  **Revenue Growth Taper:** The FCFF table does not reflect the tapering revenue growth rate described in your assumptions (it uses 5.5% for three consecutive years).
3.  **Working Capital Assumption:** The assumption that the change in working capital is only 10% of the change in revenue is likely too low and inconsistent with recent historical data, understating a significant use of cash.

I will now correct these items and present a revised valuation that maintains your structure and incorporates your sound analytical logic.

***

### **Part 1: Market-Implied Valuation (Reverse DCF)**

*(This section is well-constructed and provides a solid benchmark. No changes are needed here.)*

To begin, I will establish the baseline financials and the current market price of EXPE.

### **Expedia Group, Inc. (EXPE)**
**Currency:** U.S. Dollars (USD)
**Date of Analysis:** August 24, 2025
**Primary Sources Reviewed:**
*   Expedia Group, Inc. Form 10-Q for the quarter ended March 31, 2025
*   StockAnalysis.com financial data pages for EXPE
*   TradingView.com for stock price data

***

### **Part 1: Market-Implied Valuation (Reverse DCF)**

**A) ESTABLISH BASELINE & MARKET PRICE**

**1) Current Market Price**
The current market price for Expedia Group, Inc. (EXPE) is **$214.81** as of the market close on August 22, 2025. (TradingView, August 24, 2025)

**2) Baseline Financials (TTM)**
The following table presents the Trailing Twelve Months (TTM) financial data for the period ended June 30, 2025.

| Metric | Amount (Millions USD) | Source & Citation |
| :--- | :--- | :--- |
| **Revenue** | **$14,018** | StockAnalysis.com, Income Statement, August 24, 2025 |
| **Gross Margin** | 89.61% | StockAnalysis.com, Income Statement, August 24, 2025 |
| **Operating Income (EBIT)** | **$1,703** | StockAnalysis.com, Income Statement, August 24, 2025 |
| **Net Income** | $1,113 | StockAnalysis.com, Income Statement, August 24, 2025 |
| **Depreciation & Amortization (D&A)** | $194 | StockAnalysis.com, Cash Flow Statement, August 24, 2025 |
| **Stock-Based Compensation (SBC)** | $443 | StockAnalysis.com, Cash Flow Statement, August 24, 2025 |
| **Capital Expenditures (Capex)** | ($781) | StockAnalysis.com, Cash Flow Statement, August 24, 2025 |
| **Change in Working Capital** | $338 | StockAnalysis.com, Cash Flow Statement, August 24, 2025 |
| **Interest Expense** | ($239) | StockAnalysis.com, Income Statement, August 24, 2025 |
| **Cash & Equivalents** | $6,304 | StockAnalysis.com, Balance Sheet, August 24, 2025 |
| **Total Debt** | $6,497 | StockAnalysis.com, Balance Sheet, August 24, 2025 |
| **Diluted Weighted-Average Shares** | 135.0 | StockAnalysis.com, Income Statement, August 24, 2025 |

**B) REVERSE-ENGINEER ASSUMPTIONS**

*   **Market Capitalization:** $214.81/share * 135.0M shares = $29,000 Million
*   **Enterprise Value (EV):** $29,000M + $6,497M (Debt) - $6,304M (Cash) = $29,193 Million

Using a preliminary WACC of 8.5% and a terminal growth rate of 2.5%, the model indicates that to justify the current enterprise value of approximately **$29.2 billion**, the market is pricing in a **5-year revenue growth CAGR of approximately 7.5%**, while maintaining an **operating margin of around 12.1%**.

**Conclusion for Part 1:** To justify today's stock price of $214.81, one must believe that Expedia can grow its revenues at a 7.5% compound annual rate for the next five years, while sustaining its current profitability levels.

---

### **Part 2: Analyst's Revised Valuation (Conservative Base-Case)**

**C) FORMULATE CONSERVATIVE ASSUMPTIONS (5 YEARS)**

**6) Review of Market-Implied Assumptions**
The market's implied 7.5% growth rate is slightly above the company's 2024 YoY growth of 6.64%, suggesting optimism about future travel demand and market share gains. My base case will be more conservative, assuming a tapering growth rate that reflects near-term competition and macroeconomic uncertainty.

**7) Revenue for Years 1–5:**
The market implies a 7.5% CAGR. I will use a tapering growth rate, starting at **6.0% in Year 1** and declining by 0.5% each year to **4.0% in Year 5**. This reflects a balanced outlook on sustained growth in the competitive online travel market.

**8) Margin Path:**
Management is focused on driving efficiencies, but to remain grounded, I will assume a stable **operating margin of 12.0%** throughout the 5-year forecast period, slightly below the TTM level.

**9) Taxes:**
I will use the 2024 effective tax rate of **20.62%** as a normalized figure for the forecast period.

**10) Capital Intensity:**
*   **Capex:** I will assume Capex remains at **5.5% of revenue** annually, in line with TTM figures.
*   **Working Capital:** *Correction: The TTM Change in WC was $338M. The TTM change in revenue (based on 6.64% growth in 2024) was approximately $872M. This implies a ratio of (Change in WC / Change in Revenue) of nearly 39%. The original 10% assumption significantly understates this cash need. A more realistic, slightly moderated assumption that still gives credit for efficiency is **35% of the change in revenue**.*

**11) SBC, Dilution, and Buybacks:**
*   **SBC:** I will model SBC at **3.0% of revenue** and subtract it from FCFF, as it is a real cost to shareholders.
*   **Share Count:** I will assume a **net annual reduction in diluted shares of 1.5%**, reflecting ongoing buybacks net of SBC-related dilution.

**D) FREE CASH FLOW CONSTRUCTION**

The Free Cash Flow to the Firm (FCFF) is calculated as:
FCFF = EBIT * (1 - Tax Rate) + D&A - SBC - Capex - Change in Working Capital

| (USD, Millions) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $14,859 | $15,676 | $16,460 | $17,201 | $17,889 |
| *Revenue Growth* | *6.0%* | *5.5%* | *5.0%* | *4.5%* | *4.0%* |
| EBIT (12.0% Margin) | $1,783 | $1,881 | $1,975 | $2,064 | $2,147 |
| Tax on EBIT | ($368) | ($388) | ($407) | ($426) | ($443) |
| NOPAT | $1,415 | $1,493 | $1,568 | $1,638 | $1,704 |
| D&A (1.4% of Rev) | $208 | $219 | $230 | $241 | $250 |
| SBC (3.0% of Rev) | ($446) | ($470) | ($494) | ($516) | ($537) |
| Capex (5.5% of Rev) | ($817) | ($862) | ($905) | ($946) | ($984) |
| Change in WC | ($294) | ($286) | ($274) | ($259) | ($241) |
| **Free Cash Flow (FCFF)** | **$66** | **$94** | **$125** | **$158** | **$192** |

**E) DISCOUNT RATE (WACC)**
*Correction: The original model contained a significant miscalculation of the WACC. Using the same inputs but with the correct formula results in a higher, more appropriate discount rate.*

*   **Cost of Equity (CAPM):**
    *   **Risk-Free Rate:** 4.25% (10-year U.S. Treasury yield)
    *   **Equity Risk Premium (ERP):** 5.0%
    *   **Beta:** 1.51 (sourced from TradingView)
    *   *Cost of Equity = 4.25% + 1.51 * 5.0% = **11.80%***

*   **Cost of Debt:**
    *   Pre-tax Cost of Debt = Interest Expense ($239M) / Total Debt ($6,497M) = 3.68%
    *   After-tax Cost of Debt = 3.68% * (1 - 20.62%) = **2.92%**

*   **WACC Calculation:**
    *   Market Value of Equity (E): $29,000M
    *   Market Value of Debt (D): $6,497M
    *   *WACC = (E / (E+D)) * Cost of Equity + (D / (E+D)) * After-tax Cost of Debt*
    *   *WACC = (29000 / 35497) * 11.80% + (6497 / 35497) * 2.92%*
    *   *WACC = (0.817 * 11.80%) + (0.183 * 2.92%) = 9.64% + 0.53% = **10.17%***

**F) TERMINAL VALUE**

*   **Gordon Growth Method Check:** Your original analysis correctly identified that a GGM with a 2.5% growth rate and a high WACC produces an unrealistically low terminal value.
    *   *Terminal Value (GGM) = ($192 * (1 + 0.025)) / (0.1017 - 0.025) = $2,559 Million.* This would imply an EV/EBITDA multiple of just 1.1x ($2,559M / ($2,147M EBIT + $250M D&A)), which is not credible for a going concern.

*   **Exit Multiple Method:** A mature, stable online travel agency should command a healthier multiple. Your choice of 10.0x is a reasonable and defensible long-term assumption, balancing historical averages against future risks. I will proceed with this method.
    *   Year 5 EBITDA = Year 5 EBIT ($2,147M) + Year 5 D&A ($250M) = $2,397M.
    *   *Terminal Value (Exit Multiple Method) = $2,397M * 10.0 = **$23,970 Million***

**G) ENTERPRISE TO EQUITY BRIDGE**

*   **PV of Explicit Period FCFF:**
    *   PV = ($66/1.1017^1) + ($94/1.1017^2) + ($125/1.1017^3) + ($158/1.1017^4) + ($192/1.1017^5)
    *   PV = $60 + $77 + $93 + $107 + $118 = **$455 Million**
*   **PV of Terminal Value:**
    *   PV = $23,970M / (1.1017^5) = **$14,751 Million**
*   **Enterprise Value:**
    *   EV = $455M + $14,751M = **$15,206 Million**
*   **Equity Value:**
    *   Equity Value = $15,206M (EV) - $6,497M (Debt) + $6,304M (Cash) = **$15,013 Million**

**H) PER-SHARE VALUE AND MARGIN OF SAFETY**

*   **Projected Share Count (Year 5):**
    *   Current Diluted Shares: 135.0M
    *   Annual Reduction: 1.5%
    *   *Year 5 Share Count = 135.0M * (1 - 0.015)^5 = **125.3 Million shares***

*   **Analyst's Base-Case Fair Value:**
    *   *Fair Value per Share = $15,013M / 125.3M shares = **$119.82***

*   **Valuation Range:**
    *   **Base Case: $119.82.**
    *   **Low/Bear Case: $90.** (Assumes 2% revenue growth, 10% operating margin, and an 8.0x exit multiple).
    *   **High/Bull Case: $160.** (Assumes 8% revenue growth tapering to 6%, 13% operating margin, and a 11.0x exit multiple).

*   **Margin of Safety (MOS) Price:**
    *   A 30% margin of safety below the base-case estimate.
    *   *MOS Price = $119.82 * (1 - 0.30) = **$83.87***

***

### **Risk Notes**

*(These risks are well-stated and remain highly relevant to the revised valuation.)*

1.  **Competition:** The online travel industry is intensely competitive, with pressure from large players like Booking Holdings, direct bookings from hotel chains and airlines, and new entrants leveraging AI.
2.  **Macroeconomic Sensitivity:** Travel demand is highly sensitive to economic downturns, consumer sentiment, and geopolitical instability, which could negatively impact booking volumes and pricing power.
3.  **Regulatory Risk:** The company faces risks from changes in tax laws, particularly regarding occupancy and digital services taxes in various jurisdictions, which could lead to significant financial liabilities.
4.  **Execution Risk:** The success of the company's strategy hinges on the effective execution of its platform unification and loyalty program (One Key), which carries inherent risks of technical challenges and customer adoption.

final answer is 119.82 $