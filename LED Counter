import RPi.GPIO as GPIO
import time

# --- Setup ---
GPIO.setmode(GPIO.BCM)  # use Broadcom pin numbering

# Define pins
button_next = 17      # GPIO17 for "next LED"
button_reset = 27     # GPIO27 for "reset"
led_pins = [5, 6, 13, 19, 26, 16, 20, 21]  # 8 LED pins

# Setup LEDs
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Setup buttons with pull-up resistors
GPIO.setup(button_next, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_reset, GPIO.IN, pull_up_down=GPIO.PUD_UP)

led_count = 0

try:
    while True:
        # Check NEXT button
        if GPIO.input(button_next) == GPIO.LOW:  # button pressed
            if led_count < len(led_pins):
                GPIO.output(led_pins[led_count], GPIO.HIGH)
                led_count += 1
            while GPIO.input(button_next) == GPIO.LOW:
                time.sleep(0.01)  # debounce hold

        # Check RESET button
        if GPIO.input(button_reset) == GPIO.LOW:  # button pressed
            for pin in led_pins:
                GPIO.output(pin, GPIO.LOW)
            led_count = 0
            while GPIO.input(button_reset) == GPIO.LOW:
                time.sleep(0.01)  # debounce hold

        time.sleep(0.05)  # debounce delay

except KeyboardInterrupt:
    GPIO.cleanup()
