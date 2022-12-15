#!/usr/bin/python3

import requests
import json
import os
import os.path
from dotenv import load_dotenv

load_dotenv()

weatherStation = os.getenv('WEATHER_STATION')
deviceId = os.getenv('WF_DEVICE_ID')
tokenId = os.getenv('WF_TOKEN')
sendAlertRisingURL = "blah"
sendAlertFallingURL = "blah"
pressureHist = "pressureHist.dat"
deviceUrl = "https://swd.weatherflow.com/swd/rest/observations/device/{}?token={}".format(deviceId, tokenId)
sharpToolsUrl = "https://trigger.sharptools.io/rule/99BTs1ZmbdF40PQHxNYk/key/2f49cde4-59c9-4a45-a9de-e5468533deed/?trend="
#Read the file
if os.path.isfile(pressureHist):
    with open(aFile, "r") as tempFile:
        Press = [line.rstrip('\n') for line in tempFile]
else: 
    Press = []

#Get the json from the weather station
d = requests.get(deviceUrl)
dData = d.json()
baroTrend = dData['summary']['pressure_trend']
print(baroTrend)

if "rising" in baroTrend:
    param = "rising"
elif "falling" in baroTrend:
    param = "falling"
else:
    param = "steady"

sharpToolsUrl = sharpToolsUrl + param 
print(sharpToolsUrl)
r = requests.post(sharpToolsUrl)
print(r)
