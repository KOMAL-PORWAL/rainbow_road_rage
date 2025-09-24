import RPi.GPIO as GPIO
import time

# Use BCM numbering
GPIO.setmode(GPIO.BCM)

# List of LED GPIO pins
led_pins = [10, 12, 16, 18, 22, 24, 26, 28]

# Setup all pins as outputs
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

try:
    while True:
        for pin in led_pins:
            GPIO.output(pin, GPIO.HIGH)   # turn on LED
            time.sleep(1)                 # keep it on for 1 second
            GPIO.output(pin, GPIO.LOW)    # turn off LED
            time.sleep(0.5)               # wait 0.5 seconds before next LED

except KeyboardInterrupt:
    GPIO.cleanup()
