#!/usr/bin/python
#coding=utf-8
import sys
import os
import time
import signal

Max_process = 2
log_index = 0
    

def start():
    global Max_process
    global log_index    
   
    path = os.popen('pwd').readlines()[0] # get the current path
    
    while(1):
        processInfo = os.popen('ps -ef | grep tt.py | grep -v grep').readlines() #tt.py???
        processNum = len(processInfo)
        if processNum :
            os.system('cd '+path)
            os.system('nohup python tt.py &')
            log_index = log_index + 1
            time.sleep(5)

def stopChicd():
    processInfo = os.popen("ps -ef|grep tt.py|grep -v grep|awk '{print $2}'").readlines()
    for pid in processInfo:
        os.kill(int(pid),signal.SIGKILL)
    
def stopParent():
    parentList = os.popen("ps -ef|grep control.py|grep -v grep|awk '{print $2}'").readlines()
    for pid in parentList:
        os.kill(int(pid),signal.SIGKILL)


def stopParent2(): # stop all the other threads
    index = 0
    parentList = os.popen("ps -ef|grep control.py|grep -v grep|awk '{print $2}'").readlines()
    for pid in parentList:
        index = index+1
        if index:
            os.kill(int(pid),signal.SIGKILL)
        
    
def stopAll():
    stopChicd()
    stopParent()
        
        
    
try:
    fun = sys.argv[1]
except Exception:
    fun = ''
if fun == 'start':
    start()
if fun == 'stop':
    stopAll()
if fun == 'restart':
    stopChicd()
    stopParent2()
    time.sleep(1)
    start()
