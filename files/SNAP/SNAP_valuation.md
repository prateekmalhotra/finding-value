### **Intrinsic Value Analysis: Snap Inc. (SNAP)**

*   **Company:** Snap Inc.
*   **Ticker:** SNAP
*   **Currency:** United States Dollar (USD)
*   **Date of Analysis:** August 21, 2025
*   **Primary Sources Reviewed:**
    *   Form 10-Q for the quarter ended June 30, 2025
    *   StockAnalysis.com Financial Data (as of August 20, 2025)
    *   YCharts & Trading Economics (for Treasury Yield data as of August 20, 2025)
    *   Investing.com (for Beta data)

---

### **A) Baseline Financials (TTM)**

The following table summarizes the Trailing Twelve Months (TTM) financial data for the period ended June 30, 2025. All figures are in millions of USD.

| Metric | Value (USD Millions) | Citation |
| :--- | :--- | :--- |
| Revenue | $5,638 | (StockAnalysis Income Statement, Aug 20, 2025) |
| Gross Margin | 53.8% | (StockAnalysis Income Statement, Aug 20, 2025) |
| Operating Income (EBIT) | -$654 | (StockAnalysis Income Statement, Aug 20, 2025) |
| Net Income | -$546 | (StockAnalysis Income Statement, Aug 20, 2025) |
| Depreciation & Amortization | $153 | (StockAnalysis Cash Flow, Aug 20, 2025) |
| Stock-Based Comp (SBC) | $1,017 | (StockAnalysis Cash Flow, Aug 20, 2025) |
| Capital Expenditures (Capex) | $194 | (StockAnalysis Cash Flow, Aug 20, 2025) |
| Change in Working Capital | -$1 | (StockAnalysis Cash Flow, Aug 20, 2025) |
| Interest Expense | $63 | (StockAnalysis Income Statement, Aug 20, 2025) |
| Cash & Equivalents | $926 | (Q2 2025 10-Q, June 30, 2025, p. 9) |
| Total Debt | $4,192 | (StockAnalysis Balance Sheet, June 30, 2025) |
| Diluted Shares | 1,679 | (StockAnalysis Income Statement, Aug 20, 2025) |

---

### **B) Management Guidance Extraction**

A review of the Management's Discussion and Analysis of Financial Condition and Results of Operations section of the latest Form 10-Q, filed for the quarter ended June 30, 2025, did not yield specific, quantitative forward-looking guidance for revenue, margins, or capex. The company discusses broad strategic priorities and macroeconomic factors but refrains from providing numerical targets.

---

### **C) Forecast & Assumptions (5-Year Horizon)**

*   **Revenue Growth:** Lacking management guidance, a 3-year historical Compound Annual Growth Rate (CAGR) from FY 2021 to FY 2024 is used.
    *   **Formula:** CAGR = (Ending Revenue / Beginning Revenue)^(1 / Periods) - 1
    *   **Calculation:** ($5,361M / $4,117M)^(1/3) - 1 = **9.2%**.
    *   **Assumption:** Revenue is projected to grow at 9.2% in Year 1, with the growth rate declining by 100 basis points each year to 5.2% in Year 5, reflecting increasing scale and market maturity.

*   **Operating Margin (EBIT Margin):**
    *   **Rationale:** Snap has a history of negative operating margins. The TTM margin is -11.6%. We assume a gradual improvement toward profitability, driven by management's stated focus on cost efficiencies.
    *   **Assumption:** The operating margin will improve by 190 basis points annually, from -11.6% in the baseline year to -2.1% in Year 5. This is a conservative path that does not assume profitability within the explicit forecast period.

*   **Taxes:**
    *   **Rationale:** Due to a history of losses, Snap has significant Net Operating Loss (NOL) carryforwards.
    *   **Assumption:** A **0% tax rate** is used for the 5-year forecast period, as NOLs are expected to offset any potential pre-tax income. A 21% U.S. statutory rate is applied to the terminal year EBIT for the terminal value calculation.

*   **Capital Intensity & Other Items:** These are forecast as a percentage of revenue based on the most recent TTM figures.
    *   **D&A:** 2.7% of Revenue.
    *   **SBC:** 18.0% of Revenue.
    *   **Capex:** 3.4% of Revenue.
    *   **Change in Working Capital:** 0.0% of incremental revenue (based on the negligible TTM figure).

---

### **D) Free Cash Flow Construction**

Free Cash Flow to the Firm (FCFF) is used for this valuation because it represents cash flow available to all capital providers (both debt and equity holders) and is independent of the company's capital structure.

*   **Formula:** FCFF = EBIT * (1 - Tax Rate) + D&A - Stock-Based Comp (SBC) - Capex - Change in Working Capital

**FCFF Forecast (in millions USD):**

| Year | Revenue | EBIT | D&A | SBC | Capex | Change in WC | **FCFF** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Y1 | $6,157 | -$597 | $166 | $1,108 | $209 | $0 | **-$1,748** |
| Y2 | $6,668 | -$540 | $180 | $1,200 | $227 | $0 | **-$1,787** |
| Y3 | $7,185 | -$460 | $194 | $1,293 | $244 | $0 | **-$1,803** |
| Y4 | $7,693 | -$354 | $208 | $1,385 | $261 | $0 | **-$1,792** |
| Y5 | $8,093 | -$170 | $218 | $1,457 | $275 | $0 | **-$1,684** |

---

### **E) Discount Rate (WACC)**

*   **Cost of Equity (CAPM):**
    *   **Formula:** Cost of Equity = Risk-Free Rate + Beta * Equity Risk Premium
    *   **Risk-Free Rate:** **4.30%** (Source: U.S. 10-Year Treasury Yield, August 20, 2025)
    *   **Beta:** **0.62** (Source: Investing.com 5-Year Monthly Beta). This reflects lower systematic risk relative to the market over the measurement period, despite high company-specific volatility.
    *   **Equity Risk Premium (ERP):** **5.0%** (Standard assumption for a mature market like the U.S.).
    *   **Cost of Equity Calculation:** 4.30% + 0.62 * 5.0% = **7.40%**

*   **Cost of Debt:**
    *   **Rationale:** The effective rate on existing convertible debt is low. The interest rate on the most recently issued senior notes (6.875%) is a better proxy for the current cost of borrowing.
    *   **Pre-Tax Cost of Debt:** **6.875%**

*   **WACC Calculation:**
    *   **Formula:** WACC = (E / (E+D)) * Cost of Equity + (D / (E+D)) * Cost of Debt * (1 - Tax Rate)
    *   **Market Value of Equity (E):** **$12,130 million** (Source: Companies Market Cap, August 20, 2025)
    *   **Market Value of Debt (D):** **$4,192 million** (Book value used as a proxy)
    *   **Total Capital (E+D):** $16,322 million
    *   **WACC Calculation:** (12130/16322) * 7.40% + (4192/16322) * 6.875% * (1 - 0.21) = **6.89%**

---

### **F) Terminal Value**

*   **Gordon Growth Model:**
    *   **Formula:** Terminal Value = (FCFF_Year5 * (1 + g)) / (WACC - g)
    *   **Terminal Growth Rate (g):** **2.5%**. This rate is a long-term inflation expectation, representing a sustainable, perpetual growth rate.
    *   **FCFF_Terminal:** To calculate the terminal free cash flow, we use Year 5 EBIT, but apply the statutory tax rate as NOLs are assumed to be exhausted in the long run.
        *   NOPAT = EBIT_Y5 * (1 - Tax) = -$170 * (1 - 0.21) = -$134M
        *   FCFF_Terminal = NOPAT + D&A - SBC - Capex = -$134 + $218 - $1,457 - $275 = -$1,648M
    *   **Terminal Value Calculation:** (-$1,648 * (1 + 0.025)) / (0.0689 - 0.025) = **-$38,442 million**

*   **Exit Multiple Cross-Check:**
    *   A cross-check using an EV/EBITDA multiple is not feasible because Snap's TTM and historical EBITDA is negative, rendering the multiple not meaningful for valuation.

---

### **G) Enterprise to Equity Bridge**

*   **Enterprise Value:**
    *   **PV of Explicit FCFF:** -$1,635M + (-$1,563M) + (-$1,481M) + (-$1,387M) + (-$1,208M) = **-$7,274 million**
    *   **PV of Terminal Value:** -$38,442M / (1 + 0.0689)^5 = **-$27,587 million**
    *   **Enterprise Value (EV):** -$7,274M + (-$27,587M) = **-$34,861 million**

*   **Equity Value:**
    *   **Formula:** Equity Value = Enterprise Value - Total Debt + Cash & Equivalents
    *   **Calculation:** -$34,861M - $4,192M + $926M = **-$38,127 million**

---

### **H) Per-Share Valuation**

The intrinsic valuation model results in a negative Equity Value due to sustained, significant negative free cash flows (driven largely by stock-based compensation) throughout the explicit forecast period and into perpetuity. This indicates that under the current cost structure and conservative growth assumptions, the company does not generate positive cash flow for its capital providers.

*   **Base-Case Fair Value:** **$0.00** (An equity value cannot be negative; this result implies no intrinsic value is generated for equity holders under this model's assumptions).

*   **Valuation Range:**
    *   **Low/Bear Case:** The base case already results in a $0 value. A bear case with lower revenue growth (e.g., 5% CAGR) or slower margin improvement would also result in a **$0.00** per share value.
    *   **High/Bull Case:** An optimistic scenario requires aggressive assumptions. For instance, achieving a +5% operating margin by Year 5 and a 15% revenue CAGR would be necessary to generate a positive, albeit low, single-digit per-share value. Such assumptions are not directly supported by recent historical performance or management commentary.

*   **Margin of Safety (MOS) Price:**
    *   As the Base-Case Fair Value is $0.00, a Margin of Safety price is not applicable.

---

### **Risk Notes**

1.  **Path to Profitability:** The company has a history of significant operating losses. This valuation is highly sensitive to assumptions about future operating margin expansion. Failure to control costs, particularly Stock-Based Compensation, relative to revenue growth presents the primary risk to generating positive free cash flow.
2.  **Competitive Pressure:** Snap operates in a highly competitive digital advertising market dominated by larger players like Meta and Google. These competitors have greater resources and could impede Snap's ability to capture advertising budgets and grow revenue at the forecasted rates.
3.  **Monetization of User Base:** The valuation depends on sustained revenue growth, which requires effectively monetizing a user base that is heavily concentrated in younger, potentially less brand-loyal demographics. Changes in user behavior or failure to grow ARPU could invalidate the forecast.
4.  **Stock-Based Compensation (SBC):** SBC represents a major economic cost and a significant cash outflow in this FCFF model, accounting for ~18% of revenue. The valuation is extremely sensitive to this assumption. If SBC as a percentage of revenue does not decrease significantly, achieving positive FCFF will be mathematically challenging.

final answer is 0.00 $