
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from app.config import BASE_URL, MAX_DEPTH

visited=set()

def crawl(url,depth=0):
    if depth>MAX_DEPTH or url in visited:
        return []
    visited.add(url)
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"html.parser")
    for tag in soup(["script","style","nav","footer"]):
        tag.decompose()
    text=soup.get_text(" ",strip=True)
    results=[(url,text)]
    for a in soup.find_all("a",href=True):
        link=urljoin(url,a["href"])
        if BASE_URL.split("/Content")[0] in link:
            results+=crawl(link,depth+1)
    return results
