import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Using custom tkinter fonts utility")
root.geometry("700x450")

def change():
  my_font.configure(underline=False,overstrike=False,size=22,slant="roman")

my_font = customtkinter.CTkFont(family="Helvetica",size=44,weight="bold",slant="italic",underline=True,overstrike=True) # weight - bold/normal , slant - italic/roman

my_label  = customtkinter.CTkLabel(root,text="This is a Text",font=my_font)
my_label.pack(pady=20)

my_btn = customtkinter.CTkButton(root , text="Change Text",command=change)
my_btn.pack()

root.mainloop()
