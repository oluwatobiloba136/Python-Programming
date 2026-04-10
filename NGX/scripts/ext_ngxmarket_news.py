import os
from datetime import datetime

import requests
import pandas as pd

# --------------------------------------------------------------
# Configuration (from your M code)
# --------------------------------------------------------------
BASE_URL = "https://www.ngxpulse.ng"
RELATIVE_PATH = "/api/news"
API_KEY = "ngxpulse_lsv623iy4mh9do9j"

OUTPUT_DIR = r"C:\NGX\DailyStocksNews"   # target folder for CSV


# --------------------------------------------------------------
# Fetch data
# --------------------------------------------------------------
url = f"{BASE_URL}{RELATIVE_PATH}"
headers = {
    "X-API-Key": API_KEY,
    "Accept": "application/json",
}

response = requests.get(url, headers=headers)
response.raise_for_status()
data = response.json()

# --------------------------------------------------------------
# Normalise response to list (handles list, {news: [...]}, or {data: [...]})
# --------------------------------------------------------------
if isinstance(data, list):
    news_list = data
elif isinstance(data, dict) and "news" in data:
    news_list = data["news"]
elif isinstance(data, dict) and "data" in data:
    news_list = data["data"]
else:
    raise ValueError("Unexpected API response format.")

df = pd.DataFrame(news_list)

# --------------------------------------------------------------
# Transformations equivalent to your M code
# --------------------------------------------------------------
text_cols = ["title", "link", "description", "image", "source"]

# Ensure text columns exist
for col in text_cols:
    if col not in df.columns:
        df[col] = None

# Trim text
for col in text_cols:
    df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

# Blank text to null
for col in text_cols:
    df[col] = df[col].apply(lambda x: None if (isinstance(x, str) and x == "") else x)

# published_at as date (if present)
if "published_at" in df.columns:
    df["published_at"] = pd.to_datetime(
        df["published_at"], errors="coerce", utc=True
    ).dt.date

# --------------------------------------------------------------
# Write to CSV: C:\NGX\DailyStocksNews\ngxmkt_news_TIMESTAMP.csv
# --------------------------------------------------------------
os.makedirs(OUTPUT_DIR, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"ngxmkt_news_{timestamp}.csv"
filepath = os.path.join(OUTPUT_DIR, filename)

df.to_csv(filepath, index=False, encoding="utf-8")

print(f"Saved {len(df)} rows to {filepath}")