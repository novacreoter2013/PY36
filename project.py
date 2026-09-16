from tkinter import *
from datetime import date

root = Tk()
root.title('WORKSHOP PARTCIPENT GREETING')
root.geometry('500x700')

lbl = Label(text = "HEY THERE!!" , fg = "black" , bg = "#1465c7" , height = 1 , width=300)

name_lbl = Label(text = "PLEASE ENTER YOUR FULL NAME" , bg = "#3895D3")
name_entry = Entry()

def display():

    name = name_entry.get()
    global message
    message = "HELLO GOOD EVENING \nTODAY's DATE IS :"
    greet = "WELCOME TO THE WORKSHOP " +name+ "\n"

    text_box.insert(END , greet)
    text_box.insert(END,message)
    text_box.insert(END , date.today())


text_box = Text(height = 3)

btn = Button(text = "CHEAK IN" , command = display , height = 1 , bg = "#1261A0" , fg = 'white')

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()
