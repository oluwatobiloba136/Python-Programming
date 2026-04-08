from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import csv

BASE_URL = "https://ngxgroup.com"
html_file = "company-profile.html"  # change to your saved filename

with open(html_file, "r", encoding="utf-8", errors="ignore") as f:
    soup = BeautifulSoup(f, "html.parser")

doc_ext_pattern = re.compile(r"\.(pdf|docx?|xls[xm]?|pptx?)$", re.IGNORECASE)

financial_kw = [
    "financial statement",
    "financial statements",
    "financials",
    "results",
    "full year",
    "half year",
    "annual report",
    "quarterly report",
    "q1", "q2", "q3", "q4",
    "interim report",
]

disclosure_kw = [
    "corporate disclosure",
    "corporate disclosures",
    "disclosure",
    "corporate action",
    "corporate actions",
    "announcement",
    "press release",
    "notice",
]

director_kw = [
    "director dealings",
    "directors' dealings",
    "directors dealings",
    "director's dealings",
    "insider dealing",
    "insider dealings",
    "insider transaction",
    "insider transactions",
    "share dealing",
    "share dealings",
]

def contains_any(text: str, words) -> bool:
    if not text:
        return False
    t = text.lower()
    return any(w in t for w in words)

def classify(text: str, url: str) -> str:
    target = (text or "").lower() + " " + (url or "").lower()
    if contains_any(target, financial_kw):
        return "Financial Statements"
    if contains_any(target, disclosure_kw):
        return "Corporate Disclosures"
    if contains_any(target, director_kw):
        return "Director Dealings"
    return "Unclassified"

results = []

for a in soup.find_all("a", href=True):
    href = a["href"].strip()
    text = (a.get_text(strip=True) or "").strip()

    full_url = urljoin(BASE_URL, href)

    if not doc_ext_pattern.search(full_url):
        continue

    cat = classify(text, full_url)
    if cat == "Unclassified":
        continue

    results.append((cat, text or "(no text)", full_url))

seen = set()
unique = []
for cat, txt, url in results:
    if url not in seen:
        seen.add(url)
        unique.append((cat, txt, url))

print("Found", len(unique), "matching document links.")

for cat, txt, url in unique:
    print(f"[{cat}] {txt} -> {url}")

csv_file = "ngx_docs.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["category", "link_text", "url"])
    writer.writerows(unique)

print(f"\nWritten to {csv_file}")