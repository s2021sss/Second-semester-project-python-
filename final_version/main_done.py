from email.mime import image
from re import T
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import databasefunctions
import sqlite3 as sq



def destroy_first_window():
    """
    Удаляет начальный экран, то есть начальную кнопку и вызывает функцию для показа экрана выбора по составу или по блюду
    """
    first_button_continue.destroy()
    
    first_choice()

def destroy_choiceByingredientsAndMeals_1(): 
    """
    Разрушает кнопки с выбором по составу или по блюду и вызывает функцию для поиска по составу
    """
    choice_by_ingredients.destroy()
    choice_by_meals.destroy()
    
    search_by_ingredients()

def destroy_choiceByingredientsAndMeals_2(): 
    """
    Разрушает кнопки с выбором по составу или по блюду и вызывает функцию для поиска по приему пищи
    """
    choice_by_ingredients.destroy()
    choice_by_meals.destroy()
    
    search_by_meals()


def destroy_search_by_ingredients(): 
    """
    Разрушает кнопки с экрана поиска по составу и возвращает на экран выбора по составу или по блюду
    """
    message_entry_ingred.destroy()
    return_ingred.destroy()
    message_button_ingred.destroy()

    try:
        frame_menu_ingred.destroy()
        butt_ingred.destroy()
    except:
        pass
    try:
        frame_find_ingred.destroy()
    except:
        pass
    
    first_choice()


def destroy_search_by_zavtrak(): 
    """
    Разрушает экран поиска по завтракам и возвращает на экран выбора по составу или по блюду
    """
    return_zavtrak.destroy()

    listbox_zavtrak.destroy()
    butt_zavtrak.destroy()
    frame_menu_zavtrak.destroy()

    try:
        frame_find_zavtrak.destroy()
    except:
        pass

    first_choice()


def destroy_search_by_obed():  
    """
    Разрушает экран поиска по обедам и возвращает на экран выбора по составу или по блюду
    """
    return_obed.destroy()

    listbox_obed.destroy()
    butt_obed.destroy()
    frame_menu_obed.destroy()

    try:
        frame_find_obed.destroy()
    except:
        pass

    first_choice()


def destroy_search_by_uzhin(): 
    """
    Разрушает экран поиска по ужинам и возвращает на экран выбора по составу или по блюду
    """
    return_uzhin.destroy()

    listbox_uzhin.destroy()
    butt_uzhin.destroy()
    frame_menu_uzhin.destroy()

    try:
        frame_find_uzhin.destroy()
    except:
        pass

    first_choice()


def destroy_search_by_desert(): 
    """
    Разрушает экран поиска по десертам и возвращает на экран выбора по составу или по блюду
    """
    return_desert.destroy()

    listbox_desert.destroy()
    butt_desert.destroy()
    frame_menu_desert.destroy()

    try:
        frame_find_desert.destroy()
    except:
        pass

    first_choice()




def first_choice():
    """
    Функция, которая показывает экран первого выбора по составу или по блюду
    """
    global choice_by_ingredients_img,choice_by_meals_img, choice_by_ingredients, choice_by_meals

    choice_by_ingredients = Button(first_window, image=choice_by_ingredients_img, height=height_win, width=width_win/2, command = destroy_choiceByingredientsAndMeals_1)
    choice_by_ingredients.place(relx=0.25, rely=0.5, anchor=CENTER)
    choice_by_meals = Button(first_window, image=choice_by_meals_img, height=height_win, width=width_win/2, command = destroy_choiceByingredientsAndMeals_2)
    choice_by_meals.place(relx=0.75, rely=0.5, anchor=CENTER)



    
def search_by_ingredients(): 
    """
    Функция поиска по составу
    """
    global bg_ingredients, message_ingred, return_ingred, message_button_ingred, message_entry_ingred
    
    """
    Функция, которая выдает репет выбранного блюда
    """
    def show_message_ingred():
        global frame_find_ingred, txt_find_ingred, find_ingred, input_ingred, flag_ingred, input_text_ingred
        flag_ingred=False
        try:
           input_text_ingred = listbox_ingred.get(listbox_ingred.curselection())
           flag_ingred=True
           try:
               frame_find_ingred.destroy()
           except:
                pass
        except:
            pass
        if flag_ingred:
            find_ingred = databasefunctions.choice_ingred(input_text_ingred)
        else:
            find_ingred="Выберите блюдо из меню!"

        frame_find_ingred = Frame()
        frame_find_ingred.pack(fill=BOTH, expand=True)
        txt_find_ingred = Text(frame_find_ingred, font=("Century Gothic", 18), bg="White", wrap=WORD)
        txt_find_ingred.pack(fill=BOTH, pady=5, padx=5, expand=True)
        first_canvas.create_window(koord_w_frame2, koord_h_frame2, anchor = NW, window = frame_find_ingred, width = width_of_frame2, height = height_of_frame2)

        txt_find_ingred.tag_config('boldtext', font=("Century Gothic", 18,'bold'))
        txt_find_ingred.tag_config('boldtextlabel', font=("Century Gothic", 18,'bold'), underline=True)
        txt_find_ingred.insert(INSERT, str(find_ingred[0]), 'boldtextlabel')
        txt_find_ingred.insert(INSERT, "\nИнгредиенты: \n", 'boldtext')
        txt_find_ingred.insert(INSERT, str(find_ingred[1]))
        txt_find_ingred.insert(INSERT, "\nРецепт: \n", 'boldtext')
        txt_find_ingred.insert(INSERT, str(find_ingred[2]))

    """
    Функция, которая выдает списко блюд по выбранному ингредиенту
    """
    def show_menu_ingred():
        global frame_menu_ingred, listbox_ingred, menu_ingred, butt_ingred, message_entry_ingred_str
        try:
            frame_menu_ingred.destroy()
        except:##loging
            pass
        try:
            butt_ingred.destroy()
        except:
            pass
        frame_menu_ingred = Frame()
        frame_menu_ingred.pack(fill=X)
        listbox_ingred = Listbox(frame_menu_ingred, font=("Century Gothic", 18) )
        message_entry_ingred_str=message_entry_ingred.get().lower().replace(" ", "")
        menu_ingred =databasefunctions.menu_ingred(message_entry_ingred_str).split(", ")

        if (menu_ingred==[""]):
            menu_ingred=["Данного продукта" ,"не найдено"]
            try:
                butt_ingred.destroy()
            except:
                pass
            try:
                frame_find_ingred.destroy()
            except:##loging
                pass
        
            
        else:
            butt_ingred=Button(first_window, image=buttom_find,command=show_message_ingred)
            butt_ingred.place(x=int(koord_w_frame1*1.5)+width_of_frame1-int(size_of_butt/2), y=koord_h_frame1+int(height_of_frame1/2)-int(size_of_butt/2),width=size_of_butt, height=size_of_butt)

        listbox_ingred.insert(END, *menu_ingred)
        listbox_ingred.pack(fill=BOTH, pady=5, padx=5, expand=True)
        
        first_canvas.create_window(koord_w_frame1, koord_h_frame1, anchor = NW, window = frame_menu_ingred, width = width_of_frame1, height = height_of_frame1)
        
    def enter_ingred(event=None):
        show_message_ingred()

    first_canvas.create_image(0,0,image=bg_ingredients,anchor='nw')
    
    return_ingred = Button(first_window,  image = buttom_back, command = destroy_search_by_ingredients)
    return_ingred.place(relx=1, rely=1, anchor='se')
    
    message_ingred = StringVar()
    message_entry_ingred = Entry(first_window, width=int(width_win/20), fg="black", textvariable=message_ingred)
    message_entry_ingred.place(x=int(width_win/3), y=int(height_win*0.10), width=int(width_win/3), height=40)
    message_button_ingred=Button(first_window, image=buttom_find_big, command=show_menu_ingred)
    message_button_ingred.place(x=int(width_win/3)*2, y=int(height_win*0.10)-int((size_of_butt_big-40)/2), width=size_of_butt_big, height=size_of_butt_big)
    
    message_button_ingred.bind('<Return>', show_message_ingred)
    first_window.bind('<Return>', lambda event=None: message_button_ingred.invoke())

    
def search_by_meals(): 
    """
    Функция поиска по приему пищи 
    """
    global zavtrak_search_img, obed_search_img, uzhin_search_img, desert_search_img, zavtrak_search, obed_search, uzhin_search, desert_search

    zavtrak_search = Button(first_window, image=zavtrak_search_img, height=height_win, width=width_win/4, command = destroy_seach_zavrtak)
    zavtrak_search.place(relx=0.125, rely=0.5, anchor=CENTER)

    obed_search = Button(first_window, image=obed_search_img, height=height_win, width=width_win/4, command = destroy_seach_obed)
    obed_search.place(relx=0.375, rely=0.5, anchor=CENTER)

    uzhin_search = Button(first_window, image=uzhin_search_img, height=height_win, width=width_win/4, command = destroy_seach_uzhin)
    uzhin_search.place(relx=0.625, rely=0.5, anchor=CENTER)

    desert_search = Button(first_window, image=desert_search_img, height=height_win, width=width_win/4, command = destroy_seach_desert)
    desert_search.place(relx=0.875, rely=0.5, anchor=CENTER)


def destroy_seach_zavrtak(): 
    """
    Функция разрушает кнопки выбора завтрак/обед/ужин/десерт и открывает экран по поиску по завтраку
    """
    zavtrak_search.destroy()
    obed_search.destroy()
    uzhin_search.destroy()
    desert_search.destroy()

    zavtrak()

def destroy_seach_obed(): 
    """
    Функция разрушает кнопки выбора завтрак/обед/ужин/десерт и открывает экран по поиску по обедам
    """
    zavtrak_search.destroy()
    obed_search.destroy()
    uzhin_search.destroy()
    desert_search.destroy()

    obed()

def destroy_seach_uzhin(): 
    """
    Функция разрушает кнопки выбора завтрак/обед/ужин/десерт и открывает экран по поиску по ужинам
    """
    zavtrak_search.destroy()
    obed_search.destroy()
    uzhin_search.destroy()
    desert_search.destroy()

    uzhin()

def destroy_seach_desert(): 
    """
    Функция разрушает кнопки выбора завтрак/обед/ужин/десерт и открывает экран по поиску по десертам
    """
    zavtrak_search.destroy()
    obed_search.destroy()
    uzhin_search.destroy()
    desert_search.destroy()

    desert()
    
def zavtrak(): 
    """
    Функция поиска по завтраку 
    """
    global bg_zavtrak, return_zavtrak,  frame_menu_zavtrak, listbox_zavtrak, menu_zavtrak, butt_zavtrak 
    
    """
    Функция, которая по названию выбранного блюда выдает его рецепт
    """
    def show_message_zavtrak():
        global frame_find_zavtrak, txt_find_zavtrak, find_zavtrak, input_text, flag_zavtrak, input_text_zavtrak
        flag_zavtrak=False
        try:
           input_text_zavtrak = listbox_zavtrak.get(listbox_zavtrak.curselection())
           flag_zavtrak=True
           try:
               frame_find_zavtrak.destroy()
           except:
                pass
        except:
            pass
        if flag_zavtrak:
            find_zavtrak = databasefunctions.choice_zavtrak(input_text_zavtrak)
        else:
            find_zavtrak="Выберите блюдо из завтраков!"

        frame_find_zavtrak = Frame()
        frame_find_zavtrak.pack(fill=BOTH, expand=True)
        txt_find_zavtrak = Text(frame_find_zavtrak, font=("Century Gothic", 18), wrap=WORD)
        txt_find_zavtrak.pack(fill=BOTH, pady=5, padx=5, expand=True)
        first_canvas.create_window(koord_w_frame_NEW2, koord_h_frame_NEW2, anchor = NW, window = frame_find_zavtrak, width = width_of_frame_NEW2, height = height_of_frame_NEW2)

        if flag_zavtrak: 
            txt_find_zavtrak.tag_config('boldtext', font=("Century Gothic", 18 ,'bold'))
            txt_find_zavtrak.tag_config('boldtextlabel', font=("Century Gothic", 18,'bold'), underline=True)
            txt_find_zavtrak.insert(INSERT, str(find_zavtrak[0]), 'boldtextlabel')
            txt_find_zavtrak.insert(INSERT, "\nИнгредиенты: \n", 'boldtext')
            txt_find_zavtrak.insert(INSERT, str(find_zavtrak[1]))
            txt_find_zavtrak.insert(INSERT, "\nРецепт: \n", 'boldtext')
            txt_find_zavtrak.insert(INSERT, str(find_zavtrak[2]))
        else:
            txt_find_zavtrak.tag_config('boldtext', font=("Century Gothic", 18 ,'bold'))
            txt_find_zavtrak.insert(INSERT, find_zavtrak, 'boldtext')

    """
    Функция, которая вызывает поиск 
    """ 
    def enter_zavtrak(event=None):
        show_message_zavtrak()

    first_canvas.create_image(0,0,image=bg_zavtrak,anchor='nw')

    return_zavtrak = Button(first_window,  image = buttom_back, command = destroy_search_by_zavtrak)
    return_zavtrak.place(relx=1, rely=1, anchor='se')

    frame_menu_zavtrak = Frame()
    frame_menu_zavtrak.pack(fill=X)


    listbox_zavtrak = Listbox(frame_menu_zavtrak, font=("Century Gothic", 18))
    menu_zavtrak =databasefunctions.name_zavtrak().split(", ")
    listbox_zavtrak.insert(END, *menu_zavtrak)

    listbox_zavtrak.pack(fill=BOTH, pady=5, padx=5, expand=True)

    butt_zavtrak=Button(first_window, image=buttom_find,command=show_message_zavtrak)
    butt_zavtrak.place(x=int(koord_w_frame_NEW*1.5)+width_of_frame_NEW-int(size_of_butt/2), y=koord_h_frame_NEW+int(height_of_frame_NEW/2)-int(size_of_butt/2),width=size_of_butt, height=size_of_butt)
    butt_zavtrak.bind('<Return>', show_message_zavtrak)
    first_window.bind('<Return>', lambda event=None: butt_zavtrak.invoke())
    
    first_canvas.create_window(koord_w_frame_NEW, koord_h_frame_NEW, anchor = NW, window = frame_menu_zavtrak, width = width_of_frame_NEW, height = height_of_frame_NEW)

    
def obed(): 
    """
    Функция поиска по обеду 
    """
    global bg_obed, return_obed,  frame_menu_obed, listbox_obed, menu_obed, butt_obed 
    
    """
    Функция, которая по названию выбранного блюда выдает его рецепт
    """
    def show_message_obed():
        global frame_find_obed, txt_find_obed, find_obed, input_text, flag_obed, input_text_obed
        flag_obed=False
        try:
           input_text_obed = listbox_obed.get(listbox_obed.curselection())
           flag_obed=True
           try:
               frame_find_obed.destroy()
           except:
                pass
        except:
            pass
        if flag_obed:
            find_obed = databasefunctions.choice_obed(input_text_obed)
        else:
            find_obed="Выберите блюдо из обедов!"

        frame_find_obed = Frame()
        frame_find_obed.pack(fill=BOTH, expand=True)
        txt_find_obed = Text(frame_find_obed, font=("Century Gothic", 18), wrap=WORD)
        txt_find_obed.pack(fill=BOTH, pady=5, padx=5, expand=True)
        first_canvas.create_window(koord_w_frame_NEW2, koord_h_frame_NEW2, anchor = NW, window = frame_find_obed, width = width_of_frame_NEW2, height = height_of_frame_NEW2)
        if flag_obed:
            txt_find_obed.tag_config('boldtext', font=("Century Gothic", 18 ,'bold'))
            txt_find_obed.tag_config('boldtextlabel', font=("Century Gothic", 18,'bold'), underline=True)
            txt_find_obed.insert(INSERT, str(find_obed[0]), 'boldtextlabel')
            txt_find_obed.insert(INSERT, "\nИнгредиенты: \n", 'boldtext')
            txt_find_obed.insert(INSERT, str(find_obed[1]))
            txt_find_obed.insert(INSERT, "\nРецепт: \n", 'boldtext')
            txt_find_obed.insert(INSERT, str(find_obed[2]))
        else:
            txt_find_obed.tag_config('boldtext', font=("Century Gothic", 18 ,'bold'))
            txt_find_obed.insert(INSERT, find_obed, 'boldtext')
    """
    Функция, которая вызывает поиск 
    """ 
    def enter_obed(event=None):
        show_message_obed()

    first_canvas.create_image(0,0,image=bg_obed,anchor='nw')

    return_obed = Button(first_window,  image = buttom_back, command = destroy_search_by_obed)
    return_obed.place(relx=1, rely=1, anchor='se')

    frame_menu_obed = Frame()
    frame_menu_obed.pack(fill=X)

    
    listbox_obed = Listbox(frame_menu_obed, font=("Century Gothic", 18))
    menu_obed =databasefunctions.name_obed().split(", ")
    listbox_obed.insert(END, *menu_obed)

    listbox_obed.pack(fill=BOTH, pady=5, padx=5, expand=True)

    butt_obed=Button(first_window, image=buttom_find,command=show_message_obed)
    butt_obed.place(x=int(koord_w_frame_NEW*1.5)+width_of_frame_NEW-int(size_of_butt/2), y=koord_h_frame_NEW+int(height_of_frame_NEW/2)-int(size_of_butt/2),width=size_of_butt, height=size_of_butt)
    butt_obed.bind('<Return>', show_message_obed)
    first_window.bind('<Return>', lambda event=None: butt_obed.invoke())
    
    first_canvas.create_window(koord_w_frame_NEW, koord_h_frame_NEW, anchor = NW, window = frame_menu_obed, width = width_of_frame_NEW, height = height_of_frame_NEW)




def uzhin(): 
    """
    Функция поиска по ужину 
    """
    global bg_uzhin, return_uzhin,  frame_menu_uzhin, listbox_uzhin, menu_uzhin, butt_uzhin 

    """
    Функция, которая по названию выбранного блюда выдает его рецепт
    """
    def show_message_uzhin():
        global frame_find_uzhin, txt_find_uzhin, find_uzhin, input_text, flag_uzhin, input_text_uzhin
        flag_uzhin=False
        try:
           input_text_uzhin = listbox_uzhin.get(listbox_uzhin.curselection())
           flag_uzhin=True
           try:
               frame_find_uzhin.destroy()
           except:
                pass
        except:
            pass
        if flag_uzhin:
            find_uzhin = databasefunctions.choice_uzhin(input_text_uzhin)
        else:
            find_uzhin="Выберите блюдо из ужинов!"

        frame_find_uzhin = Frame()
        frame_find_uzhin.pack(fill=BOTH, expand=True)
        txt_find_uzhin = Text(frame_find_uzhin, font=("Century Gothic", 18), wrap=WORD)
        txt_find_uzhin.pack(fill=BOTH, pady=5, padx=5, expand=True)
        first_canvas.create_window(koord_w_frame_NEW2, koord_h_frame_NEW2, anchor = NW, window = frame_find_uzhin, width = width_of_frame_NEW2, height = height_of_frame_NEW2)

        if flag_uzhin: 
            txt_find_uzhin.tag_config('boldtext', font=("Century Gothic", 18 ,'bold'))
            txt_find_uzhin.tag_config('boldtextlabel', font=("Century Gothic", 18,'bold'), underline=True)
            txt_find_uzhin.insert(INSERT, str(find_uzhin[0]), 'boldtextlabel')
            txt_find_uzhin.insert(INSERT, "\nИнгредиенты: \n", 'boldtext')
            txt_find_uzhin.insert(INSERT, str(find_uzhin[1]))
            txt_find_uzhin.insert(INSERT, "\nРецепт: \n", 'boldtext')
            txt_find_uzhin.insert(INSERT, str(find_uzhin[2]))
        else:
            txt_find_uzhin.tag_config('boldtext', font=("Century Gothic", 18 ,'bold'))
            txt_find_uzhin.insert(INSERT, find_uzhin, 'boldtext')

    """
    Функция, которая вызывает поиск 
    """ 
    def enter_uzhin(event=None):
        show_message_uzhin()

    first_canvas.create_image(0,0,image=bg_uzhin,anchor='nw')

    return_uzhin = Button(first_window,  image = buttom_back, command = destroy_search_by_uzhin)
    return_uzhin.place(relx=1, rely=1, anchor='se')

    frame_menu_uzhin = Frame()
    frame_menu_uzhin.pack(fill=X)

    
    listbox_uzhin = Listbox(frame_menu_uzhin, font=("Century Gothic", 18))
    menu_uzhin =databasefunctions.name_uzhin().split(", ")
    listbox_uzhin.insert(END, *menu_uzhin)

    listbox_uzhin.pack(fill=BOTH, pady=5, padx=5, expand=True)

    butt_uzhin=Button(first_window, image=buttom_find,command=show_message_uzhin)
    butt_uzhin.place(x=int(koord_w_frame_NEW*1.5)+width_of_frame_NEW-int(size_of_butt/2), y=koord_h_frame_NEW+int(height_of_frame_NEW/2)-int(size_of_butt/2),width=size_of_butt, height=size_of_butt)
    butt_uzhin.bind('<Return>', show_message_uzhin)
    first_window.bind('<Return>', lambda event=None: butt_uzhin.invoke())
    
    first_canvas.create_window(koord_w_frame_NEW, koord_h_frame_NEW, anchor = NW, window = frame_menu_uzhin, width = width_of_frame_NEW, height = height_of_frame_NEW)

    
def desert(): 
    """
    Функция поиска по десертам
    """
    global bg_desert, return_desert,  frame_menu_desert, listbox_desert, menu_desert, butt_desert 

    """
    Функция, которая по названию выбранного блюда выдает его рецепт
    """
    def show_message_desert():
        global frame_find_desert, txt_find_desert, find_desert, input_text, flag_desert
        flag_desert=False
        try:
           input_text_desert = listbox_desert.get(listbox_desert.curselection())
           flag_desert=True
           try:
               frame_find_desert.destroy()
           except:
                pass
        except:
            pass
        if flag_desert:
            find_desert = databasefunctions.choice_desert(input_text_desert)
        else:
            find_desert="Выберите блюдо из десертов!"

        frame_find_desert = Frame()
        frame_find_desert.pack(fill=BOTH, expand=True)
        txt_find_desert = Text(frame_find_desert, font=("Century Gothic", 18), wrap=WORD)
        txt_find_desert.pack(fill=BOTH, pady=5, padx=5, expand=True)
        first_canvas.create_window(koord_w_frame_NEW2, koord_h_frame_NEW2, anchor = NW, window = frame_find_desert, width = width_of_frame_NEW2, height = height_of_frame_NEW2)

        if flag_desert:
            txt_find_desert.tag_config('boldtext', font=("Century Gothic", 18 ,'bold'))
            txt_find_desert.tag_config('boldtextlabel', font=("Century Gothic", 18,'bold'), underline=True)
            txt_find_desert.insert(INSERT, str(find_desert[0]), 'boldtextlabel')
            txt_find_desert.insert(INSERT, "\nИнгредиенты: \n", 'boldtext')
            txt_find_desert.insert(INSERT, str(find_desert[1]))
            txt_find_desert.insert(INSERT, "\nРецепт: \n", 'boldtext')
            txt_find_desert.insert(INSERT, str(find_desert[2]))
        else:
            txt_find_desert.tag_config('boldtext', font=("Century Gothic", 18 ,'bold'))
            txt_find_desert.insert(INSERT, find_desert, 'boldtext')

    """
    Функция, которая вызывает поиск 
    """ 
    def enter_desert(event=None):
        show_message_desert()

    first_canvas.create_image(0,0,image=bg_desert,anchor='nw')

    return_desert = Button(first_window,  image = buttom_back, command = destroy_search_by_desert)
    return_desert.place(relx=1, rely=1, anchor='se')

    frame_menu_desert = Frame()
    frame_menu_desert.pack(fill=X)

    
    listbox_desert = Listbox(frame_menu_desert, font=("Century Gothic", 18))
    menu_desert =databasefunctions.name_desert().split(", ")
    listbox_desert.insert(END, *menu_desert)

    listbox_desert.pack(fill=BOTH, pady=5, padx=5, expand=True)

    butt_desert=Button(first_window, image=buttom_find,command=show_message_desert)
    butt_desert.place(x=int(koord_w_frame_NEW*1.5)+width_of_frame_NEW-int(size_of_butt/2), y=koord_h_frame_NEW+int(height_of_frame_NEW/2)-int(size_of_butt/2),width=size_of_butt, height=size_of_butt)
    butt_desert.bind('<Return>', show_message_desert)
    first_window.bind('<Return>', lambda event=None: butt_desert.invoke())
    
    first_canvas.create_window(koord_w_frame_NEW, koord_h_frame_NEW, anchor = NW, window = frame_menu_desert, width = width_of_frame_NEW, height = height_of_frame_NEW)



"""
Основной экран
"""
first_window = Tk()

first_window.title ("Подбор блюд и рецептов по ингредиентам")
first_window.attributes('-fullscreen', True)

first_canvas=Canvas(first_window)
first_canvas.pack(fill="both", expand=True)

"""
Измерение длины и ширины экрана
"""
width_win=first_window.winfo_screenwidth()
height_win=first_window.winfo_screenheight()


"""
Импорт и изменение размеров фоновых картинок
"""
first_buttom_img_file=Image.open("Foody.png")
first_buttom_img_resize=first_buttom_img_file.resize((width_win,height_win))
first_buttom_img=ImageTk.PhotoImage(first_buttom_img_resize)

choice_by_ingredients_img_file=Image.open("choice_by_ingred.png")
choice_by_ingredients_img_resize=choice_by_ingredients_img_file.resize((int(width_win/2),height_win))
choice_by_ingredients_img = ImageTk.PhotoImage(choice_by_ingredients_img_resize)

choice_by_meals_img_file=Image.open("choice_by_meals.png")
choice_by_meals_img_resize=choice_by_meals_img_file.resize((int(width_win/2),height_win))
choice_by_meals_img=ImageTk.PhotoImage(choice_by_meals_img_resize)


bg_ingredients_file=Image.open("ingred.png")
bg_ingredients_resize=bg_ingredients_file.resize((width_win,height_win))
bg_ingredients=ImageTk.PhotoImage(bg_ingredients_resize)

bg_zavtrak_file=Image.open("zavtrak.png")
bg_zavtrak_resize=bg_zavtrak_file.resize((width_win,height_win))
bg_zavtrak=ImageTk.PhotoImage(bg_zavtrak_resize)

bg_obed_file=Image.open("obed.png")
bg_obed_resize=bg_obed_file.resize((width_win,height_win))
bg_obed=ImageTk.PhotoImage(bg_obed_resize)

bg_uzhin_file=Image.open("uzhin.png")
bg_uzhin_resize=bg_uzhin_file.resize((width_win,height_win))
bg_uzhin=ImageTk.PhotoImage(bg_uzhin_resize)

bg_desert_file=Image.open("desert.png")
bg_desert_resize=bg_desert_file.resize((width_win,height_win))
bg_desert=ImageTk.PhotoImage(bg_desert_resize)


zavtrak_search_img_file=Image.open("by_zavtrak.png")
zavtrak_search_img_resize=zavtrak_search_img_file.resize((int(width_win/4),height_win))
zavtrak_search_img=ImageTk.PhotoImage(zavtrak_search_img_resize)

obed_search_img_file=Image.open("by_obed.png")
obed_search_img_resize=obed_search_img_file.resize((int(width_win/4),height_win))
obed_search_img=ImageTk.PhotoImage(obed_search_img_resize)

uzhin_search_img_file=Image.open("by_uzhin.png")
uzhin_search_img_resize=uzhin_search_img_file.resize((int(width_win/4),height_win))
uzhin_search_img=ImageTk.PhotoImage(uzhin_search_img_resize)

desert_search_img_file=Image.open("by_desert.png")
desert_search_img_resize=desert_search_img_file.resize((int(width_win/4),height_win))
desert_search_img=ImageTk.PhotoImage(desert_search_img_resize)


"""
Определяется рахмер кнопки поиска
"""
size_of_butt=int(width_win*0.05*0.65)
size_of_butt_big=100

"""
Фоновая картинка для кнопки поиска
"""
img = Image.open('poisk.png')
img_resize_small = img.resize((size_of_butt, size_of_butt))
img_resize_big = img.resize((size_of_butt_big, size_of_butt_big))

buttom_find=ImageTk.PhotoImage(img_resize_small)
buttom_find_big=ImageTk.PhotoImage(img_resize_big)

"""
Фоновая картинка для кнопки назад
"""
back = Image.open("back.png")
back_resize=back.resize((50, 50))
buttom_back = ImageTk.PhotoImage(back_resize)

"""
Координаты окон при поиске по ингридиентам
"""
koord_w_frame1=int(width_win*0.05)
koord_h_frame1=int(height_win*0.25)
width_of_frame1=int(koord_h_frame1*1.5)
height_of_frame1= height_win-koord_h_frame1-koord_w_frame1

koord_w_frame2=width_of_frame1+2*koord_w_frame1
koord_h_frame2=int(height_win*0.25)
width_of_frame2= width_win - 3*koord_w_frame1 - width_of_frame1
height_of_frame2= height_win-koord_h_frame1-koord_w_frame1


"""
Координаты окон при поиске по блюду
"""
koord_w_frame_NEW=int(width_win*0.05)
koord_h_frame_NEW=int(height_win*0.15)
width_of_frame_NEW=int(koord_h_frame_NEW*3)
height_of_frame_NEW= height_win-koord_h_frame_NEW-koord_w_frame_NEW

koord_w_frame_NEW2=width_of_frame_NEW+2*koord_w_frame_NEW
koord_h_frame_NEW2=int(height_win*0.15)
width_of_frame_NEW2= width_win - 3*koord_w_frame_NEW - width_of_frame_NEW
height_of_frame_NEW2= height_win-koord_w_frame_NEW-koord_h_frame_NEW


first_button_continue=Button(first_window, image=first_buttom_img, height = height_win, width = width_win, command = destroy_first_window)
first_button_continue.place(relx=0.5, rely=0.5, anchor=CENTER)

first_canvas.mainloop()
