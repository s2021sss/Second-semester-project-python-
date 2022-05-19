import sqlite3 as sq

def name_zavtrak():
    """
    Функция осуществляет поиск по базе данных и выдает названия завтраков
    """
    with sq.connect("recipes") as con:
        cur = con.cursor()
        str_zavtrak=""
        cur.execute("SELECT dish FROM rs WHERE type = 1")
        for result in cur:
             str_zavtrak=str_zavtrak+str(result[0])+", "
        return str_zavtrak

def choice_zavtrak(choice):
    """
    Функция выдает состав и рецепт выбранного завтрака
    """
    with sq.connect("recipes") as con:
        cur = con.cursor()
   
        cur.execute("SELECT dish,structure, recipe FROM rs WHERE type = 1")
        
        for result in cur:
            if choice in result:
                recipe_of_choice=result
        return recipe_of_choice


def name_obed():
    """
    Функция осуществляет поиск по базе данных и выдает названия обедов
    """
    with sq.connect("recipes") as con:
        cur = con.cursor()
        str_zavtrak=""
        cur.execute("SELECT dish FROM rs WHERE type = 2")
        for result in cur:
             str_zavtrak=str_zavtrak+str(result[0])+", "
        return str_zavtrak

def choice_obed(choice):
    """
    Функция выдает состав и рецепт выбранного обеда
    """
    with sq.connect("recipes") as con:
        cur = con.cursor()
   
        cur.execute("SELECT dish,structure, recipe FROM rs WHERE type = 2")
        
        for result in cur:
            if choice in result:
                recipe_of_choice=result
        return recipe_of_choice


def name_uzhin():
    """
    Функция осуществляет поиск по базе данных и выдает названия ужинов
    """
    with sq.connect("recipes") as con:
        cur = con.cursor()
        str_zavtrak=""
        cur.execute("SELECT dish FROM rs WHERE type = 3")
        for result in cur:
             str_zavtrak=str_zavtrak+str(result[0])+", "
        return str_zavtrak
  
def choice_uzhin(choice):
    """
    Функция выдает состав и рецепт выбранного ужина
    """  
    with sq.connect("recipes") as con:
        cur = con.cursor()
   
        cur.execute("SELECT dish,structure, recipe FROM rs WHERE type = 3")
        
        for result in cur:
            if choice in result:
                recipe_of_choice=result
        return recipe_of_choice
    

def name_desert():
    """
    Функция осуществляет поиск по базе данных и выдает названия десертов
    """
    with sq.connect("recipes") as con:
        cur = con.cursor()
        str_zavtrak=""
        cur.execute("SELECT dish FROM rs WHERE type = 4")
        for result in cur:
             str_zavtrak=str_zavtrak+str(result[0])+", "
        return str_zavtrak
  
def choice_desert(choice):
    """
    Функция выдает состав и рецепт выбранного десерта
    """  
    with sq.connect("recipes") as con:
        cur = con.cursor()
   
        cur.execute("SELECT dish,structure, recipe FROM rs WHERE type = 4")
        
        for result in cur:
            if choice in result:
                recipe_of_choice=result
        return recipe_of_choice

def menu_ingred(lst):
    """
    Функция осуществляет поиск по базе данных и выдает все блюда, в состав которых входит введенный ингредиент
    """
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
    """
    Функция выдает состав и рецепт выбранного блюда
    """
    with sq.connect("recipes") as con:
        cur = con.cursor()
   
        cur.execute("SELECT dish,structure, recipe FROM rs")
        for result in cur:
            if choice in result:
                recipe_of_choice=result
        return recipe_of_choice
