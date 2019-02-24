import pigpio
import time
import sys

pi = pigpio.pi()

try:
    while True:
        direction = sys.argv[1]

        if direction == "f":
            pi.set_servo_pulsewidth(18, 1525)
            pi.set_servo_pulsewidth(13, 1350)
        elif direction == "l":
            pi.set_servo_pulsewidth(18, 1490)
            pi.set_servo_pulsewidth(13, 1365)
        elif direction == "r":
            pi.set_servo_pulsewidth(18, 1510)
            pi.set_servo_pulsewidth(13, 1380)
        elif direction == "s":
            pi.set_servo_pulsewidth(18, 1500)
            pi.set_servo_pulsewidth(13, 1370)
        else:
            pi.set_servo_pulsewidth(18, 1500)
            pi.set_servo_pulsewidth(13, 1370)

except KeyboardInterrupt:
    pi.set_servo_pulsewidth(18, 1500)
    pi.set_servo_pulsewidth(13, 1370)
    pi.stop()
