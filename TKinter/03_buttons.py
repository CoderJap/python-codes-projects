from tkinter import *


root = Tk()

def myClick():
  myLabel = Label(root , text="Look! I  have clicked a Button!")
  myLabel.pack()

myButton = Button(root,text="Click Me" , padx=50 , pady=50 , command = myClick , fg="red" , bg="yellow")

myButton.pack()


root.mainloop()