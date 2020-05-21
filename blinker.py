import RPi.GPIO as GPIO 
from time import sleep 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW) 
while True: 
    try:
         GPIO.output(7, GPIO.HIGH) 
         sleep(0.25) 
         GPIO.output(7, GPIO.LOW) 
         sleep(0.25) 
    except KeyboardInterrupt:
        GPIO.cleanup()