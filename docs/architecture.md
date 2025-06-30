# 🏧 Project Architecture

## Overview

This project implements a comprehensive data scraping and analysis system designed for collecting, storing, processing, and analyzing news articles from multiple sources. The system targets three high-profile news platforms: BBC, CNN, and TechCrunch. Each platform presents a unique structure and challenge, providing an ideal ground to demonstrate different scraping techniques including static HTML parsing, dynamic content extraction, and structured crawling.

The core goal of the project is to simulate a real-world data engineering and analysis pipeline that can handle thousands of articles, support rich text processing, and generate useful insights. These include named entity extraction, keyword trends, sentiment breakdowns, and cross-source comparisons. In addition, the project emphasizes robust design principles including modularity, reusability, extensibility, and performance optimization.

## Architecture Overview

The project follows a layered, modular structure where each component handles a specific responsibility. Scrapers are organized under `src/scrapers`, while database interaction happens inside `src/data`, and all post-processing analysis is encapsulated under `src/analysis`. The CLI logic and utility modules are cleanly separated for clarity and reusability. YAML configuration files allow settings to be decoupled from code. This structure not only promotes clarity but also makes it easy to extend or refactor individual parts.

```
final-project/
├── src/
│   ├── scrapers/       # BeautifulSoup, Selenium, Scrapy implementations
│   ├── data/           # SQLite DB interaction
│   ├── analysis/       # keyword stats, NER, charts, exports
│   ├── cli/            # command-line menu interface
│   └── utils/          # config loader, logging, text helpers
├── config/             # YAML config files (paths, sources)
├── data_output/        # scraped data, exports, reports, visualizations
├── docs/               # markdown documentation
├── tests/              # unit and integration tests
├── main.py             # interactive CLI entry point
├── requirements.txt    # dependency list
└── setup.py            # optional packaging script
```

## Scraper Logic & Protection Handling

Each news source is scraped using a different method to highlight real-world data extraction complexity:

- **BBC**: Parsed using BeautifulSoup and RSS feed XML. Ideal for static HTML parsing with predictable structure.
- **CNN**: Uses Selenium to automate a browser session (headless Chrome). Required to extract JavaScript-rendered content from CNN’s dynamic homepage.
- **TechCrunch**: Crawled using Scrapy. Utilizes item pipelines and selectors to extract data from multiple article pages with structured yield output.

To address anti-bot protections:

- Random user-agent headers are included.
- Delay and retry logic are built-in.
- The Selenium driver waits for the DOM to fully load.
- CAPTCHA detection fallback logic is documented.

## Data Pipeline Flow

1. **Scraping**: Each scraper fetches article title, link, publication date, and source.
2. **Storing**: Records are inserted into an SQLite DB with one unified table, ensuring relational consistency.
3. **Analyzing**: Analysis functions extract keyword frequency, NER results, sentiment scores, and source similarity.
4. **Exporting**: Results can be exported into CSV, JSON, and XLSX using a strategy pattern.
5. **Reporting**: A full HTML report is rendered with matplotlib/seaborn charts and summary statistics.

## Technologies Used

- **Scraping**:

  - `beautifulsoup4`, `requests`
  - `selenium`, `webdriver-manager`
  - `scrapy`

- **Data Processing**:

  - `pandas`, `numpy`
  - `textblob`, `spacy`
  - `fuzzywuzzy`, `collections.Counter`

- **Visualization**:

  - `matplotlib`, `seaborn`

- **Storage**:

  - `sqlite3`

- **Other**:

  - `concurrent.futures` for multithreading
  - `yaml` for configuration
  - `logging` for status reporting

## Design Patterns

- **Factory Pattern** is used to switch between scraper implementations dynamically.
- **Strategy Pattern** is used to plug in different export formats (CSV, JSON, Excel).

## Concurrency Model

To optimize performance, `ThreadPoolExecutor` is used to run BBC and CNN scrapers concurrently. This minimizes scraping time since the two sources are I/O-bound. TechCrunch scraping is handled asynchronously via Scrapy. The architecture supports future scaling with multiprocessing or queue-based task runners if needed.

## Configuration & Extensibility

The app is highly configurable using external YAML files. These include database paths, export directories, and which sources to scrape. Helper utilities and modular design allow easy addition of new scrapers or exporters.

Future improvements could include:

- Replacing SQLite with PostgreSQL
- Adding live sentiment dashboards
- Integrating scheduling using `cron` or `APScheduler`

## Summary

This architecture showcases a complete, scalable, and maintainable scraping and analysis system. It leverages best practices in software design, Python ecosystem tooling, and data analysis libraries. The final product is robust against site structure changes, handles anti-bot protections gracefully, and offers rich output in the form of interactive CLI, data exports, and HTML reports.
