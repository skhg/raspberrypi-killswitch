#!/usr/bin/env python

import os
import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

RED_PIN   = 15
GREEN_PIN = 13
BLUE_PIN  = 11

INPUT_PIN = 10

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

def lights_off():
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(BLUE_PIN, GPIO.LOW)

def light_on(chosenLight):
    GPIO.output(chosenLight, GPIO.HIGH)

def lights_cycle():
    lights_off()
    light_on(RED_PIN)
    time.sleep(2)

    lights_off()
    light_on(GREEN_PIN)
    time.sleep(2)

    lights_off()
    light_on(BLUE_PIN)
    time.sleep(2)

    lights_off()

def on_button_pushed(channel):
    print("Killswitch pushed!")

    lights_off()
    light_on(RED_PIN)

    print("Running the kill script...")

    os.system('~/.killswitch')

    print("Kill script completed.")

    time.sleep(5)

    lights_off()
    light_on(BLUE_PIN)
    time.sleep(2)

    lights_off()

lights_cycle()

GPIO.add_event_detect(INPUT_PIN, GPIO.BOTH, callback=on_button_pushed) # Setup event on pin 10 rising edge

while(True):
    sleep(1) # run forever

GPIO.cleanup() # Clean up

