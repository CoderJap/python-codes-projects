from tkinter import *


root = Tk()

e = Entry(root , width=50 , bg="yellow" , fg="green") # for input box
e.pack()
e.insert(0,"Enter your Name: ") # Default Text inside the input box

def myClick():
  myLabel = Label(root , text=f"Hello {e.get()}")
  myLabel.pack()

myButton = Button(root,text="Submit" ,  command = myClick )

myButton.pack()


root.mainloop()