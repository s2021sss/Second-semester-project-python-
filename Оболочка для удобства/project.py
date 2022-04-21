import sqlite3 as sq

def zavtrak():
    with sq.connect("recipes") as con:
        cur = con.cursor()

        cur.execute("SELECT dish FROM rs WHERE type = 1")
        for result in cur:
            print(result)
def zavtrak_choice():
    with sq.connect("recipes") as con:
        cur = con.cursor()
        choice_dish = input()
        print("Рецепт блюда: ")
        cur.execute("SELECT dish, structure, recipe FROM rs WHERE type = 1")
        for result in cur:
            if choice_dish in result:
                print(result)
def zavtrak_view():
    with sq.connect("recipes") as con:
        cur = con.cursor()
        view = input()
        cur.execute("SELECT dish, structure, recipe FROM rs WHERE type = 1")
        for result in cur:
            for i in result:
                if view in i:
                    print(result) #вывод зависит от место положения рецепта(если на втором месте, то выводит два раза одно и тоже)

def obed():
    with sq.connect("recipes") as con:
        cur = con.cursor()

        cur.execute("SELECT dish FROM rs WHERE type = 2")
        for result in cur:
            print(result)
def obed_choice():
    with sq.connect("recipes") as con:
        cur = con.cursor()
        choice_dish = input()
        print("Рецепт блюда: ")
        cur.execute("SELECT dish, structure, recipe FROM rs WHERE type = 2")
        for result in cur:
            if choice_dish in result:
                print(result)
def obed_view():
    with sq.connect("recipes") as con:
        cur = con.cursor()
        view = input()
        cur.execute("SELECT dish, structure, recipe FROM rs WHERE type = 2")
        for result in cur:
            for i in result:
                if view in i:
                    print(result) #вывод зависит от место положения рецепта(если на втором месте, то выводит два раза одно и тоже)

def ujin():
    with sq.connect("recipes") as con:
        cur = con.cursor()

        cur.execute("SELECT dish FROM rs WHERE type = 3")
        for result in cur:
            print(result)
def ujin_choice():
    with sq.connect("recipes") as con:
        cur = con.cursor()
        choice_dish = input()
        print("Рецепт блюда: ")
        cur.execute("SELECT dish, structure, recipe FROM rs WHERE type = 3")
        for result in cur:
            if choice_dish in result:
                print(result)
def ujin_view():
    with sq.connect("recipes") as con:
        cur = con.cursor()
        view = input()
        cur.execute("SELECT dish, structure, recipe FROM rs WHERE type = 3")
        for result in cur:
            for i in result:
                if view in i:
                    print(result) #вывод зависит от место положения рецепта(если на втором месте, то выводит два раза одно и тоже)

def desert():
    with sq.connect("recipes") as con:
        cur = con.cursor()

        cur.execute("SELECT dish FROM rs WHERE type = 4")
        for result in cur:
            print(result)
def desert_choice():
    with sq.connect("recipes") as con:
        cur = con.cursor()
        choice_dish = input()
        print("Рецепт блюда: ")
        cur.execute("SELECT dish, structure, recipe FROM rs WHERE type = 4")
        for result in cur:
            if choice_dish in result:
                print(result)
def desert_view():
    with sq.connect("recipes") as con:
        cur = con.cursor()
        view = input()
        cur.execute("SELECT dish, structure, recipe FROM rs WHERE type = 4")
        for result in cur:
            for i in result:
                if view in i:
                    print(result) #вывод зависит от место положения рецепта(если на втором месте, то выводит два раза одно и тоже)






print("Выберите тип блюда, которое вы желаете")
print("Типы: завтрак, обед, ужин, десерт")
type = input("Введите выбранный тип: ")
if type == "завтрак":
    print("Хотите искать по сотаву?")
    choice = input()
    if choice == "нет":
        print("Блюда которые у нас имеются:")
        zavtrak()
        print("Выберите блюдо, которое вам больше нравится:")
        zavtrak_choice()
    else:
        print("Что вы хотите видеть в составе: ")
        zavtrak_view()


elif type == "обед":
    print("Хотите искать по сотаву?")
    choice = input()
    if choice == "нет":
        print("Блюда которые у нас имеются:")
        obed()
        print("Выберите блюдо, которое вам больше нравится:")
        obed_choice()
    else:
        print("Что вы хотите видеть в составе: ")
        obed_view()


elif type == "ужин":
    print("Хотите искать по сотаву?")
    choice = input()
    if choice == "нет":
        print("Блюда которые у нас имеются:")
        ujin()
        print("Выберите блюдо, которое вам больше нравится:")
        ujin_choice()
    else:
        print("Что вы хотите видеть в составе: ")
        ujin_view()


elif type == "десерт":
    print("Хотите искать по сотаву?")
    choice = input()
    if choice == "нет":
        print("Блюда которые у нас имеются:")
        desert()
        print("Выберите блюдо, которое вам больше нравится:")
        desert_choice()
    else:
        print("Что вы хотите видеть в составе: ")
        desert_view()

