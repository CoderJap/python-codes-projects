from tkinter import *
from PIL import ImageTk , Image

root = Tk()
root.title("How to create new windows in tkinter")

def open():
  top = Toplevel()
  lbl = Label(top , text="This is a second window").pack()
  btn2 = Button(top , text="Close window",command=top.destroy).pack()

btn = Button(root,text="Open Second Window",command=open).pack()





mainloop()