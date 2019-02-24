import wiringpi2 as wiringpi

wiringpi.piBoardRev()

# OR, using P1 header pin numbers
wiringpi.wiringPiSetupPhys()
wiringpi.pinMode(12, 2)  # pwm only works on P1 header pin 12
wiringpi.pwmWrite(12, 0)  # duty cycle between 0 and 1024. 0 = off, 1024 = fully on

pause_time = 0.002          # you can change this to slow down/speed up

try:
    while True:
        for i in range(0, 1025):  # 1025 because it stops at 1024
            wiringpi.pwmWrite(18, i)
            sleep(pause_time)
        for i in range(1024, -1, -1):  # from 1024 to zero in steps of -1
            wiringpi.pwmWrite(18, i)
            sleep(pause_time)

finally:
    wiringpi.pwmWrite(18, 0)  # switch PWM output to 0
    wiringpi.pinMode(18, 0)  # GPIO18 to input