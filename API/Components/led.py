import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)

def led(pulselength):
  print("LED on")
  GPIO.output(4,GPIO.HIGH)

  time.sleep(pulselength)

  print("LED off")
  GPIO.output(4,GPIO.LOW)

if __name__ == '__main__':
  try:
    while True:
      led(0.5)
      time.sleep(5)

  except keyboardInterrupt:
    GPIO.output(4,GPIO.LOW)
    print("Measurement stopped by User")
    GPIO.cleanup()
