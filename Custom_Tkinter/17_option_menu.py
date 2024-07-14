import customtkinter
from PIL import Image 

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Option Menu in Custom Tkinter")
root.geometry("700x450")

def color_picker(choice):
  my_label.configure(text=choice)

def color_picker2():
  my_label.configure(text=my_option.get(),text_color=my_option.get())

def yellow():
  my_option.set("Yellow")
  my_label.configure(text=my_option.get(),text_color=my_option.get())

# set the options for our optionMenu
colors = ["Red","Green","Blue"]

# Create OptionMenu
my_option = customtkinter.CTkOptionMenu(root,values=colors,height=50,width=200,font=("Helvetica",18),fg_color="white",dropdown_font=("Helvetica",18),button_color="red",button_hover_color="green",dropdown_hover_color="purple",dropdown_fg_color="blue",dropdown_text_color="orange",text_color="red",hover=True,anchor="center",state="normal",text_color_disabled="balck",dynamic_resizing=False,corner_radius=20)
my_option.pack(pady=40)

my_label = customtkinter.CTkLabel(root , text="")
my_label.pack(pady=10)

pick_btn = customtkinter.CTkButton(root,text="Make a Choice",command=color_picker2)
pick_btn.pack(pady=10)

yellow_btn = customtkinter.CTkButton(root,text="Pick Yellow",command=yellow)
yellow_btn.pack(pady=10)

root.mainloop()