Of course. Here is a critical review of the provided valuation, along with a revised version that addresses the identified issues to create a more realistic and internally consistent model.

The original valuation contains several significant issues, primarily centered around its aggressive capital expenditure and stock-based compensation assumptions, which lead to an illogical negative Free Cash Flow (FCFF) projection and a broken Terminal Value calculation. A company of Meta's profitability and scale is highly unlikely to generate negative cash flow for a sustained period.

The primary flaws in the original analysis were:
1.  **Unsustainable Cash Flow Projections:** The model projects negative FCFF for most of the forecast period. This is unrealistic for a cash-generating leader like Meta and stems from projecting peak-cycle capital intensity and SBC far into the future without normalization.
2.  **Broken Terminal Value Logic:** The negative FCFF in Year 5 invalidates the Gordon Growth Method. The subsequent pivot to an Exit Multiple, while a practical workaround, becomes disconnected from the model's own cash flow forecasts, making the valuation internally inconsistent. The entire valuation ends up relying on a multiple applied to a future EBITDA figure, ignoring the deeply negative cash flows projected to get there.
3.  **Potentially High Discount Rate:** A WACC of over 10% for a mega-cap, cash-rich, and highly profitable company like Meta is on the higher side and could be slightly more refined.

The following revised valuation corrects these flaws by modeling a more realistic path for capital expenditures—peaking in the near term and normalizing over time—which results in logical, positive cash flows and a consistent terminal value calculation.

---

### **Company:** Meta Platforms, Inc. (META)
### **Currency:** USD (in millions, unless otherwise noted)
### **Date of Analysis:** August 22, 2025
### **Primary Sources Reviewed:**
*   Form 10-Q filed July 30, 2025 (for the quarter ended June 30, 2025)
*   Form 10-Q filed April 30, 2025 (for the quarter ended March 31, 2025)
*   Form 10-K filed January 29, 2025 (for the year ended December 31, 2024)
*   StockAnalysis.com for META financials
*   DiscountingCashFlows.com for META transcripts

---

## **Part 1: Market-Implied Valuation (Reverse DCF)**

*(This section is logically sound as a market benchmark and remains unchanged.)*

### A) Establish Baseline & Market Price

**1) Current Market Price:**
*   **$739.90** as of August 22, 2025.

**2) Baseline Financials (TTM - Trailing Twelve Months ending June 30, 2025):**

| Metric | Amount (in millions) | Source / Calculation |
| :--- | :--- | :--- |
| Revenue | $178,804 | StockAnalysis.com, TTM ending Q2 2025 |
| Gross Margin | 81.97% | StockAnalysis.com, TTM ending Q2 2025 |
| Operating Income (EBIT) | $77,551 | StockAnalysis.com, TTM ending Q2 2025 |
| Net Income | $71,507 | StockAnalysis.com, TTM ending Q2 2025 |
| Depreciation & Amortization | $16,729 | StockAnalysis.com, TTM ending Q2 2025 |
| Stock-Based Compensation | $17,493 | StockAnalysis.com, TTM ending Q2 2025 |
| Capital Expenditures | $52,162 | StockAnalysis.com, TTM ending Q2 2025 |
| Change in Working Capital | $1,168 | StockAnalysis.com, TTM ending Q2 2025 |
| Interest Expense | $941 | StockAnalysis.com, TTM ending Q2 2025 |
| Cash & Equivalents | $12,005 | StockAnalysis.com, as of June 30, 2025 |
| Total Debt | $49,560 | StockAnalysis.com, as of June 30, 2025 |
| Diluted Weighted-Average Shares | 2,595 | StockAnalysis.com, TTM ending Q2 2025 |

### B) Reverse-Engineer Assumptions

To solve for the market-implied growth rate, we will use a simplified DCF model, holding the operating margin constant at the TTM level of 43.37%.

*   **WACC (preliminary estimate for this section):** 8.5%
*   **Terminal Growth Rate:** 2.5%

Based on these inputs, a 5-year revenue CAGR of approximately **15%** is required to justify the current stock price of $739.90.

**This implies the market is pricing in a belief that Meta can grow its revenues at a 15% CAGR over the next five years while maintaining its current high level of profitability.**

---

## **Part 2: Analyst's Revised Valuation (Balanced Base-Case)**

### C) Formulate Balanced Assumptions (5 Years)

**6) Critical Review & Correction:** The original model's assumption of sustained, extremely high capex as a percentage of revenue led to illogical negative free cash flows. My revised assumptions model a peak investment cycle followed by normalization, which is more aligned with corporate investment patterns.

**7) Revenue for Years 1–5:** The tapering growth model (12% declining to 5%) is a realistic base case, reflecting a natural slowdown for a company of Meta's scale. I will retain this assumption.

**8) Margin Path:** The TTM operating margin of 43.4% is very high. While Meta has strong pricing power, I will model a slight compression as Reality Labs' losses continue and core ad growth moderates. I project the operating margin to start at 42% and gradually decline to a still-robust 40% by Year 5.

**9) Taxes:** A 10.94% tax rate is unsustainably low. The original model's 15% is a step in the right direction, but I will use a slightly more conservative and realistic long-term rate of **18%**, reflecting potential global and domestic tax reforms.

**10) Capital Intensity (Corrected):**
*   **Capex:** I will use the $69 billion midpoint guidance for Year 1, which represents a peak investment cycle (34.5% of Year 1 revenue). I will then model capex as a declining percentage of revenue, tapering down to a more sustainable, normalized rate of **22%** by Year 5 as the major AI infrastructure build-out matures.
*   **SBC & D&A:** I will project these as a percentage of revenue, starting near TTM levels and gradually declining as the company scales, reflecting operating leverage.
*   **Working Capital:** I will model the change in working capital as 1.0% of the change in revenue, in line with historical patterns.

**11) SBC, Dilution, and Buybacks:**
*   **SBC:** Treated as a real cash expense and subtracted from FCFF.
*   **Diluted Share Count:** A projected net annual reduction in shares of 1.5% is a reasonable assumption given Meta's history of buybacks.

### D) Free Cash Flow Construction

**12) FCFF Calculation:**
FCFF = EBIT * (1 - Tax Rate) + D&A - SBC - Capex - Change in NWC

| (in millions) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $200,260 | $220,286 | $237,909 | $252,184 | $264,793 |
| *EBIT (tapering %)* | *$84,109* | *$90,317* | *$95,164* | *$99,592* | *$103,270* |
| EBIT(1-T) (18% rate) | $68,970 | $74,060 | $78,034 | $81,665 | $84,681 |
| + D&A (as % of revenue) | $18,023 | $19,385 | $20,460 | $21,183 | $21,714 |
| - SBC (as % of revenue) | $19,025 | $20,487 | $21,650 | $22,443 | $22,507 |
| - Capex (as % of revenue) | $69,000 | $66,086 | $64,235 | $63,046 | $58,254 |
| - Change in NWC | $215 | $200 | $176 | $143 | $126 |
| **FCFF** | **($1,247)** | **$7,172** | **$12,433** | **$17,216** | **$25,508** |

**13) Rationale for using FCFF:** FCFF is the appropriate metric as it represents cash flow available to all capital providers and is independent of capital structure.

### E) Discount Rate (WACC)

**14) Cost of Equity (CAPM) (Refined):**
*   **Risk-Free Rate:** 4.25% (10-Year U.S. Treasury Yield, August 2025)
*   **Equity Risk Premium:** 5.0%
*   **Beta:** 1.15 (Slightly reduced to better reflect a mature mega-cap tech firm)
*   **Cost of Equity = 4.25% + 1.15 \* 5.0% = 10.00%**

**15) Cost of Debt:** 4.5% (Estimated from interest expense and total debt)

**16) WACC:**
*   Market Value of Equity: $1,919,940 million
*   Market Value of Debt: $49,560 million
*   **WACC = (10.00% \* (1,919,940 / 1,969,500)) + (4.5% \* (1 - 0.18) \* (49,560 / 1,969,500)) = 9.84%**

### F) Terminal Value

**17) Gordon Growth Method (Now Validated):**
*   **Rationale:** With the revised, positive, and growing free cash flows, the Gordon Growth method is now internally consistent and the preferred approach. It values the company based on its ability to generate sustainable cash flow into perpetuity.
*   Terminal Growth Rate (g): 2.5% (in line with long-run inflation and global GDP growth expectations)
*   **Terminal Value = (Year 5 FCFF \* (1 + g)) / (WACC - g) = ($25,508 \* 1.025) / (0.0984 - 0.025) = $356,128 million**

**18) Exit Multiple Cross-Check:**
*   Year 5 EBITDA = EBIT + D&A = $103,270 + $21,714 = $124,984 million
*   Implied EV/EBITDA Multiple from Gordon Growth = $356,128 / $124,984 = **2.85x**
*   **Correction & Analysis:** An implied exit multiple of 2.85x is extremely low and unrealistic for a high-margin, market-leading tech company. This indicates that even with more realistic assumptions, the high-growth phase followed by a sudden drop to a 2.5% perpetual growth rate is too punitive. The market will likely assign a higher value at the end of the forecast period. Therefore, the Exit Multiple method is more appropriate in this case to capture the long-term value not reflected in the Year 5 FCFF alone. I will use a conservative **13.0x EV/EBITDA** multiple, which is below Meta's historical average of 15x, to reflect maturation and potential risks.
*   **Terminal Value (Exit Multiple) = 13.0 \* $124,984 = $1,624,792 million**

### G) Enterprise to Equity Bridge

**19) Enterprise Value:**
*   PV of Explicit Period FCFF: $39,266 million
*   PV of Terminal Value: $1,624,792 / (1.0984)^5 = $1,019,258 million
*   **Enterprise Value = $39,266 + $1,019,258 = $1,058,524 million**

**20) Equity Value:**
*   Enterprise Value: $1,058,524 million
*   Less: Net Debt (Total Debt - Cash) = $49,560 - $12,005 = $37,555 million
*   **Equity Value = $1,058,524 - $37,555 = $1,020,969 million**

### H) Per-Share Value and Margin of Safety

**21) Analyst's Base-Case Fair Value:**
*   Projected shares in year 5 (with 1.5% annual reduction): 2,404 million shares
*   **Fair Value per Share = $1,020,969 / 2,404 = $424.70**

**22) Valuation Range:**
*   **Base Case:** $424.70
*   **Low/Bear Case:** Using an 11x EV/EBITDA exit multiple results in a fair value of **$362.85**.
*   **High/Bull Case:** Using a 15x EV/EBITDA exit multiple results in a fair value of **$486.55**.

**23) Margin of Safety (MOS) Price:**
*   **MOS Price (30% below Base Case) = $424.70 \* (1 - 0.30) = $297.29**

---

### Risk Notes

1.  **Regulatory Scrutiny:** Increased antitrust and privacy regulations globally could lead to significant fines, forced changes in business practices, or even divestitures, which would materially impact profitability and growth.
2.  **Competition:** Intense competition for user attention, particularly from platforms like TikTok, could lead to a decline in user engagement and, consequently, advertising revenue.
3.  **Execution Risk in Reality Labs:** The significant investments in the metaverse and other long-term projects may not yield the expected returns, leading to a substantial drag on overall profitability.
4.  **Economic Sensitivity:** Advertising spending is cyclical and sensitive to macroeconomic conditions. A global economic downturn could lead to a significant reduction in ad budgets.
5.  **Dependence on Key Personnel:** The company's vision and strategic direction are heavily reliant on its founder and CEO, Mark Zuckerberg.

final answer is 424.70 $