import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Text Box Widget in custom tkinter")
root.geometry("700x450")

# Create a function
def input():
  dialog = customtkinter.CTkInputDialog(text="What is your Name:",title="Hello There!",fg_color="yellow",button_fg_color="lightgreen",button_hover_color="lightblue",button_text_color="black",entry_fg_color="pink",entry_border_color="orange",entry_text_color="black",text_color="purple")
  user_input = dialog.get_input()

  if user_input:
    my_label.configure(text=f"Hello {user_input}")
  else:
    my_label.configure(text=f"You forgot to type anything!")


# Create a button
my_btn = customtkinter.CTkButton(root,text="Click Me",command=input)
my_btn.pack(pady=40)

# Create a Label
my_label = customtkinter.CTkLabel(root , text="")
my_label.pack(pady=10)






root.mainloop()