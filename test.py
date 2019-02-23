# External module imports
import RPi.GPIO as GPIO
import time

# Constant values
STOPVAL = 95 # Duty Cycle that stops servo
PWM0 = 12
PWM1 = 33
FREQ = 100 # 100Hz

# variables
i = 0

# setup pin number based off board numbering
GPIO.setmode(GPIO.BOARD)

# setup pin 12 to be an output pin for PWM0
GPIO.setup(PWM0, GPIO.OUT)

# PWM instance associated GPIO Pin 12 at 50Hz
p = GPIO.PWM(PWM0, FREQ)

# start pulse at Duty cycle=i
p.start(i)

# ********************* Main Code *****************
try:
    while True:
        for i in range(0, 101, 1):
            print("DC = %d", i)
            p.ChangeDutyCycle(i)
            time.sleep(1.5)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()