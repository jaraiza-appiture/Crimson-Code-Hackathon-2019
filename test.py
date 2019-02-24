import RPi.GPIO as GPIO
import pigpio
import time

pi = pigpio.pi()


pi.set_servo_pulsewidth(13, 1400)

for i in range(1300, 1400, 10):
    print ("PW = ", i)
    pi.set_servo_pulsewidth(13, i)
    time.sleep(2)


