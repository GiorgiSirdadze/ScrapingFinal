# 📖 User Guide

## Setup

Install all dependencies:

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -m textblob.download_corpora
```

## Crawling TechCrunch First (Scrapy)

```bash
cd src/scrapers
scrapy crawl techcrunch -o techcrunch.json
cd ../../../
```

## Using the App

Run:

```bash
python main.py
```

Then use the interactive menu:

```
1. Scrape all sources
2. Run advanced analysis
3. Export data
4. Generate charts and HTML report
5. Exit
```

## Output Files

- `news.db`: local SQLite database
- `data_output/reports/articles.csv/json/xlsx`: exports
- `data_output/reports/plots/*.png`: chart images
- `data_output/reports/report.html`: summary report
