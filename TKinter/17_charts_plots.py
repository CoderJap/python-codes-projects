from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title("Charts & Plots in Tkinter")
root.geometry("400x400")

def graph():
  house_prices = np.random.normal(200000,25000,5000)
  plt.hist(house_prices,200)
  plt.show()

my_btn = Button(root , text="Graph It!",command = graph)
my_btn.pack()
  



root.mainloop()