import requests

city = "lahore"

api_key = "https://api.openweathermap.org/data/2.5/weather??q={lahore}&appid={API key}"

print(requests.get(api_key).json())
