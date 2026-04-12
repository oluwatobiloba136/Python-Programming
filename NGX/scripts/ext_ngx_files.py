import requests
import sys
import os
import csv
from datetime import datetime

# --------------------------------------------------------------
# USER‑CONFIGURABLE SETTINGS
# --------------------------------------------------------------
BASE_URL = "https://doclib.ngxgroup.com"          # NGX SharePoint site
ISIN = "NGACCESS0005"                             # <-- set the ISIN of the target company

# Root output directory for all companies
OUTPUT_ROOT_DIR = r"C:\NGX\ListedCompanies"

# List of Type_of_Submission values you want to retrieve.
TYPES_OF_INTEREST = [
    "Corporate Actions",
    "Corporate Disclosures",
    "Financial Statements",
    "EarningForcast",
    "DirectorsDealings",
    "Directors Dealings",
    # Add/remove items as needed for other companies.
]

# Optional: map specific types to short category labels for the CSV.
def categorize(type_field: str) -> str:
    """Return a short label for the given Type_of_Submission."""
    if not type_field:
        return ""
    tf = type_field.strip()
    if tf == "Financial Statements":
        return "Financial Statement"
    if tf == "Corporate Disclosures":
        return "Company Disclosure"
    if tf in ("DirectorsDealings", "Directors Dealings"):
        return "Director Dealings"
    return ""

# --------------------------------------------------------------
# INTERNAL LOGIC
# --------------------------------------------------------------
def build_endpoint(isin: str, types: list) -> str:
    """Construct the SharePoint REST API query string."""
    exact_conditions = " or ".join([f"Type_of_Submission eq '{t}'" for t in types])
    meeting_condition = "substringof('Meeting',Type_of_Submission)"
    filter_expr = f"({exact_conditions} or {meeting_condition})"

    endpoint = (
        f"/_api/Web/Lists/GetByTitle('XFinancial_News')/items/"
        f"?$select=URL,Modified,InternationSecIN,Type_of_Submission"
        f"&$orderby=Modified desc"
        f"&$filter=InternationSecIN eq '{isin}' and {filter_expr}"
    )
    return endpoint

HEADERS = {"Accept": "application/json;odata=verbose"}  # Add auth headers if needed

def extract_url_value(url_field):
    """Return the plain URL string from SharePoint's URL field."""
    if isinstance(url_field, dict) and "Url" in url_field:
        return url_field["Url"]
    return url_field if isinstance(url_field, str) else None

def fetch_all_items(session, url):
    """Yield all list items from a SharePoint REST endpoint, handling pagination."""
    while url:
        try:
            resp = session.get(url, headers=HEADERS)
            resp.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}", file=sys.stderr)
            break
        data = resp.json()
        items = data.get("d", {}).get("results", [])
        for item in items:
            yield item
        url = data.get("d", {}).get("__next")  # pagination link

def main():
    # Prepare output folder for this ISIN under C:\NGX\ListedCompanies\<ISIN>
    company_folder = os.path.join(OUTPUT_ROOT_DIR, ISIN)
    os.makedirs(company_folder, exist_ok=True)

    endpoint = build_endpoint(ISIN, TYPES_OF_INTEREST)
    full_url = BASE_URL + endpoint
    print(f"Requesting: {full_url}\n")

    rows = []
    with requests.Session() as session:
        for item in fetch_all_items(session, full_url):
            url_field = item.get("URL")
            url_str = extract_url_value(url_field)
            type_field = item.get("Type_of_Submission")
            category = categorize(type_field)
            if url_str:
                rows.append([url_str, category])

    # Build filename: ISIN&NGXNEWS&TIMESTAMP
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{ISIN}_NGXNEWS_{timestamp}.csv"
    filepath = os.path.join(company_folder, filename)

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["URL", "Category"])   # header
        writer.writerows(rows)

    print(f"Saved {len(rows)} rows to {filepath}")

if __name__ == "__main__":
    if ISIN == "YOUR_ISIN_HERE":
        print("Error: Please set the ISIN variable before running.", file=sys.stderr)
        sys.exit(1)
    main()