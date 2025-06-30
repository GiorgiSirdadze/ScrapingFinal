import sqlite3
from src.utils.config import load_config



def init_db():
    cfg = load_config()
    conn = sqlite3.connect(cfg["database"])
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            title TEXT,
            link TEXT UNIQUE,
            pub_date TEXT,
            description TEXT
        )
    """)
    
    conn.commit()
    conn.close()

def save_articles(articles, source_name):
    cfg = load_config()
    conn = sqlite3.connect(cfg["database"])
    cursor = conn.cursor()

    for article in articles:
        try:
            cursor.execute("""
                INSERT OR IGNORE INTO articles (source, title, link, pub_date, description)
                VALUES (?, ?, ?, ?, ?)
            """, (
                source_name,
                article["title"],
                article["link"],
                article["pub_date"],
                article["description"]
            ))
        except Exception as e:
            print(f"Insert error: {e}")

    conn.commit()
    conn.close()


import sqlite3
from src.utils.config import load_config

def clear_articles_table():
    cfg = load_config()
    conn = sqlite3.connect(cfg["database"])
    cursor = conn.cursor()

    cursor.execute("DELETE FROM articles")  # Deletes all rows
    conn.commit()
    conn.close()
    print("✅ All rows deleted from 'articles' table.")
