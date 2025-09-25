import RPi.GPIO as GPIO
import time

# Pins for LEDs
led_pins = [10, 12, 16, 18, 22, 24, 26, 11]

# Pins for buttons
increment_button = 13
reset_button = 15

# Setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Setup LED pins, start OFF
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Setup button pins with pull-up resistors
GPIO.setup(increment_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(reset_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Keep track of how many LEDs are on
led_index = -1

def reset_leds():
    """Turn off all LEDs and reset index."""
    global led_index
    for pin in led_pins:
        GPIO.output(pin, GPIO.LOW)
    led_index = -1
    print("All LEDs reset")

def increment_pressed(channel):
    """Increment LEDs, reset if all are on."""
    global led_index
    if led_index < len(led_pins) - 1:
        led_index += 1
        GPIO.output(led_pins[led_index], GPIO.HIGH)
        print(f"LED on pin {led_pins[led_index]} turned ON")
    else:
        reset_leds()

def reset_pressed(channel):
    """Handle reset button press."""
    reset_leds()

# Detect button presses (shorter debounce time)
GPIO.add_event_detect(increment_button, GPIO.RISING, callback=increment_pressed, bouncetime=100)
GPIO.add_event_detect(reset_button, GPIO.RISING, callback=reset_pressed, bouncetime=100)

try:
    print("Press increment (pin 13) to light LEDs, reset (pin 15) to clear...")
    while True:
        time.sleep(0.1)  # Keep program alive
except KeyboardInterrupt:
    print("\nExiting program.")
finally:
    GPIO.cleanup()
