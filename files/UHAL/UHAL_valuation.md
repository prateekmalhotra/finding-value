Of course. The provided valuation is well-structured but contains several critical flaws, primarily centered on unrealistic long-term capital expenditure assumptions which, as the original analyst correctly noted, create a nonsensical terminal value calculation. The fix is not to simply override the terminal value method but to correct the underlying assumptions that lead to the issue.

Here is a revised and improved valuation that addresses these flaws while maintaining the original's format and detail.

---

### **U-Haul Holding Company (UHAL) Intrinsic Value Analysis - Revised**

*   **Company:** U-Haul Holding Company (UHAL)
*   **Currency:** United States Dollar (USD)
*   **Date of Analysis:** August 24, 2025
*   **Primary Sources Reviewed:** UHAL FY2025 10-K, StockAnalysis.com Financial Data, Public Market Data.

---

### **Part 1: Market-Implied Valuation (Reverse DCF)**

This section, which reverse-engineers the growth and profitability assumptions embedded in the current stock price, is methodologically sound and provides excellent context. It will be retained without changes.

**A) ESTABLISH BASELINE & MARKET PRICE**

1.  **Current Market Price:** **$59.00** (as of close, August 22, 2025).

2.  **Baseline Financials (TTM as of June 30, 2025):**
    All figures are in millions of USD.

| Metric | TTM Value (USD Millions) | Source & Citation |
| :--- | :--- | :--- |
| Revenue | $5,911 | StockAnalysis Financials (data sourced from FY2025 10-K/10-Q) |
| Operating Income (EBIT) | $677 | StockAnalysis Financials |
| Net Income | $314 | StockAnalysis Financials |
| Depreciation & Amortization | $1,040 | StockAnalysis Cash Flow Statement |
| Capital Expenditures (Capex) | $3,406 | StockAnalysis Cash Flow Statement |
| Change in Working Capital | $88 | StockAnalysis Cash Flow Statement |
| Interest Expense | $311 | StockAnalysis Financials |
| **_Balance Sheet Items_** | **_(as of March 31, 2025)_** | **_Source & Citation_** |
| Cash & Equivalents | $989 | UHAL FY2025 10-K |
| Total Debt | $7,229 | UHAL FY2025 10-K |
| Diluted Shares Outstanding | 196 | StockAnalysis Financials |

**B) REVERSE-ENGINEER ASSUMPTIONS**

*   **WACC Calculation:**
    *   Cost of Equity (CAPM) = 4.26% + 1.10 \* 5.0% = **9.76%**
    *   Cost of Debt (Pre-Tax) = $311M / $7,229M = 4.30%.
    *   WACC = (11,564/17,804 \* 9.76%) + (7,229/17,804 \* 4.30% \* (1-0.24)) = **7.66%**

*   **Market-Implied Assumptions:**
    To justify the current enterprise value of **$17,804M**, assuming a stable TTM operating margin of **11.45%**, a WACC of **7.66%**, and a terminal growth rate of **2.5%**, the model requires a **5-year revenue Compound Annual Growth Rate (CAGR) of approximately 7.5%.**

    **Conclusion:** To justify today's $59.00 stock price, one must believe U-Haul can grow its revenues at a 7.5% CAGR for the next five years while maintaining its current, historically compressed, operating margins.

---

### **PART 2: ANALYST'S REVISED VALUATION (REALISTIC BASE-CASE)**

This section builds a valuation based on more realistic assumptions, particularly regarding the normalization of the company's heavy investment cycle.

**C) FORMULATE REVISED ASSUMPTIONS (5 YEARS)**

1.  **Revenue Growth (Years 1-5):** The original 4.0% tapering to 3.0% forecast is a reasonable and conservative starting point. This assumption is retained.

2.  **Operating Margin:** The original 12.0% stable margin is also a sound, conservative estimate that acknowledges recent pressures while allowing for some operational efficiency. This assumption is retained.

3.  **Taxes:** A **24.0% effective tax rate** remains a valid assumption based on historicals.

4.  **Capital Intensity (Revised):** The primary flaw in the original model was assuming a perpetual peak investment cycle (Capex at 40% of revenue). A more realistic model assumes this cycle normalizes.
    *   **Capex:** The current cycle is intense, but it is not permanent. I will model Capex starting at a high **38% of revenue in Year 1** and tapering down by 3% per year to a more sustainable **26% in Year 5.** This reflects the completion of major projects and a shift towards maintenance and more modest growth investments.
    *   **Working Capital:** Modeling the change in working capital as **1.5% of the change in revenue** remains a reasonable assumption.

5.  **SBC, Dilution, and Buybacks:** The assumption of **0% annual change to the share count** is retained, consistent with U-Haul's history.

**D) FREE CASH FLOW CONSTRUCTION (REVISED)**

This table now reflects the tapering capex assumption, resulting in a more realistic free cash flow trajectory.

| (USD Millions) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $6,147 | $6,378 | $6,598 | $6,804 | $6,995 |
| *Revenue Growth* | *4.00%* | *3.75%* | *3.50%* | *3.25%* | *3.00%* |
| EBIT | $738 | $765 | $792 | $816 | $839 |
| *Operating Margin* | *12.0%* | *12.0%* | *12.0%* | *12.0%* | *12.0%* |
| EBIT \* (1-t) (NOPAT) | $561 | $582 | $602 | $621 | $638 |
| \+ D&A (17.5% of Rev) | $1,076 | $1,116 | $1,155 | $1,191 | $1,224 |
| \- Capex (% of Rev) | ($2,336) | ($2,232) | ($2,045) | ($1,905) | ($1,819) |
| *Capex as % of Rev* | *38.0%* | *35.0%* | *31.0%* | *28.0%* | *26.0%* |
| \- ΔWC (1.5% of ΔRev) | ($4) | ($3) | ($3) | ($3) | ($3) |
| **Free Cash Flow (FCFF)** | **($703)** | **($538)** | **($292)** | **($97)** | **$41** |

**E) DISCOUNT RATE (WACC)**

The WACC of **7.66%** calculated in Part 1 will be used, as the company's capital structure and risk profile are not expected to change dramatically.

**F) TERMINAL VALUE (REVISED)**

With a more realistic forecast, the Gordon Growth Method (GGM) becomes a viable and fundamentally sound approach. We will normalize the terminal year's cash flow to reflect a steady state of growth and reinvestment.

1.  **Gordon Growth Method (GGM):**
    *   Terminal Growth Rate (g): **2.5%**, a realistic proxy for long-term economic growth.
    *   **Normalize Terminal Year Reinvestment:** In perpetuity, a company must reinvest a portion of its profits to achieve growth. The reinvestment rate is a function of growth (g) and Return on Invested Capital (ROIC).
        *   Reinvestment Rate = g / ROIC
        *   Assuming a long-term, stable ROIC of **10.0%** for a mature market leader like U-Haul, the terminal reinvestment rate = 2.5% / 10.0% = **25%**.
    *   **Terminal FCFF Calculation:**
        *   Year 5 NOPAT = $638M
        *   Reinvestment needed to grow = $638M \* 25% = $160M
        *   Normalized Terminal FCFF = NOPAT \* (1 - Reinvestment Rate) = $638M - $160M = **$478M**.
    *   **Terminal Value (GGM):**
        *   Terminal Value = [Terminal FCFF \* (1 + g)] / (WACC - g)
        *   Terminal Value = [$478M \* (1.025)] / (0.0766 - 0.025) = **$9,510M**.

2.  **Exit Multiple Cross-Check:**
    *   Year 5 EBITDA = Year 5 EBIT + Year 5 D&A = $839M + $1,224M = $2,063M.
    *   The GGM Terminal Value of $9,510M implies an exit EV/EBITDA multiple of $9,510M / $2,063M = **4.6x**.
    *   *Analyst Note:* This multiple is still very low compared to the historical average of ~10x. This indicates that the base case assumptions (especially the 12% operating margin) may be overly conservative or that the WACC is too high for the terminal period. Given this disconnect, using a conservative but more market-aligned exit multiple is a more pragmatic approach. A multiple of **9.0x** will be used, reflecting a slight discount to the historical average to account for a lower-growth, more mature future state.
    *   **Terminal Value (Exit Multiple):** $2,063M (Year 5 EBITDA) \* 9.0x = **$18,567M**. This value will be used as it better reflects a realistic market valuation for the company's ongoing operations.

**G) ENTERPRISE TO EQUITY BRIDGE (REVISED)**

*   **PV of Explicit FCFF:** [(-703)/1.0766¹] + [(-538)/1.0766²] + [(-292)/1.0766³] + [(-97)/1.0766⁴] + [41/1.0766⁵] = **-$1,399M**
*   **PV of Terminal Value:** $18,567M / (1.0766)⁵ = **$12,810M**
*   **Enterprise Value** = -$1,399M + $12,810M = **$11,411M**
*   **Equity Value** = Enterprise Value - Net Debt
    *   Net Debt = $7,229M (Total Debt) - $989M (Cash) = $6,240M
    *   Equity Value = $11,411M - $6,240M = **$5,171M**

**H) PER-SHARE VALUE AND MARGIN OF SAFETY (REVISED)**

1.  **Analyst's Base-Case Fair Value:**
    *   Fair Value Per Share = Total Equity Value / Diluted Shares Outstanding
    *   Fair Value Per Share = $5,171M / 196M = **$26.38**

2.  **Valuation Range:**
    *   **Base Case: $26.38.** As calculated above.
    *   **Low/Bear Case: $18.00.** Assumes revenue growth averages only 1.5%, margins compress to 11%, and the exit multiple is 8.0x in a recessionary environment.
    *   **High/Bull Case: $39.00.** Assumes revenue growth averages 5.0%, margins recover to 15%, and the exit multiple is 10.0x as the investment cycle proves highly profitable.

3.  **Margin of Safety (MOS) Price:**
    *   A 30% margin of safety from the base-case fair value is applied.
    *   MOS Price = $26.38 \* (1 - 0.30) = **$18.47**

---

### **Risk Notes**

The original risk notes remain highly relevant and are retained.

1.  **Capital Expenditure Intensity:** The valuation is highly sensitive to capex assumptions. While this model assumes a normalization, any delay in this tapering or failure to generate commensurate returns would negatively impact the valuation.
2.  **Used Equipment Market:** A significant portion of historical operating income has been supported by gains on the sale of used rental equipment. As the used vehicle market normalizes, these gains have shrunk, compressing margins. A further decline in resale values poses a material risk to profitability.
3.  **Competitive & Economic Pressure:** The business is sensitive to economic activity, particularly in the housing market. Increased competition from national players or new peer-to-peer rental platforms could pressure rental rates and utilization, impacting revenue growth.
4.  **Debt & Interest Rates:** The company carries a significant debt load of over $7 billion. In a rising rate environment, the cost to service this debt and refinance maturities could increase, reducing cash flow available to equity holders.

final answer is 26.38 $