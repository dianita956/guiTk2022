from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Adding a spionbox/color picker!")
root.iconbitmap('c:/users/dmlpz/gui/images/chicken.ico')
root.geometry("500x400")

'''
def grab():
    myLabel.config(text=mySpin2.get())

#mySpin = Spinbox(root, from_=0, to=10, increment=2, font=("Helvetica", 20))
mySpin2 = Spinbox(root, from_=0, to=10, values=("red", "blue", "green", "purple"), font=("Helvetica", 20))
mySpin2.pack(pady=20)

myButton = Button(root, text="submit", command=grab)
myButton.pack(pady=20)

myLabel = Label(root, text="")
myLabel.pack(pady=20)
'''
def color():
    myColor = colorchooser.askcolor()[1]
    myLabel = Label(root, text=myColor).pack(pady=10)
    myLabel2 = Label(root, text="You picked a color", font=("Helvetica", 32), bg=myColor).pack()

myButton = Button(root, text="Pick a color!", command=color).pack()

myColor = colorchooser.askcolor()


root.mainloop()
