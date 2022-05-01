from email.mime import image
from re import T
from tkinter import *
from PIL import Image, ImageTk

def second_window_vibor():
    global second_canvas, second_buttom_img_1, second_buttom_img_2
    second_window = Toplevel(first_canvas)
    button_continue_1 = Button(second_window, text = "New Window button")

    second_window.title("Выбор поиска")

    second_bg = ImageTk.PhotoImage(file="выбор.png")
    second_window.attributes('-fullscreen', True)

    second_canvas = Canvas(second_window)
    second_canvas.pack(fill="both", expand=True)
    second_canvas.create_image(0, 0, image=second_bg, anchor="nw")

    second_buttom_img_1 = PhotoImage(file="выбор-1.png")
    second_buttom_img_2 = PhotoImage(file="выбор-2.png")

    second_button_continue_1 = Button(second_window, image=second_buttom_img_1, height=height_win, width=width_win/2, command=third_win_po_sostavy)
    second_button_continue_1.place(relx=0.25, rely=0.5, anchor=CENTER)
    second_button_continue_2 = Button(second_window, image=second_buttom_img_2, height=height_win, width=width_win/2, command=third_win_po_bludy)
    second_button_continue_2.place(relx=0.75, rely=0.5, anchor=CENTER)

def third_win_po_sostavy():
    global bg1
    third_window = Toplevel(second_canvas)
    button_continue_2 = Button(third_window, text="New Window button")
    third_window.title("Поиск по составу")

    bg1 = ImageTk.PhotoImage(file="по составу.png")
    third_window.attributes('-fullscreen', True)

    third_canvas = Canvas(third_window)
    third_canvas.pack(fill="both", expand=True)
    third_canvas.create_image(0, 0, image=bg1, anchor="nw")

def third_win_po_bludy():
    global bg2, fourth_canvas, fourth_buttom_1, fourth_buttom_2, fourth_buttom_3, fourth_buttom_4, fourth_buttom_1_tst
    fourth_window = Toplevel(second_canvas)
    button_continue_2 = Button(fourth_window, text="New Window button")
    fourth_window.title("Поиск по блюду")

    bg2 = ImageTk.PhotoImage(file="по блюду.png")
    fourth_window.attributes('-fullscreen', True)

    fourth_canvas = Canvas(fourth_window)
    fourth_canvas.pack(fill="both", expand=True)
    fourth_canvas.create_image(0, 0, image=bg2, anchor="nw")

    fourth_buttom_1 = PhotoImage(file="завтрак.png")
    #fourth_buttom_1_tst=Image.open("завтрак.png")
    #fourth_buttom_1=fourth_buttom_1_tst.resize((width_win, height_win), Image.ANTIALIAS)
    fourth_buttom_2 = PhotoImage(file="обед.png")
    fourth_buttom_3 = PhotoImage(file="ужин.png")
    fourth_buttom_4 = PhotoImage(file="десерт.png")

    fourth_button_continue_1 = Button(fourth_window, image=fourth_buttom_1, height=height_win, width=width_win/4, command=zavtrak)
    fourth_button_continue_1.place(relx=0.125, rely=0.5, anchor=CENTER)

    fourth_button_continue_2 = Button(fourth_window, image=fourth_buttom_2, height=height_win, width=width_win/4, command=obed)
    fourth_button_continue_2.place(relx=0.375, rely=0.5, anchor=CENTER)

    fourth_button_continue_3 = Button(fourth_window, image=fourth_buttom_3, height=height_win, width=width_win/4, command=uzhin)
    fourth_button_continue_3.place(relx=0.625, rely=0.5, anchor=CENTER)

    fourth_button_continue_4 = Button(fourth_window, image=fourth_buttom_4, height=height_win, width=width_win/4, command=desert)
    fourth_button_continue_4.place(relx=0.875, rely=0.5, anchor=CENTER)

def zavtrak():
    global bg_zavtrak
    five_window = Toplevel(fourth_canvas)
    fourth_button_continue_1 = Button(five_window, text="New Window button")
    five_window.title("Поиск по составу")

    bg_zavtrak = ImageTk.PhotoImage(file="по завтраку.png")
    five_window.attributes('-fullscreen', True)

    five_canvas = Canvas(five_window)
    five_canvas.pack(fill="both", expand=True)
    five_canvas.create_image(0, 0, image=bg_zavtrak, anchor="nw")

def obed():
    global bg6_obed
    six_window = Toplevel(fourth_canvas)
    fourth_button_continue_2 = Button(six_window, text="New Window button")
    six_window.title("Поиск по составу")

    bg6_obed = ImageTk.PhotoImage(file="по обеду.png")
    six_window.attributes('-fullscreen', True)

    six_canvas = Canvas(six_window)
    six_canvas.pack(fill="both", expand=True)
    six_canvas.create_image(0, 0, image=bg6_obed, anchor="nw")

def uzhin():
    global bg_uzhin
    seven_window = Toplevel(fourth_canvas)
    fourth_button_continue_3 = Button(seven_window, text="New Window button")
    seven_window.title("Поиск по составу")

    bg_uzhin = ImageTk.PhotoImage(file="по ужину.png")
    seven_window.attributes('-fullscreen', True)

    seven_canvas = Canvas(seven_window)
    seven_canvas.pack(fill="both", expand=True)
    seven_canvas.create_image(0, 0, image=bg_uzhin, anchor="nw")

def desert():
    global bg_desert
    eight_window = Toplevel(fourth_canvas)
    fourth_button_continue_4 = Button(eight_window, text="New Window button")
    eight_window.title("Поиск по составу")

    bg_desert = ImageTk.PhotoImage(file="по десерту.png")
    eight_window.attributes('-fullscreen', True)

    eight_canvas = Canvas(eight_window)
    eight_canvas.pack(fill="both", expand=True)
    eight_canvas.create_image(0, 0, image=bg_desert, anchor="nw")




first_window = Tk()

first_window.title ("Подбор блюд и рецептов по ингредиентам")
first_window.attributes('-fullscreen', True)

first_canvas=Canvas(first_window)
first_canvas.pack(fill="both", expand=True)

first_buttom_img=PhotoImage(file = "Your_img.png")

width_win=first_window.winfo_screenwidth()
height_win=first_window.winfo_screenheight()

first_button_continue=Button(first_window, image=first_buttom_img, height = height_win, width = width_win, command=second_window_vibor)
first_button_continue.place(relx=0.5, rely=0.5, anchor=CENTER)




first_canvas.mainloop()
