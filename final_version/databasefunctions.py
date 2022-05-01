import sqlite3 as sq

def name_zavtrak():
    with sq.connect("recipes") as con:
        cur = con.cursor()
        str_zavtrak=""
        cur.execute("SELECT dish FROM rs WHERE type = 1")
        for result in cur:
             str_zavtrak=str_zavtrak+str(result[0])+", "
        return str_zavtrak
    
def choice_zavtrak(choice):
    with sq.connect("recipes") as con:
        cur = con.cursor()
   
        cur.execute("SELECT dish,structure, recipe FROM rs WHERE type = 1")
        
        for result in cur:
            if choice in result:
                recipe_of_choice=result
        return recipe_of_choice

def name_obed():
    with sq.connect("recipes") as con:
        cur = con.cursor()
        str_zavtrak=""
        cur.execute("SELECT dish FROM rs WHERE type = 2")
        for result in cur:
             str_zavtrak=str_zavtrak+str(result[0])+", "
        return str_zavtrak
    
def choice_obed(choice):
    with sq.connect("recipes") as con:
        cur = con.cursor()
   
        cur.execute("SELECT dish,structure, recipe FROM rs WHERE type = 2")
        
        for result in cur:
            if choice in result:
                recipe_of_choice=result
        return recipe_of_choice

def name_uzhin():
    with sq.connect("recipes") as con:
        cur = con.cursor()
        str_zavtrak=""
        cur.execute("SELECT dish FROM rs WHERE type = 3")
        for result in cur:
             str_zavtrak=str_zavtrak+str(result[0])+", "
        return str_zavtrak
    
def choice_uzhin(choice):
    with sq.connect("recipes") as con:
        cur = con.cursor()
   
        cur.execute("SELECT dish,structure, recipe FROM rs WHERE type = 3")
        
        for result in cur:
            if choice in result:
                recipe_of_choice=result
        return recipe_of_choice

def name_desert():
    with sq.connect("recipes") as con:
        cur = con.cursor()
        str_zavtrak=""
        cur.execute("SELECT dish FROM rs WHERE type = 4")
        for result in cur:
             str_zavtrak=str_zavtrak+str(result[0])+", "
        return str_zavtrak
    
def choice_desert(choice):
    with sq.connect("recipes") as con:
        cur = con.cursor()
   
        cur.execute("SELECT dish,structure, recipe FROM rs WHERE type = 4")
        
        for result in cur:
            if choice in result:
                recipe_of_choice=result
        return recipe_of_choice
def menu_ingred(lst):
    with sq.connect("recipes") as con:
        cur = con.cursor()
    
        lstDone=lst.split(",")
        spisok="SELECT dish FROM rs WHERE "
    
        for i in lstDone:
            spisok = spisok + "structure like" + " "+ f"'%{i}%'"
            if (lstDone[-1]!=i):
                spisok = spisok + " AND "
    
        cur.execute(spisok)
    
        str_ingred=""
        for result in cur:
            str_ingred=str_ingred+str(result[0])+", "
        return str_ingred

def choice_ingred(choice):
    with sq.connect("recipes") as con:
        cur = con.cursor()
   
        cur.execute("SELECT dish,structure, recipe FROM rs")
        for result in cur:
            if choice in result:
                recipe_of_choice=result
        return recipe_of_choice



