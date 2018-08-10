import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(3, GPIO.IN)
GPIO.setup(5, GPIO.IN)