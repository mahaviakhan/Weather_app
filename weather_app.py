from tkinter import *
from tkinter import Tk
from tkinter import Tk, Label, Entry
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
#from timezonefinder import timezonefinder
from datetime import datetime, timezone
import requests
import pytz

win = Tk()
win.title("WeatherWise")
win.geometry("550x670+300+200")
win.resizable(False, False)

def weatherupdate():
    city = textfield.get()
    geolocator = Nominatim(user_agent="geoapiExercise")
    try:
        location = geolocator.geocode(city)
        if location:
            try:
                
                from timezonefinder import TimezoneFinder
                obj = TimezoneFinder()
                timezone_str = obj.timezone_at(lng=location.longitude, lat=location.latitude)
            except ImportError:
                #timezonefinder error.
                timezone_str = "UTC"  

            tz = pytz.timezone(timezone_str)
            current_time = datetime.now(tz)

            formatted_datetime = current_time.strftime('%Y-%m-%d | %H:%M')
            clock.config(text=formatted_datetime)

        #api key and url
        api_key = "53e1aa9433b3dc60035ac08fc32cc023"
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(api_url)
        weather_data = response.json()

        temperature_kelvin = weather_data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        condition = weather_data['weather'][0]['main']
        pressure = weather_data['main']['pressure']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        description = weather_data['weather'][0]['description']

        tem.config(text=f"{temperature_celsius:.2f} °C")
        con.config(text=f"{condition} | Feels like {temperature_celsius:.2f}°C")
        w.config(text=f": {wind_speed} m/s")
        h.config(text=f": {humidity}%")
        p.config(text=f": {pressure} hPa")
        d.config(text=f": {description}")

    except (GeocoderTimedOut, GeocoderUnavailable) as e:
        print(f"Geocoding service error: {e}")
        clock.config(text="Location service error")
        tem.config(text="")
        con.config(text="")
        w.config(text="")
        h.config(text="")
        p.config(text="")
        d.config(text="")

    city = textfield.get()
    location_label.config(text=f"Location: {city}")
# Textfield (Entry)
textfield = Entry(win, justify="center", width=25, font=("poppines", 20, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=75, y=80, height=35) 

# Search icon
search_icon = PhotoImage(file="E:/PYTHON/PYTHON PROJECTS/WEATHER APP NEW/icon 2.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=weatherupdate)
myimage_icon.place(x=415, y=80, height=35) 
#logo
logo_image=PhotoImage(file="E:/PYTHON/PYTHON PROJECTS/WEATHER APP NEW/weather.png")
logo=Label(image=logo_image)
logo.place(x=320,y=135,width=130,height=130)

#location name
location_label = Label(win, text="", font=("helvetica", 15, "bold"))
location_label.place(x=75, y=150)

# Time
clock = Label(win, font=("helvetica", 15, "bold"))
clock.place(x=75, y=120)
# Wind
wind = Label(win, text="WIND", font=("helvetica", 15, "bold"))
wind.place(x=80, y=440)

w = Label(win, text="", font=("time new roman", 15, "bold"), borderwidth=0, highlightthickness=0)
w.place(x=380, y=440)

# Humidity
hum = Label(win, text="HUMIDITY", font=("helvetica", 15, "bold"))
hum.place(x=80, y=480)

h = Label(win, text="", font=("time new roman", 15, "bold"), borderwidth=0, highlightthickness=0)
h.place(x=380, y=480)

# Description
dis = Label(win, text="DESCRIPTION", font=("helvetica", 15, "bold"))
dis.place(x=80, y=520)

d = Label(win, text="", font=("time new roman", 15, "bold"), borderwidth=0, highlightthickness=0)
d.place(x=380, y=520)

# Pressure
pre = Label(win, text="PRESSURE", font=("helvetica", 15, "bold"))
pre.place(x=80, y=560)

p = Label(win, text="", font=("time new roman", 15, "bold"), borderwidth=0, highlightthickness=0)
p.place(x=380, y=560)

# text:
text1 = Label(win, text="CURRENT WEATHER", font=("times new roman", 20, "bold")).place(x=190, y=275)

# temperature
tem = Label(win, font=("time new roman", 18, "bold"))
tem.place(x=190, y=320)

# condition
con = Label(win, font=("time new roman", 15, "bold"))
con.place(x=190, y=360)

# Weather text
weather_details = Label(win, text="Weather Details", font=("helvetica", 15, "bold"), fg="black")
weather_details.pack(padx=5, pady=10, side=BOTTOM)

# Title
name_label = Label(win, text="WeatherWise", font=("Times New Roman", 30, "bold"))
name_label.pack(padx=5, pady=10, side=TOP)

win.mainloop()