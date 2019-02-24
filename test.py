import RPi.GPIO as GPIO
import pigpio
import time

pi = pigpio.pi()

print("still")
pi.set_servo_pulsewidth(18, 1500)
pi.set_servo_pulsewidth(13, 1370)
time.sleep(2)

print("Left")
pi.set_servo_pulsewidth(18, 1500)
pi.set_servo_pulsewidth(13, 1000)
time.sleep(2)

print("right")
pi.set_servo_pulsewidth(18, 1500)
pi.set_servo_pulsewidth(13, 1800)
time.sleep(2)

print("still")
pi.set_servo_pulsewidth(18, 1500)
pi.set_servo_pulsewidth(13, 1370)
time.sleep(2)
