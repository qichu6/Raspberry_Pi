#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import time
import datetime

#文件夹id
parentsID="0B6r3QxS2zXtXNzRxb2NmUDF2MTg"

def upload(filename,parentsID=parentsID):
    try:
        #先把同名文件Trash掉
        file_list = drive.ListFile().GetList()
        for file1 in file_list:
            if file1['title'] == filename:
                file1.Trash()
        f = drive.CreateFile({"title":filename,"parents": [{"kind": "drive#fileLink", "id": parentsID}]})
        f.SetContentFile(filename)
        f.Upload()
        f.GetContentFile("down_file.txt")
        # print f['id']
        print "Finished upload ", filename
        return f['id']
    except:
        print "Upload failed."

#下载完trash掉google drive的
def delete(filename,parentsID=parentsID,trash=True):
    try:
        if trash:
            file_list = drive.ListFile({'q': "trashed=false"}).GetList()
            for file1 in file_list:
                if file1['title'] == filename and len(file1['parents']) > 0 and file1['parents'][0]['id'] == parentsID:
                    file1.Trash()
        else:
            file_list = drive.ListFile().GetList()
            for file1 in file_list:
                if file1['title'] == filename and len(file1['parents']) > 0 and file1['parents'][0]['id'] == parentsID:
                    file1.Delete()
        # print f['id']
        print "Finished delete", filename
    except:
        print "Delete failed"


def downloadDir(parentsID=parentsID):
    try:
        fileList=[]
        file_list = drive.ListFile({'q': "trashed=false"}).GetList()
        for file1 in file_list:
            #文件名相同，在文件夹id为parentsID的文件夹内，没有trashed，然后才下载这个文件
            if file1['parents'] != None and len(file1['parents']) > 0 and file1['parents'][0]['id'] == parentsID:
                file1.GetContentFile(file1['title'])
            #每下载一次就移到回收站
                file1.Trash()
                fileList.append(file1['title'])
        print "Finished download"
        return fileList
    except:
        print "Download failed"

# 读文件
def readFile(filename):
    with open(filename,"r") as f:
        date=f.readline().strip()
        time=f.readline().strip()
        msg=f.read()
    #返回数组
    return date,time,msg

#读到的文件内容保存到一个数组中
def readAll(fileList):
    allData=[]
    for filename in fileList:
        #把readFile一个三个元素的数组当成一个元素存入allData
        allData.append(readFile(filename))
    return allData

#把数组写入一个文件
def writeFile(filename,allData):  
    with open(filename,'w') as file:   #打开文件不用关闭的常用方法，其实是创建文件
        for dat in allData:#从集合里取元素的循环写法
            file.write("%s\t%s\t%s\n"%(dat[0],dat[1],dat[2]))

def readForReadFile(filename):
    allData=[]
    with open(filename,'r') as file:
        for line in file:
            if line.strip()=="":      
                continue
            lineSplit=line.strip().split("\t")
            allData.append([lineSplit[0],lineSplit[1],lineSplit[2]])
    return allData

''''' 
* datestr转换成secs 
* 将时间字符串转化为秒
* @param datestr; 
* @return secs; 
* 
''' 
def datestr2secs(datestr):  
    tmlist = []  
    array = datestr.split(' ')  
    array1 = array[0].split('-')  
    array2 = array[1].split(':')  
    for v in array1:  
        tmlist.append(int(v))  
    for v in array2:  
        tmlist.append(int(v))  
    tmlist.append(0)  
    tmlist.append(0)  
    tmlist.append(0)  
    if len(tmlist) != 9:  
        return 0  
    return int(time.mktime(tmlist)) 
''''' 
* 获得当前时间：time.time()返回的值是表示时间的秒数 
* 秒数转换为time类型:time.localtime(time.time())返回'time.struct_time'类型 
* time转换成datetime：datetime.datetime(*(time.localtime(time.time()))[:6])返回'datetime.datetime'类型 
* @return datetime_value; 
'''  
def get_current_datetime():  
    datetime_value = datetime.datetime(*(time.localtime(time.time()))[:6])  
    return datetime_value

#先过滤超时的部分，再排序
def combineData(allData,addData):
    comData=[]
    comData.extend(allData)
    comData.extend(addData)
    print comData
    dataDic={}
    nowTime=datestr2secs(str(get_current_datetime()))
    #时间放在字典里排序
    for i,dat in enumerate(comData):#游标生成元素
        # print dat[0]+" "+dat[1]
        msgTime=datestr2secs(dat[0]+" "+dat[1])
        if msgTime > nowTime:
            dataDic[i]=msgTime
    dataDic= sorted(dataDic.items(),key=lambda d:d[1])
    print dataDic
    newAllData=[]
    for dat in dataDic:
        newAllData.append(comData[dat[0]])
    print newAllData
    return newAllData

def main():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("credentials.json")
    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("credentials.json")
    global drive
    drive = GoogleDrive(gauth)
    # delete("document.txt")
    # fileID=upload("document.txt")
    # download("document.txt","down_file.txt")
    while True:
        fileList=downloadDir()
        print fileList
        addData=readAll(fileList)
        #print addData
        allData=readForReadFile("forRead.txt")
        #print allData
        comData=combineData(allData,addData)
        print comData
        writeFile("forRead.txt",comData)
        print("sleeping...")
        time.sleep(300)

if __name__ == '__main__':
        main()