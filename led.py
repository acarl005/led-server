import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 18

GPIO.setup(led, GPIO.OUT)

def light_up():
  for i in range(9):
    GPIO.output(led, 1)
    time.sleep(0.15)
    GPIO.output(led, 0)
    time.sleep(0.15)

def cleanup():
  GPIO.cleanup()


if __name__ == '__main__':
  light_up()
  cleanup()
