from tkinter import *

root = Tk()
root.title("me")
root.geometry ("400x400")

def hello():
    hello_label = Label(root, text="Hello "+ myTextbook.get())
    hello_label.pack()

myLabel = Label(root, text= "enter your first name:")
myLabel.pack()

myTextbox = Entry(root, width=30)
myTextbox.pack()

myButton = Button(root,text="Submit", command=hello)
myButton.pack()


root.mainloop()
