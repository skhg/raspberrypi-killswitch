#!/usr/bin/env python

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

redPin   = 11
greenPin = 13
bluePin  = 15

def button_callback(channel):
    print("Button was pushed!")

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(redPin, GPIO.OUT)
GPIO.output(redPin, GPIO.HIGH)

GPIO.setup(greenPin, GPIO.OUT)
GPIO.output(greenPin, GPIO.HIGH)

GPIO.setup(bluePin, GPIO.OUT)
GPIO.output(bluePin, GPIO.HIGH)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up