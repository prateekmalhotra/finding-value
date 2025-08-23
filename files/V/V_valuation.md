Of course. Below is a comprehensive analysis and corrected two-stage intrinsic valuation for Visa Inc. (V).

First, let's address the issues with the implied, incomplete model and the common pitfalls in such valuations that this corrected version will fix.

**Critique of Implicit Assumptions & Common Flaws:**

1.  **Incomplete Model:** The provided text was only the initial setup. A full valuation requires calculations for the cost of capital, free cash flow projections, a terminal value, and the final intrinsic value calculation. This corrected version builds out all necessary components.
2.  **Unrealistic Terminal Value:** You correctly identified this as a critical issue. Valuations often use an overly conservative terminal growth rate (e.g., 2.0-2.5%) that may not reflect the long-term prospects of a global, wide-moat leader like Visa. A company that grows with global commerce and digital payments can realistically grow faster than generic long-term inflation. We will correct this by using a more realistic perpetual growth rate.
3.  **Lack of Connection Between Growth and Reinvestment:** A robust model must explicitly link revenue growth to the capital required to achieve it (reinvestment). Simply projecting growth without accounting for the necessary investment in capital expenditures and working capital is a major flaw. This model will use a Sales-to-Capital ratio to enforce this discipline.
4.  **Static, Unrealistic Growth Rates:** A common mistake is to use a single high growth rate for the entire first stage. It is more realistic to model a declining growth rate as the company matures and the law of large numbers takes effect.

This revised valuation addresses these points to create a more realistic and fundamentally sound model.

---

Here is a two-stage intrinsic valuation for Visa Inc. (V).

**Company:** Visa Inc. (V)
**Currency:** U.S. Dollars (USD)
**Date of Analysis:** August 23, 2025
**Primary Sources Reviewed:**
*   Visa Inc. Q3 2025 10-Q, filed July 29, 2025
*   StockAnalysis.com financial data (queried August 23, 2025)
*   Publicly available market data for stock price, beta, and risk-free rate (queried August 23, 2025)

---

### **Part 1: Baseline Financials & Key Assumptions**

This section establishes the starting financial data and the core assumptions for the valuation model.

**A) ESTABLISH BASELINE & MARKET DATA**

1.  **Current Market Price**: **$350.04** (at close, August 22, 2025)
2.  **Shares Outstanding**: **2,015 million**
3.  **Market Capitalization**: $350.04 * 2,015m = **$705,331 million**

**B) BASELINE FINANCIALS (TTM)**: For the Trailing Twelve Months (TTM) ended June 30, 2025.

| Metric | Amount (in millions USD) | Source & Rationale |
| :--- | :--- | :--- |
| Revenue | $38,893 | StockAnalysis.com, Income Statement, TTM |
| Operating Income (EBIT) | $26,059 | StockAnalysis.com, Income Statement, TTM |
| **Operating Margin** | **67.0%** | Calculated (EBIT / Revenue) |
| Effective Tax Rate | 21.0% | Assumed based on corporate tax rates and company history |
| **NOPAT (Net Operating Profit After Tax)** | **$20,587** | Calculated ($26,059 * (1 - 0.21)) |
| Cash & Equivalents | $22,450 | StockAnalysis.com, Balance Sheet |
| Total Debt | $20,680 | StockAnalysis.com, Balance Sheet |

**C) REINVESTMENT & GROWTH ASSUMPTIONS**

*   **Sales-to-Capital Ratio**: **2.5**. This is a key assumption reflecting Visa's capital-light business model. It implies that for every $2.50 in new revenue generated, Visa must invest $1.00 in net capital (CapEx net of D&A + Investment in NWC). This enforces the link between growth and reinvestment.
*   **Stage 1 Growth (Years 1-5)**: High growth, starting at **12.0%** and declining linearly towards the 5-year average. This reflects continued expansion in digital payments and new flows.
*   **Stage 2 Growth (Years 6-10)**: Moderate growth, declining from the 5-year rate towards the terminal rate of **3.5%**. This reflects maturation as the company grows larger.
*   **Terminal Growth Rate (g)**: **3.5%**. This rate is chosen as a realistic long-term growth expectation for a dominant global company. It is above long-run inflation (~2.5%) but below expected long-run global nominal GDP growth (~4.5%), reflecting Visa's ability to outpace the general economy due to the secular shift to digital payments.

---

### **Part 2: Cost of Capital (WACC) Calculation**

The WACC is the discount rate used to find the present value of future free cash flows.

| Component | Calculation / Assumption | Result |
| :--- | :--- | :--- |
| **Cost of Equity (Ke)** | | **9.25%** |
| Risk-Free Rate (Rf) | 10-Year U.S. Treasury Yield | 4.50% |
| Equity Risk Premium (ERP) | Market-wide excess return expectation | 5.00% |
| Beta (β) | Visa's market sensitivity (levered) | 0.95 |
| *Calculation* | *Rf + β \* ERP* | *4.50% + 0.95 \* 5.00%* |
| **Cost of Debt (Kd)** | | **4.35%** |
| Pre-Tax Cost of Debt | Based on Visa's AA- credit rating | 5.50% |
| Tax Rate | Assumed effective tax rate | 21.0% |
| *Calculation (After-Tax)* | *Pre-Tax Cost \* (1 - Tax Rate)* | *5.50% \* (1 - 0.21)* |
| **WACC** | | **9.11%** |
| Equity Weight (E/V) | Market Cap / (Market Cap + Debt) | 97.2% |
| Debt Weight (D/V) | Debt / (Market Cap + Debt) | 2.8% |
| *Calculation* | *(E/V \* Ke) + (D/V \* Kd)* | *(97.2% \* 9.25%) + (2.8% \* 4.35%)* |

---

### **Part 3: Free Cash Flow to Firm (FCFF) Projection**

FCFF is projected for the 10-year high-growth period (Stage 1 & 2). All figures are in millions of USD.

| Year | Revenue Growth | Revenue | EBIT (67.0% Margin) | NOPAT (after 21% tax) | Reinvestment | **FCFF** | PV of FCFF (@9.11%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Base** | | **$38,893** | **$26,059** | **$20,587** | | | |
| 1 | 12.00% | $43,560 | $29,185 | $23,056 | $1,867 | **$21,190** | $19,421 |
| 2 | 11.25% | $48,465 | $32,472 | $25,653 | $1,962 | **$23,691** | $19,890 |
| 3 | 10.50% | $53,554 | $35,881 | $28,346 | $2,036 | **$26,311** | $20,248 |
| 4 | 9.75% | $58,776 | $39,380 | $31,110 | $2,089 | **$29,021** | $20,490 |
| 5 | 9.00% | $64,066 | $42,924 | $33,910 | $2,116 | **$31,794** | $20,620 |
| 6 | 7.90% | $69,127 | $46,315 | $36,589 | $2,024 | **$34,565** | $20,551 |
| 7 | 6.80% | $73,828 | $49,465 | $39,077 | $1,880 | **$37,197** | $20,299 |
| 8 | 5.70% | $78,036 | $52,284 | $41,305 | $1,683 | **$39,622** | $19,796 |
| 9 | 4.60% | $81,626 | $54,689 | $43,205 | $1,436 | **$41,769** | $19,150 |
| 10 | 3.50% | $84,483 | $56,603 | $44,717 | $1,143 | **$43,574** | $18,272 |
| | | | | | | | **$198,736** |

**Sum of Present Value of FCFF (Years 1-10): $198,736 million**

---

### **Part 4: Terminal Value Calculation**

The Terminal Value represents the value of all cash flows beyond Year 10, using the Gordon Growth Model.

1.  **FCFF in Year 11 (Start of Terminal Period)**:
    *   FCFF(10) * (1 + g) = $43,574m * (1 + 0.035) = **$45,100 million**

2.  **Terminal Value at end of Year 10**:
    *   TV = FCFF(11) / (WACC - g)
    *   TV = $45,100m / (9.11% - 3.50%) = $45,100m / 5.61% = **$803,912 million**

3.  **Present Value of Terminal Value**:
    *   PV(TV) = TV / (1 + WACC)^10
    *   PV(TV) = $803,912m / (1 + 0.0911)^10 = **$337,419 million**

---

### **Part 5: Intrinsic Value Calculation**

This section combines the projected cash flows and terminal value to arrive at the intrinsic value per share.

| Step | Calculation | Amount (in millions USD) |
| :--- | :--- | :--- |
| 1 | Sum of PV of FCFF (Years 1-10) | $198,736 |
| 2 | Present Value of Terminal Value | $337,419 |
| **3** | **Enterprise Value (EV)** (Step 1 + Step 2) | **$536,155** |
| 4 | Add: Cash & Equivalents | + $22,450 |
| 5 | Subtract: Total Debt | - $20,680 |
| **6** | **Intrinsic Equity Value** | **$537,925** |
| 7 | Shares Outstanding (millions) | 2,015 |
| **8** | **Intrinsic Value per Share** (Equity Value / Shares) | **$266.96** |

---

### **Part 6: Conclusion**

Based on this two-stage Discounted Cash Flow (DCF) analysis, the intrinsic value of Visa Inc. is estimated to be **$266.96 per share**.

Compared to the market price of **$350.04**, this model suggests that the stock is currently overvalued. The market price appears to be pricing in significantly higher long-term growth, a lower discount rate, or a combination of both, than what is assumed in this fundamental valuation. The key drivers of this valuation are the high-single-digit growth rates in the medium term and the terminal growth rate of 3.5%, which is realistic but may be lower than the market's more optimistic expectations.

final answer is $266.96