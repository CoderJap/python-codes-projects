from tkinter import *
from PIL import ImageTk, Image
import requests
import json


root  = Tk()
root.title("AQI APP")
root.geometry("310x120")

# Create Zipcode lookup function

def zipLookup():
  # zip.get()
  # zipLabel = Label(root , text=zip.get())
  # zipLabel.pack(row=1,column=0,columnspan=2)

  try:
    api_request = requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip.get()}&distance=5&API_KEY=5A3B61C1-62D6-4D86-8444-CC2EB4F4DDF8")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']

    if category == "Good":
      weather_color = "#0C0"

    elif category == "Moderate":
      weather_color = "#FFFF00"

    elif category == "Unhealthy for Sensitive Groups":
      weather_color = "#ff9900"

    elif category == "Unhealthy":
      weather_color = "#FF0000"

    elif category == "Very Unhealthy":
      weather_color = "#990066"

    elif category == "Hazardous":
      weather_color = "#660000"

    root.configure(background=weather_color)

    myLabel = Label(root , text=f"City: {city}\nAir Quality: {quality}\nCategory: {category}",font=("Helvetica",15),pady=7,background=weather_color)
    myLabel.grid(row=1,column=0)

  except Exception as e:
    api = "Error..."
  



# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=5A3B61C1-62D6-4D86-8444-CC2EB4F4DDF8




zip =Entry(root)
zip.grid(row=0,column=0)

zipButton= Button(root , text="Lookup Zipcode",command = zipLookup)
zipButton.grid(row=0,column=1)





root.mainloop()