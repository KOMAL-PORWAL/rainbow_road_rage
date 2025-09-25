import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# GPIO pins
led_pins = [10, 12, 16, 18, 22, 24, 26, 28]  # LEDs connected to GPIO 2 through 9
button_increment = 17               # Button to increment counter
button_reset = 27                   # Button to reset counter

# Set up LED pins as outputs
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Set up button pins as inputs with internal pull-up resistors
GPIO.setup(button_increment, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_reset, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Counter state
counter = 0

def update_leds(count):
    for i in range(8):
        GPIO.output(led_pins[i], GPIO.HIGH if i < count else GPIO.LOW)

try:
    while True:
        # Increment button (falling edge: button pressed)
        if GPIO.input(button_increment) == GPIO.LOW:
            time.sleep(0.05)  # debounce delay
            if GPIO.input(button_increment) == GPIO.LOW:
                counter += 1
                if counter > 8:
                    counter = 0
                update_leds(counter)
                # Wait until button is released
                while GPIO.input(button_increment) == GPIO.LOW:
                    time.sleep(0.01)

        # Reset button
        if GPIO.input(button_reset) == GPIO.LOW:
            time.sleep(0.05)
            if GPIO.input(button_reset) == GPIO.LOW:
                counter = 0
                update_leds(counter)
                while GPIO.input(button_reset) == GPIO.LOW:
                    time.sleep(0.01)

        time.sleep(0.01)

except KeyboardInterrupt:
    print("Cleaning up...")
    GPIO.cleanup()
