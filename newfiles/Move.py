import pigpio
import time
import sys


class movepi():
    def __init__(self):
        self.pi = pigpio.pi()
    def left(self):
        self.pi.set_servo_pulsewidth(18, 1500)
        self.pi.set_servo_pulsewidth(13, 1367)
    def right(self):
        self.pi.set_servo_pulsewidth(18, 1505)
        self.pi.set_servo_pulsewidth(13, 1370)
    def forward(self):
        self.pi.set_servo_pulsewidth(18, 1520)
        self.pi.set_servo_pulsewidth(13, 1355)
    def stop(self):
        self.pi.set_servo_pulsewidth(18, 1500)
        self.pi.set_servo_pulsewidth(13, 1370)
    def disconnect(self):
        self.pi.set_servo_pulsewidth(18, 1500)
        self.pi.set_servo_pulsewidth(13, 1370)
        self.pi.stop()
