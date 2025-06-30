from concurrent.futures import ThreadPoolExecutor
from src.data.database import init_db, save_articles
from src.scrapers.static_scraper import scrape_bbc_rss
from src.scrapers.selenium_scraper import scrape_cnn_headlines
from src.analysis.statistics import run_advanced_analysis
from src.analysis.exporter import export_articles
from src.analysis.reports import generate_charts, generate_html_report
import json
import os
import time

def load_techcrunch_articles():
    path = "src/scrapers/tc_crawler/techcrunch.json"
    if not os.path.exists(path):
        print("❌ TechCrunch JSON not found. Run `scrapy crawl techcrunch` first.")
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def scrape_all():
    init_db()

    print("🧵 Scraping BBC and CNN in parallel...")
    with ThreadPoolExecutor() as executor:
        bbc_future = executor.submit(scrape_bbc_rss)
        cnn_future = executor.submit(scrape_cnn_headlines)

        bbc = bbc_future.result()
        cnn = cnn_future.result()

    print(f"📰 BBC: {len(bbc)} articles scraped.")
    save_articles(bbc, "BBC")

    print(f"📰 CNN: {len(cnn)} articles scraped.")
    save_articles(cnn, "CNN")

    tc = load_techcrunch_articles()
    print(f"📰 TechCrunch: {len(tc)} articles loaded from JSON.")
    save_articles(tc, "TechCrunch")

def show_menu():
    while True:
        print("\n📋 What would you like to do?")
        print("1. Scrape all sources")
        print("2. Run advanced analysis")
        print("3. Export data (CSV, JSON, Excel)")
        print("4. Generate charts and HTML report")
        print("5. Exit")

        choice = input("Enter your choice (1–5): ").strip()

        if choice == "1":
            scrape_all()
        elif choice == "2":
            run_advanced_analysis()
        elif choice == "3":
            export_articles()
        elif choice == "4":
            generate_charts()
            generate_html_report()
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            time.sleep(1)
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    show_menu()
