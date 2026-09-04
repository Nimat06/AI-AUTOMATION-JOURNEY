

import requests
city = input("Enter a city name: ")
result = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}")
data = result.json()


longitude = data["results"][0]["longitude"]
latitude = data["results"][0]["latitude"]

weather_result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")
weather_data = weather_result.json()

temperature = weather_data["current_weather"]["temperature"]
windspeed = weather_data["current_weather"]["windspeed"]

print(f"Current temperature : {temperature}°C")
print(f"Current windspeed: {windspeed} km/h ")




