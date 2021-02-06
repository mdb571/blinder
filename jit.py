import os
import time
from twilio.rest import Client
from twilio import twiml

phone = ['']

def unlock():
    print("Unlocking Phone")
    os.system("adb shell input keyevent 26")
    os.system("adb shell input touchscreen swipe 930 880 930 380")
    os.system("adb shell input tap 588 1462")
    os.system("adb shell input tap 262 1450")
    os.system("adb shell input tap 874 1928")
    os.system("adb shell input tap 556 1687")

def jitsi():
    os.system("adb shell am start -a android.intent.action.VIEW -d file:///mnt/sdcard/DP/Help.mp3 -t audio/mp3")
    time.sleep(5)
    print('Help Event Trigerred....')
    client = Client('','')
    url='https://meet.jit.si/projectblind'
    for number in phone:
            
        message = client.messages \
                   .create(
                       body='\nHey there Fancy wants some help in doing something.Join using the link to help him out\n {}'.format(url),
                       from_='', #use your twilio no here
                        to=number, #use your verified phone no. here
                        )
    print("message sent")
    time.sleep(1)
    os.system("adb shell monkey -p org.jitsi.meet -c android.intent.category.LAUNCHER 1")
    time.sleep(5)
    os.system("adb shell input tap 349 736")
    print("Meeting Started")
    time.sleep(2)
    os.system("adb shell input tap 737 2279")
    # os.system("adb shell input tap 537 2265")
    time.sleep(2)
    os.system("adb shell input tap 925 2255")
    os.system("adb shell input tap 541 1319")
    os.system("adb shell input tap 276 1484")
    time.sleep(300)
    os.system("adb shell input tap 537 2265")
