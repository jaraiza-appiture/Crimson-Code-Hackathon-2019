import pigpio
import time
import sys

pi = pigpio.pi()
pi.set_mode(23, pigpio.OUTPUT)
# PWM 1/4 on
pi.set_PWM_dutycycle(18, 1)
pi.set_PWM_dutycycle(13, 1)


try:
    while True:
        pi.set_mode(32, pigpio.LOW) # turn off LED
        direction = input('enter direction:')
        # sys.argv[1]
        # distance_x = sys.argv[2]
        # distance_y = sys.argv[3]

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
            pi.set_mode(32, pigpio.HIGH) # turn on LED
            pi.set_servo_pulsewidth(18, 1500)
            pi.set_servo_pulsewidth(13, 1370)
        else:
            pi.set_servo_pulsewidth(18, 1500)
            pi.set_servo_pulsewidth(13, 1370)

except KeyboardInterrupt:
    pi.set_servo_pulsewidth(18, 1500)
    pi.set_servo_pulsewidth(13, 1370)
    pi.stop()
