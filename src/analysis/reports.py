import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from pathlib import Path
import re
from collections import Counter



DB_PATH = "data_output/news.db"
IMG_DIR = Path("data_output/reports/plots")
IMG_DIR.mkdir(parents=True, exist_ok=True)

def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM articles", conn)
    conn.close()
    return df

def plot_articles_per_source(df):
    counts = df["source"].value_counts()
    plt.figure(figsize=(8, 5))
    sns.barplot(x=counts.index, y=counts.values, palette="coolwarm")
    plt.title("Articles per Source")
    plt.ylabel("Count")
    plt.xlabel("Source")
    plt.tight_layout()
    path = IMG_DIR / "articles_per_source.png"
    plt.savefig(path)
    print(f"📊 Saved bar chart: {path}")

def plot_sentiment_pie(df):
    sentiments = {"positive": 0, "neutral": 0, "negative": 0}

    for title in df["title"]:
        score = TextBlob(title).sentiment.polarity
        if score > 0.1:
            sentiments["positive"] += 1
        elif score < -0.1:
            sentiments["negative"] += 1
        else:
            sentiments["neutral"] += 1

    labels = sentiments.keys()
    sizes = sentiments.values()
    colors = ['#2ecc71', '#f1c40f', '#e74c3c']

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    plt.title("Headline Sentiment Distribution")
    plt.tight_layout()
    path = IMG_DIR / "sentiment_pie.png"
    plt.savefig(path)
    print(f"📊 Saved pie chart: {path}")

def generate_html_report():
    df = load_data()
    total_articles = len(df)
    source_counts = df["source"].value_counts()

    # get top keywords
    all_titles = " ".join(df["title"].astype(str)).lower()
    words = re.findall(r"\b[a-z]{4,}\b", all_titles)
    stopwords = {"from", "this", "that", "with", "about", "have", "their", "just", "they", "will", "being", "into", "said", "more"}
    filtered = [w for w in words if w not in stopwords]
    top_keywords = Counter(filtered).most_common(10)

    html_path = IMG_DIR.parent / "report.html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write("<html><head><title>News Report</title></head><body style='font-family: Arial;'>\n")
        f.write("<h1>📰 News Scraping Final Report</h1>\n")

        f.write(f"<p><strong>Total Articles:</strong> {total_articles}</p>\n")

        f.write("<h2>📊 Articles per Source</h2><ul>\n")
        for src, count in source_counts.items():
            f.write(f"<li>{src}: {count}</li>\n")
        f.write("</ul>\n")
        f.write("<img src='plots/articles_per_source.png' width='600'>\n")

        f.write("<h2>🧠 Sentiment Analysis</h2>\n")
        f.write("<img src='plots/sentiment_pie.png' width='400'>\n")

        f.write("<h2>🔑 Top Keywords</h2><ul>\n")
        for word, freq in top_keywords:
            f.write(f"<li>{word}: {freq}</li>\n")
        f.write("</ul>\n")

        f.write("<p style='color:gray; font-size:12px;'>Generated automatically using Python</p>\n")
        f.write("</body></html>")

    print(f"📝 HTML report saved at: {html_path}")

def generate_charts():
    df = load_data()
    plot_articles_per_source(df)
    plot_sentiment_pie(df)
