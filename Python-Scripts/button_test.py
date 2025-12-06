#!/usr/bin/env python3
"""
button_test.py
Simulated GPIO button input test for the AltoiDS handheld.

Runs in MOCK mode if real GPIO libraries are not available.
"""

import time
import random

MOCK = False

try:
    import RPi.GPIO as GPIO
except ImportError:
    MOCK = True


# -----------------------------
# Button Definitions
# -----------------------------
BUTTON_PINS = {
    "UP": 5,
    "DOWN": 6,
    "LEFT": 13,
    "RIGHT": 19,
    "A": 16,
    "B": 20,
    "X": 21,
    "Y": 26,
    "START": 17,
    "SELECT": 27
}


def setup_gpio():
    if MOCK:
        print("[MOCK] GPIO unavailable. Running simulated mode.")
        return

    GPIO.setmode(GPIO.BCM)
    for btn, pin in BUTTON_PINS.items():
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def read_button(btn):
    if MOCK:
        # Randomly simulate a press (very low chance)
        return random.random() < 0.03
    return GPIO.input(BUTTON_PINS[btn]) == GPIO.LOW


def main():
    setup_gpio()
    print("Starting button tester. Press CTRL+C to exit.")
    try:
        while True:
            for btn in BUTTON_PINS:
                if read_button(btn):
                    print(f"[PRESS] {btn}")
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        if not MOCK:
            GPIO.cleanup()


if __name__ == "__main__":
    main()
