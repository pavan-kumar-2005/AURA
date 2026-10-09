import os
from dotenv import load_dotenv
load_dotenv()
import requests
API_KEY=os.getenv("WEATHER_API_KEY")
BASE_URL="https://api.openweathermap.org/data/2.5/weather"
def get_weather(city):
    params={
        "q":city,
        "appid":API_KEY,
        "units":"metric"
    }
    response=requests.get(BASE_URL,params=params)
    if response.status_code==200:
        data=response.json()
        temperature=round(data["main"]["temp"],1)
        humidity=data["main"]["humidity"]
        description=data["weather"][0]["description"]
        return f"The current temperature in {city} is {temperature}^C with {description}.The humidity is {humidity}%."
    else:
        return "Sorry, I couldn't get the weather information.Please check the city name or your internet connection and try again."