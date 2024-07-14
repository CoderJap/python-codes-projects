import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title("Combo boxes in custom tkinter")
root.geometry("700x450")

def color_picker(choice):
  output_label.configure(text=choice,text_color=choice)

def color_picker2():
  output_label.configure(text=my_combo.get(),text_color=my_combo.get())

def color_picker_yellow():
    # set the combo box option
    my_combo.set("Yellow")
    output_label.configure(text=my_combo.get(),text_color=my_combo.get())


my_label = customtkinter.CTkLabel(root , text="Pick a Color",font=("Helvetica",18))
my_label.pack(pady=40)

# Let's set the values for our combo box
colors = ["Red","Green","Blue"]

# let's create our combo box
my_combo = customtkinter.CTkComboBox(root,values=colors,height=50,width=200,font=("Helvetica",18),dropdown_font=("Helvetica",18),corner_radius=20,border_width=2,border_color="orange",button_color="orange",button_hover_color="lightblue",dropdown_hover_color="yellow",dropdown_fg_color="lightgreen",dropdown_text_color="black",text_color="white",hover=True,justify="center",state="normal")
my_combo.pack(pady=0)

# Create a Button
my_btn = customtkinter.CTkButton(root,text="Pick a Color",command=color_picker2)
my_btn.pack(pady=10)

# Yellow Button
yellow_btn = customtkinter.CTkButton(root,text="Pick Yellow",command=color_picker_yellow)
yellow_btn.pack(pady=10)


# Let's create an outout label
output_label = customtkinter.CTkLabel(root , text="",font=("Helvetica",18))
output_label.pack(pady=20)


root.mainloop()