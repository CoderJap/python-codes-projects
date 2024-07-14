import customtkinter
from PIL import Image 
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
  def __init__(self):
    super().__init__()

# root = customtkinter.CTk()
    self.title("Option Menu in Custom Tkinter")
    self.geometry("700x450")\
    
    self.my_text  = customtkinter.CTkTextbox(self,width=600,height=300)
    self.my_text.pack(pady=20)

    self.my_btn = customtkinter.CTkButton(self , text="Clear Box",command=self.clear)
    self.my_btn.pack(pady=20) 

  def clear(self):
    self.my_text.delete('0.0',END)

app = App()
app.mainloop()