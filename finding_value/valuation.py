import os
import argparse
import google.generativeai as genai
from dotenv import load_dotenv
from google import genai
from google.genai import types

def analyze_stock_valuation(stock_name: str, company_name: str) -> dict:
	"""
	Analyzes a stock by sending a valuation prompt to the Gemini API.

	This function takes a stock ticker symbol, formats a specific prompt to
	perform a back-of-the-envelope valuation, sends it to the Gemini model,
	and then parses the response to separate the full analysis from the
	conclusive final price.

	Args:
		stock_name: The ticker symbol of the stock to be analyzed (e.g., "AAPL").

	Returns:
		A dictionary containing two keys:
		- 'reasoning': The full, detailed response from the model.
		- 'final_answer': The extracted value string (e.g., "123.45 $") from the
		last line of the model's output. Returns None if it cannot be extracted.
	"""
	if not stock_name or not isinstance(stock_name, str):
		raise ValueError("A valid stock name must be provided as a string.")

	# Load environment variables from .env file
	# This is done once in main, but kept here for potential standalone use
	if not os.getenv("GOOGLE_API_KEY"):
		load_dotenv()

	prompt = f"""
ROLE: Conservative valuation analyst performing a back-of-the-envelope intrinsic valuation using only primary sources and management commentary.

COMPANY: {company_name} ({stock_name.upper()})

OBJECTIVE
Estimate a conservative intrinsic value per share using a transparent, step-by-step approach. The model must be simple enough to audit but rigorous in sourcing. Prefer understatement over optimism.

DATA SOURCES (IN ORDER OF PRECEDENCE)
1) Latest SEC filings (10-K/20-F, 10-Q, 8-K), annual report, and investor presentation.
2) Most recent earnings call transcript and prepared remarks (management guidance only).
3) Company IR releases and fact sheets.
4) Reputable regulatory filings (e.g., prospectuses), credit agreements, and notes to financial statements.
5) Good resources like:
	https://stockanalysis.com/stocks/{stock_name}/
	https://stockanalysis.com/stocks/{stock_name}/financials/?p=quarterly
	https://stockanalysis.com/stocks/{stock_name}/financials/balance-sheet/?p=quarterly
	https://stockanalysis.com/stocks/{stock_name}/financials/cash-flow-statement/?p=quarterly
	https://discountingcashflows.com/company/{stock_name}/transcripts/

IGNORE: sell-side/consensus/third-party estimates, blogs, social media. If a number cannot be corroborated in primary materials, do not use it.

IF SOME RESOURCE IS MISSING OR BROWSE TOOL ISN'T WORKING, DO NOT PANIC - USE OTHER REMAINING RESOURCES. BUT KEEP GOING DON'T STOP UNTIL YOU ARE CONFIDENT IN THE FINAL ANSWER.

CITATIONS
- Every number you use must be followed by a parenthetical citation with a working link and an absolute date, e.g., (10-Q, May 7, 2025, p. 12).
- If you infer a number (e.g., run-rate, TTM), show the math and cite the source of each input.
- Do not cite undated or ambiguous sources.

UNITS, CURRENCY, DATES
- State reporting currency clearly (e.g., USD). Keep all figures in the same currency.
- Use millions unless otherwise noted. Always include units.
- Use absolute dates (e.g., “for the quarter ended June 30, 2025”).

VALUATION FRAMEWORK (CONSERVATIVE)
Perform all of the following and show each step, assumption, and formula:
A) BASELINE FINANCIALS (TTM or LTM)
   1) Revenue, gross margin, operating income (or EBIT), net income, depreciation & amortization, stock-based compensation, capex, change in working capital, interest expense, cash & equivalents, total debt (incl. current), lease liabilities (if material), minority interest, and diluted weighted-average shares. Show TTM where possible; otherwise use most recent annual and latest interim to bridge. Provide a small table with each line and a citation for each figure.

B) MANAGEMENT GUIDANCE EXTRACTION
   2) Extract verbatim key elements of current guidance: revenue growth, margin targets, capex outlook, cash taxes, working capital trends, and any segment guidance. Quote briefly and cite the source and date. If no guidance is given, say so and proceed conservatively.

C) FORECAST HORIZON AND CONSERVATIVE ASSUMPTIONS (5 YEARS)
   3) Forecast revenue for Years 1–5:
      - Start from the lower end of management guidance or the most recent trailing run-rate, whichever is lower.
      - If guidance is a range, use the low end.
      - If no guidance, assume growth = min(last 3-year CAGR, inflation proxy) and justify.
   4) Margin path:
      - Use the lower of: (a) management margin guidance low end; (b) average of last 3 years; (c) last twelve months.
      - For operating margin expansion, require a concrete, cited driver (pricing, mix, cost-out). If not found, keep margins flat or compress modestly.
   5) Taxes:
      - Use the higher of the recent effective tax rate and the statutory rate disclosed. Justify choice and cite.
   6) Capital intensity:
      - Capex: use the higher of (a) management capex guide, (b) last 3-year average as % of revenue, (c) LTM. Cite.
      - Working capital: model as % of incremental revenue using the more conservative of recent history or guidance. If volatile, use a positive cash usage (i.e., working capital consumes cash).
      - D&A: fade toward recent level unless explicit capacity additions justify growth. Cite.
      - Leases: if material, treat lease repayments akin to debt service; reflect in FCFF or adjust to FCFE consistently.
   7) SBC and dilution:
      - Treat SBC as a real economic cost. Either subtract SBC from FCFF or model future diluted shares using the higher of: (a) LTM diluted shares; (b) basic shares plus in-the-money options/RSUs from the filing. Explain approach and cite.

D) FREE CASH FLOW CONSTRUCTION
   8) Define and compute FCFF each year (operating income * (1 - tax rate) + D&A - capex - change in working capital). Show the exact formula and each input with references.
   9) Cross-check FCFE if helpful (FCFF - after-tax interest + net borrowing - lease principal - minority distributions). State which metric you use for valuation and why.

E) DISCOUNT RATE (CONSERVATIVE)
  10) Cost of equity via CAPM:
      - Risk-free rate: use latest sovereign yield matching currency/tenor (e.g., 10-year U.S. Treasury). Cite date and source.
      - Equity risk premium: use a conservative range (e.g., 5.5%–6.5%); pick the higher bound and justify.
      - Beta: if not available from filings, infer a conservative beta of at least 1.0 unless a regulated/contracted profile is clearly evidenced. Explain rationale.
  11) Cost of debt: infer from interest expense / average debt or disclosed rates; add a conservative spread if necessary. Cite.
  12) WACC: compute using conservative weights (treat off-balance sheet leases as debt where material). Show formula and numbers.

F) TERMINAL VALUE (MODEST)
  13) Use the Gordon Growth method with terminal growth g capped at the lower of long-run inflation and real GDP for the reporting region; do not exceed the current risk-free rate minus 1%. Justify and cite macro source.
  14) As a cross-check, compute an exit multiple on Year 5 EBIT or EBITDA using a multiple below the 10-year sector median. Cite the sector median source and haircut rationale.

G) ENTERPRISE TO EQUITY BRIDGE
  15) Add: present value of explicit period FCFF + present value of terminal value = Enterprise Value.
  16) Subtract: net debt (debt + lease liabilities - cash and short-term investments), minority interest; add: non-core investments if clearly marked and liquid (haircut 25% by default unless market value is observable). Cite each figure.
  17) Make sure to account for **excess cash** or **excess debt** after everything is included in the bridge.

H) PER-SHARE VALUE AND MARGIN OF SAFETY
  18) Divide by a conservative diluted share count (use the higher figure as per SBC treatment).
  19) Report a valuation range:
      - Low (use lower revenue, flat margins, higher capex/WACC).
      - Base (guided low-end inputs).
      - High (only if explicitly justified by guidance; still conservative).
  20) Compute an explicit Margin of Safety (MOS) price at 25–30% below the LOW estimate.
  21) If you reference the current share price, cite an official exchange or the company IR page with timestamp; otherwise, omit.

DECISION RULES & CONSERVATISM
- When in doubt, choose the more conservative input.
- Do not count cost savings or synergies without specific, dated management disclosure.
- Do not assume buybacks beyond what’s already executed.
- Do not assume multiple expansion; if anything, apply a haircut.
- If any critical input is missing, disclose the gap and proceed with a clearly conservative proxy (and label it).

OUTPUT FORMAT (MARKDOWN)
1) Header: Company, ticker, currency, date of analysis, primary sources reviewed (bullet list with links and dates).
2) Baseline Financials (TTM): a compact table with each line item, value, unit, and citation.
3) Guidance Extracts: short quoted bullets with citations.
4) Forecast & Assumptions: list each assumption with a one-sentence rationale and a citation for the source input.
5) Free Cash Flow Build: show formulas year by year (Y1–Y5) and a mini table of FCFF.
6) Discount Rate: show risk-free, ERP, beta, cost of equity, cost of debt, WACC with formulas and citations.
7) Terminal Value: show method, inputs, and calculation, plus exit multiple cross-check and rationale.
8) Enterprise to Equity Bridge: bullet the adjustments with numbers and citations.
9) Per-Share Valuation: show Low/Base/High and the MOS price. If current price included, cite it and compute % upside/downside.
10) One-paragraph Risk Notes: list 3–5 key downside risks tied to your assumptions.
11) Final line must be: "final answer is XYZ $" where XYZ is the conservative per-share intrinsic value you estimate.

CHECKLIST BEFORE YOU SUBMIT
- Every numeric input has a citation with a link and an absolute date.
- All formulas are written out and every step is shown.
- Currency and units are consistent.
- Terminal growth is modest and justified.
- WACC components are transparent and conservative.
- SBC is treated as a real cost or dilution is explicitly modeled.
- No analyst/consensus numbers were used.
- Excess cash or excess debt adjustments are clearly accounted for.
- Remember that the last line of your output should be - final answer is XYZ $ where XYZ is the conservative per-share intrinsic value you estimate

Now begin the analysis for {company_name} ({stock_name.upper()}) following the exact structure above. Be explicit, concise, and conservative.
"""

	try:
		client = genai.Client()
		grounding_tool = types.Tool(
			google_search=types.GoogleSearch
		)

		url_context_tool = types.Tool(
			url_context = types.UrlContext
		)


		config = types.GenerateContentConfig(
			tools=[grounding_tool, url_context_tool],
			thinking_config=types.ThinkingConfig(thinking_budget=-1)
		)

		response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt, config=config)
		full_response_text = response.text

		analysis_result = {
			"reasoning": full_response_text,
			"final_answer": None
		}

		lines = full_response_text.strip().split('\n')
		if lines:
			last_line = lines[-1].lower()
			phrase_to_find = "final answer is"
			if phrase_to_find in last_line:
				try:
					start_index = last_line.find(phrase_to_find) + len(phrase_to_find)
					final_value_str = last_line[start_index:].strip()
					analysis_result["final_answer"] = final_value_str
				except Exception:
					print(f"Warning: Could not parse the final answer from the last line: '{lines[-1]}'")

		return analysis_result

	except Exception as e:
		print(f"An error occurred while communicating with the Gemini API: {e}")
		return {
			"reasoning": "NO RESPONSE",
			"final_answer": None
		}

def analyze_qualitative_aspects(stock_name: str, company_name: str) -> dict:
	"""
    Analyzes the qualitative aspects of a business, focusing on its economic moat.
    """
	if not stock_name or not isinstance(stock_name, str):
		raise ValueError("A valid stock name must be provided as a string.")

	# Load environment variables from .env file
	# This is done once in main, but kept here for potential standalone use
	if not os.getenv("GOOGLE_API_KEY"):
		load_dotenv()
		
	prompt = f"""
ROLE: Senior competitive strategy & equity analyst tasked with rigorously assessing the COMPANY’S SUSTAINABLE COMPETITIVE ADVANTAGE ("moat").

COMPANY: {company_name} ({stock_name.upper()})
OBJECTIVE
Produce a disciplined, evidence-first moat assessment for {company_name} ({stock_name.upper()}) that results in a single, defensible moat score on a 0–5 scale. Be conservative, transparent, and explicit about every step, data source, and assumption. The final output must end with the exact line:

    moat rating is X / 5

DATA SOURCES (PRIORITIZE IN THIS ORDER)
1) Latest SEC filings (10-K/20-F, 10-Q, 8-K), annual report, and investor presentation.  
2) Latest earnings call transcript and management prepared remarks (use only management-sourced claims for forward-looking statements).  
3) Company investor-relations releases, statutory filings in primary listing jurisdiction, regulatory documents, credit agreements, and audited financial statements.  
4) High-quality third-party sources (e.g., industry reports, government statistics) only to contextualize; primary evidence must be used for company-specific claims.

EVIDENCE STANDARD
- **Every factual claim must include a dated citation** (link + document title + absolute date). E.g., (10-K, Feb 25, 2025).  
- **No hallucinations.** If a claim cannot be supported by documented evidence, explicitly label it as an inference, show the inference steps, and use conservative assumptions.  
- Use absolute dates and currencies. All monetary figures must specify units (e.g., "USD, millions").

TIME HORIZON
- Assess durability over a 5–15 year horizon. Provide an explicit **estimated moat duration** in years and justify it with evidence.

ANALYTIC FRAMEWORK — DIMENSIONS TO EVALUATE (SCORE EACH 0–5)
Score each dimension on a 0–5 integer scale, where 0 = no advantage / actively losing ground; 5 = extremely durable, demonstrable advantage likely to persist for >15 years. For each dimension you must:
- Give 2–4 sentences of reasoning.
- Provide 1–3 dated citations that directly support the reasoning.
- State the numeric score for that dimension.

Dimensions (evaluate all; these are exhaustive but adapt evidence to industry specifics):

1) Network Effects (weight 18%)
   - Evidence: growth & density of user base, marginal utility of adding users, cross-side network measurements (GMV/user, DAU/MAU trends), organic viral coefficients.
   - Metrics to cite: active users (DAU/MAU), growth rates, % of engagement attributable to network interactions, third-party adoption rates.

2) Switching Costs (weight 15%)
   - Evidence: contractual lock-in (multi-year contracts, termination penalties), technical lock-in (integration depth, API adoption), behavioral lock-in (data migration costs, training).
   - Metrics: average contract length, churn rates, net retention, documented customer migration costs.

3) Cost Advantage / Unit Cost Leadership (weight 15%)
   - Evidence: demonstrable per-unit cost below peers (COGS per unit, fulfillment cost per order), proprietary low-cost inputs, proprietary manufacturing process, favorable supplier contracts.
   - Metrics: gross margin differential vs peer median, costs per unit, scale economics disclosures.

4) Intangible Assets / Brand / IP (weight 12%)
   - Evidence: registered patents (with expiry), trademarks, brand strength (price premium evidence), exclusivity agreements, regulatory exclusivity (data exclusivity, orphan drug status).
   - Metrics: patent counts + key patent expiry dates, price premium vs nearest competitor, brand awareness studies if cited.

5) Distribution & Efficient Scale (weight 10%)
   - Evidence: exclusive shelf placements, dense physical network, logistics footprint that makes entry unattractive, limited market segments where only a few players operate profitably.
   - Metrics: store/warehouse density, geographic coverage maps, shelf-share data, unit economics by region.

6) Data Advantage (weight 10%)
   - Evidence: unique, hard-to-replicate datasets; dataset breadth/depth; clear feedback loop where data improves product & increases retention; data scale & recency.
   - Metrics: size of datasets, frequency of updates, citations of data-driven product improvements.

7) Ecosystem / Platform Effects (weight 8%)
   - Evidence: third-party developer adoption, complementary product marketplace, number of integrations, partner stickiness.
   - Metrics: number of third-party apps/integrations, revenue mix from ecosystem services, developer activity levels.

8) Regulatory / Legal Barriers (weight 6%)
   - Evidence: licenses, spectrum ownership, government contracts, regulatory approvals, tariffs or trade protections that limit competitors.
   - Metrics: list of licenses and expiry dates, regulatory rulings, material compliance constraints.

9) Capital Intensity & Asset Specificity (weight 4%)
   - Evidence: sunk costs required to compete (plants, heavy capex, exclusive equipment), lead times to replicate assets, deterrent effect on new entrants.
   - Metrics: capex as % of revenue, lead times, specialized equipment counts.

10) Customer Contracts & Revenue Visibility (weight 2%)
   - Evidence: % recurring revenue, duration and renewal rates of contracts, backlog or contracted ARR/RPO.
   - Metrics: % recurring, contract duration, renewal statistics.

SCORING METHODOLOGY
1. For each dimension: produce a score 0–5 (integer), with reasoning and citations.  
2. Compute a **weighted score** = sum(score_dim * weight_dim). Weights above are the default; if industry-specific rationale requires different weights, explicitly justify any deviations and show both default and adjusted weighted results.  
3. Convert weighted score (0–100) to a 0–5 moat rating using conservative thresholds:

   - Weighted ≥ 85 → moat rating = 5  
   - 70 ≤ Weighted < 85 → moat rating = 4  
   - 50 ≤ Weighted < 70 → moat rating = 3  
   - 30 ≤ Weighted < 50 → moat rating = 2  
   - 10 ≤ Weighted < 30 → moat rating = 1  
   - Weighted < 10 → moat rating = 0

4. Report both the **numeric weighted score** (e.g., 72.4 / 100) and the **final integer moat rating** (0–5). The final line must be exactly:

    moat rating is X / 5

OUTPUT FORMAT (STRICT — MARKDOWN)
1) Header line: Company, ticker, currency, date of analysis, primary sources reviewed (bulleted list of links + absolute dates).  
2) One-line summary: proposed moat rating and estimated duration in years (e.g., "Preliminary moat rating: 3 / 5; estimated durability: ~7–10 years"). (This is a preface — still justify below.)  
3) Table: Dimensions, weight %, raw score (0–5), weighted contribution. (Show numeric computation for each.)  
4) For each dimension (1–10):  
   - **Reasoning (2–4 sentences)** — be explicit and conservative.  
   - **Evidence (1–3 bullets)** — each with citation (document title/link + absolute date).  
   - **Score:** N / 5.  
5) Aggregation: show weighted sum calculation and final weighted numeric score out of 100.  
6) Mapping: show how the numeric weighted score maps to the 0–5 final moat rating (per thresholds above).  
7) Moat duration justification: 2–3 sentences estimating years of durability and key expiry events (patent expiry, contract expiration, regulation reviews) with citations and dates.  
8) Top 3 moat erosion scenarios (each 1–2 sentences with a citation if available).  
9) KPIs to monitor (5–8 specific metrics, what direction indicates erosion vs strengthening).  
10) Short verdict paragraph (3–5 sentences) that ties together why the assigned rating is appropriate and which evidence would flip the rating.  
11) Final mandatory line (single line):  

    moat rating is X / 5

DECISION RULES & CONSERVATISM
- If evidence is mixed, err **downward**. Document the mixed evidence and why the conservative choice was made.  
- Do not use market/analyst narratives as primary evidence. Use them only for context and always label them as third-party commentary.  
- If a dimension lacks direct company-level evidence, do not invent numbers — either use conservative proxies (explicitly show the proxy and the justification) or score the dimension lower.  
- When citing patents or regulatory exclusivity, include expiry dates and legal jurisdiction.

CHECKLIST BEFORE SUBMITTING
- Every factual sentence that asserts a measurable fact has at least one dated citation.  
- Dimension scores are integers 0–5 and each has explicit evidence and reasoning.  
- Weighted contributions are computed and shown numerically.  
- Moat duration is estimated and justified with dates.  
- Final line is exactly: moat rating is X / 5

EXAMPLE OUTPUT (short illustration, do not copy for final):
- Header: {company_name} ({stock_name.upper()}), USD, Analysis date: May 7, 2025. Sources: (10-K, Feb 25, 2025), (Q1 shareholder letter, Apr 30, 2025).  
- One-line summary: Preliminary moat rating: 3 / 5; estimated durability: 7–10 years.  
- ... [full breakdown per dimension] ...  
- Final line (exact): moat rating is 3 / 5

Begin the assessment for {company_name} ({stock_name.upper()}) using the exact structure above. Be rigorous, conservative, and cite everything.
"""

	try:
		client = genai.Client()
		grounding_tool = types.Tool(
			google_search=types.GoogleSearch
		)

		url_context_tool = types.Tool(
			url_context = types.UrlContext
		)


		config = types.GenerateContentConfig(
			tools=[grounding_tool, url_context_tool],
			thinking_config=types.ThinkingConfig(thinking_budget=-1)
		)

		response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt, config=config)
		full_response_text = response.text

		analysis_result = {
			"reasoning": full_response_text,
			"final_answer": None
		}

		lines = full_response_text.strip().split('\n')
		if lines:
			last_line = lines[-1].lower()
			phrase_to_find = "moat rating is"
			if phrase_to_find in last_line:
				try:
					start_index = last_line.find(phrase_to_find) + len(phrase_to_find)
					final_value_str = last_line[start_index:].strip()
					analysis_result["final_answer"] = final_value_str
				except Exception:
					print(f"Warning: Could not parse the final answer from the last line: '{lines[-1]}'")

		return analysis_result

	except Exception as e:
		print(f"An error occurred while communicating with the Gemini API: {e}")
		return {
			"reasoning": "NO RESPONSE",
			"final_answer": None
		}

def analyze_catalysts(stock_name: str, company_name: str) -> dict:
	"""
    Analyzes the qualitative aspects of a business, focusing on its economic moat.
    """
	if not stock_name or not isinstance(stock_name, str):
		raise ValueError("A valid stock name must be provided as a string.")

	# Load environment variables from .env file
	# This is done once in main, but kept here for potential standalone use
	if not os.getenv("GOOGLE_API_KEY"):
		load_dotenv()
		
	prompt = f"""
ROLE: Catalyst strategist and equity analyst. Be an evidence-first investigator focused on identifying **near-term (0–12 months)** and **long-term (12–60 months)** catalysts that could plausibly drive the share price of {company_name} ({stock_name.upper()}) materially higher. Your work must be conservative, fully transparent, and auditable.

OBJECTIVE
Produce a prioritized, quantified, and fully-cited catalogue of potential catalysts (both positive catalysts and their key downside/anti-catalysts). For each catalyst you must show the mechanism by which the event could move the stock, provide an estimated timing window, a numeric estimate of potential impact (range), and a probability/confidence score. Emphasize corporate actions (buybacks, dividends, insider buying), operational and product catalysts, regulatory/approval events, large contract wins, partnerships, margin programs, and M&A — but include any other realistic drivers.

DATA SOURCES (ORDER OF PRECEDENCE)
1) Primary company disclosures: SEC filings (10-K/20-F, 10-Q, 8-K), annual report, definitive proxy, investor presentations, and press releases.  
2) Latest earnings call transcript and prepared management remarks (use only management-sourced forward guidance).  
3) Regulatory filings (prospectuses, credit agreements, material contracts) and regulator decisions.  
4) Exchange records for price/time if current market price is referenced.  
5) High-quality news (Reuters, Bloomberg, WSJ) only to corroborate dates/announcements — never to replace primary filings.

CITATION RULE (MANDATORY)
- **Every numeric fact, date, share count, authorization amount, or direct quote must include a dated citation** with a working link and absolute date, e.g., (10-Q, Aug 7, 2025).  
- If you infer a number (e.g., run-rate revenue), show the exact arithmetic and cite the input sources used.  
- If a claim cannot be supported by primary documentation, explicitly label it as an inference, show the inference steps, and use conservative assumptions.

DEFINITIONS
- Near-term = 0–12 months. Long-term = 12–60 months.
- Impact magnitude categories (use when estimating % price effect):  
  - Small = ~0–10% price impact  
  - Medium = ~10–30% price impact  
  - Large = >30% price impact  
  Justify any mapping from financial effect to price impact.

OUTPUT STRUCTURE (STRICT — MARKDOWN)
1) **Header:** Company, ticker, reporting currency, date of analysis, list of primary sources reviewed (bulleted with link + absolute date).  
2) **Top 3 Prioritized Catalysts (summary table)** — select the three catalysts that are (A) most likely, (B) highest expected impact, or (C) nearest-term. For each show: Catalyst title, Type, Timing window, Impact (Small/Medium/Large + % range), Probability (0–100%), and one-line evidence citation.  
3) **Near-Term Catalysts (0–12 months)** — a numbered list. For each catalyst include the following labeled fields (exact order required):

   - **Catalyst Title:**  
   - **Type:** (Corporate action / Financial / Operational / Product / Regulatory / Partnership / M&A / Macro / Other)  
   - **Description (1–2 sentences):** What is happening? Cite any announced amounts/dates.  
   - **Mechanism:** Precisely explain *how* this event would lift the share price. Use valuation math where appropriate.  
   - **Timing:** earliest possible date — latest plausible date (give absolute dates where possible). Cite source for dates.  
   - **Quantification:** show a conservative numeric scenario (Low/Base/High) with arithmetic. Every number must be cited. Show your math step-by-step.  
   - **Estimated Price Impact:** give a % range and explain basis. Be conservative.  
   - **Probability / Confidence (0–100%)** and rationale with supporting evidence.  
   - **Key Dependencies / Conditions:** what must happen for the catalyst to succeed.  
   - **Monitoring Triggers / KPIs:** 3–5 things to watch and where to find them.  
   - **Anti-Catalysts / Risks:** 1–3 reasons it could fail or be delayed.  
   - **Suggested Investor Action:** (Buy / Watch / Avoid / Hedge) and rationale.

4) **Long-Term Catalysts (12–60 months)** — same structure/fields as above but emphasizing strategic or structural events. Include multi-year P&L/FCF impact scenarios (conservative arithmetic) and valuation linkages.

5) **Prioritization & Scoring Table** — for all catalysts (near + long), produce a table with columns: ID, Title, Type, Timing (Near/Long), Impact Score (1–5), Probability Score (1–5), Expected Impact (% price range), Weighted Score = ImpactScore * ProbabilityScore. Sort descending by Weighted Score and show top 10.

6) **Timeline / Gantt (concise)** — present a quarter-by-quarter timeline for the top 8 catalysts showing expected windows. Cite timing estimates.

7) **Valuation Sensitivity Examples (short)** — pick 2 of the highest-priority catalysts and show a conservative valuation sensitivity with formulas and citations.

8) **Net Catalysts Balance & Short-Term Market Signal** — paragraph summarizing whether near-term catalysts are likely to produce positive stock performance in 0–12 months.

9) **Evidence Matrix (required)** — a concise mapping: each citation used → which claims/fields it supports.

10) **Three Highest-Risk Events That Could Negate All Catalysts** — 1–2 sentences each and citations.

11) **Final Recommendation Paragraph (2–3 sentences)** — actionable conclusion referencing the top catalyst, the expected % upside range (conservative), and the single most important indicator to monitor.

12) Give a final rating out of 5 based on all the information above.

OUTPUT FORMAT RULES & DECISION GUIDANCE
- Use primary sources for every number.  
- Do not use sell-side/consensus estimates.  
- Every number must be cited or labeled as an inference with conservative assumptions.  
- Prioritization, timeline, and evidence matrix are mandatory.  
- If a catalyst is speculative with no hard evidence, mark as low-probability and explain caveats.
- Remember to have final line as - catalyst score is x / 5

CHECKLIST BEFORE SUBMISSION
- Every numeric input has a dated citation.  
- Every inferred number shows arithmetic and sources.  
- Each catalyst includes Timing, Mechanism, Quantification, Probability, Monitoring, and Risks.  
- Prioritization table present and sorted.  
- Final recommendation included.

Be conservative and explicit at all times. It is better to be strict than lenient with these ratings. Only too good to be true cases should get 4 and above.

Begin the analysis for {company_name} ({stock_name.upper()}).

Final line of the output must read exactly:  
catalyst score is x / 5
"""

	try:
		client = genai.Client()
		grounding_tool = types.Tool(
			google_search=types.GoogleSearch
		)

		url_context_tool = types.Tool(
			url_context = types.UrlContext
		)

		config = types.GenerateContentConfig(
			tools=[grounding_tool, url_context_tool],
			thinking_config=types.ThinkingConfig(thinking_budget=-1)
		)

		response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt, config=config)
		full_response_text = response.text

		analysis_result = {
			"reasoning": full_response_text,
			"final_answer": None
		}

		lines = full_response_text.strip().split('\n')
		if lines:
			last_line = lines[-1].lower()
			phrase_to_find = "catalyst score is"
			if phrase_to_find in last_line:
				try:
					start_index = last_line.find(phrase_to_find) + len(phrase_to_find)
					final_value_str = last_line[start_index:].strip()
					analysis_result["final_answer"] = final_value_str
				except Exception:
					print(f"Warning: Could not parse the final answer from the last line: '{lines[-1]}'")

		return analysis_result

	except Exception as e:
		print(f"An error occurred while communicating with the Gemini API: {e}")
		return {
			"reasoning": "NO RESPONSE",
			"final_answer": None
		}

def analyze_fisher_qs(stock_name: str, company_name: str):
	if not stock_name or not isinstance(stock_name, str):
		raise ValueError("A valid stock name must be provided as a string.")

	# Load environment variables from .env file
	# This is done once in main, but kept here for potential standalone use
	if not os.getenv("GOOGLE_API_KEY"):
		load_dotenv()
		
	prompt = f"""
ROLE: Senior equity analyst applying Philip A. Fisher’s “15 Points” from *Common Stocks and Uncommon Profits*.

OBJECTIVE
Analyze the company **{company_name} ({stock_name.upper()})** using Fisher’s 15-point checklist. For each point:
- Give concise reasoning grounded in verifiable evidence.
- Cite specific sources (filings, earnings call transcripts, investor presentations, reputable news/trade sources, datasets) with working links and publication dates.
- End each point with a forced **Answer: Yes/No** per the decision rules below.
- Finish with a fisher score out of 15. 15 / 15 for all the best answers.

CONSTRAINTS & QUALITY BAR
- Use the **most recent** primary sources: latest annual/quarterly filings (10-K/20-F/10-Q), MD&A, earnings call transcripts, investor day decks. Supplement with major outlets (e.g., Bloomberg/Reuters/WSJ), respected trade journals, and credible third-party datasets (e.g., Statista can be cited if cross-checked).
- **No hallucinations.** If you can’t find credible, recent evidence for a point, state that and choose **No** per the decision rule.
- Use **absolute dates** (e.g., “May 7, 2025”) for events and documents.
- Prefer facts over adjectives; avoid marketing language.
- Keep each point’s reasoning to **2–5 crisp sentences**.
- If evidence is mixed, use the decision rule to choose **Yes only if** the preponderance of **recent** evidence supports it; otherwise **No**.

DECISION RULES (apply to every point)
- **Yes** = Current, concrete evidence supports Fisher’s criterion.
- **No** = Evidence is weak, outdated, contradictory, or not found.
- When applicable, evaluate at the **consolidated** level; if segment evidence diverges, explain briefly.

OUTPUT FORMAT (Markdown)
- Start with a one-line overview: “Company, date of analysis, primary sources reviewed.”
- Then present each numbered point as shown below.
- After point 15, include a fisher score line as: fisher score is X / 15.
- End with a one-paragraph synthesis highlighting what would most likely change the score in the next 12–24 months.

FISHER’S 15 POINTS (use these exact headings)

1) Products/Services with Long Runway  
**Question:** Does the company have products or services with sufficient market potential to make possible a sizable increase in sales for at least several years?  
**Reasoning & Evidence:** [2–5 sentences citing TAM/SAM growth, category share trends, new geographies, contract backlogs, unit economics. Include at least one primary source.]  
**Answer:** Yes/No  
**Citations:** [links + dates]

2) Commitment to Ongoing Development  
**Question:** Does management have a determination to continue to develop products or processes that will further increase total sales potential once current lines mature?  
**Reasoning & Evidence:** [Pipeline detail from filings/calls; R&D roadmap; capex/new capacity; partnerships; M&A for growth.]  
**Answer:** Yes/No  
**Citations:** [...]

3) R&D Effectiveness Relative to Size  
**Question:** How effective are the company’s R&D efforts in relation to its size?  
**Reasoning & Evidence:** [R&D as % of revenue vs peers; output metrics—patents, launches, feature velocity, success rates; time-to-market.]  
**Answer:** Yes/No  
**Citations:** [...]

4) Above-Average Sales Organization  
**Question:** Does the company have an above-average sales organization?  
**Reasoning & Evidence:** [Sales coverage, channel mix, retention/expansion (NRR), win rates, pipeline, key customer logos, sales productivity.]  
**Answer:** Yes/No  
**Citations:** [...]

5) Worthwhile Profit Margins  
**Question:** Does the company have a worthwhile profit margin?  
**Reasoning & Evidence:** [Gross/operating margins vs peers; margin trend over 3–5 years; unit economics; seasonality; mix.]  
**Answer:** Yes/No  
**Citations:** [...]

6) Margin Improvement Actions  
**Question:** What is the company doing to maintain or improve profit margins?  
**Reasoning & Evidence:** [Pricing power, mix shift, automation, supply-chain efficiencies, opex discipline, restructuring, product architecture.]  
**Answer:** Yes/No  
**Citations:** [...]

7) Labor & Personnel Relations  
**Question:** Does the company have outstanding labor and personnel relations?  
**Reasoning & Evidence:** [Attrition, engagement, union relations, safety metrics, compensation/benefits disclosures, Glassdoor (if used, triangulate), culture commentary from filings.]  
**Answer:** Yes/No  
**Citations:** [...]

8) Executive Relations  
**Question:** Does the company have outstanding executive relations?  
**Reasoning & Evidence:** [Board/management stability, succession planning, bench depth, incentive alignment, insider ownership, credible track record.]  
**Answer:** Yes/No  
**Citations:** [...]

9) Depth of Management  
**Question:** Does the company have depth to its management?  
**Reasoning & Evidence:** [Named executive team beyond CEO; operating leaders by segment; disclosed succession; key person risk mitigations.]  
**Answer:** Yes/No  
**Citations:** [...]

10) Cost Analysis & Accounting Controls  
**Question:** How good are the company’s cost analysis and accounting controls?  
**Reasoning & Evidence:** [Segment disclosure quality, cost line granularity, auditor opinion, internal control remarks, restatement history, working-capital discipline.]  
**Answer:** Yes/No  
**Citations:** [...]

11) Industry-Specific Competitive Clues  
**Question:** Are there other aspects of the business—peculiar to the industry—that give important clues about how outstanding the company may be versus competition?  
**Reasoning & Evidence:** [Examples: retailer lease quality & location strategy; semis node leadership; SaaS ecosystem lock-in; network effects; manufacturing yields.]  
**Answer:** Yes/No  
**Citations:** [...]

12) Long-Range vs Short-Range Profit Outlook  
**Question:** Does the company have a long-range outlook in regard to profits (willing to trade near-term results for durable growth)?  
**Reasoning & Evidence:** [Guidance posture, reinvestment narratives, capex/R&D prioritization, LT targets, willingness to forgo short-term EPS.]  
**Answer:** Yes/No  
**Citations:** [...]

13) Equity Financing Dilution Risk  
**Question:** Is the company's financial position strong enough to fund foreseeable growth without resorting to equity financing that would meaningfully dilute existing shareholders?
**Reasoning & Evidence:** [Cash balance, FCF, leverage, access to debt, historical issuance/buybacks, shelf registrations, capital intensity, unit economics.]  
**Answer:** Yes/No  
**Citations:** [...]

14) Candor with Investors  
**Question:** Does management talk freely to investors when things are going well **and** when troubles occur (i.e., no “clam up”)?  
**Reasoning & Evidence:** [Transparency in calls/letters; discussion of missteps; disclosure of KPIs; risk factor specificity; crisis communications history.]  
**Answer:** Yes/No  
**Citations:** [...]

15) Unquestionable Integrity  
**Question:** Does the company have a management of unquestionable integrity?  
**Reasoning & Evidence:** [Legal/regulatory history, related-party transactions, audit issues, governance red flags, compensation practices, code-of-conduct breaches.]  
**Answer:** Yes/No  
**Citations:** [...]

---  
**Synthesis (5–7 sentences):** Summarize the strongest positives/negatives, the 2–3 variables most likely to change the score within 12–24 months (e.g., a product launch, regulatory decision, new capacity, margin program), and what specific evidence would flip any “No” to “Yes”.

fisher score is x / 15

CHECKLIST BEFORE YOU SUBMIT
- Every point ends with “Answer: Yes/No”.
- Each point includes at least one **dated** citation with a working link.
- Numbers have units, periods, and clear timeframes.
- No speculative claims without sources; no generic platitudes.
- Remember that the last line of your output should be - fisher score is x / 15 (where x is the correct answer. So a great business will have 15 / 15)
"""	

	try:
		client = genai.Client()
		grounding_tool = types.Tool(
			google_search=types.GoogleSearch
		)

		url_context_tool = types.Tool(
			url_context = types.UrlContext
		)

		config = types.GenerateContentConfig(
			tools=[grounding_tool, url_context_tool],
			thinking_config=types.ThinkingConfig(thinking_budget=-1)
		)

		response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt, config=config)
		full_response_text = response.text

		analysis_result = {
			"reasoning": full_response_text,
			"final_answer": None
		}

		lines = full_response_text.strip().split('\n')
		if lines:
			last_line = lines[-1].lower()
			phrase_to_find = "fisher score is"
			if phrase_to_find in last_line:
				try:
					start_index = last_line.find(phrase_to_find) + len(phrase_to_find)
					final_value_str = last_line[start_index:].strip()
					analysis_result["final_answer"] = final_value_str
				except Exception:
					print(f"Warning: Could not parse the final answer from the last line: '{lines[-1]}'")

		return analysis_result

	except Exception as e:
		print(f"An error occurred while communicating with the Gemini API: {e}")
		return {
			"reasoning": "NO RESPONSE",
			"final_answer": None
		}

def main():
	"""
	Main function to parse arguments, read stock tickers from a file,
	and run the valuation analysis for each.
	"""
	# Setup argument parser
	parser = argparse.ArgumentParser(
		description="Analyze stock valuations for a list of stocks from a file."
	)
	parser.add_argument(
		"input_file",
		type=str,
		help="Path to a text file containing stock tickers, one per line."
	)
	args = parser.parse_args()

	# Configure API key once
	try:
		load_dotenv()
		api_key = os.environ.get("GOOGLE_API_KEY")
		if not api_key:
			raise EnvironmentError("GOOGLE_API_KEY not found in .env file or environment variables.")
		genai.configure(api_key=api_key)
	except Exception as e:
		print(f"Error during setup: {e}")
		return

	# Check if the input file exists
	if not os.path.exists(args.input_file):
		print(f"Error: The file '{args.input_file}' was not found.")
		return

	# Read stock tickers from the file
	try:
		with open(args.input_file, 'r') as f:
			stock_tickers = [line.strip() for line in f if line.strip()]
	except Exception as e:
		print(f"Error reading from file '{args.input_file}': {e}")
		return

	if not stock_tickers:
		print(f"No stock tickers found in '{args.input_file}'.")
		return

	# Process each stock ticker
	for ticker in stock_tickers:
		print(f"\n{'='*25} Analyzing {ticker.upper()} {'='*25}")
		result = analyze_stock_valuation(ticker)
		if result:
			print("\n--- Full Analysis ---\n")
			print(result.get("reasoning", "No reasoning provided."))
			print("\n--- Final Answer ---")
			print(result.get("final_answer", "Not found."))
		print(f"{'='*60}\n")

if __name__ == "__main__":
	main()