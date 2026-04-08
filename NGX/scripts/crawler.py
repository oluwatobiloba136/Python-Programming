from urllib.request import urlopen, Request
import json
import csv

URL = (
    "https://api.investing.com/api/financialdata/historical/1184444"
    "?start-date=2026-03-08&end-date=2026-04-08"
    "&time-frame=Daily&add-missing-rows=false"
)

def fetch_json(url: str):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json",
    }
    req = Request(url, headers=headers)
    with urlopen(req, timeout=30) as resp:
        raw = resp.read().decode("utf-8", errors="ignore")
    return json.loads(raw)

def main():
    root = fetch_json(URL)

    # Try common containers: "data" or "historical"
    if isinstance(root, dict):
        if "data" in root:
            rows = root["data"]
        elif "historical" in root:
            rows = root["historical"]
        else:
            # If unknown, just bail out with a hint
            print("Unknown JSON structure, top-level keys:", list(root.keys()))
            return
    else:
        rows = root

    # Inspect 1st row to see keys and adjust if needed
    if not rows:
        print("No rows returned")
        return

    # Typical investing-style keys; change these if your JSON differs
    sample = rows[0]
    print("Sample row:", sample)

    # Choose the columns you want
    # Update the list below to match actual keys from 'sample'
    field_order = [
        "date",          # e.g. "2026-04-08"
        "last",          # close/last price
        "open",
        "high",
        "low",
        "change",        # absolute
        "change_percent" # percent
    ]

    # Filter to existing keys only
    field_order = [f for f in field_order if f in sample]

    csv_name = "investing_1184444_daily.csv"
    with open(csv_name, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(field_order)
        for row in rows:
            if not isinstance(row, dict):
                continue
            writer.writerow([row.get(k, "") for k in field_order])

    print(f"Saved {len(rows)} rows to {csv_name}")

if __name__ == "__main__":
    main()