from setuptools import setup, find_packages

setup(
    name="news_scraper",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4",
        "requests",
        "selenium",
        "scrapy",
        "textblob",
        "spacy",
        "pandas",
        "matplotlib",
        "seaborn",
        "fuzzywuzzy",
        "scikit-learn",
        "PyYAML"
    ],
    entry_points={
        "console_scripts": [
            "news-scraper=main:show_menu"
        ]
    }
)
