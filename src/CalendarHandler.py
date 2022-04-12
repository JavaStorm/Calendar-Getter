import requests
import json
import datetime

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
creds = None
key = ""
service = None


def get():
    now = datetime.datetime.now()
    then = now + (datetime.timedelta(days=7) - datetime.timedelta(minutes=3))
    now = now.isoformat() + 'Z'
    then = then.isoformat() + 'Z'
    singleEvents = True
    orderBy = "startTime"
    link = ""
    response = requests.get(link, params={"key": key, 'timeMin': now, "timeMax": then, 'orderBy': orderBy, 'singleEvents': singleEvents})
    return json.load(response.text)

def makeList():
    pass
