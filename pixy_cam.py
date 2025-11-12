#!/usr/bin/env python3
# pixy_rpi_color_action.py
#
# This script reads detected color signatures from the Pixy2 camera
# and performs different actions based on color combinations.

from pixy import *
from ctypes import *

# Initialize Pixy2
print("Initializing Pixy2...")
pixy_init()
pixy_change_prog("color_connected_components")

# Define signature IDs
PURPLE = 1
BROWN = 2
BLUE = 3
PINK = 4

# Define thresholds for action detection
def has_signatures(blocks, sig_list):
    """Check if all signatures in sig_list are detected."""
    detected = [block.m_signature for block in blocks]
    return all(sig in detected for sig in sig_list)

# Placeholder motor control functions
def climb_bridge():
    print("🟣🟤🔵 Detected — Climbing bridge!")
    # Add GPIO or motor driver control code here, e.g.:
    # motor.forward()
    # time.sleep(2)
    # motor.stop()

def go_on_gravels():
    print("💗🟤🟣 Detected — Moving on gravels!")
    # motor.right()
    # time.sleep(2)
    # motor.stop()

# Main loop
def main():
    print("Starting color detection loop...")
    blocks = BlockArray(100)

    while True:
        count = pixy_get_blocks(100, blocks)

        if count > 0:
            sigs = [blocks[i].m_signature for i in range(count)]
            print(f"Detected signatures: {sigs}")

            # Check combinations
            if has_signatures(blocks, [PURPLE, BROWN, BLUE]):
                climb_bridge()
            elif has_signatures(blocks, [PINK, BROWN, PURPLE]):
                go_on_gravels()
        else:
            print("No objects detected.")

        time.sleep(0.2)

if __name__ == "__main__":
    import time
    main()
