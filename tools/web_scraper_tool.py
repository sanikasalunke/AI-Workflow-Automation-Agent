import requests
from bs4 import BeautifulSoup

def scrape_website(url: str) -> dict:
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    # Remove scripts/styles
    for s in soup(["script", "style"]):
        s.decompose()
    text = soup.get_text(separator="\n")
    snippet = "\n".join([line.strip() for line in text.splitlines() if line.strip()][:40])
    return {"url": url, "snippet": snippet}
