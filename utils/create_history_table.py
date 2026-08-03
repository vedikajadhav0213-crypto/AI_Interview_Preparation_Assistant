import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS interview_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    interview_score INTEGER,
    ats_score INTEGER,
    interview_date TEXT
)
""")

conn.commit()
conn.close()

print("Interview History Table Created Successfully!")