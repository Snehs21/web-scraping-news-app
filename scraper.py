
import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib.robotparser as robotparser
from sources import SOURCES

HEADERS = {"User-Agent": "Mozilla/5.0"}
DELAY = 2

def allowed_by_robots(url):
    rp = robotparser.RobotFileParser()
    rp.set_url(urljoin(url, "/robots.txt"))
    rp.read()
    return rp.can_fetch("*", url)

def fetch_headlines(source_name, keyword=None):
    source = SOURCES[source_name]
    url = source["url"]

    if not allowed_by_robots(url):
        return []

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    headlines = []

    tags = soup.find_all(
        source["headline_tag"],
        class_=source["headline_class"]
    )

    for tag in tags:
        title = tag.get_text(strip=True)
        if keyword and keyword.lower() not in title.lower():
            continue

        parent = tag.find_parent("a")
        link = urljoin(url, parent["href"]) if parent else None

        headlines.append({
            "Source": source_name.upper(),
            "Title": title,
            "URL": link,
            "Time": None
        })

    time.sleep(DELAY)
    return headlines
