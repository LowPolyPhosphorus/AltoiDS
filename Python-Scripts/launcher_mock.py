#!/usr/bin/env python3
"""
launcher_mock.py
A text-based prototype menu for the AltoiDS handheld.
Simulates navigation using keyboard input until real buttons are wired.
"""

import time

MENU_ITEMS = [
    "Start RetroPie",
    "Settings",
    "Shutdown"
]


def display_menu(selected):
    print("\n=== AltoiDS Launcher Prototype ===")
    for i, item in enumerate(MENU_ITEMS):
        prefix = ">" if i == selected else " "
        print(f"{prefix} {item}")
    print("\nUse W/S and ENTER to simulate buttons.\n")


def main():
    selected = 0

    while True:
        display_menu(selected)
        key = input("Input: ").lower().strip()

        if key == "w":
            selected = (selected - 1) % len(MENU_ITEMS)
        elif key == "s":
            selected = (selected + 1) % len(MENU_ITEMS)
        elif key == "":
            print(f"Selected: {MENU_ITEMS[selected]}")
            time.sleep(0.5)
        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()
