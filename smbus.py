from smbus2 import SMBus

# === Configuration ===
I2C_BUS = 1                  # Typically /dev/i2c-1
DEVICE_ADDR = 0x54           # Replace with your device's I2C address
COMM_BYTE = 0x00             # Register/command byte used for both write and read

# === Command Payload for getBlocks(sigmap=255, maxBlocks=1) ===
command_payload = [
    0xAE, 0xC1,    # Sync (little endian: 0xC1AE)
    32,            # Type of packet
    2,             # Length of payload
    255,           # Sigmap (all signatures)
    1              # Max blocks to return
]

with SMBus(I2C_BUS) as bus:
    # SMBus Block Write: send command
    bus.write_i2c_block_data(DEVICE_ADDR, COMM_BYTE, command_payload)
    print("Command sent.")

    # SMBus Block Read: read response
    response = bus.read_i2c_block_data(DEVICE_ADDR, COMM_BYTE)
    print(f"Received {len(response)} bytes from device:")
    print(response)

    # === Optional: Parse response ===
    if len(response) >= 20:
        sync = response[0:2]
        packet_type = response[2]
        payload_len = response[3]
        checksum = response[4] | (response[5] << 8)
        signature = response[6] | (response[7] << 8)
        x = response[8] | (response[9] << 8)
        y = response[10] | (response[11] << 8)
        width = response[12] | (response[13] << 8)
        height = response[14] | (response[15] << 8)
        angle = response[16] | (response[17] << 8)
        track_index = response[18]
        age = response[19]

        print("\nParsed Block:")
        print(f"  Sync: {sync}")
        print(f"  Packet Type: {packet_type}")
        print(f"  Payload Length: {payload_len}")
        print(f"  Checksum: {checksum}")
        print(f"  Signature: {signature}")
        print(f"  X: {x}, Y: {y}")
        print(f"  Width: {width}, Height: {height}")
        print(f"  Angle: {angle}")
        print(f"  Track Index: {track_index}")
        print(f"  Age: {age}")
    else:
        print("Response too short to parse block data.")
