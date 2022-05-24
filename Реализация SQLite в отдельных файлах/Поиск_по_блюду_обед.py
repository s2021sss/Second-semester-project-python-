import sqlite3 as sq

with sq.connect("recipes") as con:
    cur = con.cursor()

    cur.execute("SELECT dish FROM rs WHERE type = 2")
    for result in cur:
        print(result)
        
with sq.connect("recipes") as con:
    cur = con.cursor()
    
    choice=input()
    
    cur.execute("SELECT dish,structure, recipe FROM rs WHERE type = 2")
    
    for result in cur:
        if choice in result:
            print(result) 
