import serial
import time

# Replace with your Arduino's serial port
# You can run `ls /dev/ttyACM*` or `ls /dev/ttyUSB*` to check
PORT = '/dev/ttyACM0'   # May be ttyUSB0 on some setups
BAUD = 9600

def send_motor_command(direction, speed_percent):
    """
    Sends a formatted motor command to the Arduino over serial.
    
    direction: "CWO" or "CCW"
    speed_percent: 0 to 100
    """
    if direction not in ["CWO", "CCW"]:
        raise ValueError("Invalid direction. Use 'CWO' or 'CCW'.")
    if not (0 <= speed_percent <= 100):
        raise ValueError("Speed must be between 0 and 100.")

    # Format the command
    command = f"<MOT-{direction}|{speed_percent}>"
    print(f"Sending: {command}")

    # Send over serial
    with serial.Serial(PORT, BAUD, timeout=2) as ser:
        time.sleep(2)  # Give Arduino time to reset on connect
        ser.write(command.encode('utf-8'))
        # Optional: read response
        response = ser.readline().decode('utf-8').strip()
        if response:
            print("Arduino replied:", response)

# 🧪 Test the function
if __name__ == "__main__":
    # Example: Run clockwise at 50%
    send_motor_command("CWO", 50)

    time.sleep(3)

    # Then reverse at 25%
    send_motor_command("CCW", 25)

    time.sleep(3)

    # Then stop the motor
    send_motor_command("CWO", 0)
