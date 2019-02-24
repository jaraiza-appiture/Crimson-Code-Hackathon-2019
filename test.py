import RPi.GPIO as GPIO
import pigpio
import time

pi = pigpio.pi()


pi.set_servo_pulsewidth(13, 1400)
pi.set_servo_pulsewidth(18, 1500)
time.sleep(30)


try:
    while 1:
        print("Enter direction: ")
        movement = input()

        if movement == "l":
            pi.set_servo_pulsewidth(18, )

except KeyboardInterrupt:
    pi.stop()

