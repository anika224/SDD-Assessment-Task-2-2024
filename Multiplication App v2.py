from tkinter import *
from tkinter import font
from tkinter import messagebox as mb
import pyttsx3
import tkinter as tk
from functools import partial

#Making a Window
root = Tk()
root.title("Multiplication App")
root.geometry("1000x800")


#Text to Speech
def talk():
        engine = pyttsx3.init()
        engine.say(my_entry.get())
        engine.runAndWait()
        my_entry.delete(0,END)

my_entry = Entry(root, font=("Times New Roman", 10))
my_entry.pack(pady=20)

my_button = Button(root, text="Speak", command=talk)
my_button.pack(pady=20)


#Defining font change
def change_font(font_name, widgets_to_configure):
    global text_size
    text_font = (font_name, text_size)
    for widget in widgets_to_configure:
        widget.config(font=text_font)



#Defining text sizes
def set_text_size(size, font_name, widgets_to_configure):
    global text_size
    text_size = size
    for widget in widgets_to_configure:
        widget.config(font=(widget.cget("font")[0], text_size))
    

#Creating Menus
def create_menu(root):
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
   
    #settings main menu
    parent_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Settings", menu=parent_menu)
    
    
    #text size submenu
    text_size_menu = tk.Menu(parent_menu, tearoff=0)
    parent_menu.add_cascade(label="Text Size", menu=text_size_menu)
    
    text_sizes = [10, 12, 14, 16]  
    for size in text_sizes:
         text_size_menu.add_command(label=str(size), command=lambda size=size: set_text_size(size, font_name, widgets_to_configure))


    #font submenu
    font_menu = tk.Menu(parent_menu, tearoff=0)
    parent_menu.add_cascade(label="Font", menu=font_menu)
   
    font_families = font.families()
   
    for font_name in font_families:
        font_menu.add_command(label=font_name, command=partial(change_font, font_name, widgets_to_configure))


#a list of all the widgets to configure for fonts and text size
widgets_to_configure = [my_button,
                        my_entry]

quizzes_button
lessons_label,
lesson_content,
lesson_label,
quizzes_label,
x,
y,
self.question_label,
self.submit_button,
messagebox.showinfo,
messagebox.showerror,
ttk.Label]



create_menu(root)

root.mainloop()
