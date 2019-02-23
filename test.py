# External module imports
import RPi.GPIO as GPIO
import time

# ********** initiate System *****************
# The following program will control the servo making it move
# to its neutral position (90 degrees), wait 1 second and then move to its 0 degrees,
# wait 1 second and finally move to its 180 degrees.

# setup pin number based off board numbering
GPIO.setmode(GPIO.BOARD)

# setup pin 12 to be an output pin for PWM
GPIO.setup(12, GPIO.OUT)

# PWM instance associated GPIO Pin 12 at 50Hz
p = GPIO.PWM(12, 100)

p.start(0)

i = 0

# ********************* Main Code *****************
try:
    while True:
        for i in range(0, 101, 5):
            print("DC = %d", i)
            p.ChangeDutyCycle(i)
            time.sleep(2)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()

