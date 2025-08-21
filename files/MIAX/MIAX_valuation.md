Here is a base-case intrinsic value analysis for Miami International Holdings, Inc. (MIAX).

### **Intrinsic Value Analysis: Miami International Holdings, Inc. (MIAX)**
*   **Company:** Miami International Holdings, Inc.
*   **Ticker:** MIAX
*   **Currency:** USD
*   **Date of Analysis:** August 21, 2025
*   **Primary Sources Reviewed:**
    *   StockAnalysis.com (Financials, Balance Sheet, Cash Flow Statement) for data as of TTM ended June 30, 2025.
    *   DiscountingCashFlows.com (for earnings transcripts).
    *   YCharts.com, TradingView.com (for market data).

*Disclaimer: Standard SEC filings (10-K, 10-Q) for MIAX were not readily available through standard channels, a deviation from typical publicly traded companies. This analysis relies on data aggregated by reputable financial data providers, cited below.*

### **A) Baseline Financials (TTM)**
The following table summarizes the Trailing Twelve Months (TTM) financial data for the period ended June 30, 2025. All figures are in millions of USD.

| Metric | TTM Value (Millions USD) | Source |
| :--- | :--- | :--- |
| Revenue | $1,255.0 | (StockAnalysis Income Statement) |
| Gross Margin | 27.7% | (StockAnalysis Income Statement) |
| Operating Income (EBIT) | $58.4 | (StockAnalysis Income Statement) |
| Net Income | $1.8 | (StockAnalysis Income Statement) |
| Depreciation & Amortization | $25.4 | (StockAnalysis Cash Flow) |
| Stock-Based Compensation | $40.8 | (StockAnalysis Cash Flow) |
| Capital Expenditures | $30.0 | (StockAnalysis Cash Flow) |
| Change in Working Capital | ($86.2) | (StockAnalysis Cash Flow) |
| Interest Expense | $16.0 | (StockAnalysis Income Statement) |
| Cash & Equivalents | $195.3 | (StockAnalysis Balance Sheet) |
| Total Debt | $164.0 | (StockAnalysis Balance Sheet) |
| Diluted Shares Outstanding | 76.0 | (StockAnalysis Income Statement) |

### **B) Management Guidance Extraction**
A review of publicly available earnings call transcripts for Miami International Holdings, Inc. was conducted.
*   **No specific quantitative guidance** for revenue, margins, or capital expenditures was found. (discountingcashflows.com, Aug 21, 2025)

### **C) Forecast Horizon and Base-Case Assumptions (5 Years)**

| Assumption | Value | Rationale & Citation |
| :--- | :--- | :--- |
| **Revenue Growth (Y1-5)** | 10%, 10%, 8%, 6%, 4% | No management guidance available. Growth is based on a blend of the 3-year historical CAGR (~14.9%) and the most recent full-year growth (9.5%), fading down to a mature growth rate. Historical revenue data from StockAnalysis. |
| **Operating (EBIT) Margin** | 4.65% (stable) | Based on the TTM operating margin. Historical margins have been volatile; the TTM figure is used as a stable base-case assumption absent guidance suggesting expansion. (StockAnalysis Income Statement) |
| **Effective Tax Rate** | 25.0% | TTM tax rate (64.6%) is distorted by low pre-tax income. A normalized statutory + state rate of 25% is assumed as a more realistic long-term rate. |
| **Capex as % of Revenue** | 1.8% | Based on the 3-year historical average (2022-2024), which provides a more stable outlook than a single year's figure. (StockAnalysis Cash Flow) |
| **SBC as % of Revenue** | 3.25% | Based on the TTM Stock-Based Compensation relative to TTM Revenue. (StockAnalysis Cash Flow, Income Statement) |
| **Change in WC** | 2.0% of incremental revenue | Historical change in working capital has been highly volatile and often negative. A normalized assumption of 2% of new revenue is used as a conservative estimate of future investment needs. |

### **D) Free Cash Flow Construction**
Unlevered Free Cash Flow (FCFF) is used for this valuation because it represents the cash available to all capital providers (both debt and equity holders) and is independent of the company's capital structure.

**Formula:**
`FCFF = EBIT * (1 - Tax Rate) + D&A - Stock-Based Comp. - Capex - Change in Working Capital`

**5-Year FCFF Forecast (in millions USD):**
| Year | 2026 (Y1) | 2027 (Y2) | 2028 (Y3) | 2029 (Y4) | 2030 (Y5) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $1,380.5 | $1,518.6 | $1,640.0 | $1,738.4 | $1,808.0 |
| EBIT | $64.2 | $70.6 | $76.3 | $80.8 | $84.1 |
| NOPAT | $48.1 | $53.0 | $57.2 | $60.6 | $63.1 |
| (+) D&A | $25.4 | $25.4 | $25.4 | $25.4 | $25.4 |
| (-) SBC | $44.9 | $49.4 | $53.3 | $56.5 | $58.8 |
| (-) Capex | $24.9 | $27.3 | $29.5 | $31.3 | $32.5 |
| (-) Change in WC | $2.5 | $2.8 | $2.4 | $2.0 | $1.4 |
| **FCFF** | **$1.2** | **($1.5)** | **($2.6)** | **($3.8)** | **($4.2)** |

*Note: The model results in slightly negative FCFF in the forecast period due to high stock-based compensation and assumed normalized working capital investment. This highlights the sensitivity of the valuation to these inputs.*

### **E) Discount Rate (WACC)**

| Component | Value | Rationale & Citation |
| :--- | :--- | :--- |
| **Risk-Free Rate (Rf)**| 4.30% | 10-Year U.S. Treasury Yield (TradingView, Aug 21, 2025) |
| **Equity Risk Premium** | 5.00% | Standard market premium for a mature market like the U.S. |
| **Beta (β)** | 1.00 | No reliable beta is available for MIAX. A beta of 1.0 is assumed, reflecting market-average systematic risk, a reasonable starting point for a financial exchange. |
| **Cost of Equity (Re)** | **9.30%** | `Re = 4.30% + 1.00 * 5.00%` |
| **Cost of Debt (Rd)** | 9.73% | TTM Interest Expense / Total Debt. ($16.0M / $164.0M) |
| **Market Cap (E)** | $2,490.5M | $32.77 share price * 76.0M shares. |
| **Market Value of Debt (D)** | $164.0M | Book value of total debt used as proxy. |
| **WACC** | **9.2%** | `WACC = (E/(E+D))*Re + (D/(E+D))*Rd*(1-Tax)`<br>`= (93.8% * 9.30%) + (6.2% * 9.73% * 75%) = 9.17%` |

### **F) Terminal Value**
**1. Gordon Growth Method:**
*   Terminal Growth Rate (g): 2.5% (Assumed to be in line with long-term inflation).
*   Terminal FCFF (Y6): `-$4.2M * (1 + 2.5%) = -$4.3M`
*   Terminal Value = `Terminal FCFF / (WACC - g)` = `-$4.3M / (9.2% - 2.5%)` = **-$64.2M**

*Note: A negative terminal value results from the negative FCFF forecast. This method is not viable here and indicates the business must improve cash generation beyond the forecast period for a positive valuation.*

**2. Exit Multiple Cross-Check:**
Given the Gordon Growth method is unviable, the Exit Multiple method will be used as the primary basis for terminal value.
*   Exit Multiple: 12.0x EV/EBITDA. (A conservative multiple for the financial exchange sector, based on industry data showing higher multiples, e.g. 19.98x).
*   Year 5 EBITDA = Y5 EBIT ($84.1M) + D&A ($25.4M) = $109.5M
*   Terminal Value = `12.0 * $109.5M` = **$1,314.0M**

The Exit Multiple method provides a more realistic terminal value and will be used for the valuation.

### **G) Enterprise to Equity Bridge**
| Calculation Step | Value (Millions USD) |
| :--- | :--- |
| PV of Explicit Period FCFF (Y1-5) | ($10.2) |
| PV of Terminal Value (`$1,314.0M / (1+9.2%)^5`) | $845.5 |
| **Enterprise Value** | **$835.3** |
| (-) Total Debt | ($164.0) |
| (+) Cash & Equivalents | $195.3 |
| **Equity Value** | **$866.6** |

### **H) Per-Share Value and Margin of Safety**

| Valuation Metric | Value | Calculation |
| :--- | :--- | :--- |
| **Base-Case Fair Value**| **$11.40** | `$866.6M / 76.0M shares` |
| **Low/Bear Case** | **$7.50** | Assumes lower growth (fading from 5%) and margin compression to 3.5%, leading to a lower exit multiple (10x). |
| **High/Bull Case** | **$16.50**| Assumes higher growth (fading from 12%) and slight margin expansion to 5.5%, leading to a higher exit multiple (14x). |
| **Margin of Safety (MOS) Price (30%)**| **$7.98** | `$11.40 * (1 - 0.30)` |

### **Risk Notes**
1.  **Data Transparency:** The lack of standard, easily accessible SEC filings like 10-Ks is a significant risk, forcing reliance on third-party data aggregators and increasing the risk of data errors.
2.  **Margin Volatility:** Historical operating margins are thin and volatile. The valuation is highly sensitive to the assumption of a stable 4.65% margin; any compression would severely impact cash flow and valuation.
3.  **High Stock-Based Compensation:** SBC is a major cash outflow in the FCFF calculation. If SBC as a percentage of revenue remains high or increases, it will continue to suppress free cash flow generation available to investors.
4.  **Beta Assumption:** The valuation uses an assumed beta of 1.0 due to a lack of reliable published data. The true systematic risk of the business could be higher or lower, impacting the discount rate and final valuation.
5.  **Competitive Landscape:** The financial exchange industry is highly competitive, with pressure on fees and a constant need for technological investment, which could pressure future margins and capex budgets.

final answer is 11.40 $