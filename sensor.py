import RPi.GPIO as GPIO
import time
from datetime import datetime
import os
from gpiozero import Button
from jit import jitsi
import select
import sys

button = Button(12)

shouldRun = True
# GPIO setup
GPIO.setmode (GPIO.BCM)
GPIO.setwarnings(False)

# setup gpio for echo & trig
def start_sensor():
    echopin = [4,24,18]
    trigpin = [3,21,15]


    for j in range(3):
        GPIO.setup(trigpin[j], GPIO.OUT)
        GPIO.setup(echopin[j], GPIO.IN)
    try:
        # main loop
        while True:
           r, w, x = select.select([sys.stdin], [], [], .5)
           if r!=[]:
             jitsi()
            # get distances and assemble data line for writing
           for j in range(3):
                distance = ping(echopin[j], trigpin[j])
                if j==2 and distance<50:
                    os.system("adb shell am start -a android.intent.action.VIEW -d file:///mnt/sdcard/DP/Front.mp3 -t audio/mp3")
                elif j==0 and distance<10:
                    os.system("adb shell am start -a android.intent.action.VIEW -d file:///mnt/sdcard/DP/hack.mp3 -t audio/mp3")
                elif j==1 and distance<50:
                    os.system("adb shell am start -a android.intent.action.VIEW -d file:///mnt/sdcard/DP/Left.mp3 -t audio/mp3")

                
                print ("sensor", j+1,": ",distance,"cm")
                
     
        
    except KeyboardInterrupt:
        print("Exiting..")
        GPIO.cleanup()  
      

# Get reading from HC-SR04   
def ping(echo, trig):
    
    GPIO.output(trig, False)
    # Allow module to settle
    time.sleep(0.5)
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)
    pulse_start = time.time()

    # save StartTime
    while GPIO.input(echo) == 0:
        pulse_start = time.time()
        

    # save time of arrival
    while GPIO.input(echo) == 1:
        pulse_end = time.time()
        

    # time difference between start and arrival
    pulse_duration = pulse_end - pulse_start
    # mutiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = pulse_duration * 17150
    
    distance = round(distance, 2)
    
    return distance




