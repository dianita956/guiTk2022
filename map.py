from tkinter import *
import tkintermapview

root = Tk()
root.title("Guessing the Number!")
root.iconbitmap('c:/users/dmlpz/gui/images/chicken.ico')
root.geometry("900x700")

myLabel = LabelFrame(root)
myLabel.pack(pady=20)

mapWidget = tkintermapview.TkinterMapView(myLabel, width=800, height=600, corner_radius=0)
#set coordinates for san antonio botanical gardens
#mapWidget.set_position(29.45896, -98.46053)

#set address
mapWidget.set_address("555 Funston Pl, San Antonio, TX 78209")
#set a zoom level
mapWidget.set_zoom(16)


mapWidget.pack()



root.mainloop()
