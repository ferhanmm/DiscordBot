# Xbox clips grabber program
import requests
import os
import json
import time
from dateutil.parser import parse
import datetime
import pytz
import urllib.request
import calendar

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
        print("Epoch: " + dateRecordedCST.strftime('%s'))
        print("Clip ID: " + c['clipId'])
        print("URL: " + c['gameMediaContentLocators'][0]['Uri'])
        print("Directory:" + w_dir ,"\n")
        if c['clipId'] == "d32ee380-cc65-434c-a780-fe92853631cb" or c['clipId'] == "993f04f0-ac89-45bb-8218-de764e3e28d3":
          gamerFolder = w_dir+"/clips/"+c['authorInfo']['modernGamertag']
          if not os.path.exists(gamerFolder):
            os.makedirs(gamerFolder)
          gameFolder = w_dir+"/clips/"+c['authorInfo']['modernGamertag']+"/"+c['contentTitle']
          if not os.path.exists(gameFolder):
            os.makedirs(gameFolder)
          fileName = w_dir+"/clips/"+c['authorInfo']['modernGamertag']+"/"+c['contentTitle']+"/"+c['clipId']+".mp4"
          print("Filename: "+fileName)
          if not os.path.exists(fileName):
            urllib.request.urlretrieve(c['gameMediaContentLocators'][0]['Uri'], fileName)
            #os.utime(fileName, (calendar.timegm(dateRecordedCST.timetuple()), calendar.timegm(dateRecordedCST.timetuple())))
            os.utime(fileName, (int(dateRecordedCST.strftime('%s')),int(dateRecordedCST.strftime('%s'))))

      time.sleep(15)
    # for c in clipsJSON:
    #   print(c)

#print(friendsList.text)
