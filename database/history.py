import sqlite3
import json

def get_reports():

    conn = sqlite3.connect(
        "researchmatch.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM reports ORDER BY id DESC"
    )

    rows = cursor.fetchall()

    result = []

    for row in rows:

        result.append(
            {
                "id": row[0],
                "report": json.loads(row[1])
            }
        )

    return result