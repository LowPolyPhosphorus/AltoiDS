#!/usr/bin/env python3
"""
debug_logger.py
Simulated logging tool for capturing button events or system messages.
"""

import time
import random

LOGFILE = "debug_log.txt"
EVENTS = ["UP", "DOWN", "LEFT", "RIGHT", "A", "B", "X", "Y", "START", "SELECT"]


def log_event(event):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp} | EVENT: {event}\n"
    with open(LOGFILE, "a") as f:
        f.write(line)
    print(line, end="")


def main():
    print("Debug logger running. Simulating events...")
    try:
        while True:
            time.sleep(random.uniform(0.5, 2.5))
            event = random.choice(EVENTS)
            log_event(event)
    except KeyboardInterrupt:
        print("Logger stopped.")


if __name__ == "__main__":
    main()
