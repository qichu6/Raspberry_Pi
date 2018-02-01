import RPi.GPIO as GPIO
import time
from time import sleep
from lcdnew import LCD

#import lcdnew
#lcdnew.path.append('/home/pi/Desktop/test_2/lcd')
#from ..lcd import lcdnew


def setup():
 GPIO.setmode(GPIO.BCM)
 GPIO.setwarnings(False)
 GPIO.setup(21,GPIO.IN) #set the output of data detected from sensor transfer to the 21 channel(GPIO 21) in the raspberry pi board
 GPIO.setup(19,GPIO.OUT)

def loop():
 
 while True:
   i=GPIO.input(21)
   if i==0:
      lcd.clear()
      sleep(1)
      lcd.message("No one is\naround.")
      sleep(1.5)
      print "There is no motion detected", i
      GPIO.output(19,0)
      time.sleep(.08)
   elif i==1:
      lcd.clear()
      sleep(1)
      lcd.message("Welcome, we are happy\nto see you here.")
      sleep(2.5)
      lcd.clear()
      sleep(1)
      lcd.message("Please check\nyour schedule")
      sleep(2)
      lcd.clear()
      lcd.message("Nice to have you\nhere.")
      sleep(2)
      print "Motion detected", i
      GPIO.output(19,1)
      time.sleep(.08)
def destroy():
        GPIO.output(19, GPIO.LOW)    # detection off
        GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
        print 'Welcome, we are happy to see you here. Please check the schedule'
        global lcd
        lcd = LCD()
        setup()
        
        try:
                loop()
        except KeyboardInterrupt: # You can use Ctrl + C to end this program
                destroy()
