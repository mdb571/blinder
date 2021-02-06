from jit import unlock
from sensor import start_sensor
import os
from threading import Thread
import RPi.GPIO as GPIO
from gpiozero import Button
from sensor import shouldRun


print('===========LEND YOUR EYES MENU=============\n')
print('[+] Press Help Button')
    
start_sensor()
    
    
