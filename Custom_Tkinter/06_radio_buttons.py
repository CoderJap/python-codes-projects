import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title("Radio boxes in custom tkinter")
root.geometry("700x450")

def get_rad():

  if radio_var.get() == "other":
    my_label2.configure(text="Please make a selection")
  elif radio_var.get() == "Yes":
    my_label2.configure(text="Of Course You Like Pizza!")
  else:
    my_label2.configure(text="What's wrong with you!")
    

my_label1 = customtkinter.CTkLabel(root,text="Do You Like Pizza",font=("Helvetica",18))
my_label1.pack(pady=40)


radio_var = customtkinter.StringVar(value="other")

# Radio Button 1
my_rad_1 = customtkinter.CTkRadioButton(root,text="Yes I Do",value="Yes",variable=radio_var,radiobutton_width=30,radiobutton_height=30,corner_radius=5,border_width_checked=5,border_width_unchecked=2,border_color="red",hover_color="pink",fg_color="green",hover=False,text_color="yellow",font=("Helvetica",18),state="normal",text_color_disabled="orange")
my_rad_1.pack(pady=10)

# Radio Button 2
my_rad_2 = customtkinter.CTkRadioButton(root,text="No I Don't",value="No",variable=radio_var,radiobutton_width=30,radiobutton_height=30,corner_radius=5,border_width_checked=5,border_width_unchecked=2,border_color="red",hover_color="pink",fg_color="green",hover=False,text_color="yellow",font=("Helvetica",18),state="normal",text_color_disabled="orange")
my_rad_2.pack(pady=10)

# Button
my_btn = customtkinter.CTkButton(root,text="Select",command=get_rad).pack(pady=10)


# Label
my_label2 = customtkinter.CTkLabel(root , text="",font=("Helvetica",18))
my_label2.pack(pady=10)


root.mainloop()