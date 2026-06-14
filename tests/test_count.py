import sqlite3

conn = sqlite3.connect("researchmatch.db")

cursor = conn.cursor()

cursor.execute(
    "SELECT COUNT(*) FROM reports"
)

print(
    cursor.fetchone()[0]
)