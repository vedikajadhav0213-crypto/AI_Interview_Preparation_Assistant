import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill TEXT,
    question TEXT,
    answer TEXT
)
""")

conn.commit()

conn.close()

print("Questions table created successfully!")