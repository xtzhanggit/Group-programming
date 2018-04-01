import sqlite3

conn = sqlite3.connect('status.db')

cursor = conn.cursor()
cursor.execute("select * from switch")

print(cursor.fetchone())
