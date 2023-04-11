import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

pr1 = 7
pr2 = 13
pr3 = 3


def rc_time1(pr1):
    count = 0
    
    GPIO.setup(pr1, GPIO.OUT)
    GPIO.output(pr1, GPIO.LOW)
    time.sleep(0.01)
    GPIO.setup(pr1, GPIO.IN)
    
    while(GPIO.input(pr1) == GPIO.LOW):
        count += 1
    return count

def rc_time2(pr2):
    count = 0
    
    GPIO.setup(pr2, GPIO.OUT)
    GPIO.output(pr2, GPIO.LOW)
    time.sleep(0.01)
    GPIO.setup(pr2, GPIO.IN)
    
    while(GPIO.input(pr2) == GPIO.LOW):
        count += 1
    return count

def rc_time3(pr3):
    count = 0
    
    GPIO.setup(pr3, GPIO.OUT)
    GPIO.output(pr3, GPIO.LOW)
    time.sleep(0.01)
    GPIO.setup(pr3, GPIO.IN)
    
    while(GPIO.input(pr3) == GPIO.LOW):
        count += 1
    return count


def ldr_main():
    while True:
        threshold = 650
        one = 1
        two = 2
        three = 3
        GPIO.setmode(GPIO.BOARD)
        ldr_2 = rc_time2(pr2)
        ldr_3 = rc_time3(pr3)
        ldr_1 = rc_time1(pr1)
        print("ldr_1", ldr_1)
        print("ldr_2", ldr_2)
        print("ldr_3", ldr_3)
        if ldr_2 < threshold and ldr_3 > threshold and ldr_1 < threshold:
            print("card detected")
            return True
        elif ldr_1 < threshold and ldr_2 < threshold and ldr_3 < threshold :
            print("NO card detected")
            return two
        elif ldr_1 > threshold and ldr_2 > threshold and ldr_3 > threshold :
            print("NO card detected") #wrong way
            return two
        elif ldr_1 < threshold and ldr_2 > threshold and ldr_3 < threshold :
            print("Wrong card detected")
            return three
        

ldr_main()
