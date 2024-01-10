#Libraries
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_LED = 7


#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_LED, GPIO.OUT)

def led():
    GPIO.output(GPIO_LED, True)

    time.sleep(5)

    GPIO.output(GPIO_LED, False)



if __name__ == '__main__':
    try:
        while True:
            led()
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()



