import RPi.GPIO as GPIO
import pigpio
import time

pi = pigpio.pi()

pi.set_servo_pulsewidth(18, 0)
pi.set_servo_pulsewidth(13, 0)
time.sleep(5)

pi.set_servo_pulsewidth(18, 1500)  # GPIO18 (PWM0) and 1.5ms
pi.set_servo_pulsewidth(13, 1500)  # GPIO13 (PWM1) and 1.5ms

time.sleep(1)
pi.set_servo_pulsewidth(18, 1000)
pi.set_servo_pulsewidth(13, 1000)
time.sleep(1)

pi.set_servo_pulsewidth(18,1500)
pi.set_servo_pulsewidth(13,1500)
time.sleep(1)

pi.set_servo_pulsewidth(18, 1500)
pi.set_servo_pulsewidth(13, 2000)
time.sleep(1)

pi.set_servo_pulsewidth(18, 0)
pi.set_servo_pulsewidth(13, 0)
time.sleep(5)

pi.stop()
