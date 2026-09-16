from tkinter import *
from datetime import date

root = Tk()
root.title('GETTING STARTED WITH WIDGETS')
root.geometry('400x600')\

lbl = Label(text = "HEY THERE!!" , fg = "black" , bg = "#072f5f" , height = 1 , width=300)

name_lbl = Label(text = "FULL NAME" , bg = "#3895D3")
name_entry = Entry()

def display():

    name = name_entry.get()
    global message
    message = "WELCOME TO THE APPLICATION!!! \nTODAY's DATE IS :"
    greet = "HELLO " +name+ "\n"

    text_box.insert(END , greet)
    text_box.insert(END,message)
    text_box.insert(END , date.today())


text_box = Text(height = 3)

btn = Button(text = "BEGIN" , command = display , height = 1 , bg = "#1261A0" , fg = 'white')

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()
