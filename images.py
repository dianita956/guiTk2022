#to list all installed packeges run: pip freeze
from tkinter import *

from PIL import ImageTk,Image

root =Tk()
root.title("Learning how to add images with tkinter")
#adding an icon top left corner
root.iconbitmap('c:/users/dmlpz/gui/chicken.ico')

#adding an images 3 steps process
myImg = ImageTk.PhotoImage(Image.open("chicken.png"))
myLabel = Label(image=myImg)
myLabel.pack()






#creating an exit button
buttonQuit = Button(root, text="exit program", command=root.quit)
buttonQuit.pack()





root.mainloop()
