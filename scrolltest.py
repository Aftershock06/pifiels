import math, time
import scrollphathd as sphd
from scrollphathd.fonts import font5x5 as f55

def blast():
    for i in range(3): 
        sphd.clear()
        time.sleep(.5)
        sphd.fill(brightness = .4 , x = 0, y=0, width = 17, height = 7)
        sphd.show()
        time.sleep(.5)
   
def timeclock(): 
    timenow = time.strftime("%I:%M")
    sphd.clear()
    sphd.write_string(timenow, x = 0, y = 0, font = f55, brightness = .3)
    if int(time.time()) % 2 == 0:
        sphd.clear_rect(8,0,1,5)
    sphd.show()
    time.sleep(0.1)
  
while True:
    if time.strftime("%M%S") == "1500":
        blast()
    else:
        timeclock()
    

