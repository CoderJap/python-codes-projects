import customtkinter
from PIL import Image 

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Option Menu in Custom Tkinter")
root.geometry("700x450")

mode = "dark"


def switch_modes():
  global mode
  if mode == "dark":
    customtkinter.set_appearance_mode("light")
    mode = "light"

  else:
    customtkinter.set_appearance_mode("dark")
    mode = "dark"



my_text = customtkinter.CTkTextbox(root,width=600,height=300)
my_text.pack(pady=20)

my_btn = customtkinter.CTkButton(root,text="Change Light/Dark",command=switch_modes)
my_btn.pack(pady=20)




root.mainloop()