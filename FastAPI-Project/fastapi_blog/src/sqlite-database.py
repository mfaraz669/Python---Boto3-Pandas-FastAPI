import sqlite3
from fastapi import FastAPI
import os

app = FastAPI()

print("Database location:", os.path.abspath("test.db"))

conn = sqlite3.connect("test.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY,
    title TEXT,
    completed TEXT
)
""")

conn.commit()

print("Database and table created!")

@app.get("/")
def home():
    return {"message": "SQLite connected successfully"}