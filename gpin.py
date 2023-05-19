import time
import datetime
from datetime import datetime
import RPi.GPIO as GPIO

import gpiozero
from gpiozero import LED
from time import sleep

Sensor: int = 7
Led: int = 16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Sensor, GPIO.IN)
GPIO.setup(Led, GPIO.OUT)

GPIO.output(Led, 0)

time.sleep(1)
print("ready to get movement")

try:
    while True:
        now = datetime.now()
        i=GPIO.input(Sensor)
        if i==0:
            GPIO.output(Led, GPIO.LOW)  #Turn off LED
            time.sleep(0.1)
        elif i==1:
            print("Movement detected, Led is on - ", now)
            GPIO.output(Led, GPIO.HIGH)  #Turn on LED
            time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("bye")
    