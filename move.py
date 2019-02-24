import pigpio
import time
import sys


class movepi():
    def __init__(self):
        self.pi = pigpio.pi()
    def left(self):
        self.pi.set_servo_pulsewidth(18, 1490)
        self.pi.set_servo_pulsewidth(13, 1365)
    def right(self):
        self.pi.set_servo_pulsewidth(18, 1510)
        self.pi.set_servo_pulsewidth(13, 1380)
    def forward(self):
        self.pi.set_servo_pulsewidth(18, 1525)
        self.pi.set_servo_pulsewidth(13, 1350)
    def stop(self):
        self.pi.set_servo_pulsewidth(18, 1500)
        self.pi.set_servo_pulsewidth(13, 1370)
    def disconnect(self):
        self.pi.set_servo_pulsewidth(18, 1500)
        self.pi.set_servo_pulsewidth(13, 1370)
        self.pi.stop()