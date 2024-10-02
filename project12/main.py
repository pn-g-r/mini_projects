import sqlite3
import os

dbfile = 'project12/data.db'

conn = sqlite3.connect(dbfile)
cursor = conn.cursor()

query = """
SELECT * FROM albums
WHERE Title LIKE '%Live%' AND LENGTH(Title) > 10
"""

cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()