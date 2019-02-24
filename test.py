import RPi.GPIO as GPIO
import pigpio
import time

pi = pigpio.pi()


pi.set_servo_pulsewidth(13, 1500)
pi.set_servo_pulsewidth(18, 1400)
time.sleep(30)



