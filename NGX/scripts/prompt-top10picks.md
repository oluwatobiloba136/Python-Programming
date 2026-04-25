# NGX – Top 10 Long‑Term Stocks Selection Prompt (2–3 Years, High Growth, Cross‑Sector)

You are an expert **equity analyst** (fundamental + technical) focused on the **Nigerian Exchange (NGX)**.

My goal:  
- As a **long‑term investor (2–3 years)**, I want a **diversified list of 10 NGX stocks across different industries** with the **highest probability** of delivering **very strong annual returns (aspirational 100%+ per year, clearly not guaranteed)**.  
- I accept **high volatility**, but I want names where **fundamentals, technicals, and sector context** line up in a **reasonable, risk‑aware way**.

---

## 0. Constraints & Universe

1. **Exchange:** Nigerian Exchange (NGX).  

2. **Cross‑sector requirement (very important):**  
   - The final **Top 10** must span **multiple sectors**, not just banks.  
   - Aim for something like:
     - **2–3 banks/financials**,  
     - **2–3 consumer (staples/discretionary)**,  
     - **1–2 industrials/construction**,  
     - **1–2 energy/oil & gas**,  
     - **1–2 telco/ICT/other growth themes**,  
     - Adjust mix logically based on quality of ideas.  
   - No more than **3 stocks from any single sector**, unless clearly justified.

3. **Universe:**  
   - Use **liquid names only** (reasonable daily value traded).  
   - Avoid extremely illiquid microcaps unless clearly flagged as special situations.

4. **Time horizon:** **2–3 years**.  

5. **Return target:**  
   - Treat “100% yearly” as an **aggressive aspiration**, not a prediction.  
   - Your job is to **prioritise upside potential + quality** vs NGX peers.

---

## 1. Shortlisting Logic

Use cross‑sector sources and market‑mover lists to build a starting pool:

- Nairametrics – Top performing Nigerian stocks:  
  - https://nairametrics.com/2026/04/06/top-10-best-performing-nigerian-stocks-in-the-first-quarter-of-2026/  
- BusinessDay – “Stocks to watch”:  
  - https://businessday.ng/markets/article/10-stocks-to-watch-as-ngxs-rally-stretches-into-2026/  
- Zikoko / Tribune – Stocks to watch in 2026:  
  - https://www.zikoko.com/money/nigerian-stocks-to-watch-2026/  
  - https://tribuneonlineng.com/six-stocks-to-watch-in-2026/  
- TradingView – Best performing Nigerian stocks:  
  - https://www.tradingview.com/markets/stocks-nigeria/market-movers-best-performing/  

From there:

1. Build a **candidate pool (20–30 names)** ensuring **sector mix** (banks, consumer, industrials, energy, telco, etc.).  
2. Exclude:
   - Perennially lossmaking, distressed, or clearly uninvestable names unless explicitly marked as **special situations** with high risk.

---

## 2. Fundamental Filters & Scoring (Per Stock)

For each candidate, pull 3–5‑year data from:

- Company IR / annual reports (via NGX or company websites).  
- StockAnalysis (if covered):  
  - `https://stockanalysis.com/quote/ngx/[TICKER]/`  
- Marketscreener / Simply Wall St / Investing.com where necessary.

Score each stock (e.g., 1–5) on:

1. **Profitability & quality**  
   - ROE, ROA, margins, stability, through‑cycle resilience.  

2. **Growth**  
   - Revenue & EPS CAGR, visibility of future growth drivers.

3. **Balance sheet & risk**  
   - Leverage, interest coverage, sector‑specific risks (e.g., NPLs for banks, FX/commodity exposure).

4. **Valuation**  
   - P/E, P/B, EV/EBITDA vs sector & NGX averages.  
   - Preference for **quality at reasonable or cheap valuation**.

5. **Dividends** (if relevant)  
   - Yield, payout ratio, consistency & sustainability.

Give a **fundamental verdict** per stock:

> “On fundamentals, **[TICKER]** is a **[Strong Buy / Buy / Hold / Avoid]** for 2–3 years.”

---

## 3. Technical Filters & Scoring (Per Stock)

Using:

- TradingView:  
  - `https://www.tradingview.com/symbols/NSENG-[TICKER]/`  
- Investing.com or other chart sources as needed.

For each stock:

- **Trend:**  
  - Weekly & daily direction (uptrend / downtrend / range).  
  - Price relative to 50‑ and 200‑day MAs (above = bullish regime).

- **Momentum:**  
  - RSI(14) zone, and any obvious bullish/bearish divergences.

- **Key levels:**  
  - Supports/resistances and current location within the 52‑week range.

- **Liquidity/volume:**  
  - Average daily value traded, volume on big moves/breakouts.

Give a **technical verdict**:

> “Technically, **[TICKER]** is in a **[healthy uptrend / base / extended / weak]**.”

---

## 4. Integrated Ranking & Cross‑Sector Top‑10

1. Combine fundamental & technical scores (e.g., **60% fundamentals, 40% technicals**).  

2. Apply the **sector diversification** constraint:
   - Do **not** fill the Top 10 with only banks.  
   - Ensure at least **4 different sectors** represented; ideally **5+**.

3. Present the final **Top 10 NGX stocks** in a table:

```markdown
### Top 10 NGX Stocks (2–3Y, High‑Growth, Cross‑Sector)

| Rank | Ticker | Name       | Sector      | Fund. Score | Tech Score | Valuation View | Sector Role (core/satellite) | 2–3Y Thesis (1–2 lines) |
|------|--------|------------|------------|------------:|-----------:|---------------|------------------------------|-------------------------|
| 1    |        |            |            |             |            |               |                              |                         |
| 2    |        |            |            |             |            |               |                              |                         |
| 3    |        |            |            |             |            |               |                              |                         |
| 4    |        |            |            |             |            |               |                              |                         |
| 5    |        |            |            |             |            |               |                              |                         |
| 6    |        |            |            |             |            |               |                              |                         |
| 7    |        |            |            |             |            |               |                              |                         |
| 8    |        |            |            |             |            |               |                              |                         |
| 9    |        |            |            |             |            |               |                              |                         |
| 10   |        |            |            |             |            |               |                              |                         |
```

---

## 5. Time‑Boxed Plan for Each of the Top 10

For **each stock** in the Top 10, provide:

### 5.1 High‑Level Verdict

- One line, for example:  
  - “**BUY/ACCUMULATE on pullbacks**”,  
  - “**HOLD / TAKE PARTIAL PROFITS**”,  
  - or “**AVOID for now**”.  
- Indicate if it is **undervalued / fairly valued / overvalued**, and whether the trend is **up / base / extended / weak**.

### 5.2 Concrete Time‑Frame Guidance

- **Now (0–7 days):**
  - Should I **start a position / add / do nothing / trim** at the current price?  
  - Justify with 1–2 short sentences (e.g., “at resistance”, “near strong support”, “post‑earnings digestion”).

- **Next 7–14 days:**
  - Give **one primary trade idea**:
    - “Buy the dip at ₦[zone]” **or**  
    - “Only buy breakout above ₦[level] with volume”.  
  - Specify:
    - **Entry zone** (₦[X–Y])  
    - **Stop‑loss zone** (₦[S])  
    - **Targets:** TP1, TP2 (and TP3 if useful)  
    - Approximate **Risk‑Reward** (e.g., “R:R ≈ 1:2–1:3”).

- **Next 3–12 months:**
  - Directional bias (likely up / sideways / down).  
  - Key **catalysts** (earnings, macro, sector news) that could drive big moves.

---

## 6. Portfolio Construction (Cross‑Sector)

At the end, provide:

1. A suggested **sector‑balanced allocation**, e.g.:  
   - 40–50% in relatively more stable sectors (Tier‑1 banks, telcos, large consumer names),  
   - 50–60% in higher‑beta cyclicals/turnarounds (mid‑tier banks, industrials, energy, small/mid‑cap growth).

2. Clear risk guidance:  
   - The 100%+ yearly outcome is **aspirational**, not expected.  
   - Use **1–2% of capital at risk per stock** (based on stop distance).  
   - Define a **max portfolio drawdown** threshold and what to do if it is hit (e.g., de‑risk, rebalance).

---

## 7. Output Format

- Output as a single **Markdown document** I can save (e.g., `NGX_top10_cross_sector_2026.md`).  
- Use clear headings, bullet points, and tables.  
- Include **real URLs** for data/chart sources (no abstract placeholders).  
- Be **succinct and actionable**, not academic: focus on **what to buy, why, and how to manage it over 2–3 years**.