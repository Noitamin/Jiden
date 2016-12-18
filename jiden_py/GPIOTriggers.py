#!/usr/bin/python
import logging
import RPi.GPIO as GPIO
import time
import sys
import datetime
import subprocess
import os

GPIO.setmode(GPIO.BCM)

###### DEFAULT PINOUTS ######
#06 - 12
#13 - 16
#19 - 20
#26 - 21

# init list with pin numbers
#pinList = [9, 10, 22, 27, 17, 4, 3, 2]
#pinList = [int(sys.argv[1])]
pinList = sys.argv
pinListLen = len(sys.argv)
log_dir = '/home/pi/jiden/logs/jiden.log'
print pinListLen

print pinList

# loop through pins and set mode and state to 'low'

for i in range(1, pinListLen):
    GPIO.setup(int(pinList[i]), GPIO.OUT) 
    GPIO.output(int(pinList[i]), GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 0.5
logging.basicConfig(filename='/home/pi/python.log', level=logging.DEBUG)

try:
    for j in range(1, pinListLen):
        logging.warning('before datetime')
        date_time = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S") 

        logging.warning('opening jiden.log')

        if not os.path.isfile(log_dir):
            create_log_cmd = "sudo touch " + log_dir
            create_log = subprocess.Popen(create_log_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            create_log_output = create_log.communicate()
            print create_log_output

            write_log_cmd = "echo [`date +\"%D %T\"`] Triggered GPIO " + str(pinList[j]) + " \<br /\> >> " + log_dir
            write_log = subprocess.Popen(write_log_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            write_log_output = write_log.communicate() 
            print write_log_output
    
        else:
            write_tmp_cmd = "sudo tail -n 9999 " + log_dir + " | sudo tee " + log_dir + ".tmp"
            write_tmp = subprocess.Popen(write_tmp_cmd, shell=True, stdout=subprocess.PIPE)
            write_tmp.communicate()

            rm_log_cmd = "sudo rm -rf " + log_dir
            rm_log = subprocess.Popen(rm_log_cmd, shell=True, stdout=subprocess.PIPE)
            rm_log.communicate()

            mv_log_cmd = "sudo mv -f " + log_dir + ".tmp " + log_dir
            mv_log = subprocess.Popen(mv_log_cmd, shell=True, stdout=subprocess.PIPE)
            mv_log.communicate()

            write_log_cmd = "echo [`date +\"%D %T\"`] Triggered GPIO " + str(pinList[j]) + " \<br /\> >> " + log_dir
            write_log = subprocess.Popen(write_log_cmd, shell=True, stdout=subprocess.PIPE)
            write_log.communicate()
        #with open('/home/pi/jiden/logs/jiden.log', 'a') as write_log:
            #write_log.write('[' + date_time + '] Triggered GPIO' + str(pinList[j]) + '\n <br />') 
        #write_log.write('hello world')
        #write_log.close()
        #logging.warning('closing jiden.log')

        GPIO.output(int(pinList[j]), GPIO.LOW)
        time.sleep(SleepTimeL)
	
        GPIO.output(int(pinList[j]), GPIO.HIGH)
        time.sleep(SleepTimeL)

    GPIO.cleanup()

# End program cleanly with keyboard
except KeyboardInterrupt:
    print "Good Bye"

# Reset GPIO settings
GPIO.cleanup()
