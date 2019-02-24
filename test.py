import RPi.GPIO as GPIO
import pigpio
import time

pi = pigpio.pi()

pi.set_mode(12, pigpio.OUTPUT)

print("no movement")
pi.set_servo_pulsewidth(13, 0)
time.sleep(1)

print("CCW")
pi.set_servo_pulsewidth(13, 1000)

print("CW")
pi.set_servo_pulsewidth(13, 2000)

print("stop")
pi.set_servo_pulsewidth(13, 0)

