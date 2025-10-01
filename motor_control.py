import serial
import time

# Replace with your correct port from Step 2
PORT = "/dev/ttyUSB0"
BAUD = 9600

ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)  # Wait for Arduino to initialize

def send_command(cmd):
    print(f"Sending: {cmd}")
    ser.write(cmd.encode())

# Send motor commands
send_command("<MOT-CWO|50>")
time.sleep(2)
send_command("<MOT-CCW|25>")
time.sleep(2)

ser.close()
