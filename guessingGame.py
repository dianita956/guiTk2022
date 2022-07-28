#color changing number guessing game
from tkinter import *
from random import randint

root = Tk()
root.title("Guessing the Number!")
root.iconbitmap('c:/users/dmlpz/gui/images/chicken.ico')
root.geometry("500x500")

numberLabel = Label(root, text="Pick a number \nBetween 1 and 10!", font=("Brush Script MT", 32))
numberLabel.pack(pady=20)

def guesser():
    if guessBox.get().isdigit():
        # Reset out label
        numberLabel.config(text="Pick a number \nBetween 1 and 10!")
        #find out how far away our pick was from the correct number
        dif = abs(num - int(guessBox.get()))

    # check to see if correct
        if int(guessBox.get()) == num:
            bc = "SystemButtonFace"
            numberLabel.config(text="Correct!!!")
        elif dif == 5:
        #set background color to white
            bc = "white"
        elif dif < 5:
            bc = f'#ff{dif}{dif}{dif}{dif}'
        else:
            bc = f'#{dif}{dif}{dif}{dif}ff'
        #change the background of the app
        root.config(bg=bc)
        #change the backgroun of the Label
        numberLabel.config(bg=bc)

    else:
        guessBox.delete(0, END)
        numberLabel.config(text="hey! that is not a number!")

def rando():
    global num
    num = randint(1,10)
    # clear the quess box
    guessBox.delete(0,END)
    # change the colors back to normal
    numberLabel.config(bg="SystemButtonFace", text="Pick a number \nBetween 1 and 10!")
    root.config(bg="SystemButtonFace")

guessBox = Entry (root, font=("Helvetica", 100), width=2)
guessBox.pack(pady=20)

guessButton = Button(root, text="Submit", command=guesser)
guessButton.pack(pady=20)

randButton = Button(root, text="New Number", command=rando)
randButton.pack(pady=20)


# generate a random number on start to run the function rando
rando()

root.mainloop()
