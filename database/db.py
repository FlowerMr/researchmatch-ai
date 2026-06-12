import sqlite3

conn = sqlite3.connect(
    "researchmatch.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS reports(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    report TEXT
)
""")

conn.commit()