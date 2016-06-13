#!/bin/python2


# Import the modules to send commands to the system and access GPIO pins

from subprocess import call
import signal
import RPi.GPIO as gpio

# Define a function to keep script running
def loop():
    while True:
        signal.pause()

# Define a function to run when an interrupt is called
def shutdown(pin):
    call(["shutdown", "-h", "now"], shell=False)

gpio.setmode(gpio.BOARD) # Set pin numbering to board numbering
gpio.setup(36, gpio.IN, pull_up_down = gpio.PUD_UP) # Set up pin 36 as an input
gpio.add_event_detect(36, gpio.RISING, callback=shutdown, bouncetime=2000) # Set up an interrupt to look for button presses

loop() # Run the loop function to keep script running
