# NGX Stock Fundamental Analysis – Reusable Prompt Template

> Copy this prompt into ChatGPT or another LLM, replace ALL CAPS placeholders with your ticker and links, and paste relevant NGX news CSV/file content.  
> You’ll get a full markdown (.md) write‑up similar to the Aradel analysis.

---

You are an equity research assistant.  
Prepare a **comprehensive fundamental and valuation analysis** of a Nigerian stock listed on the NGX, using **only** the data sources I provide.

## 1. Stock and Data Inputs

- **Ticker / Company:**  
  NGX Ticker: `BERGER`  
  Company Name: `BERGER PAINTS PLC (BERGER)`  

- **StockAnalysis pages (all NGX‑mapped):**

  - Stock overview:  
    `https://stockanalysis.com/quote/ngx/BERGER/`

  - Income statement:  
    `https://stockanalysis.com/quote/ngx/BERGER/financials/`

  - Balance sheet:  
    `https://stockanalysis.com/quote/ngx/BERGER/financials/balance-sheet/`

  - Cash flow statement:  
    `https://stockanalysis.com/quote/ngx/BERGER/financials/cash-flow-statement/`

  - Financial ratios:  
    `https://stockanalysis.com/quote/ngx/BERGER/financials/ratios/`

  - Business metrics & revenue:  
    `https://stockanalysis.com/quote/ngx/BERGER/financials/metrics/`

  - Statistics (valuation, yields, margins, coverage):  
    `https://stockanalysis.com/quote/ngx/BERGER/statistics/`

  - Market cap history:  
    `https://stockanalysis.com/quote/ngx/BERGER/market-cap/`

  - Revenue history:  
    `https://stockanalysis.com/quote/ngx/BERGER/revenue/`

  - Dividend history:  
    `https://stockanalysis.com/quote/ngx/BERGER/dividend/`

  - Price history:  
    `https://stockanalysis.com/quote/ngx/BERGER/history/`

  - Company description (if available):  
    `https://stockanalysis.com/quote/ngx/BERGER/company/`

- **NGX / Issuer disclosures**  
  I will paste or attach a CSV/file listing recent NGX disclosures (financial statements, director dealings, corporate actions, acquisition announcements, filing delays, etc.).  
  Treat that file as “NGX_NEWS_FILE”.

---

## 2. Output Format Requirements

1. **Write the final answer as a single Markdown (.md) document** that I can save directly in VS Code.  
2. **Do not use placeholder links** like `[web:1]`. Use the **real URLs** exactly as I provided them.  
3. Use clear sections and a **Table of Contents**, similar to:

   - Sources  
   - Business Overview and Current Snapshot  
   - Growth: Revenue, Earnings and Margins  
   - Profitability and Efficiency Ratios  
   - Balance Sheet Quality and Leverage  
   - Cash Flow and Free Cash Flow  
   - Dividend Policy and Sustainability  
   - Valuation: Multiples and Implied Expectations  
   - Price History and Volatility  
   - Governance, Corporate Actions and Qualitative Factors  
   - Key Fundamental Metrics – Concepts and Company‑Specific Interpretation  
   - Valuation Conclusion: Undervalued, Overvalued, or Fair  
   - Guidance for Long‑Term Investors  
   - Guidance for Short‑Term Traders  

4. Use **full sentences**, professional equity‑research style, and keep it structured like a written report, not bullet‑spam.

---

## 3. Metrics to Compute and Interpret

For each metric below:

- Briefly **define** the metric in simple language.  
- Then **quantify it for this company** using the StockAnalysis data.  
- Finally, **interpret** it: what does it say about quality/risk, and how should an investor or trader use it?

### 3.1 Profitability

- Net Profit Margin = Net Income / Revenue  
- Gross Margin = (Revenue − COGS) / Revenue  
- Return on Equity (ROE) = Net Income / Shareholders’ Equity  
- Return on Assets (ROA) = Net Income / Total Assets  
- Return on Capital Employed (ROCE), or similar from the ratios page  

### 3.2 Valuation

- Earnings per Share (EPS)  
- Price‑to‑Earnings (P/E)  
- Price‑to‑Book (P/B)  
- Price‑to‑Sales (P/S)  
- Dividend Yield = DPS / Price  
- Free Cash Flow Yield = FCF / Market Cap  
- EV/EBITDA (and EV/EBIT if available)

### 3.3 Growth

- 1‑year and multi‑year **Revenue growth** (use revenue history & metrics pages)  
- 1‑year and multi‑year **EPS growth**  
- 1‑year and multi‑year **FCF growth**  
- Where appropriate, estimate a simple **CAGR** for revenue and EPS over 3–5 years

### 3.4 Cash Flow

- Operating Cash Flow vs Net Income  
- Free Cash Flow (FCF = OCF − CapEx)  
- FCF margin and how it compares to peers/typical E&P or sector context  

### 3.5 Debt & Capital Structure

- Debt‑to‑Equity (D/E)  
- Debt/EBITDA  
- Debt/FCF  
- Interest Coverage = EBIT / Interest Expense  

### 3.6 Liquidity & Efficiency

- Current Ratio, Quick Ratio  
- Asset Turnover  
- Inventory Turnover  
- (If visible) Receivables Turnover or qualitative comment based on cash collection

### 3.7 Enterprise Value

- Enterprise Value (EV) qualitatively (market cap ± net debt)  
- EV/EBITDA and why it’s cheap/expensive vs quality and growth

---

## 4. Governance & Qualitative Layer (Use NGX_NEWS_FILE)

From the NGX news / CSV:

- Identify and comment on:  
  - Frequency and recency of financial statements and press releases  
  - Acquisitions (e.g., NDW‑type deals) and strategic moves  
  - Interim or final dividend announcements  
  - Board changes, director appointments and retirements  
  - Director/staff share purchases and insider‑deal patterns  
  - Any notices of **delay in filing accounts** or other governance red flags  

Explain what these items mean for:

- Governance and transparency  
- Execution risk  
- Management confidence (via insider buying)  

---

## 5. Valuation Conclusion and Actionable Recommendations

### 5.1 Undervalued / Overvalued / Fair

Using all the metrics from StockAnalysis (P/E, EV/EBITDA, ROE, growth, FCF, dividend, etc.):

1. Explicitly state whether, in your judgement, the stock is:  
   - **Undervalued**, or  
   - **Overvalued**, or  
   - **Fairly valued**

2. Justify the conclusion clearly, e.g.:

   - “On a P/E of X and EV/EBITDA of Y, with ROE of Z and margins of M, the stock appears undervalued compared to its own quality and growth profile, once you adjust for MACRO_RISK and SECTOR_RISK.”

### 5.2 Advice for Long‑Term Investors

Provide a dedicated section:

- State clearly: **Buy**, **Accumulate**, **Hold**, **Trim**, or **Sell** for a long‑term fundamental investor.  
- Explain **why**, referencing:  
  - Profitability, growth, balance sheet, cash flows, dividends, valuation, and governance.  
- Explain **when to buy** (e.g., valuation thresholds, pullback conditions, events like strong earnings with muted price reaction).  
- Explain **when to hold** and **when to consider exiting** (e.g., sustained margin compression, rising D/E, repeated governance failures, P/E re‑rating to “too rich” levels).

### 5.3 Advice for Short‑Term Traders

Provide another dedicated section:

- State a tactical stance: e.g., **bullish buy‑the‑dip**, **neutral**, or **avoid**.  
- Describe how to trade the stock given its fundamentals and volatility:  
  - Earnings and dividend catalysts  
  - Buy‑the‑dip vs breakout strategies  
  - Risk management and position sizing considerations  
  - Situations where they should **not** trade long (e.g., ahead of major FX or political events, or during unresolved filing delays)

---

## 6. Formatting Constraints

- Output must be a **single markdown document** that I can save directly in VS Code (no extra explanations outside the markdown).  
- Use headings, sub‑headings, short paragraphs and bullet points exactly as you did in my Aradel report.  
- Do **not** include any internal placeholders like `[web:1]` – only the real URLs that I provided.  
- Keep the tone professional and analytical, similar to a buy‑side/sell‑side research note.

---