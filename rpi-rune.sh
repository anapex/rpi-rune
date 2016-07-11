#!/usr/bin/env python

# This was based on the rotary encoder test program found at http://www.bobrathbone.com

# Import the modules to send commands to the system and access GPIO pins

import signal
import sys
import time
import RPi.GPIO as gpio

from subprocess import call
from rotary_class import RotaryEncoder

# Define rotary GPIO inputs
RPIN_A = 24  # Pin 8
RPIN_B = 25  # Pin 10
RBUTTON = 23  # Pin 7

LPIN_A = 5  # Pin 8
LPIN_B = 6  # Pin 10
LBUTTON = 13  # Pin 7



# Define a function to keep script running
def loop():
    while True:
        signal.pause()

# Define a function to run when an interrupt is called
def shutdown(pin):
    call(["shutdown", "-h", "now"], shell=False)
    
# This is the event callback routine to handle events
def vol_event(event):
    if event == RotaryEncoder.CLOCKWISE:
        call(["mpc", "vol", "+2"], shell=False)
    elif event == RotaryEncoder.ANTICLOCKWISE:
        call(["mpc", "vol", "-2"], shell=False)
    elif event == RotaryEncoder.BUTTONDOWN:
        pass
    elif event == RotaryEncoder.BUTTONUP:
        call(["mpc", "toggle"], shell=False)
    return

def switch_event(event):
    if event == RotaryEncoder.CLOCKWISE:
        call(["mpc", "seek", "+2"], shell=False)
    elif event == RotaryEncoder.ANTICLOCKWISE:
        call(["mpc", "seek", "-2"], shell=False)
    elif event == RotaryEncoder.BUTTONDOWN:
        pass
    elif event == RotaryEncoder.BUTTONUP:
        call(["mpc", "next"], shell=False)
    return

# Define shutdown button
gpio.setmode(gpio.BOARD) # Set pin numbering to board numbering
gpio.setup(36, gpio.IN, pull_up_down = gpio.PUD_UP) # Set up pin 36 as an input
gpio.add_event_detect(36, gpio.RISING, callback=shutdown, bouncetime=2000) # Set up an interrupt to look for button presses

# Define the right switch
rswitch = RotaryEncoder(RPIN_A,RPIN_B,RBUTTON,vol_event)

# Define the left switch
lswitch = RotaryEncoder(LPIN_A,LPIN_B,LBUTTON,switch_event)

loop() # Run the loop function to keep script running