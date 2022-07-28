#to list all installed packeges run: pip freeze
from tkinter import *

from PIL import ImageTk,Image

root =Tk()
root.title("Learning how to add images with tkinter")
#adding an icon top left corner
root.iconbitmap('images/chicken.ico')

#adding an images 3 steps process
myImg1 = ImageTk.PhotoImage(Image.open("images/chicken.png"))
myImg2 = ImageTk.PhotoImage(Image.open("images/anxiety.png"))
myImg3 = ImageTk.PhotoImage(Image.open("images/behavior.png"))
myImg4 = ImageTk.PhotoImage(Image.open("images/math-anxiety2.png"))

imageList = [myImg1, myImg2, myImg3, myImg4]
#to call item in a imageList 0,1,2,3
#imageList[2]

myLabel = Label(image=myImg1)
myLabel.grid(row=0, column=0, columnspan=3)


#defining the function of the buttons
def forward(image_number):
    global myLabel
    global button_forward
    global button_back

    myLabel.grid_forget()
    myLabel = Label(image=imageList[image_number-1])
    buttonForward = Button(root, text=">>>", command=lambda: forward(image_number-1))
    buttonBack = Button(root, text="<<<", command=lambda: back(image_number-1))

    if image_number == 4:
        buttonForward=Button(root, text=">>", state=DISABLE)

    myLabel.grid(row=0, column=0, columnspan=3)
    buttonBack.grid(row=1, column=0)
    buttonForward.grid(row=1, column=2)



def back():
    global myLabel
    global button_forward
    global button_back

    myLabel.grid_forget()
    myLabel = Label(image=imageList[image_number-1])
    buttonForward = Button(root, text=">>>", command=lambda: forward(image_number-1))
    buttonBack = Button(root, text="<<<", command=lambda: back(image_number-1))


buttonBack = Button(root, text="<<", command=back)
buttonExit = Button(root, text="Exit Program", command=root.quit)
buttonForward = Button(root, text=">>>", command=lambda: forward(2))

buttonBack.grid(row=1, column=0)
buttonExit.grid(row=1, column=1)
buttonForward.grid(row=1, column=2)


#creating an exit button
#buttonQuit = Button(root, text="exit program", command=root.quit)
#buttonQuit.pack()


root.mainloop()
