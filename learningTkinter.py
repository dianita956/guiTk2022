#learning tkinter
#code written by Diane Lopez
#add grid 7/14/22
from tkinter import *

root = Tk()
root.title("me")
root.geometry ("400x400")

def hello():
    hello_label = Label(root, text="Hello "+ myTextbook.get())
    hello_label.pack()

myLabel = Label(root, text= "enter your first name:")
myLabel.grid(row=0, column=0)

myTextbox = Entry(root, width=30)
myTextbox.pack(row=1, column=0)

myButton = Button(root,text="Submit", command=hello)
myButton.pack()


root.mainloop()
