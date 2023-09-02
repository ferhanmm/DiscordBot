
import requests, json, os
import pytz
from dateutil.parser import parse
from dotenv import load_dotenv

#loading the api key from .env file
load_dotenv()
thezipcodes_token = os.getenv('thezipcodes_token')

#getting zipcode from user
x = input("Enter your Zipcode: ")

#converting zipcode to latitude and longitude
response = requests.get(f'https://thezipcodes.com/api/v1/search?zipCode={x}&countryCode=US&apiKey={thezipcodes_token}')
jsonresponse = json.loads(response.text)
latitude = jsonresponse['location'][0]['latitude']
longitude = jsonresponse['location'][0]['longitude']
city = jsonresponse['location'][0]['city']
state = jsonresponse['location'][0]['state']

#displaying the location

print(f"location :{city}, {state}")
print(f"latitude,longitude :{latitude},{longitude}")

pirateweather_token = os.getenv('pirateweather_token')

pirateweather_response = requests.get(f"https://api.pirateweather.net/forecast/{pirateweather_token}/{latitude},{longitude}?&units=us")

weatherforecast = json.loads(pirateweather_response.text)

#America/Chicago
#dateRecordedDateObject = parse(dateRecorded)
#dateRecordedCST = dateRecordedDateObject.astimezone(pytz.timezone('America/Chicago'))

sunriseTime = weatherforecast['daily']['data'][0]['sunriseTime']

#displaying the weather forecast
print(f"High: {weatherforecast['daily']['data'][0]['temperatureHigh']} Low: {weatherforecast['daily']['data'][0]['temperatureLow']}")

print(f"Sun rise: {weatherforecast['daily']['data'][0]['sunriseTime']} Sun set: {weatherforecast['daily']['data'][0]['sunsetTime']}")

print(weatherforecast['daily']['data'][0])

