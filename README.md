# News Scraping & Analysis Project

## 📰 Overview

This project is a Python-based multi-source news scraping and analysis system. It collects article data from three major websites using different scraping techniques and provides insightful analysis through charts, summaries, and automated reports.

---

## ✅ Features

- Scrapes data from:
  - BBC (RSS Feed - static)
  - CNN (JavaScript - dynamic via Selenium)
  - TechCrunch (Structured crawler via Scrapy)
- Three scraping techniques:
  - BeautifulSoup4
  - Selenium
  - Scrapy
- Stores articles in a SQLite database
- Advanced data analysis:
  - Keyword trends per source
  - Named Entity Recognition (NER)
  - Sentiment analysis of titles
  - Cross-source similarity detection
- Data export:
  - CSV, JSON, Excel
- Visualizations:
  - Bar chart, Pie chart
  - Auto-generated HTML report
- Interactive CLI interface (menu-based)

---

## 📦 Installation

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -m textblob.download_corpora
```

(Optional)

```bash
pip install .
```

---

## ⚙️ Project Structure

```
final-project/
├── src/
│   ├── scrapers/       # scraping logic and factory pattern
│   ├── data/           # DB interface
│   ├── analysis/       # stats, reports, charts
│   ├── cli/            # CLI logic (optional)
│   └── utils/          # config loader, logger, helpers
├── config/             # YAML settings and sources
├── data_output/        # all exports and reports
├── scrapy_crawler/     # Scrapy project for TechCrunch
├── docs/               # architecture, guide, API ref
├── tests/              # unit tests
├── main.py             # entry point (interactive CLI)
├── setup.py            # package installer (optional)
└── requirements.txt
```

---

## 🚀 Usage

### 1. Run Scrapy crawler first:

```bash
cd src/scrapers
scrapy crawl techcrunch -o techcrunch.json
cd ../../../
```

### 2. Launch the CLI

```bash
python main.py
```

Then choose an option:

```
1. Scrape all sources
2. Run advanced analysis
3. Export data
4. Generate charts and HTML report
5. Exit
```

---

## 📊 Output

- `news.db`: stored articles (SQLite)
- `data_output/reports/articles.csv/json/xlsx`: exports
- `data_output/reports/plots/`: chart images
- `data_output/reports/report.html`: auto-generated report

---

## 🧪 Testing

Run unit tests:

```bash
pytest tests/
```

Includes:

- DB creation test
- Table existence check

---

## 📄 Documentation

See `docs/` folder:

- `architecture.md`
- `user_guide.md`
- `api_reference.md`

---

## 👨‍💻 Author

Made with ❤️ by **Giorgi**  
Part of the final project for Python Data Scraping course (2025)

---

## ✅ Status

**COMPLETE** — all project requirements from the PDF have been satisfied and exceeded.

---

## 🏁 Final Notes

- Factory pattern is used for scraper selection
- Configuration via YAML
- Designed with modularity and clarity
- Easy to demo live or record

> "Three websites. Three scraping methods. One clean pipeline."
