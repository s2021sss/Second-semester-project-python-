import sqlite3 as sq


with sq.connect("recipes") as con:
    cur = con.cursor()
    
    lst=input()
    lstDone=lst.split(",")
    spisok="SELECT dish,structure,recipe FROM rs WHERE "
    
    for i in lstDone:
        spisok = spisok + "structure like" + " "+ f"'%{i}%'"
        if (lstDone[-1]!=i):
            spisok = spisok + " AND "
    
    cur.execute(spisok)
    
    for result in cur:
        print(result)
        

