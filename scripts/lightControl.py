#!/usr/bin/env python

import sys
import RPi.GPIO as GPIO

# The PIN Numbers - Not the GPIO numbers. See central numbers on https://www.electronicwings.com/raspberry-pi/raspberry-pi-gpio-access
RED_PIN = 15
GREEN_PIN = 13
BLUE_PIN = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

def printHelpAndExit(exitCode):
    print("Supply a single parameter for colour name [RED, GREEN, BLUE, WHITE] or OFF.")
    exit(exitCode)

if(len(sys.argv) < 2):
    printHelpAndExit(1)

def lightsOff():
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(BLUE_PIN, GPIO.LOW)

def lightOn(chosenLight):
    GPIO.output(chosenLight, GPIO.HIGH)


if(sys.argv[1] == "RED"):
    print("Red light ON")
    lightsOff()
    lightOn(RED_PIN)
    exit(0)

if(sys.argv[1] == "GREEN"):
    print("Green light ON")
    lightsOff()
    lightOn(GREEN_PIN)
    exit(0)

if(sys.argv[1] == "BLUE"):
    print("Blue light ON")
    lightsOff()
    lightOn(BLUE_PIN)
    exit(0)

if(sys.argv[1] == "WHITE"):
    print("White light ON")
    lightsOff()
    lightOn(BLUE_PIN)
    lightOn(RED_PIN)
    lightOn(GREEN_PIN)
    exit(0)

if(sys.argv[1] == "OFF"):
    print("Lights OFF")
    lightsOff()
    exit(0)

printHelpAndExit(2)
