import math, time , os, signal, sys, json, requests
import scrollphathd as sphd
from scrollphathd.fonts import font5x5 as f55

#!/usr/bin/env python3
import requests, json
from bs4 import BeautifulSoup


url = 'https://extreme-ip-lookup.com/json/'
r = requests.get(url)
data = json.loads(r.content.decode())
location = (data['region'][0]+data['region'][-1]+"/" + data['city']).lower()

def weather(): 
    w = requests.get('https://www.wunderground.com/weather/us/%s' % (location))
    weatherData = BeautifulSoup(w.content, 'html.parser')
    temp = weatherData.find(class_="wu-value wu-value-to").text.strip()
    looks = weatherData.find(class_="condition-icon").get_text()
    sphd.clear()
    sphd.write_string(temp + " F", x = 0, y = 0, font = f55, brightness = .3)
    sphd.show()
    time.sleep(2)
    sphd.clear()
    sphd.write_string(looks, x = 0, y=0, font = f55, brightness = .3)
    sphd.show()
    time.sleep(2)
    sphd.clear()

def blast():
    for i in range(3): 
        sphd.clear()
        sphd.show()
        time.sleep(.5)
        sphd.fill(brightness = .4 , x = 0, y=0, width = 17, height = 7)
        sphd.show()
        time.sleep(.5)
   
def timeclock():
    timenow = time.strftime("%I:%M")
    timenow = timenow.replace('0',"O")
    sphd.clear()
    sphd.write_string(timenow, x = 0, y = 0, font = f55, brightness = .3)
    if int(time.time()) % 2 == 0:
        sphd.clear_rect(8,0,1,5)
    sphd.show()
    time.sleep(0.1)

def runclock():
    if time.strftime("%M%S") == "0000":
        blast()
    elif int(time.strftime("%S")) % 7 == 0:
        weather()
    else:
        timeclock()
        
def handler(signum, frame):
    sys.exit(1)
   
while True:
    pid = os.getpid()
    signal.signal(signal.SIGTERM, handler)
    try:
        runclock()
    except KeyboardInterrupt:
        print("Closing Phat Clock")
        sphd.clear()
        sphd.show()
        exit()
        
    

