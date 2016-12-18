#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers
pinList = [9, 10, 22, 27, 17, 4, 3, 2]

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 1

# main loop

try:
  print "Started: cycle.py"
  for j in pinList: 
    GPIO.output(j, GPIO.LOW)
    print "  GPIO " + str(j) + " is LOW (On)"
    time.sleep(SleepTimeL)

    GPIO.output(j, GPIO.HIGH)
    print "  GPIO " + str(j) + " is HIGH (Off)"
    time.sleep(SleepTimeL);

  GPIO.cleanup()
  print "Finished: cycle.py"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "Good Bye"

  # Reset GPIO settings
  GPIO.cleanup()
