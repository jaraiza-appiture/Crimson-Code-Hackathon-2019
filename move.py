import wiringpi2 as wiringpi

wiringpi.piBoardRev()

# OR, using P1 header pin numbers
wiringpi.wiringPiSetupPhys()
wiringpi.pinMode(12, 2)  # pwm only works on P1 header pin 12
wiringpi.pwmWrite(12, 0)  # duty cycle between 0 and 1024. 0 = off, 1024 = fully on
