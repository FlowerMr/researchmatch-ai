import json

from database.db import (
    conn,
    cursor
)

def save_report(report):

    cursor.execute(
        """
        INSERT INTO reports(report)
        VALUES(?)
        """,
        [json.dumps(report)]
    )

    conn.commit()

    return True