### **Intrinsic Value Analysis: Block, Inc. (SQ)**

*   **Company:** Block, Inc. (SQ)
*   **Currency:** U.S. Dollars (USD)
*   **Date of Analysis:** August 21, 2025
*   **Primary Sources Reviewed:** TTM Financial Data from Stock Analysis, Q2 2025 Earnings Call Information, and U.S. Treasury Data.

---

### **A) Baseline Financials (TTM)**

The following table summarizes Block, Inc.'s trailing twelve months (TTM) financial data. All figures are in millions of USD.

| Metric | Value (Millions USD) | Source & Date |
| :--- | :--- | :--- |
| Revenue | $23,835 | Stock Analysis, TTM data as of Mar 31, 2025 |
| Gross Profit | $9,449 | Stock Analysis, TTM data as of Jun 30, 2025 |
| Operating Income (EBIT) | $1,285 | Stock Analysis, TTM data as of Jun 30, 2025 |
| Net Income | $2,615 | Stock Analysis, TTM data as of Mar 31, 2025 |
| Depreciation & Amortization (D&A) | $302 | Stock Analysis, TTM data as of Mar 31, 2025 |
| Stock-Based Compensation (SBC) | $1,277 | Stock Analysis, TTM data as of Mar 31, 2025 |
| Capital Expenditures (Capex) | $154 | Stock Analysis, TTM data as of Mar 31, 2025 |
| Change in Working Capital | $881 | Stock Analysis, TTM data as of Mar 31, 2025 |
| Interest Expense | $273 | Stock Analysis, TTM data as of Jun 30, 2025 |
| Cash & Equivalents | $6,400 | Seeking Alpha, Q2 2025 data |
| Total Debt | $5,100 | Seeking Alpha, Q2 2025 data |
| Diluted Weighted-Average Shares | 636 | AlphaQuery, FY 2024 data |

---

### **B) Management Guidance Extraction**

Verbatim extracts from recent management commentary:

*   **Full-Year 2025 Gross Profit:** Management raised its full-year 2025 guidance, and now "expects gross profit for 2025 to reach $10.17 billion." (CNBC, August 7, 2025)
*   **Third-Quarter 2025 Outlook:** "Block expects its gross profit to increase by 16% in the third quarter, reaching $2.6 billion." (CNBC, August 7, 2025)

---

### **C) Forecast Horizon and Base-Case Assumptions (5 Years)**

**1. Revenue Forecast:**
*   **Rationale:** Management provides gross profit guidance, which is a better indicator of underlying business performance than revenue, especially given the volatility of Bitcoin pass-through revenue. I will forecast gross profit and derive revenue based on a stable gross margin.
*   **Year 1 (2025):** The forecast starts with management's explicit guidance of **$10.17 billion in gross profit**.
*   **Years 2-5:** I project a declining growth rate for gross profit, starting from a rate slightly below the Q3 2025 guidance and decelerating. This reflects the law of large numbers and increasing market maturity.
    *   Year 2: 14%
    *   Year 3: 12%
    *   Year 4: 10%
    *   Year 5: 8%

**2. Margin Path:**
*   **Operating Margin (EBIT/Gross Profit):** The TTM EBIT of $1,285M relative to TTM Gross Profit of $9,449M yields an EBIT margin on gross profit of 13.6%. Management commentary noted achieving a 22% *adjusted* operating income margin in Q2 2025. Given the focus on profitability, I assume a gradual expansion of the GAAP EBIT margin from 14.0% in Year 1 to 18.0% in Year 5 as the business scales.

**3. Taxes:**
*   **Effective Tax Rate:** Historical tax rates have been volatile and negative. For a profitable U.S. company, a normalized statutory rate is more appropriate for a long-term forecast. I assume a blended federal and state **tax rate of 25%** for all forecast years.

**4. Capital Intensity:**
*   **Capex:** TTM Capex was 1.6% of TTM Gross Profit ($154M / $9,449M). I will hold **Capex steady at 1.6% of Gross Profit** through the forecast period.
*   **Working Capital:** TTM Change in NWC was 9.3% of TTM Gross Profit ($881M / $9,449M). I will model **Change in Working Capital as 9.0% of the *incremental* Gross Profit** each year.

---

### **D) Free Cash Flow Construction**

Free Cash Flow to the Firm (FCFF) is used because it represents cash flow available to all capital providers.

**Formula:**
`FCFF = EBIT * (1 - Tax Rate) + D&A - Stock-Based Compensation (SBC) - Capex - Change in Working Capital`

**FCFF Forecast (in Millions USD):**

| Year | 2025 (Y1) | 2026 (Y2) | 2027 (Y3) | 2028 (Y4) | 2029 (Y5) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Gross Profit | $10,170 | $11,594 | $13,000 | $14,300 | $15,444 |
| *Growth Rate* | *7.6%* | *14.0%* | *12.1%* | *10.0%* | *8.0%* |
| **EBIT** | **$1,424** | **$1,739** | **$2,080** | **$2,431** | **$2,780** |
| *EBIT Margin (% of GP)* | *14.0%* | *15.0%* | *16.0%* | *17.0%* | *18.0%* |
| Tax on EBIT (25%) | ($356) | ($435) | ($520) | ($608) | ($695) |
| **NOPAT** | **$1,068** | **$1,304** | **$1,560** | **$1,823** | **$2,085** |
| \+ D&A (assumed 3% of GP) | $305 | $348 | $390 | $429 | $463 |
| \- Stock-Based Comp (SBC) | ($1,277) | ($1,277) | ($1,277) | ($1,277) | ($1,277) |
| \- Capex (1.6% of GP) | ($163) | ($186) | ($208) | ($229) | ($247) |
| \- Chg. in NWC (9% of Incr. GP) | ($65) | ($128) | ($127) | ($117) | ($103) |
| **Free Cash Flow to Firm (FCFF)** | **($132)** | **$61** | **$338** | **$630** | **$921** |

*(Note: SBC is held flat as a conservative assumption, representing a declining % of gross profit over time.)*

---

### **E) Discount Rate (WACC)**

**1. Cost of Equity (CAPM):**
*   **Formula:** `Cost of Equity = Risk-Free Rate + Beta * Equity Risk Premium`
*   **Risk-Free Rate:** 4.29% (10-Year U.S. Treasury Yield, August 21, 2025)
*   **Equity Risk Premium:** 5.0% (standard assumption for a mature market).
*   **Beta:** 2.71 (5Y monthly beta from Stock Analysis). This high beta reflects the stock's historical volatility relative to the market, suitable for a high-growth tech company.
*   **Calculation:** `4.29% + 2.71 * 5.0% = 17.84%`

**2. Cost of Debt:**
*   **Formula:** `Cost of Debt = Interest Expense / Total Debt`
*   **Calculation:** `$273M / $5,100M = 5.35%`

**3. WACC Calculation:**
*   **Formula:** `WACC = (E / (E+D)) * Ke + (D / (E+D)) * Kd * (1 - Tax Rate)`
*   **Market Cap (E):** Assuming a recent share price of ~$77, `77 * 636M shares = ~$49,000M`
*   **Debt (D):** $5,100M
*   **Equity Weight:** `$49,000 / ($49,000 + $5,100) = 90.6%`
*   **Debt Weight:** `$5,100 / ($49,000 + $5,100) = 9.4%`
*   **WACC:** `(0.906 * 17.84%) + (0.094 * 5.35% * (1 - 0.25)) = 16.16% + 0.38% = **16.54%**`

---

### **F) Terminal Value**

**1. Gordon Growth Method:**
*   **Formula:** `Terminal Value = (FCFF_Y5 * (1 + g)) / (WACC - g)`
*   **Terminal Growth Rate (g):** 2.5%. This is a realistic long-term growth rate, in line with long-run inflation expectations.
*   **Calculation:** `($921M * (1 + 0.025)) / (0.1654 - 0.025) = $944M / 0.1404 = **$6,724M**`

**2. Exit Multiple Cross-Check:**
*   **EBITDA in Year 5:** `EBIT_Y5 + D&A_Y5 = $2,780M + $463M = $3,243M`
*   **Assumption:** A conservative 10x EV/EBITDA multiple is assumed, given historical volatility.
*   **Terminal Value (Multiple):** `$3,243M * 10 = **$32,430M**`

There is a significant discrepancy. The high WACC, driven by a very high beta, heavily penalizes the Gordon Growth model. The Exit Multiple method, while subject to market sentiment, may be more realistic here. However, per the instructions, I will choose the lower value. This is a very conservative stance.

---

### **G) Enterprise to Equity Bridge**

**1. Enterprise Value:**
*   PV of Explicit FCFF: `(-$132/(1.1654)^1) + ($61/(1.1654)^2) + ($338/(1.1654)^3) + ($630/(1.1654)^4) + ($921/(1.1654)^5) = -$113 + $45 + $215 + $340 + $429 = $916M`
*   PV of Terminal Value: `$6,724M / (1.1654)^5 = $3,131M`
*   **Total Enterprise Value:** `$916M + $3,131M = **$4,047M**`

**2. Equity Value:**
*   **Formula:** `Equity Value = Enterprise Value - Total Debt + Cash & Equivalents`
*   **Calculation:** `$4,047M - $5,100M + $6,400M = **$5,347M**`

---

### **H) Per-Share Value and Margin of Safety**

**1. Base-Case Fair Value:**
*   **Formula:** `Fair Value = Equity Value / Diluted Shares Outstanding`
*   **Calculation:** `$5,347M / 636M = **$8.41 per share**`

**2. Valuation Range:**
*   **Base Case:** **$8.41**. This result is heavily impacted by the high beta and resulting WACC, leading to a very low valuation.
*   **Low/Bear Case (~$4):** Lower gross profit growth (e.g., 5-10% annually) and no margin expansion would result in even lower FCFF and a valuation below $5.
*   **High/Bull Case (~$25):** If a lower beta (e.g., 2.0) were used, the WACC would drop to ~14.3%. Further, using the higher exit multiple terminal value would yield a valuation in the $20-30 range, demonstrating the extreme sensitivity to discount rate and terminal assumptions.

**3. Margin of Safety (MOS) Price:**
*   A 30% margin of safety is applied to the conservative base case.
*   **MOS Price:** `$8.41 * (1 - 0.30) = **$5.89**`

---

### **Risk Notes**

1.  **Macroeconomic Sensitivity:** As a payment processor and financial services provider, Block's transaction volumes and growth are highly sensitive to consumer spending and the overall health of the economy.
2.  **Competitive Pressure:** The fintech and payments space is intensely competitive, with pressure from traditional banks, other pure-play fintech companies (e.g., PayPal), and large tech companies entering the space.
3.  **Regulatory Scrutiny:** The company operates in a complex regulatory environment, particularly concerning cryptocurrencies and financial services, which could lead to increased compliance costs or restrictions.
4.  **Valuation Sensitivity:** The valuation is extremely sensitive to the discount rate (WACC), which is driven by a high beta. A small change in the beta or risk-free rate assumption leads to a large change in the intrinsic value estimate.

final answer is XYZ $8.41