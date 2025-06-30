# 🧪 API Reference

## scrapers/static_scraper.py
- `scrape_bbc_rss()` – Fetches BBC RSS articles

## scrapers/selenium_scraper.py
- `scrape_cnn_headlines()` – Scrapes headlines dynamically from CNN

## data/database.py
- `init_db()` – Initializes the DB and table
- `save_articles(articles, source)` – Saves list of articles to DB

## analysis/advanced_analysis.py
- `run_advanced_analysis()` – NER, sentiment, similarity, trends

## analysis/exporter.py
- `export_articles()` – Creates CSV/JSON/Excel exports from DB

## analysis/reports.py
- `generate_charts()` – Plots bar and pie chart
- `generate_html_report()` – Renders report.html with stats + images

## cli/interface.py (no longer used)
- Replaced by interactive `input()`-based menu in `main.py`

## main.py
- Full CLI app entry point with menu options for scrape, analyze, export, and report generation.
