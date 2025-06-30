import requests
from bs4 import BeautifulSoup

def scrape_bbc_rss():
    url = "http://feeds.bbci.co.uk/news/rss.xml"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "xml")
        items = soup.find_all("item")

        articles = []
        for item in items:
            title = item.title.text
            link = item.link.text
            pub_date = item.pubDate.text
            description = item.description.text

            articles.append({
                "title": title,
                "link": link,
                "pub_date": pub_date,
                "description": description
            })

        return articles

    except Exception as e:
        print(f"BBC scrape error: {e}")
        return []
