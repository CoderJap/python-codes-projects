import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Tab View in custom tkinter")
root.geometry("700x450")

# Create Tabview
my_tab = customtkinter.CTkTabview(root,width=600,height=250,corner_radius=20,fg_color="lightgreen",segmented_button_fg_color="yellow",segmented_button_selected_color="orange",segmented_button_selected_hover_color="purple",segmented_button_unselected_hover_color="pink",segmented_button_unselected_color="lightblue",text_color="black",state="normal",anchor="w") # anchor one have diff attributes like e , s , w , center and more etc u can check out 
my_tab.pack(pady=10)


tab_1 = my_tab.add("Tab 1")
tab_2 = my_tab.add("Tab 2")

# Put stuffs in tab

my_btn1 = customtkinter.CTkButton(tab_1,text="Click me in Tab 1")
my_btn1.pack(pady=10)

my_btn2 = customtkinter.CTkButton(tab_2,text="Click me in Tab 2")
my_btn2.pack(pady=10)



root.mainloop()