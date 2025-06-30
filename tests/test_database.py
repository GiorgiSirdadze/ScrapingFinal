import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))


import unittest
import os
import sqlite3
from src.data.database import init_db, save_articles
from src.utils.config import load_config

class TestDatabase(unittest.TestCase):

    def setUp(self):
        # Use a test database
        self.cfg = load_config()
        self.cfg["database"] = "test_articles.db"
        with open("src/utils/config.json", "w") as f:
            import json
            json.dump(self.cfg, f)
        init_db()

    def tearDown(self):
        if os.path.exists("test_articles.db"):
            os.remove("test_articles.db")

    def test_save_and_query_articles(self):
        dummy_data = [{
            "title": "Test Article",
            "link": "http://example.com/test",
            "pub_date": "2025-06-29",
            "description": "Test description"
        }]
        save_articles(dummy_data, "TestSource")

        conn = sqlite3.connect(self.cfg["database"])
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE source = 'TestSource'")
        rows = cursor.fetchall()
        conn.close()

        self.assertEqual(len(rows), 1)
        self.assertIn("Test Article", rows[0])

if __name__ == '__main__':
    unittest.main()
