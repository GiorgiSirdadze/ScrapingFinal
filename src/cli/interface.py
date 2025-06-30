import argparse

def parse_cli_args():
    parser = argparse.ArgumentParser(description="📰 News Scraper CLI")
    parser.add_argument("--scrape", action="store_true", help="Scrape articles from all sources")
    parser.add_argument("--analyze", action="store_true", help="Run advanced analysis")
    parser.add_argument("--export", action="store_true", help="Export data to CSV, JSON, Excel")
    parser.add_argument("--report", action="store_true", help="Generate visual report with charts")

    return parser.parse_args()
