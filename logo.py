
import time
import board
import neopixel

pixel_pin = board.D21

# The number of NeoPixels
num_pixels = 30

ORDER = neopixel.GRB

pixel = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.8, auto_write=False, pixel_order=ORDER
)

    

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel[i] = (63, 138, 140)
            pixel[(i+1)%30] = (63, 138, 140)
            pixel[(i+2)%30] = (63, 138, 140)
            pixel[(i+3)%30] = (63, 138, 140)
            pixel[(i+4)%30] = (63, 138, 140)
            
            pixel[(i+5)%30] = (13, 86, 121)
            pixel[(i+6)%30] = (13, 86, 121)
            pixel[(i+7)%30] = (13, 86, 121)
            pixel[(i+8)%30] = (13, 86, 121)
            pixel[(i+9)%30] = (13, 86, 121)
            
            pixel[(i+10)%30] = (17, 17, 225)
            pixel[(i+11)%30] = (17, 17, 225)
            pixel[(i+12)%30] = (17, 17, 225)
            pixel[(i+13)%30] = (17, 17, 225)
            pixel[(i+14)%30] = (17, 17, 225)
            
            pixel[(i+15)%30] = (228, 0, 0)
            pixel[(i+16)%30] = (228, 0, 0)
            pixel[(i+17)%30] = (228, 0, 0)
            pixel[(i+18)%30] = (228, 0, 0)
            pixel[(i+19)%30] = (228, 0, 0)
            
            pixel[(i+20)%30] = (255,40,0)
            pixel[(i+21)%30] = (255,40,0)
            pixel[(i+22)%30] = (255,40,0)
            pixel[(i+23)%30] = (255,40,0)
            pixel[(i+24)%30] = (255,40,0)
            
            pixel[(i+25)%30] = (144, 94, 38)
            pixel[(i+26)%30] = (144, 94, 38)
            pixel[(i+27)%30] = (144, 94, 38)
            pixel[(i+28)%30] = (144, 94, 38)
            pixel[(i+29)%30] = (144, 94, 38)
            pixel.show()
            time.sleep(wait)
        
while True:
	 rainbow_cycle(0.1)
