#!/usr/bin/env python

import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

redPin   = 15
greenPin = 13
bluePin  = 11

def lightsCycle():
    GPIO.output(redPin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(redPin, GPIO.LOW)


    GPIO.output(greenPin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(greenPin, GPIO.LOW)

    GPIO.output(bluePin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(bluePin, GPIO.LOW)

def button_callback(channel):
    print("Button was pushed!")
    lightsCycle()
    time.sleep(5)

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up

