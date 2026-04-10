import os
from datetime import datetime

import requests
import pandas as pd

# --------------------------------------------------------------
# Configuration (from your M code)
# --------------------------------------------------------------
BASE_URL = "https://www.ngxpulse.ng"
API_KEY = "ngxpulse_lsv623iy4mh9do9j"

OUTPUT_DIR = r"C:\NGX\DailyStocksDisclosure"   # target folder for CSV


# --------------------------------------------------------------
# Fetch data
# --------------------------------------------------------------
url = f"{BASE_URL}/api/ngxdata/disclosures"
headers = {
    "X-API-Key": API_KEY,
    "Accept": "application/json",
}

response = requests.get(url, headers=headers)
response.raise_for_status()
source = response.json()

# --------------------------------------------------------------
# Normalise response to list
# --------------------------------------------------------------
if isinstance(source, list):
    disclosures_list = source
elif isinstance(source, dict) and "disclosures" in source:
    disclosures_list = source["disclosures"]
elif isinstance(source, dict) and "data" in source:
    disclosures_list = source["data"]
else:
    raise ValueError("Unexpected API response format.")

df = pd.DataFrame(disclosures_list)

# --------------------------------------------------------------
# Transformations equivalent to your M code
# --------------------------------------------------------------
text_cols = [
    "symbol",
    "company",
    "title",
    "category",
    "type",
    "description",
    "document_url",
    "link",
    "source",
]

# Ensure text columns exist
for col in text_cols:
    if col not in df.columns:
        df[col] = None

# Clean text (trim)
for col in text_cols:
    df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

# Blank text to null
for col in text_cols:
    df[col] = df[col].apply(lambda x: None if (isinstance(x, str) and x == "") else x)

# Uppercase symbol
if "symbol" in df.columns:
    df["symbol"] = df["symbol"].apply(
        lambda x: x.upper() if isinstance(x, str) else x
    )

# Date-only columns
for col in ["date", "published_at", "disclosure_date"]:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce", utc=True).dt.date

# Datetime columns
for col in ["created", "modified", "created_at", "updated_at"]:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce", utc=True)

# --------------------------------------------------------------
# Write to CSV: C:\NGX\DailyStocksDisclosure\ngxmkt_disclosures_TIMESTAMP.csv
# --------------------------------------------------------------
os.makedirs(OUTPUT_DIR, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"ngxmkt_disclosures_{timestamp}.csv"
filepath = os.path.join(OUTPUT_DIR, filename)

df.to_csv(filepath, index=False, encoding="utf-8")

print(f"Saved {len(df)} rows to {filepath}")