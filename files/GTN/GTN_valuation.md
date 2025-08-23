Of course. The provided valuation analysis is a good start, but it's incomplete and contains several issues that need to be addressed to make it a reliable assessment. Below is a critique of the original, followed by a corrected and completed valuation in the same format.

### **Critique of Original Analysis**

1.  **Incomplete Calculation:** The most immediate issue is that the Cost of Equity calculation (`10.46%`) was started but not finished, and the crucial WACC (Weighted Average Cost of Capital) calculation was missing entirely.
2.  **Missing Enterprise Value:** The analysis didn't calculate the company's current Enterprise Value (EV), which is the starting point for any DCF valuation (regular or reverse).
3.  **No Tax Rate Assumption:** A tax rate is essential for calculating Net Operating Profit After Tax (NOPAT), a cornerstone of the Unlevered Free Cash Flow (FCFF) calculation. This was omitted.
4.  **Unrealistic Terminal Value Concern:** You correctly identified that the terminal value is a critical sensitivity point. Using a method grounded in industry reality, like an Exit Multiple, is often more realistic for a mature, high-debt company in a sector facing secular challenges like broadcast media, rather than a perpetual growth model which might overstate long-term prospects.
5.  **Incomplete Objective:** A reverse DCF is excellent for understanding market expectations, but it doesn't provide a definitive "fair value." The analysis should be extended to a forward-looking DCF to establish a point of view on valuation.

---

Here is the corrected and completed analysis.

### **Gray Media, Inc. (GTN) Valuation Analysis**

*   **Company:** Gray Media, Inc. (GTN)
*   **Currency:** USD
*   **Date of Analysis:** August 23, 2025
*   **Primary Sources Reviewed:** StockAnalysis.com Financials (Income Statement, Balance Sheet, Cash Flow), Nasdaq, Fintel, YCharts, Seeking Alpha, Zacks Investment Research.

---

### **Part 1: Market-Implied Valuation (Reverse DCF)**

**A) ESTABLISH BASELINE & MARKET PRICE**

1.  **Current Market Price:** $5.76 per share (Fintel, August 20, 2025).
2.  **Baseline Financials (TTM as of June 30, 2025):**

| Metric | Value (in millions) | Source |
| :--- | :--- | :--- |
| Revenue | $3,549 | StockAnalysis |
| Gross Margin | 32.46% | StockAnalysis |
| Operating Income (EBIT) | $793 | StockAnalysis |
| Net Income | $200 | StockAnalysis |
| Depreciation & Amortization | $257 | StockAnalysis |
| Stock-Based Compensation | $22 | StockAnalysis |
| Capital Expenditures | $120 | StockAnalysis |
| Change in Working Capital | $339 | StockAnalysis |
| Interest Expense | $487 | StockAnalysis |
| Cash & Equivalents | $199 | StockAnalysis |
| Total Debt | $5,695 | StockAnalysis |
| Diluted Shares Outstanding | 97 | StockAnalysis |

3.  **Calculate Market Capitalization & Enterprise Value:**
    *   **Market Capitalization:** $5.76/share * 97 million shares = **$558.7 million**
    *   **Enterprise Value (EV):** Market Cap + Total Debt - Cash
    *   EV = $558.7 + $5,695 - $199 = **$6,054.7 million**

**B) REVERSE-ENGINEER ASSUMPTIONS**

We will solve for the free cash flow growth rate (`g`) that the market is currently pricing in, given the Enterprise Value of $6,054.7 million.

*   **WACC Calculation:**
    *   **Cost of Equity (CAPM):**
        *   Risk-Free Rate: 4.26% (10-Year U.S. Treasury, August 22, 2025).
        *   Equity Risk Premium: 5.0% (standard assumption for a mature market).
        *   Beta: 1.24 (Stocktwits).
        *   *Cost of Equity = 4.26% + 1.24 \* 5.0% = 10.46%*
    *   **Cost of Debt:**
        *   Pre-Tax Cost of Debt = Interest Expense / Total Debt = $487 / $5,695 = 8.55%.
        *   Tax Rate Assumption: 21% (U.S. Federal Corporate Rate).
        *   *After-Tax Cost of Debt = 8.55% \* (1 - 21%) = 6.75%*
    *   **Capital Structure:**
        *   Market Value of Equity (E) = $558.7M
        *   Market Value of Debt (D) = $5,695M
        *   Total Capital (V) = E + D = $6,253.7M
        *   Weight of Equity (E/V) = 8.9%
        *   Weight of Debt (D/V) = 91.1%
    *   **WACC = (E/V \* Cost of Equity) + (D/V \* After-Tax Cost of Debt)**
    *   **WACC = (8.9% \* 10.46%) + (91.1% \* 6.75%) = 0.93% + 6.15% = 7.08%**

*   **Baseline Free Cash Flow to Firm (FCFF):**
    *   NOPAT = EBIT \* (1 - Tax Rate) = $793M \* (1 - 0.21) = $626.5M
    *   **FCFF** = NOPAT + D&A - CapEx - Change in WC
    *   **FCFF** = $626.5M + $257M - $120M - $339M = **$424.5M**

*   **Terminal Value Assumption:**
    *   We will use an **Exit Multiple Method**, which is more realistic for a mature, asset-heavy industry like broadcasting. A conservative but fair multiple for this sector is **6.0x EV/EBITDA**.
    *   Baseline EBITDA = EBIT + D&A = $793M + $257M = $1,050M.

*   **Solving for Implied Growth Rate:**
    By setting up a 5-year DCF model where the calculated EV equals the market EV of $6,054.7M, we solve for the growth rate (`g`).

    *   The calculation shows that a perpetual growth rate of **-0.53%** in FCFF is required to arrive at the current Enterprise Value.

    **Conclusion for Part 1:** The current market price of $5.76 implies that investors expect Gray Media's free cash flow to decline by approximately 0.5% per year over the long term. This reflects the secular headwinds of cord-cutting and the shift of advertising to digital platforms, balanced by the company's strong position in local markets and political ad revenue.

---

### **Part 2: Intrinsic Valuation (Forward DCF)**

Now, we conduct our own DCF analysis to determine an intrinsic value for GTN, using realistic, forward-looking assumptions.

**A) FORECAST ASSUMPTIONS**

1.  **FCFF Growth Rate (Years 1-5):** We will assume **0% growth**. This is a neutral assumption, balancing cyclical political ad spending (a positive) with secular industry decline (a negative). It assumes management can maintain current cash flow levels but not grow them significantly.
2.  **Discount Rate (WACC):** We will use the **7.08%** calculated above.
3.  **Terminal Value:** We will use a **6.0x EV/EBITDA** exit multiple on the Year 5 projected EBITDA. Since we assume 0% growth, Year 5 EBITDA remains $1,050M.

**B) DCF CALCULATION**

1.  **Projected FCFF (Years 1-5):** With 0% growth, FCFF is a constant **$424.5 million** per year.
2.  **Present Value of Forecasted FCFF:**

| Year | FCFF (in millions) | Discount Factor @ 7.08% | PV of FCFF (in millions) |
| :--- | :--- | :--- | :--- |
| 1 | $424.5 | 0.9339 | $396.4 |
| 2 | $424.5 | 0.8721 | $370.2 |
| 3 | $424.5 | 0.8144 | $345.7 |
| 4 | $424.5 | 0.7606 | $322.9 |
| 5 | $424.5 | 0.7103 | $301.5 |
| **Sum** | | | **$1,736.7** |

3.  **Calculate Terminal Value:**
    *   Year 5 EBITDA = $1,050M
    *   Terminal Value = Year 5 EBITDA \* Exit Multiple = $1,050M \* 6.0 = **$6,300 million**

4.  **Present Value of Terminal Value:**
    *   PV of TV = $6,300M / (1 + 7.08%)^5 = $6,300M \* 0.7103 = **$4,474.9 million**

5.  **Calculate Enterprise Value:**
    *   EV = PV of Forecasted FCFF + PV of Terminal Value
    *   EV = $1,736.7M + $4,474.9M = **$6,211.6 million**

**C) DERIVE INTRINSIC SHARE PRICE**

1.  **Calculate Intrinsic Equity Value:**
    *   Equity Value = Enterprise Value - Total Debt + Cash
    *   Equity Value = $6,211.6M - $5,695M + $199M = **$715.6 million**

2.  **Calculate Intrinsic Value Per Share:**
    *   Value per Share = Equity Value / Diluted Shares Outstanding
    *   Value per Share = $715.6M / 97 million shares = **$7.38**

### **Conclusion & Final Answer**

The reverse DCF shows the market is pricing in a slight annual decline (-0.53%) in Gray Media's free cash flow. Our own forward-looking DCF, based on a more neutral assumption of 0% growth and a realistic 6.0x exit multiple, suggests an intrinsic value of $7.38 per share. This indicates a potential undervaluation of approximately 28% compared to the current market price of $5.76. The investment thesis hinges on the company's ability to maintain its current cash flow generation in the face of industry headwinds, with its high debt load remaining the most significant risk factor.

final answer is 7.38 $