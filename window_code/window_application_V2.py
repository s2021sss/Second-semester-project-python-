from email.mime import image
from re import T
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox




def destroy_first_window(): ## Удаляет начальный экран, то есть начальную кнопку и вызывает функцию для показа экрана выбора по составу или по блюду
    first_button_continue.destroy()
    
    first_choice()



def destroy_choiceByingredientsAndMeals_1(): ## Разрушает кнопки с выбором по составу или по блюду и вызывает функцию для поиска по составу
    choice_by_ingredients.destroy()
    choice_by_meals.destroy()
    
    search_by_ingredients()

def destroy_choiceByingredientsAndMeals_2(): ## Разрушает кнопки с выбором по составу или по блюду и вызывает функцию для поиска по приему пищи
    choice_by_ingredients.destroy()
    choice_by_meals.destroy()
    
    search_by_meals()


def destroy_search_by_ingredients(): ## Разрушает кнопки с экрана поиска по составу и возвращает на экран выбора по составу или по блюду
    message_entry_ingred.destroy()
    return_ingred.destroy()
    message_button_ingred.destroy()
    
    first_choice()


def destroy_search_by_zavtrak(): ## Разрушает экран поиска по завтракам и возвращает на экран выбора по составу или по блюду
    message_entry_zavtrak.destroy()
    message_button_zavtrak.destroy()
    return_zavtrak.destroy()

    first_choice()


def destroy_search_by_obed(): ## Разрушает экран поиска по обедам и возвращает на экран выбора по составу или по блюду
    message_entry_obed.destroy()
    message_button_obed.destroy()
    return_obed.destroy()

    first_choice()


def destroy_search_by_uzhin(): ## Разрушает экран поиска по ужинам и возвращает на экран выбора по составу или по блюду
    message_entry_uzhin.destroy()
    message_button_uzhin.destroy()
    return_uzhin.destroy()

    first_choice()


def destroy_search_by_desert(): ## Разрушает экран поиска по десертам и возвращает на экран выбора по составу или по блюду
    message_entry_desert.destroy()
    message_button_desert.destroy()
    return_desert.destroy()

    first_choice()




def first_choice(): ## Экран первого выбора по составу или по блюду
    global choice_by_ingredients_img,choice_by_meals_img, choice_by_ingredients, choice_by_meals
        
    choice_by_ingredients_img = PhotoImage(file="выбор-1.png")
    choice_by_meals_img = PhotoImage(file="выбор-2.png")

    choice_by_ingredients = Button(first_window, image=choice_by_ingredients_img, height=height_win, width=width_win/2, command = destroy_choiceByingredientsAndMeals_1)
    choice_by_ingredients.place(relx=0.25, rely=0.5, anchor=CENTER)
    choice_by_meals = Button(first_window, image=choice_by_meals_img, height=height_win, width=width_win/2, command = destroy_choiceByingredientsAndMeals_2)
    choice_by_meals.place(relx=0.75, rely=0.5, anchor=CENTER)



    
    
def search_by_ingredients(): ## Поиск по составу
    global bg_ingredients, message_ingred, return_ingred, message_button_ingred, message_entry_ingred

    bg_ingredients = ImageTk.PhotoImage(file="по составу.png")
    first_canvas.create_image(0,0,image=bg_ingredients,anchor='nw')
    

    return_ingred = Button(first_window,  image = buttom_back, command = destroy_search_by_ingredients)
    return_ingred.place(relx=1, rely=1, anchor='se')

    
    message_ingred = StringVar()
    message_entry_ingred = Entry(first_window, width=int(width_win/20), fg="black", textvariable=message_ingred)
    message_entry_ingred.place(x=int(width_win/3), y=100,width=int(width_win/3), height=30)
    message_button_ingred=Button(first_window, image=buttom_find, command=show_message_ingred)
    message_button_ingred.place(x=int(width_win/3)*2, y=70,width=100, height=100)
    
    message_button_ingred.bind('<Return>',enter)

    


    
def search_by_meals(): ## Поиск по приему пищи 
    global zavtrak_search_img, obed_search_img, uzhin_search_img, desert_search_img, zavtrak_search, obed_search, uzhin_search, desert_search
    
    zavtrak_search_img = PhotoImage(file="завтрак.png")
    obed_search_img = PhotoImage(file="обед.png")
    uzhin_search_img = PhotoImage(file="ужин.png")
    desert_search_img = PhotoImage(file="десерт.png")

    zavtrak_search = Button(first_window, image=zavtrak_search_img, height=height_win, width=width_win/4, command = destroy_seach_zavrtak)
    zavtrak_search.place(relx=0.125, rely=0.5, anchor=CENTER)

    obed_search = Button(first_window, image=obed_search_img, height=height_win, width=width_win/4, command = destroy_seach_obed)
    obed_search.place(relx=0.375, rely=0.5, anchor=CENTER)

    uzhin_search = Button(first_window, image=uzhin_search_img, height=height_win, width=width_win/4, command = destroy_seach_uzhin)
    uzhin_search.place(relx=0.625, rely=0.5, anchor=CENTER)

    desert_search = Button(first_window, image=desert_search_img, height=height_win, width=width_win/4, command = destroy_seach_desert)
    desert_search.place(relx=0.875, rely=0.5, anchor=CENTER)


def destroy_seach_zavrtak(): ## Разрушает кнопки выбора завтрак/обед/ужин/десерт и открывает экран по поиску по завтраку
    zavtrak_search.destroy()
    obed_search.destroy()
    uzhin_search.destroy()
    desert_search.destroy()

    zavtrak()

def destroy_seach_obed(): ## Разрушает кнопки выбора завтрак/обед/ужин/десерт и открывает экран по поиску по обедам
    zavtrak_search.destroy()
    obed_search.destroy()
    uzhin_search.destroy()
    desert_search.destroy()

    obed()

def destroy_seach_uzhin(): ## Разрушает кнопки выбора завтрак/обед/ужин/десерт и открывает экран по поиску по ужинам
    zavtrak_search.destroy()
    obed_search.destroy()
    uzhin_search.destroy()
    desert_search.destroy()

    uzhin()

def destroy_seach_desert(): ## Разрушает кнопки выбора завтрак/обед/ужин/десерт и открывает экран по поиску по десертам
    zavtrak_search.destroy()
    obed_search.destroy()
    uzhin_search.destroy()
    desert_search.destroy()

    desert()
    
def zavtrak(): ## Поиск по завтраку 
    global bg_zavtrak, message_zavtrak, message_entry_zavtrak, return_zavtrak,message_button_zavtrak

    bg_zavtrak = ImageTk.PhotoImage(file="по завтраку.png")
    first_canvas.create_image(0,0,image=bg_zavtrak,anchor='nw')


    return_zavtrak = Button(first_window,  image = buttom_back, command = destroy_search_by_zavtrak)
    return_zavtrak.place(relx=1, rely=1, anchor='se')


    message_zavtrak= StringVar()
    message_entry_zavtrak = Entry(first_window, width=int(width_win/20), fg="black", textvariable=message_zavtrak)
    message_entry_zavtrak.place(x=int(width_win/3), y=100,width=int(width_win/3), height=30)
    message_button_zavtrak=Button(first_window, image=buttom_find, command=show_message_zavtrak)
    message_button_zavtrak.place(x=int(width_win/3)*2, y=70,width=100, height=100)
    message_button_zavtrak.bind('<Return>',enter)
    

    

    
def obed(): ## Поиск по обеду 
    global bg_obed, message_obed, message_entry_obed, return_obed, message_button_obed

    bg_obed = ImageTk.PhotoImage(file="по обеду.png")
    first_canvas.create_image(0,0,image=bg_obed,anchor='nw')

    return_obed = Button(first_window,  image = buttom_back, command = destroy_search_by_obed)
    return_obed.place(relx=1, rely=1, anchor='se')


    message_obed= StringVar()
    message_entry_obed = Entry(first_window, width=int(width_win/20), fg="black", textvariable=message_obed)
    message_entry_obed.place(x=int(width_win/3), y=100,width=int(width_win/3), height=30)
    message_button_obed=Button(first_window, image=buttom_find, command=show_message_obed)
    message_button_obed.place(x=int(width_win/3)*2, y=70,width=100, height=100)
    message_button_obed.bind('<Return>',enter)



def uzhin(): ## Поиск по ужину 
    global bg_uzhin, message_uzhin, message_entry_uzhin, return_uzhin, message_button_uzhin

    bg_uzhin = ImageTk.PhotoImage(file="по ужину.png")
    first_canvas.create_image(0,0,image=bg_uzhin,anchor='nw')

    return_uzhin = Button(first_window,  image = buttom_back, command = destroy_search_by_uzhin)
    return_uzhin.place(relx=1, rely=1, anchor='se')


    message_uzhin= StringVar()
    message_entry_uzhin = Entry(first_window, width=int(width_win/20), fg="black", textvariable=message_uzhin)
    message_entry_uzhin.place(x=int(width_win/3), y=100,width=int(width_win/3), height=30)
    message_button_uzhin=Button(first_window, image=buttom_find, command=show_message_uzhin)
    message_button_uzhin.place(x=int(width_win/3)*2, y=70,width=100, height=100)
    message_button_uzhin.bind('<Return>',enter)


    
def desert(): ## Поиск по десертам 
    global bg_desert, message_desert, message_entry_desert, return_desert, message_button_desert

    bg_desert = ImageTk.PhotoImage(file="по десерту.png")
    first_canvas.create_image(0,0,image=bg_desert,anchor='nw')

    return_desert = Button(first_window,  image = buttom_back, command = destroy_search_by_desert)
    return_desert.place(relx=1, rely=1, anchor='se')


    message_desert= StringVar()
    message_entry_desert = Entry(first_window, width=int(width_win/20), fg="black", textvariable=message_desert)
    message_entry_desert.place(x=int(width_win/3), y=100,width=int(width_win/3), height=30)
    message_button_desert=Button(first_window, image=buttom_find, command=show_message_desert)
    message_button_desert.place(x=int(width_win/3)*2, y=70,width=100, height=100)
    message_button_desert.bind('<Return>',enter)







## Вместо этих функций будут функции для поиска
    

def show_message_ingred():
    messagebox.showinfo("GUI Python", message_ingred.get())
    

def show_message_zavtrak():
    messagebox.showinfo("GUI Python", message_zavtrak.get())


def show_message_obed():
    messagebox.showinfo("GUI Python", message_obed.get())

def show_message_uzhin():
    messagebox.showinfo("GUI Python", message_uzhin.get())

def show_message_desert():
    messagebox.showinfo("GUI Python", message_desert.get())



def enter(event=None):
    show_message_ingred()

    

first_window = Tk()

first_window.title ("Подбор блюд и рецептов по ингредиентам")
first_window.attributes('-fullscreen', True)

first_canvas=Canvas(first_window)
first_canvas.pack(fill="both", expand=True)

first_buttom_img=PhotoImage(file = "Your_img.png")

#Измеряет длину и ширину экрана
width_win=first_window.winfo_screenwidth()
height_win=first_window.winfo_screenheight()

##Кнопка для поиска
buttom_find=PhotoImage(file = "find.png")

##Кнопка для возращения назад 
back = Image.open("back.jpg")
back_resize=back.resize((50, 50))
buttom_back = ImageTk.PhotoImage(back_resize)

first_button_continue=Button(first_window, image=first_buttom_img, height = height_win, width = width_win, command = destroy_first_window)
first_button_continue.place(relx=0.5, rely=0.5, anchor=CENTER)

first_canvas.mainloop()
