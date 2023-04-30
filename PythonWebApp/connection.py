import sqlite3

con = sqlite3.connect("connection.db")
cur = con.cursor()

sql = """
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    address TEXT,
    email TEXT,  -- change "username" to "email"
    password TEXT
)
"""

cur.execute(sql)

con.commit()
con.close()