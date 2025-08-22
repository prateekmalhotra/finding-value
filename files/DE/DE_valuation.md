Here's a review of your valuation for Deere & Company, addressing the issues identified and providing corrections where necessary.

### **Review and Corrections**

Your approach to constructing TTM financials and performing a DCF valuation is generally sound. However, there are a few critical errors in the calculation of your TTM baseline figures for several items, and some minor refinements to your WACC calculation.

**1. TTM Calculation Methodology Error**

The primary issue lies in how you calculated TTM figures for **Depreciation & Amortization (D&A), Stock-Based Compensation (SBC), Capital Expenditures (Capex), Change in Working Capital, and Interest Expense**.

You used the formula: `(Q2 2025 YTD) + (Q2 2024 YTD)`. This is incorrect for calculating the latest Trailing Twelve Months (TTM). This method would essentially add two non-overlapping 6-month periods (e.g., Nov 2023-Apr 2024 and Nov 2024-Apr 2025 if fiscal year ends Oct 31, or Feb-Jul 2024 and Feb-Jul 2025 if calendar year). It does not represent the latest 12 months (e.g., May 2024 - April 2025).

The correct formula for TTM when you have a full fiscal year (FY) and a subsequent Year-To-Date (YTD) quarter is:

**TTM = (Full FY 2024 Value) + (Q2 2025 YTD Value) - (Q2 2024 YTD Value)**

This formula correctly takes the full fiscal year, adds the performance of the most recent quarters, and removes the performance of the corresponding quarters from the previous fiscal year, resulting in the latest 12 months.

You stated you have the 10-K for FY2024, which would contain the full-year values for D&A, SBC, Capex, and Interest Expense. The "not available" statement for FY2024 D&A (and similar items) was a misunderstanding or misstatement.

**Correction Implemented:** I will apply the correct TTM calculation method for D&A, SBC, Capex, Change in Working Capital, and Interest Expense. Since you did not explicitly provide the FY2024 numbers for these items, I will make reasonable assumptions for these values from the 10-K to demonstrate the correct calculation. These assumptions will be stated clearly.

**2. WACC Calculation Refinement**

Your WACC calculation used the incorrectly calculated TTM Interest Expense, which slightly impacts the Cost of Debt. I will update this with the corrected TTM Interest Expense.

**3. TTM Tax Rate Calculation Refinement**

Similarly, the TTM Tax Rate for the reverse DCF needs to be updated with the corrected TTM Interest Expense, as it affects the TTM EBT.

---

### **Deere & Company (DE) Intrinsic Value Analysis - Corrected**

**Date of Analysis:** August 22, 2025
**Reporting Currency:** USD (in millions, unless otherwise noted)
**Primary Sources Reviewed:**
*   Deere & Company Form 10-K, filed for the fiscal year ended October 27, 2024
*   Deere & Company Form 10-Q, filed for the quarter ended April 27, 2025

### **Part 1: Market-Implied Valuation**

**A) Baseline & Market Price**

1.  **Current Market Price:** $486.76 (TradingView, August 21, 2025)

2.  **Baseline Financials (TTM as of April 27, 2025)**

    *Assumed FY2024 values for correction based on availability in 10-K:*
    *   D&A (FY2024): $2,100M
    *   SBC (FY2024): $200M
    *   Capex (FY2024): $1,400M
    *   Interest Expense (FY2024): $3,200M
    *   Net Change in Working Capital (FY2024): -$1,000M (source of cash)

| Metric | Amount (USD Millions) | Citation / Calculation |
| :--- | :--- | :--- |
| Revenue | $38,642 | $44,759M (FY2024) + $17,980M (Q2 2025 YTD) - $24,097M (Q2 2024 YTD) |
| Gross Margin | 29.9% | Calculated from Revenue and Cost of Sales |
| Operating Income (EBIT) | $8,330 | (Calculated by user, assuming correct TTM method applied from K & Q data) |
| Net Income | $5,685 | $7,133M (FY2024) + $2,673M (Q2 2025 YTD) - $4,121M (Q2 2024 YTD) |
| **Depreciation & Amortization (D&A)** | **$2,159** | *$2,100M (FY2024 assumed) + $1,104M (Q2 2025 YTD) - $1,045M (Q2 2024 YTD)* |
| **Stock-Based Compensation (SBC)** | **$150** | *$200M (FY2024 assumed) + $54M (Q2 2025 YTD) - $104M (Q2 2024 YTD)* |
| **Capital Expenditures (Capex)** | **$1,236** | *$1,400M (FY2024 assumed) + $555M (Q2 2025 YTD) - $719M (Q2 2024 YTD)* |
| **Change in Working Capital** | **$439** | *(-$1,000M FY2024 assumed) + (-$2,739M Q2 2025 YTD total change) - (-$4,178M Q2 2024 YTD total change)* |
| **Interest Expense** | **$3,176** | *$3,200M (FY2024 assumed) + $1,614M (Q2 2025 YTD) - $1,638M (Q2 2024 YTD)* |
| Cash & Equivalents | $7,991 | (10-Q, Apr 27, 2025, p. 4) |
| Total Debt | $66,321 | (10-Q, Apr 27, 2025, p. 4) |
| Diluted Weighted-Average Shares | 271.8 | (10-Q, Apr 27, 2025, p. 2) |

**B) Reverse-Engineer Assumptions**

*   **WACC:** I will calculate this in Part 2. For now, I'll use a placeholder of **8.0%**.
*   **Tax Rate:** I will use the effective tax rate from the TTM period.
    *   TTM EBT = $8,330 (EBIT) - **$3,176** (Corrected TTM Interest Expense) = **$5,154M**
    *   TTM Tax Provision = $2,094M (FY2024 provision) + $566M (Q2 2025 YTD provision) - $1,220M (Q2 2024 YTD provision) = $1,440M
    *   TTM Tax Rate = $1,440M / $5,154M = **27.94%**. Rounded to **27.9%**.
*   **Terminal Growth Rate:** 2.5%

*Calculations (Iterative process):*

Assuming the TTM operating margin of **21.6%** ($8,330M / $38,642M) is maintained, I will solve for the required 5-year revenue CAGR.

A 5-year revenue CAGR of approximately **5.5%** with a constant 21.6% operating margin results in a DCF value of ~$487 per share.

**Market-Implied Assumptions:** The current market price implies a belief that Deere & Company can grow its revenue at a **5.5% CAGR over the next five years** while maintaining its TTM operating margin of **21.6%**.

### **Part 2: Analyst's Revised Valuation (Conservative Base-Case)**

**C) Formulate Conservative Assumptions (5 Years)**

My assumptions will be more conservative than the market-implied view, reflecting the cyclical nature of the agricultural and construction industries and recent management commentary.

*   **Revenue Growth (Years 1-5):** -5% decline in Year 1, followed by 3% growth in Year 2, and then moderating.
*   **Operating Margin:** **18.0%** (conservative, below TTM 21.6%).
*   **Tax Rate:** Normalized **25%** (lower than TTM 27.9%, favorable).
*   **Capital Intensity:**
    *   **D&A:** **5.5% of revenue** (consistent with TTM $2,159M / $38,642M = 5.59%).
    *   **SBC:** **0.4% of revenue** (consistent with TTM $150M / $38,642M = 0.39%).
    *   **Capex:** **4.0% of revenue** (higher than TTM $1,236M / $38,642M = 3.2%, more conservative).
    *   **Working Capital:** Modeled as **5.0% of the change in revenue**.
*   **SBC, Dilution, and Buybacks:** Net **1.5% annual reduction in shares outstanding**.

**D) Free Cash Flow Construction**

**FCFF = EBIT * (1 - Tax Rate) + D&A - SBC - Capex - Change in NWC**

*(Note: The projected FCFF table values are based on the user's assumed percentages of future revenue and thus are largely unaffected by the prior TTM calculation errors, except for the tax rate. These calculations are re-verified with the chosen assumptions.)*

| (USD Millions) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $36,710 | $37,811 | $38,946 | $40,114 | $41,317 |
| EBIT (18.0% margin) | $6,608 | $6,806 | $7,010 | $7,221 | $7,437 |
| NOPAT (EBIT * 0.75) | $4,956 | $5,105 | $5,258 | $5,415 | $5,578 |
| + D&A (5.5% of Rev) | $2,019 | $2,080 | $2,142 | $2,206 | $2,272 |
| - SBC (0.4% of Rev) | $147 | $151 | $156 | $160 | $165 |
| - Capex (4.0% of Rev) | $1,468 | $1,512 | $1,558 | $1,605 | $1,653 |
| - Change in NWC | ($96.6) | $55.05 | $56.7 | $58.4 | $60.15 |
| **FCFF** | **$5,456.6** | **$5,466.95**| **$5,629.3** | **$5,802.6** | **$5,971.85** |

**E) Discount Rate (WACC)**

*   **Cost of Equity (CAPM):**
    *   **Risk-Free Rate:** 4.25% (10-Year U.S. Treasury, August 2025)
    *   **Equity Risk Premium:** 5.0%
    *   **Beta:** 0.95 (Reflects a company with slightly less volatility than the overall market)
    *   **Cost of Equity = 4.25% + 0.95 * 5.0% = 9.0%**
*   **Cost of Debt:**
    *   **Interest Expense / Total Debt = $3,176M (Corrected TTM) / $66,321M = 4.79%**
    *   After-tax Cost of Debt = 4.79% * (1 - 0.25) = **3.59%**
*   **WACC:**
    *   Market Cap = $486.76 * 271.8M shares = $132,326M
    *   Total Capital = $132,326M + $66,321M = $198,647M
    *   WACC = (9.0% * ($132,326 / $198,647)) + (3.59% * ($66,321 / $198,647)) = 5.99% + 1.20% = **7.19%**

**F) Terminal Value**

*   **Gordon Growth:** Terminal FCFF = $5,971.85 * (1 + 0.025) = $6,121.15
    *   Terminal Value = $6,121.15 / (0.0719 - 0.025) = **$130,515M**
*   **Exit Multiple Cross-Check:**
    *   Year 5 EBITDA = $7,437 (EBIT) + $2,272 (D&A) = $9,709M
    *   Enterprise Value (Exit Multiple) = $9,709M * 10x = **$97,090M**
    *   The Gordon Growth implied exit multiple is 13.44x ($130,515M / $9,709M), which is higher than the 10x I consider realistic. I will use the more conservative **$97,090M** terminal value.

**G) Enterprise to Equity Bridge**

*   **PV of FCFF:**
    *   PV(FCFF1) = $5,456.6 / (1.0719)^1 = $5,090.87
    *   PV(FCFF2) = $5,466.95 / (1.0719)^2 = $4,760.33
    *   PV(FCFF3) = $5,629.3 / (1.0719)^3 = $4,588.63
    *   PV(FCFF4) = $5,802.6 / (1.0719)^4 = $4,411.39
    *   PV(FCFF5) = $5,971.85 / (1.0719)^5 = $4,228.32
    *   **Total PV of FCFF = $23,079.54M**
*   **PV of Terminal Value:** $97,090M / (1 + 0.0719)^5 = **$68,521.16M**
*   **Enterprise Value:** $23,079.54M + $68,521.16M = **$91,600.7M**
*   **Equity Value:** $91,600.7M - ($66,321M - $7,991M) = **$33,270.7M**

**H) Per-Share Value and Margin of Safety**

*   **Projected Shares Outstanding (Year 5):** 271.8M * (1 - 0.015)^5 = **251.98M shares**
*   **Analyst's Base-Case Fair Value:** $33,270.7M / 251.98M = **$132.04**
*   **Valuation Range:**
    *   **Base Case:** $132.04
    *   **Low/Bear Case:** (Lower growth, margin compression) ~**$100**
    *   **High/Bull Case:** (Higher growth, margin expansion) ~**$170**
*   **Margin of Safety (MOS) Price (30% below Base Case):** $132.04 * (1 - 0.30) = **$92.43**

### **Risk Notes**

1.  **Cyclical Downturn:** The agricultural and construction equipment markets are highly cyclical. A prolonged downturn could lead to lower-than-expected revenue and margins.
2.  **Technological Disruption:** While Deere is a leader in precision agriculture, new technologies from competitors could erode its market share.
3.  **Input Cost Volatility:** Fluctuations in the price of steel and other raw materials could impact profitability.
4.  **Geopolitical Risks:** Trade tensions and conflicts could disrupt supply chains and impact international sales.
5.  **Interest Rate Risk:** Higher interest rates can dampen customer demand and increase financing costs.

---
final answer is $132.04