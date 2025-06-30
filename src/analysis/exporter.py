import sqlite3
import pandas as pd
from pathlib import Path
from src.utils.config import load_config

cfg = load_config()

EXPORT_DIR = Path(cfg["export_dir"])
EXPORT_DIR.mkdir(parents=True, exist_ok=True)

def export_articles():
    conn = sqlite3.connect(cfg["database"])
    df = pd.read_sql_query("SELECT * FROM articles", conn)
    conn.close()

    csv_path = EXPORT_DIR / "articles.csv"
    json_path = EXPORT_DIR / "articles.json"
    xlsx_path = EXPORT_DIR / "articles.xlsx"

    df.to_csv(csv_path, index=False)
    df.to_json(json_path, orient="records", indent=2)
    df.to_excel(xlsx_path, index=False)

    print(f"\n✅ Exported {len(df)} articles to:")
    print(f"  - {csv_path}")
    print(f"  - {json_path}")
    print(f"  - {xlsx_path}")
