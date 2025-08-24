Of course. I will provide a critical review of the provided valuation, identify its weaknesses, and then generate a revised, more realistic valuation in the same format.

### **Critique of the Original Valuation**

The provided valuation is well-structured and follows a sound DCF methodology. However, there are two significant issues that impact the credibility of the final number:

1.  **Unrealistically Low Beta and WACC:** The use of a 0.29 beta is an extreme outlier, even for a defensive insurance company. Publicly available sources often show betas for HMN in the 0.5-0.7 range. This exceptionally low beta leads to a Cost of Equity (5.86%) and a WACC (5.68%) that are likely too low. A low WACC understates risk and inflates the present value of future cash flows, particularly the terminal value. This was correctly identified in the original analysis when the Gordon Growth Method (GGM) produced a "very high" 20.1x implied exit multiple. The problem wasn't the GGM itself, but the low discount rate used as an input.

2.  **Flawed Working Capital Assumption for an Insurer:** The original model identifies that the TTM Change in Working Capital ($391.2M) is an anomaly but replaces it with a proxy common for industrial companies ("5.0% of the *change* in revenue"). This method is inappropriate for an insurance company whose balance sheet dynamics (premiums, reserves, float) do not behave like traditional inventory and receivables. This resulted in a tiny, almost negligible working capital investment forecast, which likely overstates free cash flow.

### **Revisions to be Made**

I will correct these flaws by:
*   Using a more realistic, albeit still conservative, **beta of 0.60** to calculate a new WACC.
*   Modeling the investment in **Net Operating Assets as a percentage of *total* revenue**, a more stable and appropriate proxy for the cash required to support an insurer's growth.
*   Re-evaluating the terminal value using both the Gordon Growth Method (which becomes more viable with a realistic WACC) and the Exit Multiple Method to arrive at a "just right" estimate.

Here is the corrected valuation.

---

## **Horace Mann Educators Corporation (HMN) Intrinsic Value Analysis**

*   **Company:** Horace Mann Educators Corporation (HMN)
*   **Currency:** USD
*   **Date of Analysis:** August 24, 2025
*   **Primary Sources Reviewed:** StockAnalysis.com (sourcing from S&P Global Intelligence), SEC Filings (via search), Treasury Department data.

### **Part 1: Market-Implied Valuation**

#### **Current Market Price**
*   **$45.97** (as of August 22, 2025).

#### **Baseline Financials (TTM ended June 30, 2025)**
*(This data from the original analysis is unchanged)*
| Metric | Amount (Millions) | Source & Citation |
| :--- | :--- | :--- |
| **Revenue** | $1,649.0 | (stockanalysis.com, Income Statement) |
| **Operating Income (EBIT)** | $209.7 | (stockanalysis.com, Income Statement) |
| **Net Income** | $140.1 | (stockanalysis.com, Income Statement) |
| **Depreciation & Amortization**| $27.0 | (stockanalysis.com, Cash Flow Statement) |
| **Stock-Based Compensation** | $10.0 | (stockanalysis.com, Cash Flow Statement) |
| **Capex (proxy)** | $27.0 | (Proxy based on D&A) |
| **Change in Working Capital**| $391.2 | (stockanalysis.com, Cash Flow Statement) |
| **Interest Expense** | $34.7 | (stockanalysis.com, Income Statement) |
| **Cash & Equivalents** | $38.7 | (stockanalysis.com, Balance Sheet) |
| **Total Debt** | $547.5 | (stockanalysis.com, Balance Sheet) |
| **Diluted Shares**| 41.55 | (stockanalysis.com, Income Statement) |

#### **Market-Implied Assumptions**
To justify the current market price of $45.97, the market is pricing in a **5-year revenue CAGR of approximately 5.5%** while assuming the company can maintain its TTM **operating margin of 12.72%**.

*Critique:* This conclusion relies on the market using a very low discount rate (WACC of ~5.7%). This suggests the market perceives very little risk in HMN's future cash flows. An investor should be cautious about whether this low level of priced-in risk is truly justified.

---

### **Part 2: Analyst's Revised Valuation**

#### **Revised Forecast & Assumptions**
My base-case valuation incorporates more realistic assumptions for risk and capital intensity.

*   **Revenue Growth:** I project a **4.5% revenue growth rate in Year 1, tapering to 3.0% by Year 5**. This remains a reasonable and conservative outlook.
*   **Operating Margin:** I assume a stable **10.5% operating margin**. This is below the high TTM margin but above the historical average, representing a sustainable level of profitability.
*   **Tax Rate:** A **21.0% effective tax rate** is used.
*   **Revised Capital Intensity:**
    *   Capex is assumed to equal D&A, at 1.6% of revenue, assuming maintenance-level investment.
    *   **Change in Working Capital:** To better model an insurer, I will assume the net investment required to support growth is **2.5% of total revenue**. This proxy accounts for the necessary increases in reserves and other operating assets as the business writes more premiums. This is a more realistic and material cash outflow than the previous assumption.
*   **Share Count:** I project a **net 0.5% annual reduction** in diluted shares outstanding.

#### **Revised Discount Rate (WACC)**
*   **Cost of Equity (CAPM):**
    *   *Risk-Free Rate:* 4.26% (10-Year U.S. Treasury Yield)
    *   *Equity Risk Premium:* 5.5%
    *   *Revised Beta:* **0.60**. This is a more conventional beta for a low-volatility company in the defensive insurance sector, correcting the previous outlier.
    *   *Cost of Equity = 4.26% + 0.60 \* 5.5% = 7.56%*
*   **After-Tax Cost of Debt:** 5.08% (Unchanged from original analysis)
*   **Revised WACC Calculation:**
    *   *Weight of Equity = 77.7% | Weight of Debt = 22.3%* (Unchanged)
    *   *WACC = (77.7% \* 7.56%) + (22.3% \* 5.08%) = 5.87% + 1.13% = **7.00%***

#### **Revised Free Cash Flow Build**
*Formula: FCFF = EBIT * (1 - Tax Rate) + D&A - SBC - Capex - Change in Working Capital*

| (in millions USD) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $1,723.2 | $1,792.1 | $1,854.8 | $1,910.4 | $1,967.7 |
| EBIT (10.5% margin) | $181.0 | $188.2 | $194.8 | $200.6 | $206.6 |
| EBIT * (1-Tax Rate) | $143.0 | $148.7 | $153.9 | $158.5 | $163.2 |
| D&A (1.6% of Rev) | $27.6 | $28.7 | $29.7 | $30.6 | $31.5 |
| Capex | ($27.6) | ($28.7) | ($29.7) | ($30.6) | ($31.5) |
| SBC (as % of Rev)| ($10.4) | ($10.8) | ($11.2) | ($11.5) | ($11.9) |
| **Change in WC (2.5% of Rev)** | **($43.1)** | **($44.8)** | **($46.4)** | **($47.8)** | **($49.2)** |
| **FCFF** | **$89.5** | **$93.1** | **$96.6** | **$99.8** | **$103.6** |

#### **Revised Terminal Value**
With a more realistic WACC of 7.00%, the Gordon Growth Method becomes a more reliable primary method for the terminal value.

*   **Gordon Growth Method:**
    *   *Terminal Growth Rate (g):* 2.5% (long-term inflation and economic growth).
    *   *Terminal Value = FCFF Year 5 \* (1 + g) / (WACC - g)*
    *   *Terminal Value = $103.6M \* (1 + 2.5%) / (7.00% - 2.5%) = $106.2M / 4.50% = **$2,359.8M***

*   **Exit Multiple Cross-Check:**
    *   *Year 5 EBITDA = Year 5 EBIT + Year 5 D&A = $206.6M + $31.5M = $238.1M*
    *   *Implied Exit Multiple = Terminal Value / Year 5 EBITDA = $2,359.8M / $238.1M = **9.9x***
    *   This 9.9x implied multiple is highly realistic for the insurance sector and aligns perfectly with the 10.0x multiple used in the original analysis. This alignment gives strong confidence in the terminal value calculation.

#### **Revised Enterprise to Equity Bridge**
*   **PV of Explicit Period FCFF (discounted at 7.00%):**
    *   PV of 5-Year FCFF = ($89.5/1.07¹) + ($93.1/1.07²) + ($96.6/1.07³) + ($99.8/1.07⁴) + ($103.6/1.07⁵) = $83.6 + $81.3 + $78.8 + $76.1 + $73.9 = **$393.7 million**
*   **PV of Terminal Value:**
    *   *PV of TV = $2,359.8M / (1.0700)^5 = **$1,682.5 million***
*   **Enterprise Value:**
    *   *Enterprise Value = $393.7M + $1,682.5M = **$2,076.2 million***
*   **Less: Net Debt:** ($508.8 million) (Total Debt $547.5M - Cash $38.7M)
*   **Equity Value:** **$1,567.4 million**

#### **Revised Per-Share Valuation**
*   **Projected Year 5 Diluted Share Count:** **40.52 million** (Unchanged from original analysis)
*   **Analyst's Base-Case Fair Value:**
    *   *Fair Value = Equity Value / Projected Shares*
    *   *Fair Value = $1,567.4M / 40.52M = **$38.68 per share***
*   **Valuation Range:**
    *   **Base Case: $38.68**
    *   **Low/Bear Case: ~$31** (Lower growth and margins, 9.0x exit multiple)
    *   **High/Bull Case: ~$47** (Higher growth and margins, 11.0x exit multiple)
*   **Margin of Safety (MOS) Price (25%):** **$29.01**

### **Risk Notes**
*(These notes from the original analysis remain relevant)*
1.  **Interest Rate Sensitivity:** As an insurer, HMN's investment income and balance sheet are sensitive to changes in interest rates. A rapid decline in rates could pressure investment portfolio yields.
2.  **Catastrophe Losses:** The Property & Casualty segment is exposed to unpredictable catastrophe losses from weather events, which can cause significant volatility in earnings.
3.  **Competition:** The market for insurance and retirement products for educators is competitive. Larger, more diversified insurers could increase their focus on this niche, pressuring growth and margins.
4.  **Regulatory Risk:** The insurance industry is highly regulated. Changes in capital requirements, accounting standards, or consumer protection laws could adversely affect operations and profitability.

final answer is 38.68 $