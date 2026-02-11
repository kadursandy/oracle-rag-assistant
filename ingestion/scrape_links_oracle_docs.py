import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

BASE_URL = "https://docs.oracle.com/en-us/iaas/Content/services.htm"

# Headers to mimic a browser (some sites block default Python User-Agent)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/115.0 Safari/537.36"
}

def get_links_from_page(url):
    """Return a list of absolute links from a given URL"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=12)
        response.raise_for_status()
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    links = set()

    for a in soup.find_all("a", href=True):
        href = a.get("href")

        # Normalize to absolute
        full_url = urljoin(url, href)

        # Only include HTTP(S) links
        parsed = urlparse(full_url)
        if parsed.scheme in ["http", "https"]:
            links.add(full_url)

    return list(links)


def main():
    print("➡️ Fetching links from main page…")
    initial_links = get_links_from_page(BASE_URL)

    print(f"✔ Found {len(initial_links)} links on main page:\n")
    for link in initial_links:
        print(link)

    # Optional: Fetch & print links from each sub-page
    print("\n➡️ Fetching links from each sub-page:")
    all_subpage_links = set()

    for link in initial_links:
        time.sleep(1)  # polite delay
        print(f"\n🔹 Sub-page: {link}")
        sub_links = get_links_from_page(link)
        for sl in sub_links:
            print("      ", sl)
            all_subpage_links.add(sl)

    print("\n✔ Total unique links collected from all sub-pages:", len(all_subpage_links))


if __name__ == "__main__":
    main()
