from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_cnn_headlines():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    url = "https://edition.cnn.com/world"
    driver.get(url)
    time.sleep(4)

    articles = []

    try:
        headlines = driver.find_elements(
            By.XPATH, "//a[.//span[@class='container__headline-text']]"
        )
        print("Found", len(headlines), "headline links")

        # Phase 1: collect titles & links first
        raw_articles = []
        for h in headlines[:10]:
            title = h.text.strip()
            link = h.get_attribute("href")
            if title and link and link.startswith("http"):
                raw_articles.append((title, link))

        # Phase 2: go visit each article
        for title, link in raw_articles:
            description = ""
            pub_date = ""

            try:
                driver.get(link)
                time.sleep(2)

                # Description
                try:
                    desc_tag = driver.find_element(By.XPATH, "//p[contains(@class, 'vossi-paragraph')]")
                    description = desc_tag.text.strip()
                except:
                    description = ""

                # Date
                try:
                    date_tag = driver.find_element(By.XPATH, "//div[contains(@class, 'vossi-timestamp')]")
                    pub_date = date_tag.text.strip()
                except:
                    pub_date = ""

                print("Scraping:", title)
                print("Link:", link)
                print("Date:", pub_date)
                print("Desc:", description[:80], "..." if len(description) > 80 else "")
                print("-" * 50)

            except Exception as e:
                print(f"Error loading article: {e}")

            articles.append({
                "title": title,
                "link": link,
                "pub_date": pub_date,
                "description": description
            })

    except Exception as e:
        print(f"CNN scrape error: {e}")

    driver.quit()
    return articles

