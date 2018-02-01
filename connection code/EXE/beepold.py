import RPi.GPIO as GPIO
import time
from time import sleep
from lcdnew import LCD

class Beep():
   def setup(self, pin = 11):
      #if not GPIO:
        #import RPi.GPIO as GPIO
        #self.GPIO = GPIO
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)        # the BOARD mode maens numbering GPIOs by physical location
        #GPIO.setmode(GPIO.BCM)         # check the GPIO mode set for LCD class, which is BCM and different from the BOARD mode that is set for Beep class
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.OUT)   # Set pin's mode is output
        GPIO.output(self.pin, GPIO.HIGH) # Set pin high(+3.3V) to turn off the ringing

   def loop(self):
        GPIO.cleanup() #since the mode for LCD has been set as BCM, if user wants to use beep
        lcd = LCD()    #user needs to cleanup the GPIO to release the resources first, 
        lcd.clear()    #then user can initialize the GPIO mode(BOARD, different from BCM) for Beep, and cleanup the GPIO before turning to use the LCD 
        lcd.message("Hi***") # or user may consider changing the BCM mode for Beep, like setting a matrix for modifying the BCM mode numbering
        sleep(2)
        for j in range(0,36): # set the total length of time for ringing
          #while True:
          #i=self.GPIO.input(8)
          #if i==0:
          GPIO.cleanup()
          self.setup()
          GPIO.output(self.pin, GPIO.LOW) #if input is 0, which represents the output of GPIO is low 
          sleep(0.2)   # set the length of time for ringing the bell
          GPIO.output(self.pin, GPIO.HIGH)
          sleep(0.2)   # set the length of time for stopping the ringing
          #elif i==1:  
          #self.GPIO.output(pin, GPIO.HIGH) 
          #time.sleep(0.1)  

   def destroy(self): #It needs to be initialized first, as the loop() function may have cleanup the resources for setting the mode for LCD
        self.setup()  #since it would have a RuntimeError: The GPIO channel has not been set up as an OUTPUT. 
        GPIO.output(self.pin, GPIO.HIGH)   # turn the beep off
        GPIO.cleanup()                     # now you may release resources

if __name__ == '__main__':     # the program starts now
        print 'You got an alert about the schedule'
        global beep, lcd
        #lcd = LCD()
        beep = Beep()
        beep.setup() #use since the mode for beep needs to be set as BOARD
        try:
                beep.loop()
        except KeyboardInterrupt: # You can use Ctrl + C to end this program
                beep.destroy()

