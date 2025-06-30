import sqlite3
import re
from collections import Counter, defaultdict
from textblob import TextBlob
import spacy
from fuzzywuzzy import fuzz

nlp = spacy.load("en_core_web_sm")

DB_PATH = "data_output/news.db"
STOPWORDS = {"the", "and", "in", "on", "to", "of", "for", "a", "is", "at", "with", "by", "an", "as", "from", "that"}

def fetch_articles():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT source, title FROM articles")
    rows = cursor.fetchall()
    conn.close()
    return rows

def clean_title(title):
    title = title.lower()
    title = re.sub(r"[^a-z\s]", "", title)
    return title

def keyword_trends_by_source(articles):
    print("\n🔍 Keyword trends by source:")
    per_source_words = defaultdict(list)

    for source, title in articles:
        words = clean_title(title).split()
        filtered = [w for w in words if w not in STOPWORDS]
        per_source_words[source].extend(filtered)

    for source, words in per_source_words.items():
        print(f"\nTop keywords for {source}:")
        for word, count in Counter(words).most_common(5):
            print(f"  {word}: {count}")

def find_similar_titles(articles, threshold=80):
    print("\n🔗 Cross-source similar headlines:")
    titles_by_source = defaultdict(list)
    for source, title in articles:
        titles_by_source[source].append(title)

    sources = list(titles_by_source.keys())

    for i in range(len(sources)):
        for j in range(i+1, len(sources)):
            src1, src2 = sources[i], sources[j]
            for t1 in titles_by_source[src1]:
                for t2 in titles_by_source[src2]:
                    score = fuzz.token_set_ratio(t1, t2)
                    if score >= threshold:
                        print(f"\n{src1} and {src2} both reported:")
                        print(f"  \"{t1}\"")
                        print(f"  \"{t2}\"")
                        print(f"  (similarity score: {score}%)")

def named_entity_report(articles):
    print("\n🧠 Named Entities in Headlines:")
    entities = defaultdict(Counter)
    for _, title in articles:
        doc = nlp(title)
        for ent in doc.ents:
            entities[ent.label_][ent.text] += 1

    for label in ["PERSON", "ORG", "GPE"]:
        print(f"\nTop {label}s:")
        for ent, count in entities[label].most_common(5):
            print(f"  {ent}: {count}")

def sentiment_analysis(articles):
    print("\n❤️ Sentiment Analysis:")
    sentiment_counts = {"positive": 0, "neutral": 0, "negative": 0}
    negative_titles = []

    for _, title in articles:
        blob = TextBlob(title)
        score = blob.sentiment.polarity

        if score > 0.1:
            sentiment_counts["positive"] += 1
        elif score < -0.1:
            sentiment_counts["negative"] += 1
            negative_titles.append(title)
        else:
            sentiment_counts["neutral"] += 1

    print(f"Positive: {sentiment_counts['positive']}")
    print(f"Neutral: {sentiment_counts['neutral']}")
    print(f"Negative: {sentiment_counts['negative']}")

    print("\nMost negative headlines:")
    for t in negative_titles[:5]:
        print(f"  - {t}")

def run_advanced_analysis():
    articles = fetch_articles()
    keyword_trends_by_source(articles)
    find_similar_titles(articles)
    named_entity_report(articles)
    sentiment_analysis(articles)
