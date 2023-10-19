import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.OUT)
pwm=GPIO.PWM(16, 50)

pwm.start(0)

def SetAngle(angle):

	duty = angle / 18 + 2

	GPIO.output(16, True)

	pwm.ChangeDutyCycle(duty)

	sleep(1)

	GPIO.output(16, False)

	pwm.ChangeDutyCycle(0)
	


try:
	while True:
		SetAngle(int(input("graad: ")))

		
except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

pwm.stop()
