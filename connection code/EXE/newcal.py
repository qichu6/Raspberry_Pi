import gdata.service
import gdata.calendar
import gdata.calendar.service
import atom
import atom.service
import time
import getopt
import sys
import os
import string
import xe
from feed.date.rfc3339 import tf_from_timestamp
from datetime import datetime #for the time on the rpi end
from apscheduler.scheduler import Scheduler #use the apsheduler==2.1.2 version

import RPi.GPIO as GPIO

from subprocess import call
from sys import exit
from sys import argv

from time import sleep
from lcdnew import LCD
from beep import Beep
from motion import Motion
import logging # add for the problem that no handerls could be found for logger "apscheduler.scheduler"
#logging.basicConfig()       
#def setup():
#   calendar_service = gdata.calendar.service.CalendarService()
#   calendar_service.email = 'ellenzi166@gmail.com'
#   calendar_service.password = '365elY##'
#   calendar_service.source = 'Google-Calendar_Python_Sample-1.0'
#   calendar_service.ProgrammaticLogin()
#   scheduler = Scheduler(standalone=True)
#   scheduler.add_interval_job(callable_func,seconds=8)
#   scheduler.start()
calendar_service = gdata.calendar.service.CalendarService()
calendar_service.email = 'ellenzi166@gmail.com'
calendar_service.password = '365elY##'
calendar_service.source = 'Google-Calendar_Python_Sample-1.0'
calendar_service.ProgrammaticLogin()
        
def FullTextQuery(calendar_service, text_query='schedule'):
        print 'Searching for events on Calendar: \'%s\'' % ( text_query,)
        query = gdata.calendar.service.CalendarEventQuery('default', 'private', 'full', text_query)
        feed = calendar_service.CalendarQuery(query)
        for i, an_event in enumerate(feed.entry):
                for a_when in an_event.when:
                        lcd.clear()
                        lcd.message("*_* *_* *_*")
                        sleep(2)
                        lcd.clear()
                        print an_event.title.text ,"Number:",i,"Event Time:",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(tf_from_timestamp(a_when.start_time))),"Current Time:",time.strftime('%Y-%m-%d %H:%M')
                        lcd.message(an_event.title.text ,"Number:",i,"Event Time:",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(tf_from_timestamp(a_when.start_time))),"Current Time:",time.strftime('%Y-%m-%d %H:%M'))
                        sleep(2)
                        lcd.clear()
                        if time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(tf_from_timestamp(a_when.start_time))) == time.strftime('%Y-%m-%d %H:%M:%S'):
                                print "You got an alert about schedule"
                                lcd.message("You got an alert\nabout schedule-->>")
                                sleep(2)
                                lcd.clear()
                                #print "..."
                                command1 ="cd" + " " + "/home/pi/Desktop/test_2/EXE"
                                command2 ="sudo" + " " +"python" + "motion.py"
                                print command1
                                os.system(command1)
                                print command2                          
                                os.system(command2) 
                                #beepfile = random.choice(os.listdir("/home/pi/beep/")£© #chooses the beep file
                                #motionfile = random.choice(os.listdir("/home/pi/motion/")) #chooses the motion file                           
                                #print "File selected:", beepfile
                                command3 ="cd" + " " + "/home/pi/Desktop/test_2/EXE"
                                command4="sudo" + " " +"python" + "beep.py" 
                                print command3
                                os.system(command3)
                                print command4                          
                                os.system(command4) 
                                command5 ="cd" + " " + "/home/pi/Desktop/test_2/EXE"
                                command6 ="sudo" + " " +"python" + "lcdnew.py"
                                print command5
                                os.system(command5)
                                print command6                          
                                os.system(command6)
                        else:
                                print "Reminder: please check your schedule" #the "start" event's start time != the system's current time
 
def callable_func():
        os.system("clear")
        print "Searching your schedule....."
        FullTextQuery(calendar_service)
        print "...End of search..."
 
def destroy():
        
        GPIO.cleanup()         # now you can release resources

if __name__ == '__main__':     # Program start from here
        print 'Welcome, we are happy to see you here. Please check the schedule'
        global lcd
        lcd = LCD()
        #lcd.noBlink()
        lcd.clear()
        sleep(1)
        lcd.message("Welcome to your\nschedule board.")
        sleep(3)
        lcd.clear()
        #logging.basicConfig() #YAO BU REMOVE IT????
        #setup()
        try:
                scheduler = Scheduler(standalone=True)
                scheduler.add_interval_job(callable_func,seconds=8)
                scheduler.start()

        #try:
                #FullTextQuery()
        except KeyboardInterrupt: # You can use Ctrl + C to end this program
                destroy()



