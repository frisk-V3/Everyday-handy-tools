import json
import qrcode
import io
import sqlite3
import numpy as np

# JSON整形
def format_json(text):
    try:
        return json.dumps(json.loads(text), indent=4, ensure_ascii=False)
    except: return "無効なJSON"

# QR生成
def make_qr(text):
    qr = qrcode.make(text)
    buf = io.BytesIO()
    qr.save(buf, format="PNG")
    return buf.getvalue()

# Todo (SQLite)
class TodoDB:
    def __init__(self):
        self.conn = sqlite3.connect("todo.db", check_same_thread=False)
        self.conn.execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, task TEXT)")
    def add(self, task):
        self.conn.execute("INSERT INTO todos (task) VALUES (?)", (task,))
        self.conn.commit()
    def get(self):
        return self.conn.execute("SELECT * FROM todos").fetchall()
