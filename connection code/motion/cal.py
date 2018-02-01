import atom.service
import gdata.service
import gdata.calendar
import gdata.calendar.service
import atom
import time
import getopt
import sys
import os
import string
import xe
from feed.date.rfc3339 import tf_from_timestamp
from datetime import datetime #for the time on the rpi end
from apscheduler.scheduler import Scheduler 

import RPi.GPIO as GPIO

from subprocess import call
from sys import exit
from sys import argv

from time import sleep
import lcdnew
import beep
import motion

calendar_service = gdata.calendar.service.CalendarService()
calendar_service.email = 'yao6@gwu.edu'
calendar_service.password = 'Y495286z*'
calendar_service.source = 'Google-Calendar_Python_Sample-1.0'
calendar_service.ProgrammaticLogin()
 
def FullTextQuery(calendar_service, text_query='wake'):
	print 'Full text query for events on Primary Calendar: \'%s\'' % ( text_query,)
	query = gdata.calendar.service.CalendarEventQuery('default', 'private', 'full', text_query)
	feed = calendar_service.CalendarQuery(query)
	for i, an_event in enumerate(feed.entry):
		for a_when in an_event.when:
			print "---"
			print an_event.title.text ,"Number:",i,"Event Time:",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(tf_from_timestamp(a_when.start_time))),"Current Time:",time.strftime('%Y-%m-%d %H:%M')
 
			if time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(tf_from_timestamp(a_when.start_time))) == time.strftime('%Y-%m-%d %H:%M:%S'):
				print "You got an alert about schedulle"
				print "..."
                                command1 ="cd" + " " + "/home/pi/Desktop/test_2/"
                                command2 ="sudo" + " " +"python" + "motion.py"
                                print command1
				os.system(command1)
                                print command2				
                                os.system(command2) 
				#beepfile = random.choice(os.listdir("/home/pi/beep/")£© #chooses the .beep file
#motionfile = random.choice(os.listdir("/home/pi/motion/")) #chooses the .motion file				
print "File Selected:", beepfile
				command3 ="cd" + " " + "/home/pi/Desktop/test_2/"
                                command4="sudo" + " " +"python" + "beep.py" 
				print command3
				os.system(command3)
                                print command4				
                                os.system(command4) 
                                command5 ="cd" + " " + "/home/pi/Desktop/test_2/"
                                command6 ="sudo" + " " +"python" + "lcdnew.py"
                                print command5
				os.system(command5)
                                print command6				
                                os.system(command6)
			else:
				print "Reminder: please check your schedule" #the "start" event's start time != the system's current time
 
def callable_func():
	os.system("clear")
	print "Begin....."
	FullTextQuery(calendar_service)
	print "....End...."
 
scheduler = Scheduler(standalone=True)
scheduler.add_interval_job(callable_func,seconds=8)
scheduler.start()

