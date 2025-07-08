import requests
from datetime import datetime

# Replace this with your actual API key from OpenWeatherMap
api_key = "Enter_Your_API_Key_Here"

# Ask the user for a city name
location = input("\nEnter the city name: ")

# Construct the API URL
complete_api_link = (
    f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
)

# Send request to OpenWeatherMap API
response = requests.get(complete_api_link)
api_data = response.json()

try:
    # Extract weather data
    temp_kelvin = api_data["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15  # Convert Kelvin to Celsius
    weather_desc = api_data["weather"][0]["description"]
    humidity = api_data["main"]["humidity"]
    wind_speed = api_data["wind"]["speed"]
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    # Write weather data to a file
    with open("weatherinfo.txt", "w") as f:
        f.write("-------------------------------------------------------------\n")
        f.write(f"Weather Stats for - {location.upper()}  || {date_time}\n")
        f.write("-------------------------------------------------------------\n")
        f.write(f"\tCurrent temperature is : {temp_celsius:.2f} °C\n")
        f.write(f"\tCurrent weather desc   : {weather_desc}\n")
        f.write(f"\tCurrent Humidity       : {humidity} %\n")
        f.write(f"\tCurrent wind speed     : {wind_speed} km/h\n")

    # Also print to console
    print(f"\nCurrent temperature is: {temp_celsius:.2f} °C")
    print(f"Current weather desc  : {weather_desc}")
    print(f"Current Humidity      : {humidity} %")
    print(f"Current wind speed    : {wind_speed} km/h")

except KeyError:
    # Handle invalid city name or bad API key
    if api_data.get("message"):
        print("\nError:", api_data["message"].capitalize())
    else:
        print("\nSomething went wrong. Please check your API key and try again.")
