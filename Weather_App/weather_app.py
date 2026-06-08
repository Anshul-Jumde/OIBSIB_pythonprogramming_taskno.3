import customtkinter as ctk
import datetime

ctk.set_appearance_mode("dark")
import requests

def get_weather():
    city = city_entry.get()
    city = city_entry.get().strip()

    if not city:
        condition_label.configure(
            text="Please enter a city name!"
        )
        return

    try:
        url = f"https://wttr.in/{city}?format=j1"
        data = requests.get(url).json()

        temperature = data["current_condition"][0]["temp_C"]
        
        temp = int(temperature)

        if temp >= 40:
            temperature_label.configure(text_color="red")
        elif temp >= 30:
            temperature_label.configure(text_color="orange")
        elif temp >= 20:
            temperature_label.configure(text_color="green")
        else:
            temperature_label.configure(text_color="blue")
            print("Temperature:", temperature)
            
            
        temperature_label.configure(
            text=f"Temperature: {temperature}°C"
        )
                
        humidity = data["current_condition"][0]["humidity"]
        wind = data["current_condition"][0]["windspeedKmph"]
        condition = data["current_condition"][0]["weatherDesc"][0]["value"]
        feels_like = data["current_condition"][0]["FeelsLikeC"]

        city = city.title()
        app.title(f"Smart Weather App - {city}")

        if "Clear" in condition or "Sunny" in condition:
            emoji = "☀️"
            tip = "Stay hydrated and avoid direct sunlight."
            app.configure(fg_color="#87CEEB")

        elif "Cloud" in condition:
            emoji = "☁️"
            tip = "Pleasant weather today."
            app.configure(fg_color="#94A3B8")

        elif "Rain" in condition:
            emoji = "🌧️"
            tip = "Carry an umbrella."
            app.configure(fg_color="#64748B")

        else:
            emoji = "🌍"
            tip = "Have a great day."
            app.configure(fg_color="#0F172A")
    

        humidity_label.configure(
            text=f"Humidity: {humidity}%"
        )

        wind_label.configure(
            text=f"Wind Speed: {wind} km/h"
        )
        feels_label.configure(
    text=f"Feels Like: {feels_like}°C"
        )

        city_label.configure(
            text=f"Weather In: {city}"
        )

        tip_label.configure(
            text=f"Tip: {tip}"
        )
        last_search_label.configure(
    text=f"Last Search: {city}"
        )

        condition_label.configure(
        text=f"Condition: {emoji} {condition}"
    )

    except Exception as e:
        print("FULL ERROR:", repr(e))

        condition_label.configure(
            text=f"Error: {e}"
        )
def clear_weather():
    city_entry.delete(0, "end")

    temperature_label.configure(
    text="Temperature: --",
    text_color="white"
     )
    humidity_label.configure(text="Humidity: --")
    wind_label.configure(text="Wind Speed: --")
    condition_label.configure(text="Condition: --")
    
    city_label.configure(text="Weather In: --")
    feels_label.configure(text="Feels Like: --")
    tip_label.configure(text="Tip: --")
    
    app.title("Smart Weather App")

app = ctk.CTk()
app.geometry("700x650")
app.title("Smart Weather App")

current_hour = datetime.datetime.now().hour

if 6 <= current_hour < 18:
    app.configure(fg_color="#87CEEB")  # Day Sky Blue
else:
    app.configure(fg_color="#0F172A")  # Night Dark Blue
    

title = ctk.CTkLabel(
    app,
    text="SMART WEATHER APP",
    font=("Arial", 24, "bold")
)
title.pack(pady=20)

subtitle = ctk.CTkLabel(
    app,
    text="Get real-time weather information",
    text_color="gray"
)
subtitle.pack(pady=5)

time_label = ctk.CTkLabel(
    app,
    text=datetime.datetime.now().strftime("%d %B %Y | %I:%M %p"),
    text_color="gray"
)
time_label.pack(pady=5)

city_frame = ctk.CTkFrame(app, fg_color="transparent")
city_frame.pack(pady=20)

ctk.CTkLabel(
    city_frame,
    text="City",
    width=100
).pack(side="left")

city_entry = ctk.CTkEntry(
    city_frame,
    width=250
)
city_entry.pack(side="left")

button_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)
button_frame.pack(pady=15)

get_weather_button = ctk.CTkButton(
    button_frame,
    text="Get Weather",
    command=get_weather
)
get_weather_button.pack(side="left", padx=5)

clear_button = ctk.CTkButton(
    button_frame,
    text="Reset",
    command=clear_weather
)
clear_button.pack(side="left", padx=5)

temperature_label = ctk.CTkLabel(
    app,
    text="Temperature: --",
    font=("Arial", 18, "bold")
)
temperature_label.pack(pady=5)

humidity_label = ctk.CTkLabel(
    app,
    text="Humidity: --",
    font=("Arial", 18, "bold")
)
humidity_label.pack(pady=5)

wind_label = ctk.CTkLabel(
    app,
    text="Wind Speed: --",
    font=("Arial", 18, "bold")
)
wind_label.pack(pady=5)

condition_label = ctk.CTkLabel(
    app,
    text="Condition: --",
    font=("Arial", 18, "bold")
)
condition_label.pack(pady=5)

city_label = ctk.CTkLabel(
    app,
    text="Weather In: --",
    font=("Arial", 18, "bold")
)
city_label.pack(pady=5)

feels_label = ctk.CTkLabel(
    app,
    text="Feels Like: --",
    font=("Arial", 18, "bold")
)
feels_label.pack(pady=5)

tip_label = ctk.CTkLabel(
    app,
    text="Tip: --",
    wraplength=500,
    font=("Arial", 16)
)
tip_label.pack(pady=10)

last_search_label = ctk.CTkLabel(
    app,
    text="Last Search: --",
    text_color="gray"
)
last_search_label.pack(pady=5)


app.mainloop()
