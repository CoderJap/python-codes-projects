import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Open new window in custom tkinter")
root.geometry("700x450")


def new():
  new_window  = customtkinter.CTkToplevel(root,fg_color="white",)
  new_window.title("This is a new window")
  new_window.geometry("400x200")
  new_window.resizable(False,True) # Width, Height

  def close():
    new_window.destroy()
    new_window.update()

  # Close Button
  new_btn = customtkinter.CTkButton(new_window,text="Close Button",command=close)
  new_btn.pack(pady=40)



my_btn = customtkinter.CTkButton(root,text="Open New Window",command=new)
my_btn.pack(pady=40)

root.mainloop()
