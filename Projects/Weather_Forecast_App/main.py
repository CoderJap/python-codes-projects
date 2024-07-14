from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import pytz
from PIL import Image, ImageTk
from opencage.geocoder import OpenCageGeocode
import requests

PATH = "C:\\Users\\Japjot Singh\\Desktop\\Python\\Projects\\Weather_Forecast_App\\images\\"
root = Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False,False)

def getWeather():

  city = textfield.get()

  key = 'f9139d2842954cf2b078012b37d4d4bd' # open cage api key
  geocoder = OpenCageGeocode(key)
  result = geocoder.geocode(city)
      
  location = result[0]
  lat = location['geometry']['lat']
  lng = location['geometry']['lng']
            
  obj = TimezoneFinder()
  timezone_result = obj.timezone_at(lng=lng, lat=lat)
            
  timezone.config(text=timezone_result)
  long_lat.config(text=f"{round(lat, 4)}°N, {round(lng, 4)}°E")
                
  home = pytz.timezone(timezone_result)
  local_time = datetime.now(home)
  current_time = local_time.strftime("%I:%M %p")
  clock.config(text=current_time)



          

  # weather 
  api=f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lng}&exclude=hourly&appid=3bd9a1cdd214253c105ebfd471ba907"
  json_data = requests.get(api).json()

  # current
  # temp = json_data['main']['temp']
  print(json_data)

 




# icon
image_icon = PhotoImage(file=f"{PATH}Images\\logo.png")
root.iconphoto(False,image_icon)

Round_box = PhotoImage(file=f"{PATH}Images\\Rounded Rectangle 1.png")
Label(root,image=Round_box,bg="#57adff").place(x=30,y=110)

#label
label1 = Label(root , text="Temperature",font=("Helvetica",11),fg="white",bg="#203243")
label1.place(x=50,y=120)

label2 = Label(root , text="Humidity",font=("Helvetica",11),fg="white",bg="#203243")
label2.place(x=50,y=140)

label3 = Label(root , text="Pressure",font=("Helvetica",11),fg="white",bg="#203243")
label3.place(x=50,y=160)

label4 = Label(root , text="Wind Speed",font=("Helvetica",11),fg="white",bg="#203243")
               
label4.place(x=50,y=180)

label5 = Label(root , text="Description",font=("Helvetica",11),fg="white",bg="#203243")
label5.place(x=50,y=200)

# search box
search_image = PhotoImage(file=f"{PATH}Images\\Rounded Rectangle 3.png") 
my_image = Label(image=search_image,bg="#57adff")
my_image.place(x=270,y=120)

weat_image = PhotoImage(file=f"{PATH}Images\\Layer 7.png")
weatherimage = Label(root,image=weat_image,bg="#203243")
weatherimage.place(x=290,y=127)

textfield = tk.Entry(root,justify="center",width=15,font=("poppins",25,"bold"),bg="#203243",border=0,fg="white")
textfield.place(x=370,y=130)
textfield.focus()

Search_icon = PhotoImage(file=f"{PATH}Images\\Layer 6.png")
myimage_icon = Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=getWeather)
myimage_icon.place(x=645,y=125)

# Bottom box 
frame = Frame(root,width=900,height=180,bg="#212120")
frame.pack(side=BOTTOM)

# bottom boxes\
firstbox = PhotoImage(file=f"{PATH}Images\\Rounded Rectangle 2.png")

secondbox = PhotoImage(file=f"{PATH}Images\\Rounded Rectangle 2 copy.png")

Label(frame,image=firstbox,bg="#212120").place(x=30,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=300,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=400,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=500,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=600,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=700,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=800,y=30)


# clock (to place time)

clock = Label(root,font=("Helvetica",30,'bold'),fg="white",bg="#57adff")
clock.place(x=30,y=20)


# timezone

timezone = Label(root,font=("Helvetica",20),fg="white",bg="#57adff")
timezone.place(x=700,y=20)

long_lat= Label(root,font=("Helvetica",10),fg="white",bg="#57adff")
long_lat.place(x=700,y=50)


































root.mainloop()