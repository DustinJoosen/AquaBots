import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

#ik heb de 16 pin op de gpio gebruikt. als er een andere pin gebruikt moet worden, of er zo'n grove aansluiting is voor servo, moeten we de pin veranderen.
GPIO.setup(16, GPIO.OUT)
pwm=GPIO.PWM(16, 50)

pwm.start(0)

def SetAngle(angle):

	duty = angle / 18 + 2
	
	GPIO.output(16, True)

	pwm.ChangeDutyCycle(duty)
    #deze sleep en output(false) werkt tegen jitter. nadeel is dat dat er maar 1 positie per seconde kan gegeven. ik vermoed dat dit voldoende is en het roer niet 
    # zo vaak van positie hoeft te veranderen
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


