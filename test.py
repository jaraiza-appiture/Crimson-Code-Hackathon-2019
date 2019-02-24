import RPi.GPIO as GPIO
import pigpio
import time

pi = pigpio.pi()

pi.set_servo_pulsewidth(18, 0)
pi.set_servo_pulsewidth(13, 0)
time.sleep(5)

pi.stop()
