import sqlite3 as sq

with sq.connect("recipes") as con:
    cur = con.cursor()
    view = input ("Выберите: ")
    cur.execute("SELECT dish, structure FROM rs")
    
    for structure in cur:
            for i in structure:
                if view in i:
                    print(structure)
                    print("\n")
                    print("Уточните блюдо которое хотите выбрать")

with sq.connect("recipes") as con:
    cur = con.cursor()
    
    choice = input ("Уточните выбор: ")
    cur.execute("SELECT dish, structure, recipe FROM rs")
    
    for structure in cur:
        if choice in structure:
            print(structure)
            
