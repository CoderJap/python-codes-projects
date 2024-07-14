import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Sliders in custom tkinter")
root.geometry("700x450")

def sliding(value):
  my_label.configure(text=int(value))  

my_slide = customtkinter.CTkSlider(root,from_=0,to=100,command=sliding,orientation="horizontal",number_of_steps=10,width=400,height=50,fg_color="red",progress_color="green",button_color="yellow",button_hover_color="orange",state="normal") # border_width ids also one attribute here                     
my_slide.pack(pady=40)


# Set default starting point
my_slide.set(0)

my_label = customtkinter.CTkLabel(root,text=int(my_slide.get()),font=("Helvetica",18))
my_label.pack(pady=20)







root.mainloop()