from tkinter import *
from PIL import ImageTk , Image


root  = Tk()
root.title("Checkboxes in Tkinter")
root.geometry("400x400")

# var =IntVar()
var =StringVar()

c= Checkbutton(root , text="Check this",variable=var,onvalue="On",offvalue="Off")
c.deselect() # so that at start it remains unchecked
c.pack()

def show():
  mylabel = Label(root , text=var.get())
  mylabel.pack()

myButton= Button(root , text="Show Selection",command=show)
myButton.pack()


mainloop()