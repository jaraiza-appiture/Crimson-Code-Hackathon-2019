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
p = GPIO.PWM(12, 50)

# Calculate duty cycle
dc = 1.5 / 20


# ********************* Main Code *****************
try:
    while True:
        p.start(0)
        p.ChangeDutyCycle(7.5)  # turn towards 90 degree
        time.sleep(1)  # sleep 1 second
        p.ChangeDutyCycle(2.5)  # turn towards 0 degree
        time.sleep(1)  # sleep 1 second
        p.ChangeDutyCycle(12.5)  # turn towards 180 degree
        time.sleep(1)  # sleep 1 second
        p.ChangeDutyCycle(0)  # no Pulse to servos
        time.sleep(1)
        p.stop()
        time.sleep(2)

except KeyboardInterrupt:
    print("ctr-c pressed\n")
    p.ChangeDutyCycle(0)
    p.stop()
    GPIO.cleanup()

