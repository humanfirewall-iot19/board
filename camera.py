#! /usr/bin/env python3
from gpiozero import Button
from time import sleep
from hashlib import sha256
from picamera import PiCamera
import requests

# get the board serial number
def getserial():
    # Extract serial from cpuinfo file
    cpuserial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo','r')
        for line in f:
            if line[0:6]=='Serial':
                cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = "ERROR000000000"
    return cpuserial

#initialize the button
button = Button(3)
#initialize the camera
camera=PiCamera()
camera.resolution = (1920, 1080)
camera.rotation=180
#we get the sha256 hash of the board's serial and enconde it in utf8
serial=sha256(getserial().encode("utf-8")).hexdigest()

#we stop the script if the response code is not 200 (ok)
while True:
    # we wait for the button to be pressed avoiding polling
    button.wait_for_press()
    #camera.start_preview()
    #sleep(5)
    camera.capture('/home/pi/{}.jpg'.format(serial))
    #camera.stop_preview()
    print("Pressed")
    #sending data to server
    response= requests.post('http://134.209.95.86:8080/uploader?id={}'.format(serial),files={'file':open('{}.jpg'.format(serial),'rb')})
    response.raise_for_status()
    sleep(5)
