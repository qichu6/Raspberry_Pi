import RPi.GPIO as GPIO
import time
from time import sleep
from lcdnew import LCD

#lcdnew.path.append('/home/pi/Desktop/test_2/lcd')
#from ..lcd import lcdnew # doesn't work

class Motion:
  flag = False
  def setup(self, pin_in = 21, pin_out = 19, flag = False):
    self.flag = flag
    self.pin_in = pin_in
    self.pin_out = pin_out
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(self.pin_in,GPIO.IN) #set the output of data detected from sensor transfer to the 21 channel(GPIO 21) in the raspberry pi board
    GPIO.setup(self.pin_out,GPIO.OUT)

  def loop(self): 
    while True:
      i=GPIO.input(self.pin_in)
      if i==0:
        lcd.clear()
        sleep(1)
        lcd.message("No one is\naround.")
        sleep(1.5)
        print "There is no motion detected", i
        GPIO.output(self.pin_out,0)
        sleep(.08)
      elif i==1:
        
        flag = True
        lcd.clear()
        sleep(1)
        lcd.message("Welcome,we are\nhappy to see you.")
        sleep(2.5)
        lcd.clear()
        sleep(1)
        lcd.message("Please check\nyour schedule")
        sleep(2)
        lcd.clear()
        lcd.message("Nice to have you\nhere.")
        sleep(2)
        print "Motion detected", i
        GPIO.output(self.pin_out,1)
        sleep(.08)
        return flag
  def destroy(self):
        GPIO.output(self.pin_out, GPIO.LOW)    # turn the detection off
        GPIO.cleanup()               # now you can release resource

if __name__ == '__main__':     # Program start from here
        print 'Welcome, we are happy to see you here. Please check the schedule'
        global lcd, motion
        lcd = LCD()
        motion = Motion()
        motion.setup()
        
        try:
                motion.loop()
                
        except KeyboardInterrupt: # You can use Ctrl + C to end this program
                lcd.clear()
                motion.destroy()
