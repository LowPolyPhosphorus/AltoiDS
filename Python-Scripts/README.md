# AltoiDS Preliminary Code Overview

This directory contains the initial software components developed for the AltoiDS handheld.
Because the grant has not yet been awarded, these scripts are written to operate in mock/simulated mode so they can run without hardware. Each script represents part of the planned system architecture for the final device.

These files demonstrate early-stage development of:

Input handling

Power management

RetroArch configuration generation

Menu/UI logic

Debug utilities

GPIO planning and validation

They will be expanded after hardware is acquired.

## 1. button_test.py

Purpose: Simulated GPIO input tester
Role in final system: Verifies tactile switch wiring and ensures all button inputs register correctly once connected.

### Key Features:

Works with real GPIO or in MOCK mode with random simulated button presses

Prints live button events

Helps validate correct wiring and pull-up resistor configuration

Intended for first hardware test after assembly

## 2. generate_button_map.py

Purpose: Automatically generate a RetroArch input configuration file based on the planned GPIO assignments.
Role in final system: Ensures that RetroPie/RetroArch correctly interprets button inputs from the AltoiDS control PCB/wiring.

### Key Features:

Outputs a standard retroarch_gpio.cfg

Maps all ABXY, D-pad, Start, and Select inputs

Allows consistent configuration across images and OS reinstalls

## 3. power_button_daemon.py

Purpose: Background service for monitoring a dedicated power/shutdown button.
Role in final system: Provides safe shutdown functionality and protects the filesystem from corruption.

### Key Features:

Long-press detection with HOLD_TIME threshold

Calls shutdown -h now on real hardware

Fully simulated behavior for development

Designed to run as a systemd service in the final build

## 4. launcher_mock.py

Purpose: Prototype of the handheld’s front-end launcher.
Role in final system: Will become the UI for selecting RetroPie, settings, and system functions.

### Key Features:

Text-based mock menu navigated with keyboard (W/S + Enter)

Demonstrates UI flow before a display and physical buttons are installed

Establishes layout for a future graphical launcher

## 5. pinout_validator.py

Purpose: Validates planned GPIO wiring assignments.
Role in final system: Prevents wiring mistakes and pin conflicts before soldering.

### Key Features:

Detects duplicate GPIO assignments

Helps ensure the final button matrix is electrically safe and functional

Reduces risk of rebuilding wiring after discovering a conflict

## 6. debug_logger.py

Purpose: Simulated event logger for system and input diagnostics.
Role in final system: Will be used to verify inputs, power events, and launcher actions during live debugging.

### Key Features:

Writes timestamped events to debug_log.txt

Generates random simulated button events

Useful for verifying the logging pipeline before hardware exists
