# Xbox clips grabber program
import requests
import os
import json
import time
from dateutil.parser import parse
import datetime
import pytz
import urllib.request

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('XAPI_TOKEN')
w_dir = os.getcwd()

payload={}
headers = {
  'Accept-Language': 'en-US',
  'Authorization': 'Bearer ' + TOKEN
}

#pull list of friends for WhiskeredNut
def friendsXUIDList():

  url = "https://xapi.us/api/2533274854380880/friends"

  friends = requests.request("GET", url, headers=headers, data=payload)
  friendsJSON = json.loads(friends.text)

  #for f in friendsJSON['people']:
    #print(f['xuid'])
  return friendsJSON['people'] 

for f in friendsXUIDList():
    if f['xuid'] == "2535437729137168":
      
      print(f['xuid'])
      clipsURL = "https://xapi.us/api/"+f['xuid']+"/alternative-game-clips"

      clips = requests.request("GET", clipsURL, headers=headers, data=payload)
      clipsJSON = json.loads(clips.text)


      for c in clipsJSON['items']:

        #America/Chicago
        dateRecorded = c['dateRecorded']
        dateRecordedDateObject = parse(dateRecorded)
        dateRecordedCST = dateRecordedDateObject.astimezone(pytz.timezone('America/Chicago'))

        
        print("Gamertag: " + c['authorInfo']['modernGamertag'])
        print("Game: " + c['contentTitle'])
        #print("Date Recorded: " + c['dateRecorded'])
        print("Date Recorded: " + dateRecordedCST.strftime('%m-%d-%y %I:%M:%S'))
        print("Clip ID: " + c['clipId'])
        print("URL: " + c['gameMediaContentLocators'][0]['Uri'])
        print("Directory:" + w_dir ,"\n")
        if c['clipId'] == "00358c5f-370e-4e50-8df6-9f96b30c05b2":
          #os.mkdir(w_dir+"/clips/"+c['authorInfo']['modernGamertag'])
          fileName = w_dir+"/clips/"+c['authorInfo']['modernGamertag']+"/"+c['clipId']+".mp4"
          print("Filename: "+fileName)
          urllib.request.urlretrieve(c['gameMediaContentLocators'][0]['Uri'], fileName)

      time.sleep(15)
    # for c in clipsJSON:
    #   print(c)

#print(friendsList.text)
