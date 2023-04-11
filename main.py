
import RPi.GPIO as GPIO
import pygame
pygame.mixer.init()
pygame.mixer.music.load("welcome message.wav")
pygame.mixer.music.play()
GPIO.cleanup()


from lights_on import light, light_one
#import RPi.GPIO as GPIO

#light()
#welcome message
"""
import pygame
pygame.mixer.init()
pygame.mixer.music.load("audio_files/welcome message.wav")
pygame.mixer.music.play()
GPIO.cleanup()
"""
from threading import Thread
import time

def run1():
    import play_rfid_cards

def run2():
    import logo
    
def run_all():
	print("In main block")
	t1 = Thread(target=run1)
	threads = [t1]
	t2 = Thread(target=run2)
	threads += [t2]

	t1.start()
	t2.start()

	for tloop in threads:
		tloop.join()

	print("End of main block")
	
run_all()

