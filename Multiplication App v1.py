from tkinter import *
from tkinter import font
import pyttsx3
from tkinter import messagebox as mb

#Making a window
root = Tk()
root.title("Multiplication App")
root.geometry(window_name.winfo_screenwidth(),window_name.winfo_screenheight())
window_name = "%dx%d" %

#Main Menu Label
label = tk.Label(window, text="Hello Tkinter!")
label.pack()



def talk():
    engine = pyttsx3.init()
    engine.say(my_entry.get())
    engine.runAndWait()
    my_entry.delete(0,END)

def tts_button():
    pass

#if tts_button == True:
#    talk() == True
#else:
#    talk() == False


my_entry = Entry(root, font=("Times New Roman", 10))
my_entry.pack(pady=20)

my_button = Button(root, text="Speak", command=talk)
my_button.pack(pady=20)


def create_menu(root):
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
   
    #edit main menu
    parent_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Edit", menu=parent_menu)
    
    
    #text size submenu
    text_size_menu = tk.Menu(parent_menu, tearoff=0)
    parent_menu.add_cascade(label="Text Size", menu=text_size_menu)
    
    text_sizes = [10, 12, 14, 16]  
    for size in text_sizes:
         text_size_menu.add_command(label=str(size), command=lambda size=size: set_text_size(size, font_name, widgets_to_configure))
   



root.mainloop
    
