import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Text Box Widget in custom tkinter")
root.geometry("700x450")

def delete():
  my_text.delete(0.0,'end')

def copy():
  global stuff
  stuff = my_text.get(0.0,'end')

def paste():
  if stuff:
   my_text.insert('end',stuff)
  else:
    my_text.insert('end',"There is nothing to paste!")


my_text = customtkinter.CTkTextbox(root,width=600,height=200,corner_radius=1,border_width=10,border_color="purple",border_spacing=10,fg_color="yellow",text_color="black",font=("Helvetica",18),wrap="word", # char , word , none , default it is char
   activate_scrollbars="True",scrollbar_button_color="black",
   scrollbar_button_hover_color="red",      
 )
my_text.pack(pady=20)

my_frame = customtkinter.CTkFrame(root)
my_frame.pack(pady=10)

delete_btn = customtkinter.CTkButton(my_frame,text="Delete",command=delete)
copy_btn = customtkinter.CTkButton(my_frame,text="Copy",command=copy)
paste_btn = customtkinter.CTkButton(my_frame,text="Paste",command=paste)

delete_btn.grid(row=0,column=0)
copy_btn.grid(row=0,column=1,padx=10)
paste_btn.grid(row=0,column=2)


root.mainloop()