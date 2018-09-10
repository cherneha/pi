import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

GPIO.setmode(GPIO.BCM)

print("set mode done")
a1 = 20
a2 = 26
GPIO.setup(a1, GPIO.OUT)
GPIO.setup(a2, GPIO.OUT)

GPIO.output(a1, GPIO.HIGH)
GPIO.output(a2, GPIO.LOW)

time.sleep(5)

GPIO.output(a1, GPIO.LOW)
GPIO.output(a2, GPIO.LOW)

GPIO.cleanup()


