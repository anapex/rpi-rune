#!/usr/bin/env python

# This was based on the rotary encoder test program found at http://www.bobrathbone.com

import sys
import time
from rotary_class import RotaryEncoder
from subprocess import call

# Define GPIO inputs
RPIN_A = 14  # Pin 8
RPIN_B = 15  # Pin 10
RBUTTON = 4  # Pin 7
LPIN_A = 14  # Pin 8
LPIN_B = 15  # Pin 10
LBUTTON = 4  # Pin 7

# This is the event callback routine to handle events
def vol_event(event):
    if event == RotaryEncoder.CLOCKWISE:
        call(["mpc", "vol", "+2"], shell=False)
    elif event == RotaryEncoder.ANTICLOCKWISE:
        call(["mpc", "vol", "-2"], shell=False)
    elif event == RotaryEncoder.BUTTONDOWN:
        pass
    elif event == RotaryEncoder.BUTTONUP:
        print "Button up"
        call(["mpc", "toggle"], shell=False)
    return

def switch_event(event):
    if event == RotaryEncoder.CLOCKWISE:
        call(["mpc", "vol", "+2"], shell=False)
    elif event == RotaryEncoder.ANTICLOCKWISE:
        call(["mpc", "vol", "-2"], shell=False)
    elif event == RotaryEncoder.BUTTONDOWN:
        pass
    elif event == RotaryEncoder.BUTTONUP:
        print "Button up"
        call(["mpc", "toggle"], shell=False)
    return

# Define the right switch
rswitch = RotaryEncoder(RPIN_A,RPIN_B,RBUTTON,vol_event)

# Define the left switch
lswitch = RotaryEncoder(LPIN_A,LPIN_B,LBUTTON,switch_event)

while True:
    time.sleep(0.5)
