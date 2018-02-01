#!/bin/sh
### BEGIN INIT INFO  
# Provides:          syncGoogleDrive 
# Required-Start:    
# Required-Stop:     
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start or stop the /dev/video0 
### END INIT INFO
pushd /home/pi/Desktop/test_2
#改一下文件名 logfile.txt是程序输出的数据，存在文件里
python test.py 2>&1>>logfile.txt  
popd
