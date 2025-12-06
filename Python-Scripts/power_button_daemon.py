#!/usr/bin/env python3
"""
power_button_daemon.py
Watches a GPIO pin for a long-press shutdown signal.
"""

import time
import os

MOCK = False

try:
    import RPi.GPIO as GPIO
except ImportError:
    MOCK = True


SHUTDOWN_PIN = 4
HOLD_TIME = 2.0  # seconds


def setup():
    if MOCK:
        print("[MOCK] Power button monitoring enabled.")
        return

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SHUTDOWN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def button_pressed():
    if MOCK:
        return False
    return GPIO.input(SHUTDOWN_PIN) == GPIO.LOW


def main():
    setup()
    pressed_at = None
    print("Power button daemon started.")

    try:
        while True:
            if button_pressed():
                if pressed_at is None:
                    pressed_at = time.time()
            else:
                pressed_at = None

            if pressed_at and (time.time() - pressed_at >= HOLD_TIME):
                print("Shutdown triggered.")
                if not MOCK:
                    os.system("sudo shutdown -h now")
                break

            time.sleep(0.05)
    except KeyboardInterrupt:
        print("Exiting daemon...")
    finally:
        if not MOCK:
            GPIO.cleanup()


if __name__ == "__main__":
    main()
