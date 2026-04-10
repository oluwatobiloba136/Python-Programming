import os
from datetime import datetime

import requests
import pandas as pd

# --------------------------------------------------------------
# Configuration (from your M code)
# --------------------------------------------------------------
BASE_URL = "https://www.ngxpulse.ng"
API_KEY = "ngxpulse_lsv623iy4mh9do9j"

OUTPUT_DIR = r"C:\NGX\DailyStocksMkts"   # target folder for CSV


# --------------------------------------------------------------
# Fetch data
# --------------------------------------------------------------
url = f"{BASE_URL}/api/ngxdata/market"
headers = {
    "X-API-Key": API_KEY,
    "Accept": "application/json",
}

response = requests.get(url, headers=headers)
response.raise_for_status()
source = response.json()

# --------------------------------------------------------------
# Normalise: get market record, then its data
# --------------------------------------------------------------
if isinstance(source, dict) and "market" in source:
    market_record = source["market"]
else:
    market_record = source

# Put record into DataFrame
df = pd.DataFrame([market_record])

# If there is a nested "data" record, expand it to columns
if "data" in df.columns:
    data_expanded = pd.json_normalize(df["data"])
    # Prefix-free column names matching your M code
    data_expanded.columns = [c.split(".")[-1] for c in data_expanded.columns]
    df = pd.concat([df.drop(columns=["data"]), data_expanded], axis=1)

# --------------------------------------------------------------
# Types and cleaning – mirroring the M code
# --------------------------------------------------------------
numeric_cols = [
    "asi",
    "pct_change",
    "volume",
    "deals",
    "value",
    "market_cap",
    "advancers",
    "decliners",
    "unchanged",
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

# status text clean
if "status" in df.columns:
    df["status"] = df["status"].apply(
        lambda x: x.strip() if isinstance(x, str) else x
    )

# Dates: date, trade_date, updated_at
for col in ["date", "trade_date"]:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce").dt.date

if "updated_at" in df.columns:
    df["updated_at"] = pd.to_datetime(
        df["updated_at"], errors="coerce", utc=True
    ).dt.date

# --------------------------------------------------------------
# Write to CSV: C:\NGX\DailyStocksMkts\ngxmkt_market_TIMESTAMP.csv
# --------------------------------------------------------------
os.makedirs(OUTPUT_DIR, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"ngxmkt_market_{timestamp}.csv"
filepath = os.path.join(OUTPUT_DIR, filename)

df.to_csv(filepath, index=False, encoding="utf-8")

print(f"Saved {len(df)} rows to {filepath}")