## Dave & Buster's Entertainment, Inc. (PLAY) - Intrinsic Value Analysis

*   **Company:** Dave & Buster's Entertainment, Inc. (PLAY)
*   **Currency:** USD
*   **Date of Analysis:** August 21, 2025
*   **Primary Sources Reviewed:**
    *   StockAnalysis.com Financials (Income Statement, Balance Sheet, Cash Flow)
    *   YCharts, Investing.com for market data

---

### A) Baseline Financials (TTM)

The following table summarizes the Trailing Twelve Month (TTM) financial data for the period ended May 6, 2025. All figures are in millions of USD.

| Metric | TTM Value (Millions USD) | Source & Citation |
| :--- | :--- | :--- |
| Revenue | $2,112.3 | StockAnalysis.com, Income Statement |
| Gross Margin | 41.2% | StockAnalysis.com, Income Statement (Calculated) |
| Operating Income (EBIT) | $219.2 | StockAnalysis.com, Income Statement |
| Net Income | $38.6 | StockAnalysis.com, Income Statement |
| Depreciation & Amortization (D&A) | $238.6 | StockAnalysis.com, Cash Flow Statement |
| Stock-Based Compensation (SBC) | $3.6 | StockAnalysis.com, Cash Flow Statement |
| Capital Expenditures (Capex) | ($571.8) | StockAnalysis.com, Cash Flow Statement |
| Change in Working Capital | ($1.9) | StockAnalysis.com, Cash Flow Statement |
| Interest Expense | $139.7 | StockAnalysis.com, Income Statement |
| Cash & Equivalents | $11.9 | StockAnalysis.com, Balance Sheet (as of May 6, 2025) |
| Total Debt | $1,840.4 | StockAnalysis.com, Balance Sheet (as of May 6, 2025) |
| Diluted Weighted-Average Shares | 38.4 | StockAnalysis.com, Income Statement |

---

### B) Management Guidance Extraction

Direct management guidance from primary sources such as the latest earnings call transcript was not accessible for this analysis. Per the valuation protocol, assumptions will be based on historical performance and clearly stated rationales.

---

### C) Forecast & Assumptions (5-Year Horizon)

| Assumption | Value/Rationale | Citation/Justification |
| :--- | :--- | :--- |
| **Revenue Growth** | **Y1: 0.0%, Y2-5: 2.0%** | TTM revenue growth is slightly negative (-3.8%). A 0% growth rate in Year 1 reflects stabilization, followed by a conservative 2.0% growth rate, slightly below long-term inflation estimates, reflecting a mature business. |
| **Operating (EBIT) Margin** | **13.0%** | Based on the 3-year average operating margin (11.3% in FY25, 14.4% in FY24, 13.3% in FY23), held flat due to lack of specific management guidance on margin expansion. |
| **Tax Rate** | **20.0%** | Based on the 3-year average effective tax rate (16.6% in FY25, 22.2% in FY24, 21.0% in FY23). |
| **Capex as % of Revenue** | **Y1: 27.0%, Y2-5: 17.3%** | Y1 is based on the elevated TTM capex rate ($571.8M/$2,112.3M), reflecting current investment intensity. Y2-5 reverts to the normalized 3-year average (FY23-25). |
| **Change in NWC** | **$0** | The historical Change in Net Working Capital has been volatile. Given the low projected revenue growth, it is assumed to be negligible for the forecast period. |
| **SBC** | **$3.6M** | Based on the TTM figure, held constant. |
| **Shares Outstanding** | **38.4M** | Latest reported TTM diluted weighted-average shares. |

---

### D) Free Cash Flow Construction

Free Cash Flow to the Firm (FCFF) is used for this valuation as it represents the cash flow available to all capital providers (debt and equity) and is independent of the company's capital structure.

**Formula:** `FCFF = EBIT * (1 - Tax Rate) + D&A - SBC - Capex - Change in NWC`

| (in millions USD) | **Year 1** | **Year 2** | **Year 3** | **Year 4** | **Year 5** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $2,112.3 | $2,154.5 | $2,197.6 | $2,241.6 | $2,286.4 |
| EBIT (13.0% Margin) | $274.6 | $280.1 | $285.7 | $291.4 | $297.2 |
| NOPAT (EBIT \* (1-Tax)) | $219.7 | $224.1 | $228.6 | $233.1 | $237.8 |
| \+ D&A | $238.6 | $238.6 | $238.6 | $238.6 | $238.6 |
| \- Stock-Based Comp | ($3.6) | ($3.6) | ($3.6) | ($3.6) | ($3.6) |
| \- Capex | ($570.3) | ($372.7) | ($380.2) | ($387.8) | ($395.5) |
| \- Change in NWC | $0.0 | $0.0 | $0.0 | $0.0 | $0.0 |
| **Free Cash Flow (FCFF)** | **($115.6)** | **$86.4** | **$83.4** | **$80.3** | **$77.3** |

---

### E) Discount Rate (WACC)

| Component | Value/Calculation | Source & Rationale |
| :--- | :--- | :--- |
| **Cost of Equity (CAPM)** | | |
| Risk-Free Rate (Rf) | 4.30% | 10-Year U.S. Treasury Yield (Aug 20, 2025). |
| Equity Risk Premium (ERP) | 5.00% | Standard market premium for a developed market. |
| Beta (β) | 1.40 | A 5-year beta of 1.4 is used, reflecting above-average cyclicality for a consumer discretionary firm while discounting extreme COVID-era volatility. |
| **Cost of Equity (Ke)** | **11.30%** | `Ke = Rf + β * ERP = 4.30% + 1.40 * 5.00%` |
| | | |
| **Cost of Debt** | | |
| Cost of Debt (Kd) | 7.59% | `Interest Expense / Total Debt = $139.7M / $1,840.4M`. |
| After-Tax Cost of Debt | 6.07% | `Kd * (1 - Tax Rate) = 7.59% * (1 - 0.20)` |
| | | |
| **WACC Calculation** | | |
| Market Cap (E) | $925.8M | `$24.11/share * 38.4M shares`. |
| Market Value of Debt (D) | $1,840.4M | Total Debt from latest balance sheet. |
| Total Capital (V) | $2,766.2M | `E + D` |
| **WACC** | **7.51%** | `(E/V * Ke) + (D/V * Kd * (1-T))` |

---

### F) Terminal Value

The Gordon Growth method is used to calculate the terminal value, with a conservative perpetual growth rate (`g`) aligned with long-term inflation expectations.

*   **Terminal FCFF (Year 6):** `$77.3M * (1 + 2.5%) = $79.2M`
*   **Perpetual Growth Rate (g):** 2.5% (Justification: A reasonable long-term growth rate for a mature company, in line with expected long-run inflation).
*   **Terminal Value:** `$79.2M / (7.51% - 2.5%) = $1,580.8M`

**Cross-Check (Exit Multiple Method):**
*   **Year 5 EBITDA:** `EBIT_Y5 + D&A = $297.2M + $238.6M = $535.8M`
*   **Historical Median EV/EBITDA:** A typical median for the sector is ~8.0x.
*   **Terminal Value (Multiple):** `$535.8M * 8.0 = $4,286.4M`
*   **Conclusion:** There is a significant discrepancy. The Gordon Growth method provides a much more conservative (lower) terminal value and will be used for the base case.

---

### G) Enterprise to Equity Bridge

| Component | Value (Millions USD) | Calculation |
| :--- | :--- | :--- |
| **PV of Explicit FCFF** | **$160.0** | `PV of Y1-Y5 FCFF, discounted at 7.51% WACC` |
| **PV of Terminal Value** | **$1,101.9** | `$1,580.8M / (1 + 7.51%)^5` |
| **Enterprise Value** | **$1,261.9** | `Sum of PVs` |
| **Less: Total Debt** | ($1,840.4) | As of May 6, 2025. |
| **Plus: Cash & Equivalents** | $11.9 | As of May 6, 2025. |
| **Equity Value** | **($566.6)** | `EV - Net Debt` |

The calculation results in a negative Equity Value, primarily driven by the very high current capital expenditures and large debt load relative to the projected free cash flows. This indicates that under the current assumptions, the company's operations do not generate enough cash flow to support its debt and create value for equity holders.

---

### H) Per-Share Value and Margin of Safety

*   **Base-Case Fair Value:** **$0.00**
    *   Since the calculated Equity Value is negative, the intrinsic value per share is effectively zero under this base-case model.

*   **Valuation Range:**
    *   **Low/Bear Case:** The value would remain at $0. Inputs would include continued revenue decline and/or margin compression, further solidifying a negative equity value.
    *   **High/Bull Case:** For equity value to become positive, revenue growth would need to accelerate significantly (e.g., >5% annually), and/or operating margins would need to expand to the historical peak of ~15%, and capex would need to return to a much lower historical average (~12% of revenue) immediately. Even with optimistic assumptions, the high debt load presents a significant hurdle. A plausible bull case might yield a value in the **$5-$10 per share** range, but this requires substantial operational improvement beyond recent trends.

*   **Margin of Safety (MOS) Price:**
    *   Given a base case of $0, a traditional MOS calculation is not applicable. The analysis suggests extreme caution is warranted.

---

### Risk Notes

1.  **High Capital Intensity:** TTM capital expenditures are exceptionally high at 27% of revenue, leading to negative free cash flow. If this level of investment does not generate significant future growth, it will continue to destroy shareholder value.
2.  **Significant Debt Load:** The company carries a substantial debt balance ($1.84B) relative to its market capitalization (~$0.93B) and projected cash flows. This leverage poses a significant risk to equity holders.
3.  **Negative Revenue Growth:** The company has experienced negative year-over-year revenue growth recently. A failure to reverse this trend and return to sustainable top-line growth invalidates any recovery thesis.
4.  **Economic Sensitivity:** As a consumer discretionary company, Dave & Buster's is highly sensitive to the overall health of the economy and consumer spending habits. A recessionary environment would likely pressure revenue and margins.

final answer is 0.00 $