#!/usr/bin/env python

import os
import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import sys

if len(sys.argv) < 2:
    print("Usage: killswitch.py /path/to/kill_script")
    exit(1)

full_kill_script_path = ""

if os.path.isfile(sys.argv[1]):
    full_kill_script_path = os.path.abspath(sys.argv[1])
    print ("Killswitch script found at " + full_kill_script_path)
else:
    print ("No script found at " + sys.argv[1])
    exit(2)

RED_PIN   = 15
GREEN_PIN = 13
BLUE_PIN  = 11

INPUT_PIN = 10

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

GPIO.setup(INPUT_PIN, GPIO.IN)

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
    if GPIO.input(channel) == GPIO.HIGH:
        print("Killswitch pushed!")

        lights_off()
        light_on(RED_PIN)

        print("Running the kill script...")

        os.system(full_kill_script_path) # User-defined executable script here which can do anything

        print("Kill script completed.")

        time.sleep(5)

        lights_off()
        light_on(BLUE_PIN)
        time.sleep(2)

        lights_off()

lights_cycle()

GPIO.add_event_detect(INPUT_PIN, GPIO.BOTH, callback=on_button_pushed) # On any kind of event for the input pin, trigger the callback

while(True):
    time.sleep(1) # Just run forever

GPIO.cleanup()

