# AltoiDS
A concept for fitting a complete retro gaming emulator into an XL Altoids tin. The challenge is cramming a functional handheld console into a space designed for mints while keeping it playable and portable.
## The Concept
Take classic gaming systems (NES, Game Boy, SNES, Genesis) and squeeze them into pocket-sized hardware. The design centers around a Radxa Zero 3W single-board computer paired with a 2.8" SPI display. Full gaming controls include a D-pad, ABXY buttons, Start, and Select. Audio output through a 3.5mm headphone jack. A 2000mAh LiPo battery powers everything with onboard charging and voltage regulation to keep the system stable.
## Design Approach
The build avoids custom PCBs in favor of modular components and 3D-printed mounting solutions. Tactile switches connect directly to GPIO pins with pull-up resistors to handle button inputs. The screen mounts to the lid of the tin, visible when opened. Internal 3D-printed shells organize and secure the electronics, buttons, and battery without permanent modifications to the enclosure.
Button sizing varies by function: 12x12mm switches for primary controls (ABXY and directional), smaller 6x6mm switches for secondary functions (Start/Select). Everything connects through dupont wiring to keep assembly flexible and repairable.
## The Constraints
This concept exists within Hack Club's Blueprint challenge framework, which provides up to $400 for hardware. The goal is building something functional within budget while exploring how embedded systems handle emulation and how far miniaturization can go before usability breaks down.
The XL Altoids tin defines the physical limits. Every component choice considers space, power draw, and thermal management. The Radxa Zero 3W was chosen for its balance of processing power and compact form factor. The display size represents the largest screen that fits while leaving room for controls and electronics.
## Pricing
Although this project would usually fit Tier 2 or 3 in scope, the total budget slightly exceeds $200 due to shipping costs. The project is classified as Tier 1 because the grant supports a higher-cost build that cannot be achieved at Tier 2 levels
### Other
I plan a DIY, hands-on assembly and wiring process, even without a custom PCB, including manually routing wires, configuring GPIO pins, soldering components, and designing 3D-printed mounts to maximize space and functionality inside the XL Altoids tin.
![image](https://raw.githubusercontent.com/LowPolyPhosphorus/AltoiDS/main/Altoids%20Images/12-3-25%20%282%29/image%20%282%29.webp)
![image](https://raw.githubusercontent.com/LowPolyPhosphorus/AltoiDS/main/Altoids%20Images/12-5-25/image%20(1).png)
