from urllib.request import urlopen, Request
import json
import csv

API_URL = "https://www.ngnmarket.com/api/news/Nigerian%20Exchange%20Group"

# "https://www.ngnmarket.com/api/news/Mtn%20Nigeria%20Communications%20Plc"

AUTH_TOKEN = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
    "eyJzdWIiOiI1NTMiLCJ1c2VyX3V1aWQiOiJiZTVhMzI5OS0zMTdiLTExZjEtOTU3ZS0wMjQyYWMxMjAwMDIiLCJlbWFpbCI6InRvYmkua2F6ZWVtQG91dGxvb2suY29tIiwiaWF0IjoxNzc1NDU0Mjk2LCJleHAiOjE3NzYwNTkwOTZ9."
    "7ASgVxho_YYH8M7wALH4Zmec2-0Ld23K9FPfCSP_MAo"
)

def fetch_json(url: str):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        ),
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Accept": "application/json",
    }
    req = Request(url, headers=headers)
    with urlopen(req, timeout=20) as resp:
        raw = resp.read().decode("utf-8", errors="ignore")
    return json.loads(raw)

def extract_news_urls(root):
    """
    Expected shape:
      {
        "success": true,
        "data": [
          {
            "title": "...",
            "link": "...",
            "source": "...",
            "pubDate": "..."
          },
          ...
        ]
      }
    """
    items = root.get("data") or []
    urls = []

    for item in items:
        if not isinstance(item, dict):
            continue
        title = item.get("title") or ""
        url   = item.get("link") or ""
        date  = item.get("pubDate") or ""
        source = item.get("source") or ""

        if not url:
            continue

        urls.append((title, url, date, source))

    # De‑duplicate by URL
    seen = set()
    unique = []
    for title, url, date, source in urls:
        if url not in seen:
            seen.add(url)
            unique.append((title, url, date, source))
    return unique

def main():
    root = fetch_json(API_URL)
    news = extract_news_urls(root)

    print(f"Found {len(news)} news URLs:\n")
    for title, url, date, source in news:
        label = title or "(no title)"
        src = f" [{source}]" if source else ""
        if date:
            print(f"[{date}]{src} {label} -> {url}")
        else:
            print(f"{label}{src} -> {url}")

    csv_name = "nsegxn_ngnmarket_news_urls.csv"
    with open(csv_name, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["title", "url", "pubDate", "source"])
        w.writerows(news)

    print(f"\nNews URLs written to {csv_name}")

if __name__ == "__main__":
    main()