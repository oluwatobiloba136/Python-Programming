import os
from datetime import datetime

import requests
import pandas as pd

# --------------------------------------------------------------
# Configuration (from your M code)
# --------------------------------------------------------------
URL = "https://doclib.ngxgroup.com/REST/api/statistics/ticker"

OUTPUT_DIR = r"C:\NGX\DailyStocksTickers"   # target folder for CSV

HEADERS = {
    "Accept": "application/json, odata, */*; q=0.01",
    "Content-Type": "application/json, odata, */*; q=0.01",
    "Origin": "https://ngxgroup.com",
    "Referer": "https://ngxgroup.com/exchange/trade/equities/listed-companies/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
}

PARAMS = {
    "filter": "TickerType eq 'EQUITIES'"
}

# --------------------------------------------------------------
# Fetch data
# --------------------------------------------------------------
resp = requests.get(URL, headers=HEADERS, params=PARAMS)
resp.raise_for_status()
js = resp.json()

# --------------------------------------------------------------
# Normalise JSON to list of records
# --------------------------------------------------------------
if isinstance(js, list):
    data = js
elif isinstance(js, dict) and "value" in js:
    data = js["value"]
else:
    raise ValueError("Unexpected API response format.")

df = pd.DataFrame(data)

# Keep only the needed columns
cols = ["Id", "SYMBOL", "Value", "PercChange", "TickerType", "SYMBOL2"]
df = df[cols]

# Cast types
df["Id"] = pd.to_numeric(df["Id"], errors="coerce").astype("Int64")
df["Value"] = pd.to_numeric(df["Value"], errors="coerce")
df["PercChange"] = pd.to_numeric(df["PercChange"], errors="coerce")

df["SYMBOL"] = df["SYMBOL"].astype(str)
df["TickerType"] = df["TickerType"].astype(str)
df["SYMBOL2"] = df["SYMBOL2"].astype(str)

# Extract text between [ and ] from SYMBOL2 -> CSI
def extract_csi(text: str) -> str | None:
    if not isinstance(text, str):
        return None
    start = text.find("[")
    end = text.find("]", start + 1)
    if start != -1 and end != -1:
        return text[start + 1 : end]
    return None

df["CSI"] = df["SYMBOL2"].apply(extract_csi)

# Add ExtractDate = today's date
df["ExtractDate"] = datetime.now().date()

# Drop old SYMBOL2 column if you don't need it
df = df[["Id", "SYMBOL", "Value", "PercChange", "TickerType", "CSI", "ExtractDate"]]

# --------------------------------------------------------------
# Write to CSV: C:\NGX\DailyStocksTickers\ngxmkt_tickers_TIMESTAMP.csv
# --------------------------------------------------------------
os.makedirs(OUTPUT_DIR, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"ngxmkt_tickers_{timestamp}.csv"
filepath = os.path.join(OUTPUT_DIR, filename)

df.to_csv(filepath, index=False, encoding="utf-8")

print(f"Saved {len(df)} rows to {filepath}")