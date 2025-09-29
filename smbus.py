from smbus2 import SMBus, i2c_msg

# === CONFIGURATION ===
I2C_BUS = 1              # usually 1 on Pi
I2C_ADDR = 0x54          # replace with your device's address
COMM_BYTE = 0x00         # SMBus command code for block read (depends on your device)

# === COMMAND PAYLOAD ===
sync = [0xAE, 0xC1]      # Sync bytes
packet_type = 32         # Command type
payload_length = 2       # Number of bytes in the payload
sigmap = 255             # All signatures
max_blocks = 10          # Number of blocks to return

# Full command packet
command = sync + [packet_type, payload_length, sigmap, max_blocks]

# === SMBus I2C Communication ===
with SMBus(I2C_BUS) as bus:
    # Send command
    write = i2c_msg.write(I2C_ADDR, command)
    bus.i2c_rdwr(write)

    # Perform SMBus block read
    # You send a command byte (COMM) and receive a block (up to 32 bytes)
    response = bus.read_i2c_block_data(I2C_ADDR, COMM_BYTE)

    print("Received response:")
    print(response)
