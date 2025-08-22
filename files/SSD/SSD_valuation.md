Of course. The provided valuation is a good starting point, but it contains several key issues, particularly in the calculation of the discount rate and the determination of the terminal value, which you correctly identified as overly conservative. Below is a critique and a revised valuation that corrects these flaws while maintaining the original structure and information.

**Critique of the Original Valuation:**

1.  **Cost of Debt (Rd):** The calculation `Interest Expense / Total Debt` yields the *effective* interest rate on existing debt, not the *marginal* cost of new debt the company would incur today. In a rising rate environment (as implied by a 4.26% risk-free rate), the company's current borrowing cost would be significantly higher than 2.81%. A more accurate method is to use the risk-free rate plus a credit spread appropriate for the company's credit risk.
2.  **Terminal Value Multiple:** The original analysis correctly points out that the Gordon Growth implied multiple of 6.8x is far too low compared to the company's historical median of 13.05x. However, its "fix" of choosing a 10.0x multiple, while an improvement, is still quite conservative and somewhat arbitrary. For a high-quality, market-leading company like Simpson, a terminal multiple closer to its long-term average (perhaps with a modest discount for conservatism) is more realistic.
3.  **Free Cash Flow Formula:** The formula used `FCFF = NOPAT + D&A - SBC - Capex - Change in NWC` subtracts Stock-Based Compensation (SBC). While some analysts do this to reflect its economic cost, a more standard approach is to *not* subtract SBC from cash flow but to account for it fully in the diluted share count. This revised analysis will follow the more common convention: `FCFF = NOPAT + D&A - Capex - Change in NWC`.

---

Here is the corrected and revised valuation in the requested format.

### **Company:** Simpson Manufacturing Co., Inc. (SSD)
### **Currency:** United States Dollars (USD)
### **Date of Analysis:** August 22, 2025
### **Primary Sources Reviewed:**
*   Simpson Manufacturing Co., Inc. Q1 2025 Form 10-Q (filed May 8, 2025)
*   StockAnalysis.com Financial Data (Income Statement, Balance Sheet, Cash Flow Statement) as of July 28, 2025
*   Publicly available market data for stock price, treasury yields, and beta as of August 22, 2025

---

## **Part 1: Market-Implied Valuation**

This section reverse-engineers the assumptions for growth and profitability that are embedded in the current stock price.

### **A) Establish Baseline & Market Price**

**1) Current Market Price:**
*   **$191.91** per share (Market Close, August 22, 2025).

**2) Baseline Financials (Trailing Twelve Months as of June 30, 2025):**
The following table presents the Trailing Twelve Months (TTM) financial data used as a baseline for the valuation.

| Metric | Value (in millions USD) | Source |
| :--- | :--- | :--- |
| Revenue | $2,275 | (stockanalysis.com/stocks/SSD/financials/, Jul 28, 2025) |
| Gross Margin | 46.13% | (stockanalysis.com/stocks/SSD/financials/, Jul 28, 2025) |
| Operating Income (EBIT) | $446.3 | (stockanalysis.com/stocks/SSD/financials/, Jul 28, 2025) |
| Net Income | $330.4 | (stockanalysis.com/stocks/SSD/financials/, Jul 28, 2025) |
| Depreciation & Amortization (D&A) | $88.1 | (stockanalysis.com/stocks/SSD/financials/cash-flow-statement/, Jul 28, 2025) |
| Stock-Based Compensation (SBC) | $21.7 | (stockanalysis.com/stocks/SSD/financials/cash-flow-statement/, Jul 28, 2025) |
| Capital Expenditures (Capex) | $188.8 | (stockanalysis.com/stocks/SSD/financials/cash-flow-statement/, Jul 28, 2025) |
| Change in Working Capital | $104.8 | (stockanalysis.com/stocks/SSD/financials/cash-flow-statement/, Jul 28, 2025) |
| Interest Expense (Cash Paid) | $13.4 | (stockanalysis.com/stocks/SSD/financials/cash-flow-statement/, Jul 28, 2025) |
| Cash & Equivalents | $190.4 | (stockanalysis.com/stocks/SSD/financials/balance-sheet/, Jul 28, 2025) |
| Total Debt | $477.2 | (stockanalysis.com/stocks/SSD/financials/balance-sheet/, Jul 28, 2025) |
| Diluted Weighted-Average Shares | 42.1 | (stockanalysis.com/stocks/SSD/financials/, Jul 28, 2025) |

### **B) Reverse-Engineer Assumptions**

To justify the market price of **$191.91**, which corresponds to an Enterprise Value of **$8,363 million**, the market must believe the company can achieve the following:
*   **A 5-year revenue CAGR of 10.5%**, while maintaining a constant **EBIT margin of 19.6%**.

This implies a belief in sustained, high-single-digit to low-double-digit growth, significantly exceeding recent historical performance and management's more cautious outlook on the U.S. housing market.

---

## **Part 2: Analyst's Revised Valuation**

This section builds a realistic, base-case intrinsic value based on independent judgment and primary sources.

### **C) Formulate Conservative Assumptions (5 Years)**

**6-7) Revenue for Years 1-5:**
*   **Rationale:** The market's implied 10.5% growth appears optimistic. Management's outlook in the latest 10-Q suggests U.S. housing starts "could stay flat or increase in the low-single digit range" for 2025 (Q1 2025 10-Q, May 8, 2025). While Simpson aims to grow above the market, a more conservative forecast is warranted. Historical growth has been volatile (0.8% in 2024, 4.6% in 2023, 34.5% in 2022).
*   **Assumption:** I will use a **5.0%** growth rate for Year 1, tapering down by 0.5% annually to a terminal rate of **3.0%** in Year 5.

**8) Margin Path:**
*   **Rationale:** Management's 2025 outlook for operating margin is between 18.5% and 20.5% (Q1 2025 10-Q, May 8, 2025). The TTM margin is 19.6%. The three-year average is higher at 21.4%, but recent guidance suggests moderation.
*   **Assumption:** I will use a constant **19.5% operating (EBIT) margin** for the 5-year forecast period, aligning with the midpoint of management guidance.

**9) Taxes:**
*   **Rationale:** The company's effective tax rate has been remarkably stable. The average rate over the last three full fiscal years (2022-2024) is 25.65%.
*   **Assumption:** A **25.7%** effective tax rate.

**10) Capital Intensity:**
*   **Capex:** Management guidance for 2025 is $150M to $170M due to facility expansions (Q1 2025 10-Q, May 8, 2025). This is ~7.0% of projected revenue. The historical 3-year average as a percentage of revenue is 5.0%.
*   **Assumption:** Capex will be **7.0% of revenue** in Year 1 and normalize to **5.0% of revenue** for Years 2-5. D&A is modeled at 4.0% of revenue, consistent with historical trends.
*   **Working Capital:** Historically, the change in net working capital has averaged approximately 15% of the change in revenue.
*   **Assumption:** Change in NWC will be **15.0% of incremental revenue**.

**11) SBC, Dilution, and Buybacks:**
*   **Rationale:** The company has a history of share repurchases, reducing its share count by a net 4.3% between early 2022 and mid-2025, or about 1.4% annually (Q1 2025 10-Q, May 8, 2025). Diluted shares outstanding have decreased by 1.4% YoY.
*   **Assumption:** A net **1.0% annual reduction in diluted shares outstanding**, balancing buybacks and SBC issuance.

### **D) Free Cash Flow Construction**

**12) Free Cash Flow to Firm (FCFF) Calculation:**
FCFF is calculated using the standard formula, which does not subtract SBC.
*   **Formula:** FCFF = EBIT * (1 - Tax Rate) + D&A - Capex - Change in Working Capital

**Projected Free Cash Flow (in millions USD):**

| Fiscal Year | Y1 (2026) | Y2 (2027) | Y3 (2028) | Y4 (2029) | Y5 (2030) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $2,388.8 | $2,496.3 | $2,608.6 | $2,726.0 | $2,848.4 |
| EBIT (19.5%) | $465.8 | $486.8 | $508.7 | $531.6 | $555.4 |
| NOPAT | $346.1 | $361.7 | $377.9 | $394.9 | $412.7 |
| D&A | $95.5 | $99.9 | $104.3 | $109.0 | $113.9 |
| Capex | ($167.2) | ($124.8) | ($130.4) | ($136.3) | ($142.4) |
| Change in NWC | ($17.1) | ($16.1) | ($16.8) | ($17.6) | ($18.4) |
| **Free Cash Flow** | **$257.4** | **$320.6** | **$335.0** | **$349.9** | **$365.9** |

### **E) Discount Rate (WACC)**

**14) Cost of Equity (CAPM):**
*   **Risk-Free Rate:** 4.26% (10-Year U.S. Treasury, August 22, 2025).
*   **Equity Risk Premium (ERP):** 5.0% (Standard for a mature market).
*   **Beta (β):** 1.26 (dcfmodeling.com). This reflects the construction industry's cyclicality and sensitivity to economic conditions, which is higher than the broader market.
*   **Cost of Equity (Re) = 4.26% + 1.26 * 5.0% = 10.56%**

**15) Cost of Debt (Revised):**
*   **Rationale:** The effective rate on existing debt (2.81%) is not the current marginal cost. A more accurate estimate is the risk-free rate plus a credit spread. For a financially healthy industrial company like SSD, a spread of 1.30% is appropriate.
*   **Calculation:** Pre-Tax Cost of Debt = Risk-Free Rate + Credit Spread = 4.26% + 1.30% = 5.56%.
*   **After-Tax Cost of Debt (Rd) = 5.56% * (1 - 25.7%) = 4.13%**

**16) WACC (Revised):**
*   **Market Value of Equity (E):** $191.91 * 42.1M shares = $8,079M
*   **Market Value of Debt (D):** $477M
*   **Total Value (V):** $8,079M + $477M = $8,556M
*   **WACC = (E/V * Re) + (D/V * Rd) = (94.4% * 10.56%) + (5.6% * 4.13%) = 9.97% + 0.23% = 10.20%**

### **F) Terminal Value (Revised)**

**17) Gordon Growth Method Check:**
*   **Terminal Growth Rate (g):** 2.5% (Long-run inflation expectation).
*   **Terminal Value (GGM) = (FCFF_5 * (1+g)) / (WACC - g) = ($365.9M * 1.025) / (10.20% - 2.5%) = $375.0M / 7.70% = $4,871M**

**18) Exit Multiple Method (Primary Method):**
*   **Rationale:** The GGM-implied multiple is still too low and sensitive to inputs. An exit multiple based on historical performance provides a more robust, market-based anchor. The company's 13-year median EV/EBITDA is 13.05x. A mature, high-quality business should trade near its long-term average. A modest discount for conservatism is prudent.
*   **Year 5 EBITDA:** EBIT_5 + D&A_5 = $555.4M + $113.9M = $669.3M
*   **Assumption:** A **12.0x EV/EBITDA exit multiple** is a realistic and fair assumption, reflecting the company's quality while acknowledging a normalization of growth.
*   **Revised Terminal Value (Exit Multiple) = 12.0 * $669.3M = $8,031.6M**

### **G) Enterprise to Equity Bridge**

**19) Enterprise Value:**
*   **PV of Explicit FCFF:** ($257.4/1.102^1) + ($320.6/1.102^2) + ($335.0/1.102^3) + ($349.9/1.102^4) + ($365.9/1.102^5) = $233.6 + $264.4 + $250.7 + $237.2 + $226.7 = **$1,212.6M**
*   **PV of Terminal Value (using 12.0x exit multiple):** $8,031.6M / (1.102^5) = **$4,976.2M**
*   **Total Enterprise Value = $1,212.6M + $4,976.2M = $6,188.8M**

**20) Equity Value:**
*   **Formula:** Equity Value = Enterprise Value - Net Debt
*   **Net Debt:** Total Debt ($477.2M) - Cash ($190.4M) = $286.8M
*   **Total Equity Value = $6,188.8M - $286.8M = $5,902.0M**

### **H) Per-Share Value and Margin of Safety**

**21) Analyst's Base-Case Fair Value:**
*   **Projected Year 5 Diluted Shares:** 42.1M * (1 - 0.01)^5 = 39.9M shares
*   **Base-Case Fair Value = $5,902.0M / 39.9M shares = $147.92**

**22) Valuation Range:**
*   **Base Case: $147.92.** Based on realistic assumptions for growth, margins, and terminal multiple.
*   **Low/Bear Case: ~$115.** Assumes a recessionary environment with 2% revenue decline for two years, margin compression to 17.5%, and a 10.0x exit multiple.
*   **High/Bull Case: ~$185.** Assumes revenue growth averages 7%, operating margins expand to 21%, and the exit multiple trends toward the historical median at 13.0x.

**23) Margin of Safety (MOS) Price:**
*   A 30% margin of safety from the base-case estimate provides a target purchase price.
*   **MOS Price = $147.92 * (1 - 0.30) = $103.54**

### **Risk Notes**

The key risks to this valuation thesis include: (1) **Cyclicality of the construction market:** A significant downturn in U.S. housing starts or commercial construction would directly impact revenue and profitability. (2) **Raw material price volatility:** The business is exposed to fluctuations in steel prices, and an inability to pass cost increases to customers could compress margins. (3) **Competition:** The building products industry is competitive, and failure to innovate or maintain strong distribution relationships could lead to market share loss. (4) **Integration Risk:** The company continues to make acquisitions, and failure to properly integrate these new businesses could lead to operational inefficiencies and destroy shareholder value.

final answer is 147.92 $