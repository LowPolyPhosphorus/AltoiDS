#!/usr/bin/env python3
"""
pinout_validator.py
Validates planned GPIO wiring for conflicts and duplicates.
"""

PINOUT = {
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


def main():
    print("Validating pinout...\n")

    used = {}
    errors = []

    for name, pin in PINOUT.items():
        if pin in used:
            errors.append(f"CONFLICT: {name} and {used[pin]} both use GPIO {pin}")
        else:
            used[pin] = name

    if errors:
        print("Errors found:")
        for e in errors:
            print(" -", e)
    else:
        print("No conflicts detected. Pinout is valid.")


if __name__ == "__main__":
    main()
