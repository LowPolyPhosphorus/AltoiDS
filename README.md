# AltoiDS
AltoiDS is a compact retro gaming handheld built inside an XL Altoids tin. The goal is to fit a fully working emulator system into a small enclosure using off-the-shelf parts, simple wiring, and 3D printed internal mounts. This build does not use a custom PCB and stays within Hack Club Blueprint Tier 2 pricing.

## Project Summary
The system runs on a Radxa Zero 3W paired with a 2.8 inch ILI9341 SPI display. Controls use tactile switches wired directly to GPIO with pull-up resistors. Power comes from a 2000 mAh LiPo battery with a TP4056 charger and MT3608 boost converter. All components are arranged and held in place using custom 3D printed brackets designed specifically for the interior layout of the XL tin.

The main challenge is managing part placement, wiring paths, and structural stability inside the limited internal volume. CAD work so far includes exterior form testing and internal mounting prototypes to make sure components fit securely.

## Hardware
- Radxa Zero 3W  
- 2.8 inch SPI display (ILI9341)  
- 12x12 mm tactile switches (D-pad and ABXY)  
- 6x6 mm tactile switches (Start and Select)  
- 2000 mAh LiPo battery  
- TP4056 charge module  
- MT3608 boost converter  
- 10k resistor kit for GPIO pull-ups  
- 3.5 mm headphone jack (optional)  
- Dupont wires and soldered connections  
- 3D printed mounts for the screen, buttons, battery, and Radxa board  

## Software Setup
A lightweight Linux image is configured for the Radxa with emulators for NES, SNES, Game Boy, Game Boy Color, and Genesis. GPIO input mapping and display configuration will be finalized once all hardware is installed.

## Blueprint Tier
The total cost is about **190 dollars including shipping**, which places the project inside **Tier 2**. The project uses modular wiring and 3D printed structures instead of a custom PCB to stay within budget.

## Build Method
The assembly is fully DIY:
- Soldering and routing all wiring manually  
- Connecting buttons directly to GPIO  
- Building the layout using 3D printed brackets  
- Fitting components without altering the tin  
- Testing power, input, and display in stages  

## Images
![image](https://raw.githubusercontent.com/LowPolyPhosphorus/AltoiDS/main/Altoids%20Images/12-3-25%20%282%29/image%20%282%29.webp)
![image](https://raw.githubusercontent.com/LowPolyPhosphorus/AltoiDS/main/Altoids%20Images/12-5-25/image%20(1).png)
