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
		
	prompt = f"""Do back of the envelope valuation for {stock_name.upper()} stock. Company name: {company_name}. Please keep it simple to understand and your final answer should be fair value / share. Be a little pessimistic in your assumptions.

	Use internet search: SEC filings, news, earnings calls, issued guidances, and historical data to guide your decisions. Focus more on recent information & don't use valuation techniques that rely on revenue multiples because what we need to focus on are the earnings, in case you can't estimate earnings - estimate margin and multiply that to projected revenue.

Remember to use company guidances and management projections / comments from most recent earnings call. Do not use anything from analysts they are fucking stupid. Use things said by management. Please give all the steps in the calculation. Make sure your final value accounts for company debt: so subtract net debt from final value. Make sure all numbers you use in calculations are accurate: shares outstanding, debt, cash, revenue, etc.

The P/E ratio or discount % you use for discounted cash flow projection, keep it on the more conservative side. Overall keep valuation conservative but still realistic. Like Peter Lynch said, only if a company growing at 20% EPS YoY it should get PE of 20.

Some resources you can use to make sure all numbers you use are absolutely accurate. It is very important that they are 100% accurate:

https://stockanalysis.com/stocks/{stock_name}/
https://stockanalysis.com/stocks/{stock_name}/financials
https://stockanalysis.com/stocks/{stock_name}/financials/balance-sheet
https://stockanalysis.com/stocks/{stock_name}/financials/cash-flow-statement
https://discountingcashflows.com/company/{stock_name}/transcripts/

Use GAAP guidances and numbers wherever possible. For non-GAAP stuff, please convert to GAAP first.

And the last line of the output should be: final answer is xyz $
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
			tools=[grounding_tool, url_context_tool]
		)

		response = client.models.generate_content(model="gemini-2.5-pro", contents=prompt, config=config)
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
			"reasoning": f"Error during analysis for {stock_name}: {e}",
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
    Analyze the qualitative aspects and economic moat of {stock_name.upper()}. Company name: {company_name}.
    Your goal is to determine the durability and strength of the company's competitive advantages.

    Use internet search on official sources like SEC filings (especially the 'Business' and 'Risk Factors' sections of the latest 10-K), recent earnings call transcripts, and official company press releases.

    Based on your analysis, provide a clear reasoning for the strength of the moat. Be as descriptive as possible. First talk about the business itself.

    To identify the moat, consider these factors:
    1.  **Intangible Assets:** Brand recognition, patents, regulatory licenses. Does the company have a brand that commands pricing power?
    2.  **Switching Costs:** Are customers locked into the company's ecosystem? How difficult or expensive is it for customers to switch to a competitor?
    3.  **Network Effects:** Does the product or service become more valuable as more people use it? (e.g., social media, marketplaces).
    4.  **Cost Advantages:** Can the company produce its goods or services at a lower cost than competitors due to scale, process, or location?

    Give reasoning for all points and do an indepth web search until you are confident in your answers.

    Finally, rate the company's moat on a scale of 1 to 5.
    - **1/5:** No discernible moat. Highly competitive industry.
    - **3/5:** A moderate, identifiable moat that may be weakening or not yet proven durable.
    - **5/5:** A wide, deep, and durable moat. These are exceptional businesses that can fend off competition and sustain high returns on capital for decades (e.g., Moody's, Coca-Cola).

    A good starting point:

    https://stockanalysis.com/stocks/{stock_name}/

    Resources to use for earnings calls:

    https://discountingcashflows.com/company/{stock_name}/transcripts/

    Resources for any recent developments:

    Use seekingalpha and reddit to look for any meaningful discussions around this topic
    Use news websites to find any developments in the sector that could inform more about this topic

    Remember to cite your sources.

    Provide your reasoning first, and ensure the very last line of your entire output is in the following format:
    moat rating is x / 5
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
			tools=[grounding_tool, url_context_tool]
		)

		response = client.models.generate_content(model="gemini-2.5-pro", contents=prompt, config=config)
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
			"reasoning": f"Error during analysis for {stock_name}: {e}",
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
Analyze the near-term and long-term catalysts for {stock_name.upper()} stock. Company name: {company_name}. Your analysis should be a comprehensive research effort into events and factors that could materially impact the company's value.

Use internet search: SEC filings (especially recent 10-Ks, 10-Qs, and Form 4s), news, earnings call transcripts, investor presentations, and company press releases. You must also consider the broader industry trends and economic cycles affecting the business.

Good place to start getting basic info: https://stockanalysis.com/stocks/{stock_name}/

Insider buying can be found at: http://openinsider.com/search?q={stock_name}

Institutional buying info: https://whalewisdom.com/stock/{stock_name}

company stock Buyback info: https://www.tipranks.com/stocks/{stock_name}/buybacks

Your analysis must cover the following specific points:

1.  **Capital Allocation & Insider Confidence:**
    * **Stock Buybacks:** Is the company actively repurchasing its own shares? Detail any announced buyback programs, their size, and recent activity.
    * **Insider Buying & Selling:** Scrutinize recent Form 4 filings. Are key executives and directors net buyers or sellers of the stock? Significant open-market buys are a strong positive signal.
    * **Insider Ownership:** What is the percentage of shares held by insiders? High ownership is a good sign of alignment with shareholders.

2.  **Business & Industry Catalysts:**
    * **Near-Term (Next 6-12 Months):** Identify any upcoming product launches, expected regulatory approvals, major contract wins, cost-saving initiatives mentioned by management, or other specific events that could serve as a short-term catalyst.
    * **Long-Term (1-5+ Years):** What are the major secular trends the company is poised to benefit from? Analyze its R&D pipeline, market expansion opportunities, and strategic positioning against competitors.
    * **News & Market Sentiment:** Synthesize the tone of recent news coverage. Is the narrative around the company positive, negative, or neutral?

After presenting a detailed analysis covering these points, provide a final score reflecting the strength and likelihood of these catalysts positively impacting the stock.

**Scoring Guide:**
- **1/5:** Significant headwinds, negative insider signals, no clear catalysts.
- **3/5:** A balanced outlook with some potential catalysts offset by risks or neutral insider activity.
- **5/5:** Multiple, clear, and powerful catalysts on the horizon, backed by strong insider confidence (buybacks/buying) and positive industry trends.

Provide your reasoning first, and the very last line of your output must be in the following format:
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
			tools=[grounding_tool, url_context_tool]
		)

		response = client.models.generate_content(model="gemini-2.5-pro", contents=prompt, config=config)
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
			"reasoning": f"Error during analysis for {stock_name}: {e}",
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
Finish with a fisher score out of 15.

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
- After point 15, include a fisher score line as: **fisher score is X / 15**.
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
**Question:** In the foreseeable future, will growth require such equity financing that dilution will largely cancel existing stockholders’ benefit from anticipated growth?  
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
- Remember that the last line of your output should be - fisher score is x / 15
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
			tools=[grounding_tool, url_context_tool]
		)

		response = client.models.generate_content(model="gemini-2.5-pro", contents=prompt, config=config)
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
			"reasoning": f"Error during analysis for {stock_name}: {e}",
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