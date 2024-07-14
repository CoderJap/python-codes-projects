from tkinter import *
from PIL import ImageTk , Image
from tkinter import filedialog

root  = Tk()
root.title("Using file dialog")


def open():
  
  root.filename = filedialog.askopenfilename(initialdir="C:\\Users\\Japjot Singh\\Desktop\\Python\\TKinter\\images",title="Select a File",filetypes=(("webp files","*.webp"),("all files","*.*"),("jpg files","*.jpg")))

  global my_image


  my_label = Label(root,text=root.filename).pack()
  my_image = ImageTk.PhotoImage(Image.open(root.filename))
  my_image_label = Label(image=my_image).pack()

my_btn = Button(root , text="Open File",command = open).pack()

btn = Button(root,text="close",command =root.quit).pack()

mainloop()