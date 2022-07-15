from tkinter import *

root =Tk()

#creating an textbox(entry box) you can change the dimension and color.
e = Entry(root, width=50)
e.pack()
#default text inside text box
e.insert(0,"enter your name: ")


'''
#creating a label widget
myLabel1 =Label(root, text ="Hello World")
myLabel2 =Label(root, text="my name is diane")
myLabel3 =Label(root, text=" ")

#add labels onto the screen

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)
'''
# adding buttons, padx and pady changes the dimension to the button
def myClick():
    hello = "Hello " + e.get()
    myLabel1 = Label(root, text=hello)
    myLabel1.pack()

myButton = Button(root, text="click here, pls to continue", padx=50, pady=50, command=myClick, fg="#ffff33", bg="#0000ff")
myButton.pack()

root.mainloop()
