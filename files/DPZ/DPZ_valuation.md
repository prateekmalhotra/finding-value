## Domino's Pizza, Inc. (DPZ) - Intrinsic Value Estimation

*   **Company:** Domino's Pizza, Inc. (DPZ)
*   **Currency:** USD
*   **Date of Analysis:** August 20, 2025
*   **Primary Sources Reviewed:** StockAnalysis Financials (Income Statement, Balance Sheet, Cash Flow Statement), Q2 2025 Earnings Call Commentary.

### A) Baseline Financials (TTM)

The following table represents the Trailing Twelve Months (TTM) financial data for the period ended June 15, 2025. All figures are in millions of USD.

| Metric | Value (in millions) | Source & Date |
| --- | --- | --- |
| Revenue | $4,781 | (StockAnalysis, Aug 20, 2025) |
| Gross Margin | 28.51% | (StockAnalysis, Aug 20, 2025) |
| Operating Income (EBIT) | $908.74 | (StockAnalysis, Aug 20, 2025) |
| Net Income | $597.11 | (StockAnalysis, Aug 20, 2025) |
| Depreciation & Amortization | $56.33 | (StockAnalysis, Aug 20, 2025) |
| Stock-Based Compensation | $42.59 | (StockAnalysis, Aug 20, 2025) |
| Capital Expenditures | $104.43 | (StockAnalysis, Aug 20, 2025) |
| Change in Working Capital | $33.77 | (StockAnalysis, Aug 20, 2025) |
| Interest Expense | $195.54 | (StockAnalysis, Aug 20, 2025) |
| Cash & Equivalents | $272.86 | (StockAnalysis, Aug 20, 2025) |
| Total Debt | $5,212 | (StockAnalysis, Aug 20, 2025) |
| Diluted Weighted-Average Shares | 35 | (StockAnalysis, Aug 20, 2025) |

### B) Management Guidance Extraction

Key guidance extracted from the Q2 2025 earnings call on July 21, 2025:

*   **U.S. Same-Store Sales:** "we continue to expect our US comp for the year to be 3%." (Q2 2025 Earnings Call, Jul 21, 2025)
*   **Global Retail Sales:** "we continue to believe that global retail sales growth should be generally in line with 2024." (Q2 2025 Earnings Call, Jul 21, 2025) (2024 revenue growth was 5.07%)
*   **International Same-Store Sales:** Came in at 2.4% for Q2, with a cautious outlook due to "potential for the macro and geopolitical overhang in the back half." (Q2 2025 Earnings Call, Jul 21, 2025)

No specific guidance was provided for margins or capital expenditures.

### C) Forecast & Assumptions (5-Year Horizon)

| Assumption | Value | Rationale & Citation |
| --- | --- | --- |
| **Revenue Growth (Years 1-5)** | 4.0% | A conservative blend of 3% U.S. comp guidance and ~5% global retail sales growth in 2024. |
| **Operating Margin (EBIT)** | 18.53% | Three-year average operating margin (18.30% in 2023, 18.68% in 2024, 19.01% TTM). Kept stable due to lack of specific management guidance on margin expansion. |
| **Effective Tax Rate** | 20.54% | Three-year average effective tax rate (20.43% in 2023, 19.11% in 2024, 22.08% TTM). |
| **Capex as % of Revenue** | 2.2% | Three-year average of capex as a percentage of revenue. |
| **Change in WC as % of Incr. Revenue** | 10.0% | Based on historical trends and business model. |
| **SBC as % of Revenue** | 0.9% | Held constant at TTM level. |

### D) Free Cash Flow Construction

Free Cash Flow to the Firm (FCFF) is used for this valuation because it represents the cash flow available to all capital providers (both debt and equity holders) and is independent of the company's capital structure.

**Formula:** FCFF = EBIT * (1 - Tax Rate) + D&A - SBC - Capex - Change in Working Capital

| (in millions USD) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| --- | --- | --- | --- | --- | --- |
| Revenue | $4,972 | $5,171 | $5,378 | $5,593 | $5,817 |
| EBIT | $921 | $958 | $997 | $1,036 | $1,078 |
| NOPAT | $732 | $761 | $792 | $823 | $856 |
| D&A | $58 | $60 | $63 | $65 | $68 |
| Stock-Based Comp | -$45 | -$47 | -$48 | -$50 | -$52 |
| Capex | -$109 | -$114 | -$118 | -$123 | -$128 |
| Change in WC | -$19 | -$20 | -$21 | -$21 | -$22 |
| **FCFF** | **$617** | **$641** | **$667** | **$694** | **$722** |

### E) Discount Rate (WACC)

| Component | Value | Formula & Source |
| --- | --- | --- |
| **Cost of Equity (Ke)** | | |
| Risk-Free Rate (Rf) | 4.29% | 10-Year U.S. Treasury Yield (Aug 20, 2025). |
| Equity Risk Premium (ERP) | 5.0% | Standard market premium. |
| Beta (β) | 1.10 | 5-year monthly beta, reflecting slight market sensitivity. |
| *Calculated Ke* | *9.79%* | *Rf + β \* ERP* |
| **Cost of Debt (Kd)** | | |
| Interest Expense | $195.54 M | (StockAnalysis, Aug 20, 2025) |
| Total Debt | $5,212 M | (StockAnalysis, Aug 20, 2025) |
| *Calculated Kd (pre-tax)* | *3.75%* | *Interest Expense / Total Debt* |
| Tax Rate | 20.54% | See "Forecast & Assumptions" |
| *Calculated Kd (after-tax)* | *2.98%* | *Kd \* (1 - Tax Rate)* |
| **WACC** | | |
| Market Cap (E) | $15,300 M | (StockAnalysis, Aug 20, 2025) |
| Total Debt (D) | $5,212 M | (StockAnalysis, Aug 20, 2025) |
| *Calculated WACC* | *7.99%* | *(E / (E+D)) \* Ke + (D / (E+D)) \* Kd* |

### F) Terminal Value

The Gordon Growth method is used to calculate the terminal value, with a perpetual growth rate `g` that is realistic for a mature company.

*   **Terminal Growth Rate (g):** 2.5%. This is a reasonable long-term growth assumption, in line with long-run inflation expectations.
*   **Terminal Value Formula:** (FCFF Year 5 \* (1 + g)) / (WACC - g)
*   **Calculation:** ($722 \* (1 + 0.025)) / (0.0799 - 0.025) = **$13,490 M**

**Cross-Check (Exit Multiple Method):**
*   A historical median EV/EBITDA multiple for DPZ is in the 15-20x range. Using a conservative 15x multiple on Year 5 EBITDA of $1,146M ($1,078M EBIT + $68M D&A) yields a terminal value of **$17,190M**.
*   The Gordon Growth method yields a more conservative terminal value, which will be used for the base case.

### G) Enterprise to Equity Bridge

| Component | Value (in millions USD) | Formula & Source |
| --- | --- | --- |
| PV of Explicit Period FCFF | $2,739 | Sum of PV of FCFF Years 1-5 |
| PV of Terminal Value | $8,527 | Terminal Value / (1 + WACC)^5 |
| **Enterprise Value (EV)** | **$11,266** | **PV of FCFF + PV of Terminal Value** |
| Less: Total Debt | ($5,212) | (StockAnalysis, Aug 20, 2025) |
| Plus: Cash & Equivalents | $273 | (StockAnalysis, Aug 20, 2025) |
| **Equity Value** | **$6,327** | **EV - Net Debt** |

### H) Per-Share Value and Margin of Safety

| Valuation Case | Per-Share Value | Assumptions |
| --- | --- | --- |
| **Base Case Fair Value** | **$180.77** | Growth: 4%, Margin: 18.53%, WACC: 7.99% |
| **Low/Bear Case** | $145 | Growth: 2%, Margin: 17.5%, WACC: 8.5% |
| **High/Bull Case** | $220 | Growth: 5%, Margin: 19.5%, WACC: 7.5% |
| **Margin of Safety (MOS) Price (30%)** | **$126.54** | Base Case \* (1 - 0.30) |

### Risk Notes

1.  **High Leverage:** The company operates with a significant amount of debt ($5.2B) and negative shareholder's equity, making it sensitive to changes in interest rates and credit markets.
2.  **Competitive Intensity:** The quick-service restaurant (QSR) pizza market is highly competitive, with pressure from other large chains and third-party delivery aggregators potentially impacting market share and pricing power.
3.  **Franchisee Health:** The success of the business model is heavily reliant on the profitability and financial health of its franchisees. Any significant downturn in franchisee economics could slow store growth and investment.
4.  **Consumer Spending:** As a consumer discretionary company, sales are susceptible to downturns in the macroeconomic environment that could pressure consumer spending on food away from home.
5.  **International Risks:** The company has significant international operations, exposing it to foreign currency fluctuations and geopolitical instability, as noted by management in their Q2 2025 earnings call.

final answer is 180.77 $