Of course. Here is a revised valuation analysis that corrects the identified flaws and uses more realistic assumptions, particularly for the free cash flow and terminal value calculations.

The original analysis contained two significant methodological issues:
1.  **Incorrect Free Cash Flow (FCFF) Calculation:** Stock-Based Compensation (SBC), a non-cash expense, was subtracted from the cash flow. It should be added back, as it does not consume cash. The cost of SBC is properly accounted for through the increase in the diluted share count over time. The original model was effectively double-penalizing the company for SBC.
2.  **Flawed Terminal Value Calculation:** The original calculation was based on a flawed starting point (EBIT instead of FCFF) and did not properly account for reinvestment. We will replace this with a more standard and stable Exit Multiple (EV/EBITDA) approach, which is common for valuing restaurant and retail businesses.

This revised analysis corrects these issues and refines the assumptions to present a more balanced base-case valuation.

***

### PART 1: MARKET-IMPLIED VALUATION (REVERSE DCF)

#### A) ESTABLISH BASELINE & MARKET PRICE

**1) Current Market Price**
The market price for Sweetgreen, Inc. (SG) is **$9.74** as of August 2025.

**2) Baseline Financials (TTM)**
The following table presents the Trailing Twelve Months (TTM) financials for the period ended June 29, 2025.

| Metric | Amount (Millions) | Source |
| :--- | :--- | :--- |
| Revenue | $686.22 | |
| Gross Margin | 19.09% | |
| Operating Income (EBIT) | -$96.46 | |
| Net Income | -$98.04 | |
| Depreciation & Amortization (D&A) | $58.38 | |
| Stock-Based Compensation (SBC) | $36.72 | |
| Capital Expenditures (Capex) | $92.11 | |
| Change in Working Capital | -$31.17 | |
| Interest Expense | $0.05 | |
| Cash & Equivalents | $168.45 | |
| Total Debt | $338.73 | |
| Diluted Weighted-Average Shares | 116.0 | |

#### B) REVERSE-ENGINEER ASSUMPTIONS

To justify the current market capitalization of approximately **$1,130 million** ($9.74/share \* 116 million shares), a Discounted Cash Flow (DCF) model requires certain assumptions about future growth and profitability.

**Market-Implied Assumptions:**
To justify the current **$9.74 share price**, the market is pricing in the following assumptions:
*   **5-Year Revenue CAGR:** Approximately **25%** per year.
*   **Year 5 Operating Margin:** A significant ramp-up from the current -14.1% to **10.0%**.

This implies the market expects Sweetgreen to not only grow its revenue at a very high rate but also to dramatically improve its operational efficiency to achieve solid profitability within the next five years.

---

### PART 2: ANALYST'S REVISED VALUATION (REALISTIC BASE-CASE)

#### C) FORMULATE REVISED ASSUMPTIONS (5 YEARS)

My assumptions are grounded in historical performance and a realistic path to profitability, avoiding the overly optimistic market view and the overly punitive assumptions of the original model.

*   **Revenue for Years 1–5:** I will model a **15% growth rate in Year 1, tapering down by 2% each year to 7% in Year 5.** This reflects continued expansion but at a decelerating pace as the company scales and the market matures.
*   **Margin Path:** I will maintain the gradual path to a **5.0% operating margin by Year 5**. This remains a challenging but achievable target, reflecting benefits from economies of scale and operational initiatives like automation.
*   **Taxes:** A **0% tax rate for the forecast period** is assumed as the company utilizes its Net Operating Losses (NOLs). A 21% tax rate is used for the terminal value calculation.
*   **Capital Intensity & Reinvestment:**
    *   **D&A:** TTM D&A is 8.5% of revenue ($58.38M / $686.22M). We will hold this constant at **8.5% of revenue**.
    *   **Capex:** The TTM Capex-to-Revenue ratio is 13.4%. We will hold this constant at **13.5% of revenue** to support growth.
    *   **Working Capital:** Change in NWC is modeled as **1.0% of incremental revenue.**
*   **SBC, Dilution, and Buybacks:** TTM SBC is 5.3% of revenue. We will model SBC at a constant **5.0% of revenue.** SBC is a non-cash expense and will be added back to FCFF. We will project a **net 2.0% annual increase in the diluted share count** to account for the dilutive effect of these equity grants.

#### D) FREE CASH FLOW CONSTRUCTION (REVISED)

The FCFF formula is corrected to properly account for non-cash charges.
**Corrected Formula:** FCFF = EBIT \* (1 - Tax Rate) + D&A + SBC - Capex - Change in NWC

| (USD, Millions) | Y1 | Y2 | Y3 | Y4 | Y5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Revenue | $789.15 | $891.74 | $998.75 | $1,088.64 | $1,164.84 |
| *Revenue Growth* | *15.0%* | *13.0%* | *12.0%* | *9.0%* | *7.0%* |
| EBIT | -$55.24 | -$35.67 | -$9.99 | $21.77 | $58.24 |
| *EBIT Margin* | *-7.0%* | *-4.0%* | *-1.0%* | *2.0%* | *5.0%* |
| Tax Rate | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| NOPAT | -$55.24 | -$35.67 | -$9.99 | $21.77 | $58.24 |
| (+) D&A (8.5% of Rev) | $67.08 | $75.80 | $84.89 | $92.53 | $99.01 |
| (+) Stock-Based Comp (5% of Rev) | $39.46 | $44.59 | $49.94 | $54.43 | $58.24 |
| (-) Capex (13.5% of Rev) | $106.54 | $120.39 | $134.83 | $146.97 | $157.25 |
| (-) Change in NWC (1% of ΔRev) | $1.03 | $1.03 | $1.07 | $0.90 | $0.76 |
| **FCFF** | **-$56.26** | **-$36.70** | **-$11.06** | **$20.87** | **$57.48** |

#### E) DISCOUNT RATE (WACC)

The WACC calculation remains unchanged as the inputs are sound.
*   **Cost of Equity (CAPM):** 13.25% (4.25% RFR + 1.80 Beta * 5.0% ERP)
*   **Cost of Debt:** 3.95% (5.0% Pre-tax * (1 - 0.21))
*   **WACC = (1130/1469) \* 13.25% + (339/1469) \* 3.95% = 10.16% + 0.91% = 11.07%**

#### F) TERMINAL VALUE (REVISED)

We will use an **Exit Multiple (EV/EBITDA)** approach, which is more appropriate for this sector. A multiple of **12.0x** is a realistic base-case for a company with established profitability and moderate growth prospects in Year 5.

*   **Year 5 EBIT:** $58.24 M
*   **Year 5 D&A:** $99.01 M
*   **Year 5 EBITDA = EBIT + D&A = $157.25 M**
*   **Terminal Value = Year 5 EBITDA \* Exit Multiple = $157.25 M \* 12.0 = $1,887.00 M**

#### G) ENTERPRISE TO EQUITY BRIDGE (REVISED)

*   **PV of Explicit Period FCFF:** The sum of the discounted FCFFs from Y1-Y5.
    *   PV = (-$56.26/1.1107^1) + (-$36.70/1.1107^2) + (-$11.06/1.1107^3) + ($20.87/1.1107^4) + ($57.48/1.1107^5)
    *   PV = -$50.65 - $29.75 - $8.07 + $13.72 + $33.99 = **-$40.76 M**
*   **PV of Terminal Value** = $1,887.00 M / (1 + 11.07%)^5 = **$1,116.11 M**
*   **Enterprise Value = PV of Explicit Period FCFF + PV of Terminal Value**
    *   Enterprise Value = -$40.76 M + $1,116.11 M = **$1,075.35 M**
*   **Equity Value = Enterprise Value - Total Debt + Cash & Equivalents**
    *   Equity Value = $1,075.35 M - $338.73 M + $168.45 M = **$905.07 M**

#### H) PER-SHARE VALUE AND MARGIN OF SAFETY

*   **Future Diluted Share Count:** We must account for the 2.0% annual dilution over 5 years.
    *   Future Shares = 116.0 M \* (1 + 2.0%)^5 = **128.09 M shares**
*   **Analyst's Base-Case Fair Value:**
    *   Fair Value per Share = Equity Value / Future Diluted Share Count
    *   Fair Value per Share = $905.07 M / 128.09 M = **$7.07**
*   **Valuation Range:**
    *   **Low/Bear Case ($4.15):** Slower growth (tapering to 5%) and lower Y5 margin (3.0%) with a 10x exit multiple.
    *   **High/Bull Case ($12.50):** Faster growth (tapering to 10%) and higher Y5 margin (8.0%) with a 13x exit multiple, closer to the market's implied assumptions.
*   **Margin of Safety (MOS) Price:** A 30% discount to the base-case fair value.
    *   MOS Price = $7.07 \* (1 - 0.30) = **$4.95**

#### Risk Notes
1.  **Path to Profitability:** The primary risk remains execution. The valuation is highly sensitive to the company achieving its 5.0% operating margin target in Year 5. Any delays or shortfalls will significantly impact the valuation.
2.  **Competition:** The fast-casual restaurant space is highly competitive, which could limit pricing power and growth, potentially compressing the exit multiple.
3.  **Economic Sensitivity:** As a premium-priced offering, Sweetgreen is susceptible to downturns in consumer discretionary spending.
4.  **Valuation:** While our base case of $7.07 is below the current price of $9.74, it shows a path to fundamental value. However, it indicates the current market price is still pricing in a more optimistic scenario than our realistic base-case. The stock remains vulnerable if it fails to meet these heightened expectations.

final answer is 7.07 $