from tkinter import *
import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()

root.title("Entry widgets in custom tkinter")
root.geometry("600x350")

def submit():
  my_label.configure(text=f"Hello {my_entry.get()}")

def clear():
  my_entry.delete(0,END)



my_label = customtkinter.CTkLabel(root , text="",font=("Helvetica",24))
my_label.pack(pady=40)

my_entry = customtkinter.CTkEntry(root , placeholder_text="Enter Your Name",height=50,width=200,font=("Helvetica",18),corner_radius=50,text_color="black",placeholder_text_color="purple",
fg_color=("orange","yellow"), # outer , inner
)

my_entry.pack(pady=20)

my_button = customtkinter.CTkButton(root , text = "Submit",command= submit)
my_button.pack(pady=10)

clear_button = customtkinter.CTkButton(root , text="Clear",command=clear)
clear_button.pack(pady=10)
root.mainloop()




