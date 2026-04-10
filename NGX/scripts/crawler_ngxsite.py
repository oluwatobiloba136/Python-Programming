
# Generated Code
import requests, sys, os, csv
from datetime import datetime

BASE_URL = "https://doclib.ngxgroup.com"
ENDPOINT = (
    "/_api/Web/Lists/GetByTitle('XFinancial_News')/items/"
    "?$select=URL,Modified,InternationSecIN,Type_of_Submission"
    "&$orderby=Modified desc"
    "&$filter=InternationSecIN eq 'NGZENITHBNK9' "
    "and (Type_of_Submission eq 'Corporate Actions' "
    "or Type_of_Submission eq 'Corporate Disclosures' "
    "or substringof('Meeting',Type_of_Submission) "
    "or Type_of_Submission eq 'Financial Statements' "
    "or Type_of_Submission eq 'EarningForcast' "
    "or Type_of_Submission eq 'DirectorsDealings' "
    "or Type_of_Submission eq 'Directors Dealings')"
)
HEADERS = {"Accept": "application/json;odata=verbose"}

def extract_url_value(url_field):
    if isinstance(url_field, dict) and "Url" in url_field:
        return url_field["Url"]
    return url_field if isinstance(url_field, str) else None

def fetch_all_items(session, url):
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
        url = data.get("d", {}).get("__next")

def categorize(type_field):
    if not type_field:
        return ""
    tf = type_field.strip()
    if tf == "Financial Statements":
        return "Financial Statement"
    if tf == "Corporate Disclosures":
        return "Company Disclosure"
    if tf in ("DirectorsDealings", "Directors Dealings"):
        return "Director Dealings"
    return ""  # others left blank

def main():
    with requests.Session() as session:
        full_url = BASE_URL + ENDPOINT
        rows = []
        for item in fetch_all_items(session, full_url):
            url_field = item.get("URL")
            url_str = extract_url_value(url_field)
            type_field = item.get("Type_of_Submission")
            category = categorize(type_field)
            if url_str:
                rows.append([url_str, category])
        
        folder = "zenith"
        os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"ZENITH_{timestamp}.csv"
        filepath = os.path.join(folder, filename)
        
        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["URL", "Category"])
            writer.writerows(rows)
        
        print(f"Saved {len(rows)} rows to {filepath}")

if __name__ == "__main__":
    main()