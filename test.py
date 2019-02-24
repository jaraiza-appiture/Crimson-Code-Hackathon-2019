# External module imports
import RPi.GPIO as GPIO
import time

# Constant values
STOP = 95  # Duty Cycle that stops servo
PWM0 = 12
PWM1 = 33
FREQ = 100  # 100Hz
CCW = 80
CW = 85

# variables
i = 0

# setup pin number based off board numbering
GPIO.setmode(GPIO.BOARD)

# setup pin 12 & 33 to  be an output pin for PWM0 and PWM1
GPIO.setup(PWM0, GPIO.OUT)
GPIO.setup(PWM1, GPIO.OUT)

# PWM instance associated GPIO Pin 12 and 33 at 100 HZ
p0 = GPIO.PWM(PWM0, FREQ)
p1 = GPIO.PWM(PWM1, FREQ)

# start pulse at Duty cycle=i
p0.start(i)
p1.start(i)

# ********************* Main Code *****************
try:
    while True:
        print("enter direction:")
        x = input()

        if x == "left":
            p0.ChangeDutyCycle(CCW)
            p1.ChangeDutyCycle(CW)
        elif x == "right":
            p0.ChangeDutyCycle(7.5)
            p1.ChangeDutyCycle(7.5)
        elif x == "forward":
            p0.ChangeDutyCycle(CCW)
            p1.ChangeDutyCycle(CW)
        elif x == "backward":
            p0.ChangeDutyCycle(CW)
            p1.ChangeDutyCycle(CCW)
        elif x == "fix":
            p0.ChangeDutyCycle(50)
            p1.ChangeDutyCycle(50)
        else:
            p0.ChangeDutyCycle(0)
            p1.ChangeDutyCycle(0)

except KeyboardInterrupt:
    p0.stop()
    p1.stop()
    GPIO.cleanup()
