import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Scrollable frames in custom tkinter")
root.geometry("700x450")

# Create a scrollable frame 
my_frame = customtkinter.CTkScrollableFrame(root,orientation="vertical",height=200,width=300,label_text="Frame",label_fg_color="purple",label_text_color="yellow",label_font=("Helvetica",18),                            label_anchor="center", # w , n , ne , e , se ,s , sw , nw , center
 border_width=3,border_color="pink",fg_color="lightblue",  scrollbar_fg_color="orange",scrollbar_button_color="black",corner_radius=5,                                    )
my_frame.pack(pady=40)
# for loop for button

for x in range(20):
  customtkinter.CTkButton(my_frame,text="This is a Button!").pack(pady=10)

root.mainloop()