from tkinter import *
from PIL import ImageTk , Image

root  = Tk()
root.title("frames")

frame = LabelFrame(root,text="This is my Frame...",padx=50,pady=50) # inside padding
frame.pack(padx=10,pady=10) # outside frame padding 

b1 = Button(frame , text="Don't Click Here!",command=root.quit)


b2 = Button(frame , text="Other one...")

b1.grid(row=0,column=0)
b2.grid(row=1,column=1)




root.mainloop()