import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUTPUT)
GPIO.setup(5, GPIO.OUTPUT)

GPIO.output(3, GPIO.HIGH)
GPIO.output(5, GPIO.LOW)