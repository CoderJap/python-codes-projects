from tkinter import *
from PIL import ImageTk , Image

root  = Tk()
root.title("Sliders in Tkinter")
root.geometry("400x400")

vertical  = Scale(root , from_=0, to=200)
vertical.pack()

def slide(v):
  my_label = Label(root , text=horizontal.get()).pack()
  root.geometry(f"{horizontal.get()}x400")

horizontal = Scale(root , from_=0,to=400,orient=HORIZONTAL,command=slide)
horizontal.pack()




my_btn = Button(root , text="Click Me!",command = slide).pack()

mainloop()

