import sqlite3
import json
import os

DB_NAME = "requests.db"

def init_db():
    if not os.path.exists(DB_NAME):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                operation TEXT,
                input_data TEXT,
                result TEXT
            )
        """)
        conn.commit()
        conn.close()

def save_request(operation: str, input_data: dict, result):
    init_db()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO requests (operation, input_data, result)
        VALUES (?, ?, ?)
    """, (operation, json.dumps(input_data), json.dumps(result)))
    conn.commit()
    conn.close()
