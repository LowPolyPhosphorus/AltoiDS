# input_watchdog.py
import time
import RPi.GPIO as GPIO
from gpio_map import GPIO_MAP

GPIO.setmode(GPIO.BCM)
for pin in GPIO_MAP.values():
    if isinstance(pin, int):
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

last_state = {}

print("Input watchdog running... Press CTRL+C to exit.")

while True:
    for name, pin in GPIO_MAP.items():
        if isinstance(pin, int):
            state = GPIO.input(pin)
            if name not in last_state:
                last_state[name] = state
            if last_state[name] != state:
                print(f"[EVENT] {name} changed: {state}")
                last_state[name] = state
    time.sleep(0.02)
