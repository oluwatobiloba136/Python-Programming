import os
from datetime import datetime

import requests
import pandas as pd

# --------------------------------------------------------------
# Configuration
# --------------------------------------------------------------
URL = "https://doclib.ngxgroup.com/REST/api/issuers/companydirectory"
OUTPUT_DIR = r"C:\NGX\DailyStocksCompanies"

HEADERS = {
    "Accept": "application/json, odata, */*; q=0.01",
    "Content-Type": "application/json, odata, */*; q=0.01",
    "Origin": "https://ngxgroup.com",
    "Referer": "https://ngxgroup.com/exchange/data/company-profile/",
    "User-Agent": "Mozilla/5.0",
}

PARAMS = {
    "$orderby": "CompanyName"
}

# --------------------------------------------------------------
# Fetch data
# --------------------------------------------------------------
resp = requests.get(URL, headers=HEADERS, params=PARAMS)
resp.raise_for_status()
source = resp.json()

# --------------------------------------------------------------
# Normalise JSON to list of records
# --------------------------------------------------------------
if isinstance(source, list):
    data = source
elif isinstance(source, dict) and "value" in source:
    data = source["value"]
else:
    raise ValueError("Unexpected API response format.")

df = pd.DataFrame(data)

# --------------------------------------------------------------
# Keep only required columns
# --------------------------------------------------------------
cols = [
    "InternationSecIN",
    "Symbol",
    "PrevClose",
    "OpenPrice",
    "DaysHigh",
    "DaysLow",
    "Volume",
    "Value",
    "MarketCap",
    "SharesOutstanding",
    "Dividend",
    "Yield",
    "Sector",
    "SubSector",
    "CompanyName",
    "MarketClassification",
    "DateListed",
    "DateOfIncorporation",
    "Website",
    "Logourl",
    "StockPricePercChange",
    "StockPriceChange",
    "StockPriceCur",
    "CompanyProfileSummary",
    "NatureofBusiness",
    "CompanyAddress",
    "Telephone",
    "Fax",
    "Email",
    "CompanySecretary",
    "Auditor",
    "Registrars",
    "BoardOfDirectors",
    "ID",
    "HIGH52WK_PRICE",
    "HIGH52WK_DATETIME",
    "LOW52WK_PRICE",
    "LOW52WK_DATETIME",
    "Symbol2",
    "LS_STD",
    "OFFICIAL_OPEN",
    "OFFICIAL_CLOSE",
]
# keep intersection only to avoid KeyError if API changes
keep = [c for c in cols if c in df.columns]
df = df[keep]

# --------------------------------------------------------------
# Type conversions (approximate to M code)
# --------------------------------------------------------------
numeric_cols = [
    "PrevClose",
    "OpenPrice",
    "DaysHigh",
    "DaysLow",
    "Volume",
    "Value",
    "MarketCap",
    "SharesOutstanding",
    "Dividend",
    "Yield",
    "StockPricePercChange",
    "StockPriceChange",
    "StockPriceCur",
    "HIGH52WK_PRICE",
    "LOW52WK_PRICE",
    "OFFICIAL_OPEN",
    "OFFICIAL_CLOSE",
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

int_cols = ["Volume", "MarketCap", "SharesOutstanding", "ID"]
for col in int_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

# Date conversions
date_cols_from_tz = [
    "DateListed",
    "DateOfIncorporation",
    "HIGH52WK_DATETIME",
    "LOW52WK_DATETIME",
]
for col in date_cols_from_tz:
    if col in df.columns:
        # try with timezone then plain date
        dt = pd.to_datetime(df[col], errors="coerce", utc=True)
        # if all NaT, try without utc
        if dt.isna().all():
            dt = pd.to_datetime(df[col], errors="coerce")
        df[col] = dt.dt.date

# --------------------------------------------------------------
# Reorder columns
# --------------------------------------------------------------
order = [
    "ID",
    "Symbol",
    "Symbol2",
    "CompanyName",
    "Sector",
    "SubSector",
    "MarketClassification",
    "InternationSecIN",
    "DateListed",
    "DateOfIncorporation",
    "PrevClose",
    "OpenPrice",
    "DaysHigh",
    "DaysLow",
    "StockPriceCur",
    "StockPriceChange",
    "StockPricePercChange",
    "Volume",
    "Value",
    "MarketCap",
    "SharesOutstanding",
    "Dividend",
    "Yield",
    "HIGH52WK_PRICE",
    "HIGH52WK_DATETIME",
    "LOW52WK_PRICE",
    "LOW52WK_DATETIME",
    "OFFICIAL_OPEN",
    "OFFICIAL_CLOSE",
    "LS_STD",
    "Website",
    "Logourl",
    "Email",
    "Telephone",
    "Fax",
    "CompanyAddress",
    "CompanySecretary",
    "Auditor",
    "Registrars",
    "BoardOfDirectors",
    "CompanyProfileSummary",
    "NatureofBusiness",
]
order = [c for c in order if c in df.columns]
df = df[order]

# --------------------------------------------------------------
# Extract text between [ and ] from Symbol2 -> CSI
# --------------------------------------------------------------
def extract_csi(val):
    if not isinstance(val, str):
        return None
    start = val.find("[")
    end = val.find("]", start + 1)
    if start != -1 and end != -1:
        return val[start + 1 : end]
    return None

if "Symbol2" in df.columns:
    df["CSI"] = df["Symbol2"].apply(extract_csi)
    df = df.rename(columns={"Symbol2": "Symbol2_raw"})

# --------------------------------------------------------------
# Add ExtractDate
# --------------------------------------------------------------
df["ExtractDate"] = datetime.now().date()

# --------------------------------------------------------------
# Write to CSV: C:\NGX\DailyStocksCompanies\ngxmkt_companies_TIMESTAMP.csv
# --------------------------------------------------------------
os.makedirs(OUTPUT_DIR, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"ngxmkt_companies_{timestamp}.csv"
filepath = os.path.join(OUTPUT_DIR, filename)

df.to_csv(filepath, index=False, encoding="utf-8")

print(f"Saved {len(df)} rows to {filepath}")