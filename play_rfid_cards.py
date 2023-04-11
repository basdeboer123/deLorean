import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import pygame
import time



def play(id, reader):
	if id == 249970602707:
		pygame.mixer.init()
		pygame.mixer.music.load("Desktop/marty dad.m4a")
		pygame.mixer.music.play()
	elif id == 190979194201:
		pygame.mixer.init()
		pygame.mixer.music.load("Desktop/marty girlfriend.wav")
		pygame.mixer.music.play()
	elif id == 396270672148:
		pygame.mixer.init()
		pygame.mixer.music.load("Desktop/marty mom.wav")
		pygame.mixer.music.play()
	elif id == 811187935594:
		pygame.mixer.init()
		pygame.mixer.music.load("Desktop/marty to himself.m4a")
		pygame.mixer.music.play()
	elif id == 536462706551:
		pygame.mixer.init()
		pygame.mixer.music.load("Desktop/message from grandma.wav")
		pygame.mixer.music.play()
	elif id == 878581881173:
		pygame.mixer.init()
		pygame.mixer.music.load("Desktop/message from jasmin.wav")
		pygame.mixer.music.play()
	elif id == 1076131181228:
		pygame.mixer.init()
		pygame.mixer.music.load("Desktop/welcome message set up complete.wav")
		pygame.mixer.music.play()
	elif id == 329227650256:
		pygame.mixer.init()
		pygame.mixer.music.load("Desktop/locked message may 2023.wav")
		pygame.mixer.music.play()
	elif id == 741125733527:
		pygame.mixer.init()
		pygame.mixer.music.load("Desktop/locked message may 2026.wav")
		pygame.mixer.music.play()
	elif id == 2:
		pygame.mixer.init()
		pygame.mixer.music.load("Desktop/insert personal ID.wav")
		pygame.mixer.music.play()
	elif id == 3:
		pygame.mixer.init()
		pygame.mixer.music.load("Desktop/wrong ID card.wav")
		pygame.mixer.music.play()
		
	previous_iteration = 0
	while True:
		try:
			id, text = reader.read_no_block()
			if previous_iteration == id:
				pygame.mixer.music.stop()
				break
			previous_iteration = id
		finally:
			pass
			
           

def audio_rfid(last_id, reader):
    while True:
        try:
            id, text = reader.read_no_block()
            print(id)
            if id and id != last_id:
                last_id = id
                #check inserted key card
                
                from ldr import ldr_main
                
                
                y = ldr_main()
                print("test")
                print("y output:", y)
                GPIO.cleanup()
                if y == True:
                    play(id, reader)
                    GPIO.cleanup()
                   
                    
                elif y == 2:
                    play(2, reader)
                elif y == 3:
                    play(3, reader)
                    pass
                    
            elif not id and last_id:
                last_id = None
        finally:
            pass
            
reader = SimpleMFRC522()
last_id = None
audio_rfid(last_id, reader)
