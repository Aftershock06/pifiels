import math, time , os, signal, sys
import scrollphathd as sphd
from scrollphathd.fonts import font5x5 as f55

#!/usr/bin/env python3

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
    else:
        timeclock()

def handler(signum, frame):
    print 'Shutting down...'
    sys.exit(1)
   
while True:
    os = os.getpid()
    signal.signal(signal.SIGTERM, handler)
    try:
        runclock()
    except KeyboardInterrupt:
        print("Closing Phat Clock")
        sphd.clear()
        sphd.show()
        exit()
        
    

