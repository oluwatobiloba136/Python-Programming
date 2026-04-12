import os
import csv
from datetime import datetime
from playwright.sync_api import sync_playwright


# ---------- CONFIG ----------
OUTPUT_DIR = r"C:\NGX\DailyInvest"
os.makedirs(OUTPUT_DIR, exist_ok=True)

URL = (
    "https://api.investing.com/api/financialdata/assets/equitiesByCountry/default"
    "?fields-list=id%2Cname%2Csymbol%2CisCFD%2Chigh%2Clow%2Clast%2ClastPairDecimal"
    "%2Cchange%2CchangePercent%2Cvolume%2Ctime%2CisOpen%2Curl%2Cflag%2CcountryNameTranslated"
    "%2CexchangeId%2CperformanceDay%2CperformanceWeek%2CperformanceMonth%2CperformanceYtd"
    "%2CperformanceYear%2Cperformance3Year%2CtechnicalHour%2CtechnicalDay%2CtechnicalWeek"
    "%2CtechnicalMonth%2CavgVolume%2CfundamentalMarketCap%2CfundamentalRevenue"
    "%2CfundamentalRatio%2CfundamentalBeta%2CpairType"
    "&country-id=20&filter-domain=&page=0&page-size=100&limit=0"
    "&include-additional-indices=false&include-major-indices=false"
    "&include-other-indices=false&include-primary-sectors=false"
    "&include-market-overview=false"
)


def main():
    with sync_playwright() as p:
        # Launch real Chromium browser
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Let the browser make the API request
        resp = page.request.get(URL)
        print("Status:", resp.status)
        if resp.status != 200:
            raise RuntimeError(f"HTTP status {resp.status} from Investing.com")

        data = resp.json()

        # Adjust this once you inspect the structure
        if isinstance(data, dict) and "data" in data:
            records = data["data"]
        elif isinstance(data, dict) and "assets" in data:
            records = data["assets"]
        elif isinstance(data, list):
            records = data
        else:
            records = []

        if not records:
            print("No records returned.")
            browser.close()
            return

        # Choose fields – must exist in the JSON
        fields = [
            "id", "name", "symbol", "isCFD", "high", "low", "last",
            "lastPairDecimal", "change", "changePercent", "volume", "time",
            "isOpen", "url", "flag", "countryNameTranslated", "exchangeId",
            "performanceDay", "performanceWeek", "performanceMonth",
            "performanceYtd", "performanceYear", "performance3Year",
            "technicalHour", "technicalDay", "technicalWeek",
            "technicalMonth", "avgVolume", "fundamentalMarketCap",
            "fundamentalRevenue", "fundamentalRatio", "fundamentalBeta",
            "pairType",
        ]

        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_path = os.path.join(OUTPUT_DIR, f"tradeview_{ts}.csv")

        with open(out_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            for r in records:
                row = {k: r.get(k, "") for k in fields}
                writer.writerow(row)

        print(f"Saved {len(records)} rows to {out_path}")

        browser.close()


if __name__ == "__main__":
    main()