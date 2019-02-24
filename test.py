import RPi.GPIO as GPIO
import pigpio
import time

pi = pigpio.pi()

pi.set_mode(12, pigpio.OUTPUT)

pi.set_servo_pulsewidth(18, 2000)
time.sleep(30)


