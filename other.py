from tkinter import *
from tdlGame import travelGame

root = Tk()

root.title("TDL Travel Fortune!")
root.iconbitmap('c:/users/dmlpz/gui/images/tdl.ico')
root.geometry("600x400")

def submit():
    game = travelGame(myBox.get())
    myLabel.config(text=game)

myBox = Entry(root, text="play", command=game)
myBox.pack(pady=20)

myLabel = Label(root, text = "", font=("Helvetica", 18))
myLabel.pack(pady=20)

myButton = Button(root, text="Submit choice", command=submit)
myButton.pack(pady=20)


root.mainloop()
