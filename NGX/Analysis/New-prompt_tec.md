# Reusable Prompt – NGX Technical Analysis from Historical OHLCV Data

> Use this template with any NGX stock when you already did a fundamental analysis and you have an OHLCV history file (Excel/CSV).  
> Replace ALL_CAPS placeholders with your details, then paste into the model.

---

You are a trading and market‑structure analyst.  
I already have a separate **fundamental analysis** for this stock which yo just provided; your task now is to produce a **complementary technical analysis** using **only the historical data file I provide**.

## 1. Stock and File Details

- **Ticker / Company:**  
  NGX Ticker: `BERGER`  
  Company Name: `BERGER PAINTS PLC (BERGER)`   

- Historical data file (already attached in this chat):  
  File name: `FILENAME_HERE.xlsx` or `FILENAME_HERE.csv`  

This file has (at minimum) columns like:

- Date  
- Open  
- High  
- Low  
- Close (and/or Adjusted Close)  
- Daily % Change (if available)  
- Volume  

Use **only** this file for your technical analysis; do **not** fetch external price data.

---

## 2. Output Format Requirements

1. Write the answer as a **single Markdown (.md) document** that I can save in VS Code.  
2. Do **not** include any internal tool/citation markers – just clean text and headings.  
3. Use clear sections, similar to:

   - Scope and Data  
   - Big Picture Trend  
   - Key Levels: Support, Resistance and Ranges  
   - Momentum and Price Behaviour  
   - Volume and Participation  
   - Volatility Profile  
   - Trend Phase Classification (relative to fundamentals)  
   - Practical Technical Takeaways for Investors  
   - Practical Technical Takeaways for Short‑Term Traders  
   - How Technicals Confirm or Challenge the Fundamental Thesis  
   - Summary Technical View  

4. Use concise paragraphs and bullets; tone should be professional and analytical, like a trader’s note.

---

## 3. What to Analyze from the Historical Data

### 3.1 Big Picture Trend

- Identify the major direction over the full sample (uptrend, downtrend, range).  
- Highlight key phases:
  - Base/accumulation zones  
  - Breakouts and re‑rating legs  
  - Consolidation or distribution zones  

Explain **where current price sits relative to the full history** (e.g., near highs, mid‑range, deep pullback).

### 3.2 Key Levels: Support and Resistance

- From the OHLC data, infer:
  - Major historical support zones (price areas with many lows or bounces).  
  - Major resistance zones (areas with repeated highs or failed breakouts).  
  - Any “psychological” levels (round numbers) the stock reacts to.

Explain how these levels would be used:

- For investors (where to add on dips).  
- For traders (entries, stops, targets).

### 3.3 Momentum and Price Behaviour

- Use the daily **Change** or Close-to-Close pattern to describe:
  - Strong up‑days and down‑days (e.g., ±5–10 % moves).  
  - Periods of flat trading (Open=High=Low=Close) or narrow ranges.  

Comment on:

- Whether big moves tend to cluster around certain dates (earnings windows, etc., if visible).  
- Whether momentum has recently strengthened, weakened, or gone sideways.

### 3.4 Volume and Participation

- Analyze Volume vs price:
  - Are big up‑moves associated with high volume?  
  - Are consolidations on lower or moderate volume?  
  - Any signs of climactic selling (huge volume + large down‑day)?

Summarize whether volume **confirms or contradicts** the trend:

- Uptrend + higher volume on up‑days → healthy accumulation.  
- Uptrend + highest volume on down‑days → potential distribution.

### 3.5 Volatility Profile

- Use the daily percentage changes to characterize volatility:
  - Typical 1‑day move range (e.g., ±2–3 % or ±8–10 %).  
  - Frequency of outlier days (>±7–10 %).  

Explain implications for:

- Stop‑loss placement.  
- Position sizing and gap risk.  
- Suitability for different trading styles (swing vs intraday vs long‑term).

### 3.6 Trend Phase Classification vs Fundamentals

Assume a **strong fundamental backdrop** (you don’t need to restate it; just reference it generically).

- Classify the current phase as one of:
  - Accumulation/Base  
  - Breakout/Re‑rating  
  - Healthy consolidation in uptrend  
  - Topping/Distribution  
  - Downtrend/De‑rating  

Explain how this **technical phase** interacts with the fundamental story:

- E.g., “Fundamentals are strong and technicals show a high‑level consolidation, which is typical after a re‑rating and can precede further upside if support holds.”

---

## 4. Actionable Technical Takeaways

### 4.1 For Long‑Term Investors

Provide concise, practical guidance such as:

- Whether the long‑term trend supports a **Hold**, **Buy the dip**, or “wait for better entry” stance.  
- Approximate **price zones** from the data where:
  - It makes sense to accumulate on weakness (key supports).  
  - Risk becomes elevated (break of major support or loss of long‑term trend).  

Make sure your suggestions are **conditional** (“If price stays above X, investors can …; if it breaks below Y, reassess …”), not absolute.

### 4.2 For Short‑Term Traders

Give tactical guidance derived **only** from the historical OHLCV:

- Preferred bias: buy‑the‑dip, breakout, mean‑reversion, or stay aside.  
- Typical setups:
  - Dip to support with stabilizing volume.  
  - Breakout above a clear resistance on strong volume.  
  - Conditions under which to avoid longs (e.g., after parabolic run + signs of distribution).

Discuss:

- Approximate stop‑loss ranges (e.g., a few percent below recent support, adjusted to observed volatility).  
- The importance of position sizing given the observed 1‑day volatility.

---

## 5. Constraints and Style

- Do **not** bring in any external price or indicator data (no RSI/MACD from elsewhere unless you can infer their logic qualitatively from the OHLCV).  
- Base everything strictly on the historical file’s Date, Open, High, Low, Close, Change and Volume.  
- Do not restate the full fundamental analysis; only **reference it conceptually** (e.g., “fundamentals are strong/weak”).  
- Finish with a short **Summary Technical View** (1–2 paragraphs) that clearly states:
  - Trend direction  
  - Key support/resistance  
  - Volatility character  
  - Whether technicals broadly **confirm** or **challenge** the existing fundamental thesis.

---