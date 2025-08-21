Here is a base-case intrinsic value analysis for monday.com Ltd. (MNDY).

### **Valuation of monday.com Ltd. (MNDY)**
*   **Company:** monday.com Ltd.
*   **Ticker:** MNDY
*   **Currency:** USD
*   **Date of Analysis:** August 21, 2025
*   **Primary Sources Reviewed:** StockAnalysis.com Financial Data, Q2 2025 Earnings Release, US Treasury Department.

---

### A) Baseline Financials (TTM)

The following table summarizes the Trailing Twelve Months (TTM) financial data ending June 30, 2025. All figures are in millions of USD.

| Metric | TTM Value | Source & Citation |
| :--- | :--- | :--- |
| Revenue | $1,100.0 | StockAnalysis.com, Income Statement, Aug 21, 2025 |
| Gross Margin | 89.42% | StockAnalysis.com, Income Statement, Aug 21, 2025 |
| Operating Income (EBIT) | ($19.6) | StockAnalysis.com, Income Statement, Aug 21, 2025 |
| Net Income | $40.0 | StockAnalysis.com, Income Statement, Aug 21, 2025 |
| Depreciation & Amortization | $9.2 | StockAnalysis.com, Cash Flow, Aug 21, 2025 |
| Stock-Based Compensation | $153.7 | StockAnalysis.com, Cash Flow, Aug 21, 2025 |
| Capital Expenditures | ($16.8) | StockAnalysis.com, Cash Flow, Aug 21, 2025 |
| Change in Working Capital | ($117.3) | StockAnalysis.com, Cash Flow, Aug 21, 2025 |
| Interest Expense | $0.0 | StockAnalysis.com, Income Statement, Aug 21, 2025 |
| Cash & Equivalents | $1,591.0 | StockAnalysis.com, Balance Sheet, Aug 21, 2025 |
| Total Debt | $126.2 | StockAnalysis.com, Balance Sheet, Aug 21, 2025 |
| Diluted Shares | 53.0 | StockAnalysis.com, Income Statement, Aug 21, 2025 |

---

### B) Management Guidance Extraction

The following guidance was provided for the full fiscal year 2025, as of the earnings announcement on August 11, 2025.

*   **Full Year 2025 Revenue:** "Total revenue of $1,224 million to $1,229 million, representing year-over-year growth of approximately 26%."
*   **Full Year 2025 Non-GAAP Operating Income:** "Non-GAAP operating income of $154 million to $158 million and operating margin of approximately 13%."
*   **Full Year 2025 Adjusted Free Cash Flow:** "Adjusted free cash flow of $320 million to $326 million and adjusted free cash flow margin of 26% to 27%."

---

### C) Forecast & Assumptions (5-Year Horizon)

The base-case forecast relies on management guidance and historical trends.

| Assumption | Value | Rationale & Citation |
| :--- | :--- | :--- |
| **Revenue Growth (Y1)** | **26.2%** | Midpoint of management's FY 2025 guidance ($1,226.5M). (Investor Release, Aug 11, 2025) |
| **Revenue Growth (Y2-Y5)** | **24% -> 18%** | Assumes a gradual deceleration from the guided Year 1 rate as the company scales, which is a prudent approach for high-growth companies. |
| **GAAP Operating Margin** | **-0.3% -> 0.5%** | Starting with management's non-GAAP guidance (13%) and subtracting estimated SBC (~13.3%), then assuming modest improvement of 0.2% annually. |
| **Tax Rate** | **23.0%** | A normalized statutory tax rate is assumed for future profitable years, as historical rates are not meaningful due to prior losses. |
| **Capex as % of Revenue** | **1.5%** | Based on the 3-year historical average (2022-2024), reflecting stable capital intensity. (StockAnalysis.com) |
| **SBC as % of Revenue** | **13.0%** | Aligned with recent TTM levels (14.0%) and the primary reconciling item between GAAP/Non-GAAP income. Assumed to remain stable. (StockAnalysis.com) |
| **Change in WC as % of Δ Revenue** | **40.0%** | Based on the 3-year historical average, which captures the cash flow impact of unearned revenue and accounts receivable growth. (StockAnalysis.com) |

---

### D) Free Cash Flow Construction

Free Cash Flow to the Firm (FCFF) is used for this valuation as it represents cash flow available to all capital providers and is independent of capital structure.
**Formula:** `FCFF = EBIT * (1 - Tax Rate) + D&A - SBC - Capex - Change in Working Capital`

| (USD, Millions) | Year 1 (2025) | Year 2 (2026) | Year 3 (2027) | Year 4 (2028) | Year 5 (2029) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Revenue | $1,226.5 | $1,520.9 | $1,855.5 | $2,226.6 | $2,627.3 |
| **EBIT** | **($3.7)** | **($1.5)** | **$3.7** | **$11.1** | **$21.0** |
| EBIT * (1-Tax) | ($3.7) | ($1.5) | $2.9 | $8.6 | $16.2 |
| + Depreciation & Amortization | $11.0 | $13.7 | $16.7 | $20.0 | $23.6 |
| - Stock-Based Comp | ($159.4) | ($197.7) | ($241.2) | ($289.5) | ($341.6) |
| - Capex | ($18.4) | ($22.8) | ($27.8) | ($33.4) | ($39.4) |
| - Change in WC | ($101.3) | ($117.7) | ($133.9) | ($148.4) | ($160.3) |
| **Free Cash Flow (FCFF)** | **($271.8)** | **($326.1)** | **($383.4)** | **($442.6)** | **($501.5)** |

---

### E) Discount Rate (WACC)

| Component | Value | Calculation / Source |
| :--- | :--- | :--- |
| **Cost of Equity (Ke)** | **10.64%** | `Risk-Free Rate + (Beta * Equity Risk Premium)` |
| Risk-Free Rate | 4.29% | 10-Year US Treasury Yield (YCharts, Aug 21, 2025) |
| Equity Risk Premium | 5.00% | Standard market assumption for developed markets. |
| Beta (5-Yr) | 1.27 | Reflects higher volatility than the market, appropriate for a tech stock. (Barchart.com) |
| **Cost of Debt (Kd)** | **5.50%** | Estimated rate based on current risk-free rates plus a credit spread. |
| Tax Rate | 23.0% | Long-term normalized tax rate assumption. |
| Market Cap (E) | $9,188 M | $173.37/share * 53.0M shares. (StockAnalysis.com, Aug 21, 2025) |
| Net Debt (D) | ($1,465 M) | $126.2M Debt - $1,591M Cash. The company has significant net cash. |
| **WACC** | **10.64%** | `Ke * (E / (E+D)) + Kd * (D / (E+D)) * (1-T)`. As the company has net cash, WACC is equal to the Cost of Equity. |

---

### F) Terminal Value

The Gordon Growth method is used to calculate the terminal value, with a conservative perpetual growth rate.

| Component | Value | Calculation |
| :--- | :--- | :--- |
| Terminal FCFF (Year 6) | ($514.0 M) | `Year 5 FCFF * (1 + g)` |
| Discount Rate (WACC) | 10.64% | From WACC calculation. |
| Terminal Growth Rate (g) | 2.50% | Capped at long-run inflation expectations. |
| **Terminal Value** | **($6,314 M)** | `(Terminal FCFF) / (WACC - g)` |
| Present Value of TV | **($3,799 M)** | `TV / (1 + WACC)^5` |

**Exit Multiple Cross-Check:** A cross-check is not meaningful in this case, as the negative projected FCFF and EBIT make exit multiples an unreliable validation method. The Gordon Growth method, while also negative, is used as the primary approach based on the formulaic requirements.

---

### G) Enterprise to Equity Bridge

| Component | Value | Calculation |
| :--- | :--- | :--- |
| PV of Explicit FCFF (Y1-5) | ($1,380 M) | Sum of discounted annual FCFF. |
| PV of Terminal Value | ($3,799 M) | From Terminal Value calculation. |
| **Enterprise Value** | **($5,179 M)** | `PV of FCFF + PV of Terminal Value` |
| Less: Total Debt | ($126 M) | From Balance Sheet. |
| Plus: Cash & Equivalents | $1,591 M | From Balance Sheet. |
| **Equity Value** | **($3,714 M)** | `Enterprise Value - Debt + Cash` |

---

### H) Per-Share Value and Margin of Safety

| Component | Value | Calculation |
| :--- | :--- | :--- |
| Equity Value | ($3,714 M) | From Equity Bridge calculation. |
| Diluted Shares Outstanding | 53.0 M | From Baseline Financials. |
| **Base-Case Fair Value** | **($70.08)** | `Equity Value / Diluted Shares` |

The model yields a negative intrinsic value, which suggests that under the current assumptions grounded in GAAP earnings and treating stock-based compensation as a full cash cost, the company's future cash flows do not support its current valuation. The significant negative cash flow is driven primarily by the high stock-based compensation relative to a slightly negative GAAP EBIT.

**Valuation Range:**
*   **Base Case:** **($70.08)**. Based on the assumptions outlined above.
*   **Low/Bear Case:** The value would be even more negative with lower revenue growth (e.g., 15-20%) or if SBC remains a higher percentage of revenue.
*   **High/Bull Case:** Achieving positive value would require a significant and rapid improvement in GAAP operating margins, far exceeding the modest assumptions used, or a substantial reduction in stock-based compensation as a percentage of revenue. For example, if the company achieved a 10% GAAP operating margin in Year 5, the valuation would turn positive.

**Margin of Safety (MOS) Price:**
*   A Margin of Safety is not applicable as the calculated intrinsic value is negative.

---

### One-paragraph Risk Notes

Key risks to this valuation include: 1) **High Stock-Based Compensation:** The model treats SBC as a cash expense, which heavily impacts FCFF. If SBC is lower than projected or its dilutive effect is less severe, the valuation would improve. 2) **Path to GAAP Profitability:** The forecast assumes a very slow path to GAAP profitability. Faster-than-expected operating leverage and margin expansion could lead to a positive valuation. 3) **Competition:** The work management software space is highly competitive, and failure to maintain growth rates against rivals like Asana or Smartsheet would invalidate revenue forecasts. 4) **Market Sentiment:** A significant portion of the company's current market value is based on non-GAAP metrics and long-term growth expectations, which are not fully captured in this strict, fundamentals-based DCF model. A change in market sentiment on growth stocks could lead to high volatility.

final answer is -70.08 $