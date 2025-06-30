from .static_scraper import scrape_bbc_rss
from .selenium_scraper import scrape_cnn_headlines

def scraper_factory(source):
    if source == "BBC":
        return scrape_bbc_rss
    elif source == "CNN":
        return scrape_cnn_headlines
    elif source == "TechCrunch":
        raise NotImplementedError("TechCrunch is handled by Scrapy. Run scrapy crawler separately.")
    else:
        raise ValueError("Unknown source provided to factory.")
