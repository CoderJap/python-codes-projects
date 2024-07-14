import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title("Progress bar in Custom Tkinter")
root.geometry("700x450")

def clicked():
  progressbar.step()
  my_label.configure(text=(int(progressbar.get()*100)))

def start():
  progressbar.start()

def stop():
  progressbar.stop()

progressbar = customtkinter.CTkProgressBar(root,orientation="horizontal",height=50,width=300,corner_radius=20,border_width=2,border_color="yellow",fg_color="orange",progress_color="pink",mode="indeterminate",determinate_speed=2,indeterminate_speed=5,)
progressbar.pack(pady=40)

# Set the default progress starting point
progressbar.set(0)


my_btn= customtkinter.CTkButton(root,text="Click Me",command=clicked)
my_btn.pack(pady=10)

start_btn = customtkinter.CTkButton(root , text="Start",command=start).pack(pady=10)

stop_btn = customtkinter.CTkButton(root , text="Stop",command=stop).pack(pady=10)

my_label = customtkinter.CTkLabel(root,text="",font=("Helvetica",18))
my_label.pack(pady=10)




root.mainloop()


