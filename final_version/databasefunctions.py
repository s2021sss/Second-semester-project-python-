import sqlite3 as sq
"""
Функция осуществляет поиск по базе данных и выдает названия завтраков
"""
def name_zavtrak():
    with sq.connect("recipes") as con:
        cur = con.cursor()
        str_zavtrak=""
        cur.execute("SELECT dish FROM rs WHERE type = 1")
        for result in cur:
             str_zavtrak=str_zavtrak+str(result[0])+", "
        return str_zavtrak
"""
Функция выдает состав и рецепт выбранного завтрака
"""
def choice_zavtrak(choice):
    with sq.connect("recipes") as con:
        cur = con.cursor()
   
        cur.execute("SELECT dish,structure, recipe FROM rs WHERE type = 1")
        
        for result in cur:
            if choice in result:
                recipe_of_choice=result
        return recipe_of_choice

"""
Функция осуществляет поиск по базе данных и выдает названия обедов
"""
def name_obed():
    with sq.connect("recipes") as con:
        cur = con.cursor()
        str_zavtrak=""
        cur.execute("SELECT dish FROM rs WHERE type = 2")
        for result in cur:
             str_zavtrak=str_zavtrak+str(result[0])+", "
        return str_zavtrak
"""
Функция выдает состав и рецепт выбранного обеда
"""
def choice_obed(choice):
    with sq.connect("recipes") as con:
        cur = con.cursor()
   
        cur.execute("SELECT dish,structure, recipe FROM rs WHERE type = 2")
        
        for result in cur:
            if choice in result:
                recipe_of_choice=result
        return recipe_of_choice

"""
Функция осуществляет поиск по базе данных и выдает названия ужинов
"""
def name_uzhin():
    with sq.connect("recipes") as con:
        cur = con.cursor()
        str_zavtrak=""
        cur.execute("SELECT dish FROM rs WHERE type = 3")
        for result in cur:
             str_zavtrak=str_zavtrak+str(result[0])+", "
        return str_zavtrak
"""
Функция выдает состав и рецепт выбранного ужина
"""    
def choice_uzhin(choice):
    with sq.connect("recipes") as con:
        cur = con.cursor()
   
        cur.execute("SELECT dish,structure, recipe FROM rs WHERE type = 3")
        
        for result in cur:
            if choice in result:
                recipe_of_choice=result
        return recipe_of_choice
    
"""
Функция осуществляет поиск по базе данных и выдает названия десертов
"""
def name_desert():
    with sq.connect("recipes") as con:
        cur = con.cursor()
        str_zavtrak=""
        cur.execute("SELECT dish FROM rs WHERE type = 4")
        for result in cur:
             str_zavtrak=str_zavtrak+str(result[0])+", "
        return str_zavtrak
"""
Функция выдает состав и рецепт выбранного десерта
"""    
def choice_desert(choice):
    with sq.connect("recipes") as con:
        cur = con.cursor()
   
        cur.execute("SELECT dish,structure, recipe FROM rs WHERE type = 4")
        
        for result in cur:
            if choice in result:
                recipe_of_choice=result
        return recipe_of_choice
"""
Функция осуществляет поиск по базе данных и выдает все блюда, в состав которых входит введенный ингредиент
"""
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
"""
Функция выдает состав и рецепт выбранного блюда
"""
def choice_ingred(choice):
    with sq.connect("recipes") as con:
        cur = con.cursor()
   
        cur.execute("SELECT dish,structure, recipe FROM rs")
        for result in cur:
            if choice in result:
                recipe_of_choice=result
        return recipe_of_choice
