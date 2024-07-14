import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()
root.geometry("700x450")

def game():
  if check_var.get() == "on":
    my_label.configure(text="You Clicked this CheckBox!!")
  else:
     my_label.configure(text="You Didn't Clicked this CheckBox!!")

  text_var.set("Game Starting...")



def clear():
  my_check.deselect()
  text_var.set("Would you like to play a game?")

# Checkbox State
check_var = customtkinter.StringVar(value="off")

# Checkbox Text
text_var = customtkinter.StringVar(value="Would you like to play a game?")

my_check = customtkinter.CTkCheckBox(root,text="Would you like to play a game?",variable=check_var,onvalue="on",offvalue="off",checkbox_width=50,checkbox_height=50,font=("helvetica",18),corner_radius=30,fg_color="red",hover_color="green",hover=False,textvariable=text_var)
my_check.pack(pady=40)

my_btn = customtkinter.CTkButton(root,text="Submit",command=game)
my_btn.pack(pady=20)

clear_btn = customtkinter.CTkButton(root , text="Clear Me",command=clear).pack(pady=15)

toggle_btn = customtkinter.CTkButton(root , text="Toggle",command=my_check.toggle).pack(pady=10)

select_btn = customtkinter.CTkButton(root , text="Select",command=my_check.select).pack(pady=10)

my_label = customtkinter.CTkLabel(root , text="")
my_label.pack(pady=20)


root.mainloop()