import time
import datetime
from datetime import datetime
import RPi.GPIO as GPIO
from time import sleep

Sensor: int = 7
Led: int = 16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)    #connect to RP
GPIO.setup(Sensor, GPIO.IN) #Read output pin
GPIO.setup(Led, GPIO.OUT)   #LED output pin

GPIO.output(Led, False)  #set LED to value 0 - Turn off LED

time.sleep(1)
print("ready to get movement")

def motion_detected(sensor):
    '''detection function'''
    now = datetime.now()
    print(f"Movement detected on pin sensor {sensor}, Led is on - {now}")
    GPIO.output(Led, True)
    time.sleep(0.1)
    GPIO.output(Led,False)

try:
    GPIO.add_event_detect(Sensor, GPIO.RISING, callback=motion_detected, bouncetime=1000)
    while True:
        pass
except KeyboardInterrupt:
    GPIO.cleanup()
    print("bye")