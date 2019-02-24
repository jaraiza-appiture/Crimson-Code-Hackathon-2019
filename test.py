import RPi.GPIO as GPIO
import pigpio
import time

pi = pigpio.pi()

pi.set_mode(12, pigpio.OUTPUT)

print("no movement")
pi.set_servo_pulsewidth(18, 0)
time.sleep(1)

print("CCW")
pi.set_servo_pulsewidth(18, 2000)
time.sleep(3)

print("CW")
pi.set_servo_pulsewidth(18, 1000)
time.sleep(3)

print("stop")
pi.set_servo_pulsewidth(18, 1500)
pi.set_PWM_dutycycle(18, 0)
time.sleep(3)


