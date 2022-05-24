import sqlite3 as sq

with sq.connect("recipes") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE rs (
    type INTEGER,
    dish TEXT,
    structure TEXT,
    recipe TEXT
    )""")