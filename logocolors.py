import time
import board
import neopixel
#pixels = neopixel.NeoPixel(board.D18, 30)

# On a Raspberry pi, use this instead, not all pins are supported
pixel_pin = board.D21

# The number of NeoPixels
num_pixels = 30

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

while True:
	
	pixels.fill((63, 138, 140)) #teal
	pixels.show()
	time.sleep(1)
	pixels.fill((13, 86, 121)) #blue
	pixels.show()
	time.sleep(1)
	pixels.fill((17, 17, 225)) # dark blue
	pixels.show()
	time.sleep(1)
	pixels.fill((228, 0, 0)) # red
	pixels.show()
	time.sleep(1)
	pixels.fill((255,40,0)) #orange
	pixels.show()
	time.sleep(1)
	pixels.fill((144, 94, 38)) #tan
	pixels.show()
	time.sleep(1)
	"""
	pixels.fill((0, 255, 120)) #teal
	pixels.show()
	time.sleep(1)
	pixels.fill((0, 128, 128)) #teal
	pixels.show()
	time.sleep(1)
	
	
	#pixels.fill((25, 59, 72)) # dark blue
	#pixels.show()
	#time.sleep(1)
"""
	

