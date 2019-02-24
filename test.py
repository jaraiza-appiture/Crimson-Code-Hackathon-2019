import RPi.GPIO as GPIO
import pigpio
import time

pi = pigpio.pi()


pi.set_servo_pulsewidth(13, 1400)
pi.set_servo_pulsewidth(18, 1500)
time.sleep(30)


