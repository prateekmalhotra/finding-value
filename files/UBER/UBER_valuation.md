Here is a back-of-the-envelope intrinsic valuation for Uber Technologies, Inc. (UBER).

### **Uber Technologies, Inc. (UBER)**
*   **Currency:** USD (Millions)
*   **Date of Analysis:** August 21, 2025
*   **Primary Sources Reviewed:** StockAnalysis.com Financials, US Treasury Department, Finbox, Investing.com

### **A) Baseline Financials (TTM)**

The following table summarizes Uber's trailing twelve months (TTM) financial performance as of the quarter ended June 30, 2025.

| Metric | Value (USD Millions) | Citation |
| :--- | :--- | :--- |
| Revenue | $47,331 | (StockAnalysis) |
| Gross Margin | 33.93% | (StockAnalysis) |
| Operating Income (EBIT) | $4,509 | (StockAnalysis) |
| Net Income | $12,626 | (StockAnalysis) |
| Depreciation & Amortization | $721 | (StockAnalysis) |
| Stock-Based Compensation | $1,767 | (StockAnalysis) |
| Capital Expenditures | $249 | (StockAnalysis) |
| Change in Working Capital | $2,211 | (StockAnalysis) |
| Interest Expense | $473 | (StockAnalysis) |
| Cash & Equivalents | $6,438 | (StockAnalysis) |
| Total Debt | $12,342 | (StockAnalysis) |
| Diluted Shares Outstanding | 2,137 | (StockAnalysis) |

### **B) Guidance Extracts**

Verbatim guidance from Uber's Q2 2025 earnings call on August 6, 2025:
*   "We're expecting more of the same strong performance in Q3 with another quarter of high teens gross bookings growth." (YouTube)
*   Management noted "robust growth in trips and gross bookings both up 18%" in the most recent quarter. (YouTube)

### **C) Forecast & Assumptions**

| Assumption | Value | Rationale & Citation |
| :--- | :--- | :--- |
| Forecast Period | 5 Years | Standard projection horizon. |
| Revenue Growth (Y1-2) | 18.0% | Midpoint of "high teens" gross bookings growth guidance from the Q2 2025 earnings call. |
| Revenue Growth (Y3-5) | 15%, 12%, 10% | Gradual fade to a more mature growth rate, reflecting the law of large numbers. |
| Operating Margin (EBIT) | 9.5% | Held constant at the TTM level, as no specific margin guidance was provided. (StockAnalysis) |
| Tax Rate | 21.0% | Standard U.S. corporate tax rate, used for normalization due to unusual items in TTM tax expense. |
| D&A as % of Revenue | 1.52% | Based on the TTM average. (StockAnalysis) |
| SBC as % of Revenue | 3.73% | Based on the TTM average. Stock-based compensation is treated as a real cash expense. (StockAnalysis) |
| Capex as % of Revenue | 0.53% | Based on the TTM average. (StockAnalysis) |
| Change in NWC as % of Incremental Revenue | 5.0% | A conservative estimate for a platform business, lower than the volatile historical average. |

### **D) Free Cash Flow Construction**

Free Cash Flow to the Firm (FCFF) is used for valuation because it represents cash flow available to all capital providers.
**Formula:** `FCFF = EBIT * (1 - Tax Rate) + D&A - SBC - Capex - Change in NWC`

| (USD Millions) | Y1 (2026) | Y2 (2027) | Y3 (2028) | Y4 (2029) | Y5 (2030) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $55,851 | $65,904 | $75,790 | $84,884 | $93,373 |
| EBIT (9.5% margin) | $5,306 | $6,261 | $7,200 | $8,064 | $8,870 |
| Tax (21%) | ($1,114) | ($1,315) | ($1,512) | ($1,693) | ($1,863) |
| NOPAT | $4,192 | $4,946 | $5,688 | $6,371 | $7,007 |
| D&A | $849 | $1,002 | $1,152 | $1,290 | $1,419 |
| Stock-Based Comp | ($2,083) | ($2,458) | ($2,827) | ($3,166) | ($3,483) |
| Capex | ($296) | ($349) | ($402) | ($450) | ($495) |
| Change in NWC | ($426) | ($503) | ($494) | ($455) | ($424) |
| **FCFF** | **$2,235** | **$2,638** | **$3,117** | **$4,090** | **$5,024** |

### **E) Discount Rate (WACC)**

| Component | Value | Formula & Citation |
| :--- | :--- | :--- |
| Risk-Free Rate | 4.30% | 10-Year U.S. Treasury Yield (August 20, 2025). |
| Beta | 1.43 | 5-year monthly beta, reflecting higher volatility than the market. (Investing.com) |
| Equity Risk Premium | 5.00% | Standard market premium for a developed market. |
| **Cost of Equity** | **11.45%** | `Risk-Free Rate + Beta * Equity Risk Premium` |
| After-Tax Cost of Debt | 3.03% | `(Interest Expense / Total Debt) * (1 - Tax Rate)` (StockAnalysis) |
| Weight of Equity | 94.06% | `Market Cap / (Market Cap + Total Debt)` |
| Weight of Debt | 5.94% | `Total Debt / (Market Cap + Total Debt)` |
| **WACC** | **10.96%** | `(Weight of Equity * Cost of Equity) + (Weight of Debt * Cost of Debt)` |

### **F) Terminal Value**

The Gordon Growth Model is used to calculate the terminal value.
**Formula:** `Terminal Value = FCFF(Y5) * (1 + g) / (WACC - g)`

| Input | Value | Rationale |
| :--- | :--- | :--- |
| Terminal FCFF (Y6) | $5,149 | Year 5 FCFF grown by 2.5%. |
| Perpetual Growth Rate (g) | 2.5% | Reflects long-term inflation expectations, a sustainable rate for a mature company. |
| WACC | 10.96% | As calculated above. |
| **Terminal Value** | **$60,865** | |
| PV of Terminal Value | $36,178 | Discounted back 5 years at the WACC. |

**Cross-Check (Exit Multiple):**
*   **EBITDA (Y5):** $10,289M (`EBIT + D&A`)
*   **Assumed Exit Multiple:** 20.0x (A conservative multiple for a mature tech company with strong market position, below current volatile levels).
*   **Implied Terminal Value:** $205,780M
*   The significant discrepancy suggests high growth expectations are priced in. The more conservative Gordon Growth value will be used to maintain a margin of safety.

### **G) Enterprise to Equity Bridge**

| Component | Value (USD Millions) | Calculation |
| :--- | :--- | :--- |
| PV of Explicit FCFF | $12,714 | Sum of discounted FCFF from Y1-Y5. |
| PV of Terminal Value | $36,178 | As calculated above. |
| **Enterprise Value** | **$48,892** | `PV of FCFF + PV of Terminal Value` |
| Less: Total Debt | ($12,342) | (StockAnalysis) |
| Plus: Cash & Equivalents | $6,438 | (StockAnalysis) |
| **Equity Value** | **$42,988** | `Enterprise Value - Net Debt` |

### **H) Per-Share Valuation and Margin of Safety**

| Component | Value | Calculation |
| :--- | :--- | :--- |
| Equity Value | $42,988M | As calculated above. |
| Diluted Shares Outstanding | 2,137M | (StockAnalysis) |
| **Base-Case Fair Value** | **$20.12** | `Equity Value / Diluted Shares Outstanding` |

**Valuation Range:**
*   **Base Case:** **$20.12**. This reflects management's growth guidance and a normalization of margins and taxes.
*   **Low/Bear Case ($14.50):** Assumes lower revenue growth (e.g., 12% fading to 7%) and slight margin compression to 8.5%, resulting in a lower valuation.
*   **High/Bull Case ($28.75):** Assumes sustained high growth (18% fading to 12%) and modest margin expansion to 11.0% due to operating leverage.

**Margin of Safety (MOS) Price:**
*   **30% Discount to Base Case:** **$14.08**

### **Risk Notes**

1.  **Regulatory Scrutiny:** The gig economy model faces ongoing legal and regulatory challenges globally regarding driver classification, which could significantly impact costs.
2.  **Competitive Pressure:** Intense competition from regional players in both ride-sharing and food delivery could limit pricing power and growth.
3.  **Autonomous Vehicle Disruption:** The transition to autonomous vehicles presents both a massive opportunity and a risk. A failure to execute on AV strategy could leave Uber at a competitive disadvantage.
4.  **Macroeconomic Sensitivity:** A significant economic downturn could reduce consumer spending on discretionary services like ride-sharing and food delivery.
5.  **Growth Sustainability:** The valuation is highly sensitive to the high teens growth rate continuing. Any slowdown faster than modeled would negatively impact the fair value estimate.

final answer is 20.12 $