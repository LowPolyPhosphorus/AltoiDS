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

<details>
  <summary><strong>Bill of Materials (CSV)</strong></summary>

| Item | Description | Qty | Unit Price | Link | Running Total |
|------|-------------|-----|------------|------|---------------|
| Radxa Zero 3W 4GB | Main board for emulation | 1 | $52.63 | [AliExpress](https://www.aliexpress.us/item/3256807428419499.html?gatewayAdapt=esp2usa4itemAdapt) | $52.63 |
| 2.8″ SPI TFT Display | Compact screen for handheld | 1 | $7.50 | [Elecrow](https://www.elecrow.com/2-8-inch-320x240-spi-serial-tft-lcd-module-display-with-driver-ic-ili9341.html?r=cmVsYXRl) | $60.13 |
| MicroSD Card 128GB | Storage for OS and ROMs | 1 | $15.00 | [Amazon](https://www.amazon.com/SAMSUNG-Smartphones-Nintendo-Switch-MB-ME128SA-AM/dp/B0CWPN662Q/ref=sr_1_1?th=1) | $75.13 |
| Flat Li-ion / LiPo Battery 2000 mAh | Battery power source | 1 | $7.07 | [AliExpress](https://www.aliexpress.us/item/3256810055637543.html) | $82.20 |
| TP4056 Charging Module | Charging circuit for battery | 1 | $1.98 | [AliExpress](https://www.aliexpress.us/item/3256804241424963.html) | $84.18 |
| Step-up / Voltage Boost Module | Converts battery voltage to 5 V | 1 | $2.93 | [AliExpress](https://www.aliexpress.us/item/3256808260885117.html) | $87.11 |
| ABXY Button Set (extras used for dpad) | Main controls | 1 | $7.61 | [AliExpress](https://www.aliexpress.us/item/3256808778757512.html) | $94.72 |
| Start / Select 6x6mm buttons | Extra small buttons for start/select | 1 | $2.38 | [AliExpress](https://www.aliexpress.us/item/3256801442931013.html) | $97.10 |
| 3.5 mm Panel‑Mount Audio Jack | Headphone output | 1 | $0.72 | [AliExpress](https://www.aliexpress.us/item/3256806443682492.html) | $97.82 |
| Dupont Jumper Wires | Wiring for board + buttons + battery | 1 | $8.44 | [AliExpress](https://www.aliexpress.us/item/3256810340724400.html) | $106.26 |
| XL‑sized Tin | Altoids tin or similar metal enclosure | 1 | $22.95 | [eBay](https://www.ebay.com/itm/227108602323) | $129.21 |
| Toggle Power Switch | Supplies power on/off cleanly | 1 | $2.50 | [AliExpress](https://www.aliexpress.us/item/2251801856197853.html) | $131.71 |
| Resistor Kit 1/4W | Resistors to prevent ghost presses from buttons | 1 | $5.98 | [Amazon](https://www.amazon.com/Resistor-Resistors-Assortment-Breadboard-Electronics/dp/B0F4P352BB) | $137.69 |
| **Shipping (+fees)** | | | **$35.81** | | **$173.50** |
</details>

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

## Gallery
![image](https://raw.githubusercontent.com/LowPolyPhosphorus/AltoiDS/main/Altoids%20Images/12-3-25%20%282%29/image%20%282%29.webp)
![image](https://raw.githubusercontent.com/LowPolyPhosphorus/AltoiDS/main/Altoids%20Images/12-5-25/image%20(1).png)
![Image 1 PNG](Altoids%20Images/image%20(1).png)
![Image 1 WEBP](Altoids%20Images/image%20(1).webp)
![Image WEBP](Altoids%20Images/image.webp)
## Renders
![Cutouts View](CAD%20Models/AltoiDS-cutouts-Render.png)
![Insert View](CAD%20Models/AltoiDSw\tin-Render.png)
