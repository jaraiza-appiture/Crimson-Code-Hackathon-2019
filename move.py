import pigpio
import time
import sys

pi = pigpio.pi()

# PWM 1/4 on
pi.set_PWM_dutycycle(18, 64)
pi.set_PWM_dutycycle(13, 64)

#if len(sys.argv) < 2:
 #   print("ERROR: no values given")
  #  exit()

try:
    while True:
        direction = input('enter direction:')
        # sys.argv[1]
        # distance_x = sys.argv[2]
        # distance_y = sys.argv[3]

        if direction == "FORWARD":
            pi.set_servo_pulsewidth(18, 1800)
            pi.set_servo_pulsewidth(13, 1000)
        elif direction == "BACKWARD":
            pi.set_servo_pulsewidth(18, 1000)
            pi.set_servo_pulsewidth(13, 1800)
        elif direction == "LEFT":
            pi.set_servo_pulsewidth(18, 1800)
            pi.set_servo_pulsewidth(13, 1800)
        elif direction == "RIGHT":
            pi.set_servo_pulsewidth(18, 1000)
            pi.set_servo_pulsewidth(13, 1000)
        elif direction == "STOP":
            pi.set_servo_pulsewidth(18, 1500)
            pi.set_servo_pulsewidth(13, 1370)
        else:
            pi.set_servo_pulsewidth(18, 1500)
            pi.set_servo_pulsewidth(13, 1370)

except KeyboardInterrupt:
    pi.set_servo_pulsewidth(18, 1500)
    pi.set_servo_pulsewidth(13, 1370)
    pi.stop()
