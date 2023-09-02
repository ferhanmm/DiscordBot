import requests, json, os
from dotenv import load_dotenv

#Load the weatherapi token from the .env file
load_dotenv()
TOKEN = os.getenv('weatherapi_token')

#Request the zipcode from the user
x = input("Enter your Zipcode: ")

#Create the url for the request using the token and zipcode
url = "http://api.weatherapi.com/v1/forecast.json?key=" + TOKEN + "&q=" + x + "&days=1&aqi=no&alerts=no"

#Make the request and load the response into a json object
response = requests.request("GET", url)
weather = json.loads(response.text)

#Print the weather data
print("Location: " + weather["location"]["name"] + ", " + weather['location']['region'] + " " + weather['location']['country'])
print(f"High: {weather['forecast']['forecastday'][0]['day']['maxtemp_f']} Low: {str(weather['forecast']['forecastday'][0]['day']['mintemp_f'])}")


