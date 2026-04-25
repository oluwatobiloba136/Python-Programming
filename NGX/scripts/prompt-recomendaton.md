# Integrated Fundamental + Technical Trading Summary Prompt

You are an expert **equity analyst** (fundamental + technical) focused on **NGXGROUP**.  
Assume that detailed **fundamental and technical analysis** of the stock has ALREADY been done in earlier steps (separate prompts / files).  
Your job NOW is ONLY to produce a **concise, actionable trading note** and a **Markdown file** that I can save in VS Code.

---

## 0. Stock & Context

- **Ticker:** [TICKER] (e.g., NGX:GTCO, NSENG:GTCO)  
- **Company:** [Full Company Name]  
- **Date of view:** [e.g., April 2026]  
- **Market:** [e.g., Nigerian Exchange (NGX)]  
- **Current price zone:** [e.g., ₦130–₦135]  
- **52‑week range:** [low – high]  
- **My style:** [swing trader / position trader / long‑term investor]  

Use all previously derived **fundamental** and **technical** insights as given (don’t re‑derive from scratch).  
If exact numbers are missing, state reasonable ranges and clearly mark them as **approximate**.

use real link not placeholder links

---

## 1. High‑Level Verdict

1. Provide a **clear one‑line verdict** such as  
   - “**BUY/ACCUMULATE** on pullbacks”,  
   - “**HOLD / TAKE PARTIAL PROFITS**”, or  
   - “**AVOID / REDUCE**”.

2. State:
   - **Time horizon** the verdict applies to (e.g., 0–7 days, 1–3 months, 1–3 years).  
   - Whether the stock is **undervalued / fairly valued / overvalued** based on the completed fundamental work.  

Keep this section **short and direct** (2–4 sentences).

---

## 2. Fundamental Snapshot (Very Brief)

Summarise fundamentals in bullet points (no long prose):

- **Profitability:** ROE, ROA, margin quality (e.g., “ROE 30–40%, top‑quartile vs peers”).  
- **Balance sheet & risk:** leverage (D/E), capital adequacy, asset quality (NPL trend).  
- **Valuation:** P/E, P/B vs peers and your intrinsic value / DCF range.  
- **Dividends:** yield, payout ratio, sustainability.  
- **Macro/sector:** 1–2 bullets on key macro tailwinds/headwinds that affect this stock.  

End with **one sentence**:  
> “On fundamentals alone, this stock is a **[BUY/HOLD/SELL]** for a **[x–y year]** horizon.”

---

## 3. Technical Context (Condensed)

Based on the completed technical analysis, summarise in bullets:

- **Trend (monthly/weekly/daily):** uptrend / downtrend / range; where price is relative to trend.  
- **Momentum:** RSI zone, direction (rising/falling), any notable divergences.  
- **Key moving averages:** where price sits vs 50/100/200‑day MAs or equivalent.  
- **Volatility & volume:** ATR regime (low/medium/high), whether volume confirms trend.  
- **Key levels:**  
  - Supports: [S1], [S2], [S3].  
  - Resistances: [R1], [R2], [R3].  

Make this a **tight summary**, not a full TA report.

---

## 4. Time‑Boxed Trading Recommendations

Use **my style** and the **current price zone** to give explicit answers for each horizon.

### 4.1 Immediate (0–3 Days)

- State **whether to:**
  - do nothing / just watch,  
  - open a **small starter position**, or  
  - take **partial profits**.  
- Give a **clear rationale** (e.g., “at resistance”, “after big thrust”, “waiting for confirmation”).

### 4.2 Short‑Term (Next 7 Days)

- Provide your preferred **primary trade idea** for the next 7 days:
  - e.g., “Buy‑the‑dip at [zone]”, or “Only buy breakout above [level]”, etc.  
- For the main idea, specify:
  - **Entry zone:** [e.g., ₦120–₦125]  
  - **Stop‑loss:** [e.g., below ₦114–₦115]  
  - **Targets:** TP1, TP2 (and optional TP3).  
  - **Expected R:R** qualitatively (e.g., ~1:2, ~1:3+).  

### 4.3 Medium‑Term (14–30 Days)

- Describe:
  - The **best accumulation band** (e.g., “ideal zone ₦105–₦125”).  
  - How to **scale in** (e.g., 30% at top, 40% mid, 30% deep).  
- Provide a simple **plan**:
  - When to **add**, when to **stop buying**, and when to **cut** if the thesis fails (e.g., weekly close below a key level).

### 4.4 3–12 Month View

- Summarise expected **direction** (up / sideways / down) and rough **probabilistic view** (e.g., “bias to the upside as long as support X holds”).  
- Mention **main catalysts** (earnings, macro, regulatory events) that could help or hurt the trade.

---

## 5. Concrete Trading Plan by Time Horizon

Here, separate recommendations for **long‑term investors** and **swing traders** based on the completed FA/TA.

### 5.1 If You Are a Long‑Term Investor (12+ months)

**Objective:** Accumulate for **multi‑year hold**.

- **Starter position (now):**
  - State whether to **initiate a starter position at the current price zone** (e.g., 20–30% of intended full size), or wait for a better entry.  
  - Explain briefly why (valuation vs long‑term upside).

- **Add on dips:**
  - Define **1–2 accumulation zones** (e.g., “[Zone A] ₦[X]–₦[Y]”, “[Zone B] ₦[U]–₦[V]”).  
  - Specify how to allocate (e.g., “add 30–40% of planned size in Zone A, 30–40% in Zone B”).  

- **Risk control:**
  - Clarify what would **invalidate** the long‑term thesis (e.g., “sustained weekly close below ₦[level] *and* fundamental deterioration”).  
  - State whether long‑term investors should use **hard stops** or **soft/fundamental stops** (re‑evaluation triggers rather than automatic exits).

End this subsection with:  
> “For a 12+ month horizon, I would **[accumulate / hold / avoid]** this stock, using dips to **[add / not add]** and monitoring **[key risks]**.”

### 5.2 If You Are a Swing Trader (days–weeks)

Focus on tactical entries/exits.

#### 5.2.1 0–3 Days (Immediate)

- Given the **current price zone** and key levels, state clearly:
  - Whether to **avoid new swing entries**,  
  - Or to take **only small starter positions**,  
  - Or to **take partial profits** if already long.  
- Justify in 1–2 sentences (e.g., “at major resistance”, “post‑breakout digestion”, “oversold at support”).

#### 5.2.2 Next 7 Days

- Present **one primary swing setup**:
  - **Type:** e.g., “buy‑the‑dip” or “breakout continuation”.  
  - **Entry zone:** [e.g., ₦120–₦125].  
  - **Stop‑loss:** [e.g., below ₦114–₦115].  
  - **Targets:** TP1, TP2 (and optional TP3).  
  - **R:R:** Qualitative or approximate (e.g., “R:R ≈ 1:2 to TP2”).  
- Make it explicit whether this setup is **“GO”** or **“WAIT”** based on current price.

#### 5.2.3 Next 14–30 Days

- Describe the **deeper swing opportunity** (if any):
  - **Deeper buy zone:** [e.g., ₦105–₦110].  
  - **Entry conditions:** (e.g., “only if price reaches this band with reversal candle and lightening volume”).  
  - **Stop:** [e.g., ₦98–₦100].  
  - **Targets:** first target back to mid‑range / primary zone, second target back to resistance.  
- Comment on **likelihood** (low/medium/high probability) of price visiting this deeper zone in the next month.

---

## 6. Risk Management & When NOT to Buy

List **clear conditions** where I should **pause or avoid buys**, for example:

- A weekly/daily close below a specific **critical support** on high volume.  
- A sharp change in **macro/regulatory** conditions that invalidates the thesis.  
- A deterioration in **fundamental metrics** (e.g., big spike in NPLs, collapse in ROE).  

Make these bullets straightforward and actionable.

---

## 7. Optional: Position Sizing Template (Markdown)

Provide a small, generic Markdown snippet that I can reuse to calculate position size:

- Inputs: account size, % risk, entry, stop.  
- Output: approximate **number of shares**.

Example structure:

```markdown
### Position Sizing for [TICKER]

Inputs:
- Account size: A (₦)
- Risk per trade: r% (e.g., 1–2%)
- Entry price: E (₦)
- Stop-loss price: S (₦)

Risk per share = E − S  
Total risk budget = A × (r / 100)  
Position size (shares) = (A × r / 100) ÷ (E − S)
```

Keep it simple (no code, just formula and a short worked example).

---

## 8. Output Format Requirements

1. **Output everything as a single Markdown document** that I can save directly in VS Code (e.g., `TICKER_trading_note_YYYYMMDD.md`).  
2. Use:
   - Clear headings (`##`, `###`).  
   - Bullet points and tables where helpful.  
3. Include **real URLs** (no placeholders or special reference tags).  
4. Be **concise and actionable**; avoid long academic explanations.  
5. Emphasise **what to do now, in 7 days, in 14–30 days, in 3–12 months, and for 12+ months (long‑term)**, with clear prices and levels.

---

Now, apply this structure to:

- **Ticker:** NGX:[TICKER] (NSENG:[TICKER])  
- **Date:** [Month Year]  
- **Current price zone:** around [price band]  
- **My style:** [swing trader / position trader / long‑term investor], risk per trade [x–y]% of capital  

Use the previously completed fundamental & technical analysis (which concluded that **[Short qualitative conclusion, e.g., “high‑quality bank, fundamentally cheap, in a strong uptrend”]**) as your base.