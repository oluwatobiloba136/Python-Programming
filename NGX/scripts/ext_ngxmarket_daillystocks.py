import requests
import pandas as pd

# Configuration – taken directly from your M code
BASE_URL = "https://www.ngxpulse.ng"
RELATIVE_PATH = "/api/ngxdata/stocks"
API_KEY = "ngxpulse_lsv623iy4mh9do9j"

# Build the request URL and headers
url = f"{BASE_URL}{RELATIVE_PATH}"
headers = {
    "X-API-Key": API_KEY,
    "Accept": "application/json"
}

# Fetch the data
response = requests.get(url, headers=headers)
response.raise_for_status()  # Will raise an exception for non‑200 responses
data = response.json()

# Normalize the response to a list of stock records (handles both list and dict formats)
if isinstance(data, list):
    stocks = data
elif isinstance(data, dict) and "stocks" in data:
    stocks = data["stocks"]
else:
    raise ValueError("Unexpected API response format.")

# Convert to DataFrame
df = pd.DataFrame(stocks)

# Define expected columns based on your M code
numeric_cols = ["current_price", "previous_close", "change_percent", "pct_change_7d",
                "volume", "market_cap", "shares_outstanding"]
text_cols = ["symbol", "name", "sector", "market"]
date_col = "trade_date"

# Ensure all expected columns exist (fill missing with appropriate defaults)
for col in numeric_cols:
    if col not in df.columns:
        df[col] = 0
for col in text_cols:
    if col not in df.columns:
        df[col] = None
if date_col not in df.columns:
    df[date_col] = None

# Clean and type‑convert the data
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

for col in text_cols:
    if col in df.columns:
        df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

if "symbol" in df.columns:
    df["symbol"] = df["symbol"].apply(lambda x: x.upper() if isinstance(x, str) else x)

if date_col in df.columns:
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce', utc=True).dt.date

for col in text_cols:
    if col in df.columns:
        df[col] = df[col].apply(lambda x: None if (isinstance(x, str) and x == "") else x)

# Print the result to the terminal (as requested)
print(df.to_string(index=False))