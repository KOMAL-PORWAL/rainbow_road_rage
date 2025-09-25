import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# LED GPIO pins in game order (Red, Red, Red, Green, Yellow, Yellow, Yellow)
led_pins = [10, 12, 16, 18, 22, 24, 26]
green_led_index = 3  # index of green LED

# Button GPIO pin
button_pin = 15

# Set difficulty (smaller = faster)
delay = 0.15  # seconds between LEDs — tweak for difficulty

# Setup LED pins
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Setup button with internal pull-up
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup PWM for green LED
green_led_pwm = GPIO.PWM(led_pins[green_led_index], 100)  # 100 Hz
green_led_pwm_started = False

def win_animation():
    print("You Win!")
    green_led_pwm.start(0)
    for i in range(20):  # 2 seconds of blinking
        green_led_pwm.ChangeDutyCycle((i % 2) * 100)
        time.sleep(0.1)
    green_led_pwm.stop()
    GPIO.output(led_pins[green_led_index], GPIO.LOW)

def lose_animation():
    print("Missed!")
    for _ in range(3):
        for pin in led_pins:
            GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.2)
        for pin in led_pins:
            GPIO.output(pin, GPIO.LOW)
        time.sleep(0.2)

try:
    print("Cyclone game started. Press button on GREEN LED to win!")
    button_pressed = False

    while True:
        for i in range(len(led_pins)):
            # Turn on the current LED, turn off others
            for j, pin in enumerate(led_pins):
                GPIO.output(pin, GPIO.HIGH if i == j else GPIO.LOW)

            start_time = time.time()
            while time.time() - start_time < delay:
                # Detect a clean button press
                if GPIO.input(button_pin) == GPIO.LOW:
                    if not button_pressed:
                        button_pressed = True
                        if i == green_led_index:
                            win_animation()
                        else:
                            lose_animation()
                    break
                else:
                    button_pressed = False
                time.sleep(0.01)  # Polling delay

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
