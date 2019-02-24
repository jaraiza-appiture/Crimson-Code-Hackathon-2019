import pigpio
import time
import sys

pi = pigpio.pi()

# PWM 1/4 on
pi.set_PWM_dutycycle(18, 1)
pi.set_PWM_dutycycle(13, 1)


try:
    while True:
        direction = input('enter direction:')
        # sys.argv[1]
        # distance_x = sys.argv[2]
        # distance_y = sys.argv[3]

        if direction == "f":
            pi.set_servo_pulsewidth(18, 1520)
            pi.set_servo_pulsewidth(13, 1355)
        elif direction == "l":
            pi.set_servo_pulsewidth(18, 1475)
            pi.set_servo_pulsewidth(13, 1355)
        elif direction == "r":
            pi.set_servo_pulsewidth(18, 1500)
            pi.set_servo_pulsewidth(13, 1370)
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
