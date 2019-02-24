import RPi.GPIO as GPIO
import pigpio
import time

pi = pigpio.pi()

pi.set_servo_pulsewidth(13, 0)
time.sleep(1)

pi.set_servo_pulsewidth(13, 1000)
pi.set_servo_pulsewidth(12, 2000)

pi.stop()
