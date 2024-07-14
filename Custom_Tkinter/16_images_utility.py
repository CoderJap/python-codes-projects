import customtkinter
from PIL import Image 

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Using custom tkinter Images Utility")
root.geometry("700x450")


my_img = customtkinter.CTkImage(light_image=Image.open('C:\\Users\\Japjot Singh\\Desktop\\Python\\Custom_Tkinter\\images\\demo-1.webp'),dark_image=Image.open('C:\\Users\\Japjot Singh\\Desktop\\Python\\Custom_Tkinter\\images\\demo-1.webp'),size=(500,500))
# size -> (Width,Height)



my_label = customtkinter.CTkLabel(root , text="",image=my_img)
my_label.pack(pady=10)


root.mainloop()