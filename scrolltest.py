import math, time
import scrollphathd as sphd
from scrollphathd.fonts import font5x5 as f55

while True:
    timenow = time.strftime("%I:%M")
    sphd.clear()
    sphd.write_string(timenow, x = 0, y = 0, font = f55, brightness = .3)
    if int(time.time()) % 2 == 0:
        sphd.clear_rect(8,0,1,5)
    sphd.show()
    time.sleep(0.1)
    

