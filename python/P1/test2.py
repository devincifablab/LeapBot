#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

GPIO.setup(16, GPIO.OUT)

p = GPIO.PWM(12, 50)

p.start(7.5)


p2 = GPIO.PWM(16, 50)

p2.start(7.5)

try:
        while True:
		p.ChangeDutyCycle(7.5)  # turn towards 90 degree
		time.sleep(1) # sleep 1 second
		p.ChangeDutyCycle(2.5)  # turn towards 0 degree
		time.sleep(1) # sleep 1 second
		p.ChangeDutyCycle(12.5) # turn towards 180 degree
                time.sleep(1) # sleep 1 second 

                p2.ChangeDutyCycle(7.5)  # turn towards 90 degree
                time.sleep(1) # sleep 1 second
                p2.ChangeDutyCycle(2.5)  # turn towards 0 degree
                time.sleep(1) # sleep 1 second
                p2.ChangeDutyCycle(12.5) # turn towards 180 degree
                time.sleep(1) # sleep 1 second


except KeyboardInterrupt:
	p.stop()
        p2.stop()
        GPIO.cleanup()
