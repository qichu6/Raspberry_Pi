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
import subprocess
from subprocess import call
from sys import exit
from sys import argv

from time import sleep
from lcdnew import LCD
from beep import Beep
from motion import Motion
import logging # add for the problem that no handerls could be found for logger "apscheduler.scheduler"
#logging.basicConfig()
import re #yinru zhengze biaodashi

calendar_service = gdata.calendar.service.CalendarService()
calendar_service.email = 'ellenzi166@gmail.com'
calendar_service.password = '365elY##'
calendar_service.source = 'Google-Calendar_Python_Sample-1.0'
calendar_service.ProgrammaticLogin()
        

def Search():
                    #lcd.clear()
                    #lcd.message("*_* *_* *_*")
                    #sleep(2)
                    #lcd.clear()
                        
                    f = open ('/home/pi/Desktop/test_2/forRead.txt','r') # r stands for opening the file as read only
                    result = list() # turn the yuanzu into list
                    data = f.readlines()        
                    for line in data:
                        line = line.strip()
                        if not len(line) or line.startswith('#'): #if the line is empty or a text for reference that starts with '#' notation
                               continue  # skip and move to next line
                        result.append(line) #save results
                    result.sort()           #the results after sorting
                    open('newSchedule.txt','w').write('%s'%'\n'.join(result)) # w stands for opening the file as writing files        
                    content = result[0]
                    #f = open ('newSchedule.txt','r')
                    #if time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(tf_from_timestamp(content.start_time))) == time.strftime('%Y-%m-%d %H:%M:%S'):
                    t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    sStr1 = t
                    sStr2 = content
                    
                    #<span style = "color:#333300;">#import the zhengze biaoda shi pipei module Py 3.0
                    #detepat = re.compile('(\d+)/(\d+)/(\d+)') # setup the date's zhengze biaodashi
                    #results = detepat.finditer(sStr1)
                    #for m in results:
                         #print (m.group())</span>

                         
                    if  True: #== content.strftime('%Y-%m-%d %H:%M:%S'):#???
                        #lcd.message("You got an alert\nabout schedule>>")
                        #sleep(2)
                        #lcd.clear()
                                
                        command1 ="cd" + " " + "/home/pi/Desktop/test_2/EXE"                       
                        print command1
                        os.system(command1)

                        command2 ="sudo" + " " +"python"+ " " + "motion.py"
                        print command2
                        
                        subprocess.Popen(command2, shell = True) # different from the os.system() command, it allows the threads run in parallel pipelines
                        if Motion.flag == True: # flag is a global variable, defined in motion.py
                           command3 = "sudo" + " " +"python"+ " " + "control.py" + "stop" # if the loop() in motion.py return flag == True (someone is around), then stop the current thread
                           print command3
                           os.system(command3) # execute the stop-the-current-thread command
                           GPIO.cleanup() # release the resources
                        
                           
                        command4="sudo" + " " +"python"+ " " + "beep.py"                         
                        print command4                          
                        #os.system(command4)
                        subprocess.Popen(command4, shell = True)
                        
                        
                        command5 ="sudo" + " " +"python"+ " " + "lcdnew.py"
                        print command5                          
                        subprocess.Popen(command5, shell = True)
                        print "Reminder: please check your schedule" #the "start" event's start time != the system's current time
 
def destroy():
        #lcd.clear()
        os.system(command3)
        GPIO.cleanup()         # now you can release resources

if __name__ == '__main__':     # Program start from here
        print 'Welcome, we are happy to see you here. Please check the schedule'
        global lcd, t
        #lcd = LCD()
        #lcd.noBlink()
        #lcd.clear()
        #sleep(1)
        #lcd.message("Welcome to your\nschedule board.")
        #sleep(3)
        #lcd.clear()
        #logging.basicConfig() #YAO BU REMOVE IT????
        #setup()
        #GPIO.cleanup() 
        beep = Beep()
        try:
                #scheduler = Scheduler(standalone=True)
                #scheduler.add_interval_job(callable_func,seconds=8)
                #scheduler.start()

        #try:
                Search()
        except KeyboardInterrupt: # You can use Ctrl + C to end this program
                beep.destroy()
                GPIO.cleanup()
                



