#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers
<<<<<<< HEAD
#pinList = [9, 10, 22, 27, 17, 4, 3, 2]
pinList = [6, 12, 13, 16, 19, 20, 26, 21]
=======
#pinList = [6, 12, 13, 16, 19, 20, 26, 21]
#pinList = [12, 6, 16, 13, 20, 19, 21, 26, 2, 3, 4, 14, 15, 17, 18, 27, 22, 23, 24, 10, 9, 24, 11, 8, 7, 5]
pinList = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21]
>>>>>>> origin

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    #GPIO.output(i, GPIO.LOw)

# time to sleep between operations in the main loop

SleepTimeL = 1

# main loop

try:
  print "Started: cycle.py"
  for j in pinList: 
    GPIO.output(j, GPIO.HIGH)
    print "  GPIO " + str(j) + " is HIGH (ON)"
    time.sleep(SleepTimeL);

    GPIO.output(j, GPIO.LOW)
    print "  GPIO " + str(j) + " is LOW (OFF)"
    time.sleep(SleepTimeL)

  #GPIO.cleanup()
  print "Finished: cycle.py"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "Good Bye"

  # Reset GPIO settings
  #GPIO.cleanup()
