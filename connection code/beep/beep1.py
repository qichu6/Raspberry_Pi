#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
from time import sleep

BeepPin = 11    # pin11

def setup():
        GPIO.setmode(GPIO.BOARD)        # Numbers GPIOs by physical location
        GPIO.setup(BeepPin, GPIO.OUT)   # Set BeepPin's mode is output
        GPIO.output(BeepPin, GPIO.HIGH) # Set BeepPin high(+3.3V) to off beep

def loop():
    for j in range(0,36): # set the total length of time for beeping
        #while True:
        #i=GPIO.input(8)
    #if i==0:   
        GPIO.output(BeepPin, GPIO.LOW) #if input is 0, which represents the output of GPIO is low 
        time.sleep(0.2)   # set the length of time for ringing the bell
        GPIO.output(BeepPin, GPIO.HIGH)
        time.sleep(0.2)   # set the length of time for stopping the bell
    #elif i==1:  
        #GPIO.output(BeepPin, GPIO.HIGH) 
                #time.sleep(0.1)  

def destroy():
        GPIO.output(BeepPin, GPIO.HIGH)    # beep off
        GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
        print 'You got an alert about the schedule'
        setup()
        try:
                loop()
        except KeyboardInterrupt: # You can use Ctrl + C to end this program
                destroy()

