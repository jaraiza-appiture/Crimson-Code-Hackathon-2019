import RPi.GPIO as GPIO
import pigpio
import time

pi = pigpio.pi()

pi.set_PWM_dutycycle(18, 0)
pi.set_PWM_dutycycle(13, 0)
time.sleep(2)


pi.set_PWM_dutycycle(18, 64)
pi.set_PWM_dutycycle(18, 64)
time.sleep(2)

pi.set_PWM_dutycycle(18, 0)
pi.set_PWM_dutycycle(13, 0)
time.sleep(2)

pi.stop()
GPIO.cleanup()
