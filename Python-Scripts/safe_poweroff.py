# safe_poweroff.py
import time
import os
import RPi.GPIO as GPIO
from gpio_map import GPIO_MAP

BUTTON = GPIO_MAP["POWER"]

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Poweroff daemon running...")

held_time = 0

while True:
    if GPIO.input(BUTTON) == 0:
        held_time += 0.1
        if held_time >= 2:
            print("Shutdown triggered.")
            os.system("sudo shutdown -h now")
            time.sleep(5)
        time.sleep(0.1)
    else:
        held_time = 0
        time.sleep(0.1)



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
