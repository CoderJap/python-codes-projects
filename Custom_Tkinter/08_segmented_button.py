import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Segmented Buttons in custom tkinter")
root.geometry("700x450")

# Create our function
def clicker(value):
  my_label.configure(text=f"Hello {value}")

# Our button values 
my_values = ["John","April","Wes"]

# Create the button
my_seg_btn = customtkinter.CTkSegmentedButton(root,values=my_values,command=clicker,width=300,height=100,font=("Helvetica",18),corner_radius=3,border_width=5,fg_color="orange",selected_color="lightblue",selected_hover_color="yellow",unselected_color="pink",unselected_hover_color="purple",text_color="black",state="normal",text_color_disabled="darkblue",dynamic_resizing="True")
my_seg_btn.pack(pady=40)

# Set default Selection
# my_seg_btn.set("John")

# Create a Label
my_label = customtkinter.CTkLabel(root,text="",font=("Helvetica",18))
my_label.pack(pady=20)

root.mainloop()
