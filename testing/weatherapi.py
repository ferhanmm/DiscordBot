import requests, json, os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('weatherapi_token')

x = input("Enter your Zipcode: ")

url = "http://api.weatherapi.com/v1/forecast.json?key=" + TOKEN + "&q=" + x + "&days=1&aqi=no&alerts=no"

response = requests.request("GET", url)

weather = json.loads(response.text)

print("Location: " + weather["location"]["name"] + ", " + weather['location']['region'] + " " + weather['location']['country'])
print(f"High: {weather['forecast']['forecastday'][0]['day']['maxtemp_f']} Low: {str(weather['forecast']['forecastday'][0]['day']['mintemp_f'])}")


