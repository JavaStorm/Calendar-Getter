import requests
import json
import datetime
import ConfigHandler

configData = ConfigHandler.loadConfig('resources/config.json')
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
creds = None
key = configData["APIkey"]
service = None


def get():
    now = datetime.datetime.now()
    then = now + (datetime.timedelta(days=7) - datetime.timedelta(minutes=3))
    now = now.isoformat() + 'Z'
    then = then.isoformat() + 'Z'
    singleEvents = True
    orderBy = "startTime"
    link = configData["calendarLink"]
    response = requests.get(link, params={"key": key, 'timeMin': now, "timeMax": then, 'orderBy': orderBy, 'singleEvents': singleEvents})
    return response.text

def makeList():
    pass
