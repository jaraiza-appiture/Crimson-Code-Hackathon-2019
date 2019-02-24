import RPi.GPIO as GPIO
import pigpio
import time

pi = pigpio.pi()


pi.set_servo_pulsewidth(13, 1400)

for i in range(500, 2001, 100):
    pi.set_servo_pulsewidth(13, i)
    time.sleep(2)


