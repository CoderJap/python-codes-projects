import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Switch Widget in custom tkinter")
root.geometry("700x450")

def switcher():
  my_label.configure(text=switch_var.get())


def clicker():
  # switch.deselect()
  # switch.select()
  switch.toggle()


# create a string var
switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(root , text="Switch",command=switcher,variable=switch_var,onvalue="on",offvalue="off",switch_width=200,switch_height=25,corner_radius=20,border_color="green",border_width=5,fg_color="yellow",progress_color="lightblue",button_color="purple",button_hover_color="red",font=("Helvetica",18),text_color="orange",state="normal",)
switch.pack(pady=40)

# create a label
my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=10)

# create a button
my_btn = customtkinter.CTkButton(root,text="Toggle",command=clicker)
my_btn.pack(pady=20)


root.mainloop()
