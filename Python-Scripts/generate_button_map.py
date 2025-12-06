#!/usr/bin/env python3
"""
generate_button_map.py
Creates a RetroArch-compatible button mapping file based on GPIO assignments.
"""

import json

PIN_ASSIGNMENTS = {
    "input_up_btn": 5,
    "input_down_btn": 6,
    "input_left_btn": 13,
    "input_right_btn": 19,
    "input_a_btn": 16,
    "input_b_btn": 20,
    "input_x_btn": 21,
    "input_y_btn": 26,
    "input_start_btn": 17,
    "input_select_btn": 27
}


def generate_config():
    config = ""
    for key, pin in PIN_ASSIGNMENTS.items():
        config += f"{key} = \"{pin}\"\n"
    return config


def save_config(path="retroarch_gpio.cfg"):
    cfg = generate_config()
    with open(path, "w") as f:
        f.write(cfg)
    print(f"Created RetroArch GPIO config: {path}")


if __name__ == "__main__":
    save_config()
