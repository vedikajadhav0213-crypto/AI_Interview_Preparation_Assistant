import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

questions = [
    ("Python", "Easy", "What is Python?", "Python is a high-level programming language."),

    ("Python", "Medium", "Explain OOP in Python.", "OOP stands for Object-Oriented Programming."),

    ("Python", "Easy", "What is a List?", "A list is a mutable collection."),

    ("SQL", "Easy", "What is SQL?", "SQL is a language used to manage databases."),

    ("SQL", "Medium", "What is JOIN?", "JOIN combines rows from two or more tables."),

    ("Flask", "Easy", "What is Flask?", "Flask is a lightweight Python web framework."),

    ("Machine Learning", "Medium", "What is Machine Learning?", "Machine Learning enables computers to learn from data.")
]

cursor.executemany(
    """
    INSERT INTO questions(category, difficulty, question, answer)
    VALUES (?, ?, ?, ?)
    """,
    questions
)

conn.commit()
conn.close()

print("Questions inserted successfully!")