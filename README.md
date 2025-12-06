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

 |Item                                  |Description                                    |Qty|Unit Price|Link                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |Running Total|
|--------------------------------------|-----------------------------------------------|---|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
|Radxa Zero 3W 8GB                     |Main board for emulation                       |1  |$51       |https://shop.allnetchina.cn/collections/rock-3/products/copy-of-radxa-zero-3w?variant=48051150979388                                                                                                                                                                                                                                                                                                                                                                               |$51          |
|2.8″ SPI TFT Display                  |Compact screen for handheld                    |1  |$7.50     |https://www.elecrow.com/2-8-inch-320x240-spi-serial-tft-lcd-module-display-with-driver-ic-ili9341.html?r=cmVsYXRl                                                                                                                                                                                                                                                                                                                                                                  |$58.50       |
|MicroSD Card 128GB                    |Storage for OS and ROMs                        |1  |$15       |https://www.amazon.com/SAMSUNG-Smartphones-Nintendo-Switch-MB-ME128SA-AM/dp/B0CWPN662Q/ref=sr_1_1?th=1                                                                                                                                                                                                                                                                                                                                                                             |$73.50       |
|Flat Li-ion / LiPo Battery 2000 mAh   |Battery power source                           |1  |$9.99     |https://www.amazon.com/Qimoo-Battery-Rechargeable-Connector-Electronic/dp/B0CNLWVCK1/ref=sr_1_4?                                                                                                                                                                                                                                                                                                                                                                                   |$83.49       |
|TP4056 Charging Module                |Charging circuit for battery                   |1  |$6.29     |https://www.amazon.com/Enhanced-Function-Micro-USB-Internal-Protection/dp/B01IYFQAOM/ref=sr_1_5?                                                                                                                                                                                                                                                                                                                                                                                   |$89.78       |
|Step-up / Voltage Boost Module        |Converts battery voltage to 5 V                |1  |$6.99     |https://www.amazon.com/Dorhea-MT3608-DC-DC-Boost-Converter/dp/B089JYBF25/ref=sr_1_12?                                                                                                                                                                                                                                                                                                                                                                                              |$96.77       |
|ABXY Button Set (extras used for dpad)|Main controls                                  |1  |$8.99     |https://www.amazon.com/12x12x7-3-Momentary-Electronics-Prototyping-Projects/dp/B0FHW6ZHMD/ref=sr_1_19_sspa?                                                                                                                                                                                                                                                                                                                                                                        |$105.76      |
|Start / Select 6x6mm buttons          |Extra small buttons for start/select           |1  |$6.99     |https://www.amazon.com/CHANZON-RA11-BUTTON-SWITCH/dp/B09R3Q48GY?th=1                                                                                                                                                                                                                                                                                                                                                                                                               |$112.75      |
|3.5 mm Panel‑Mount Audio Jack         |Headphone output                               |1  |$9.99     |https://www.amazon.com/Treedix-Female-Breakout-Plastic-Connector/dp/B08H8DR7ZW/ref=sr_1_4?crid=2GP8819OC1Y3K&dib=eyJ2IjoiMSJ9.eHpc-                                                                                                                                                                                                                                                                                                                                                |$122.74      |
|Jumper Wires                          |Wiring for board + buttons + battery           |1  |$6.98     |https://www.amazon.com/Elegoo-EL-CP-004-Multicolored-Breadboard-arduino/dp/B01EV70C78/ref=sr_1_1_sspa?=sr_1_1_sspa?                                                                                                                                                                                                                                                                                                                                                                |$129.72      |
|XL‑sized Tin                          |Altoids tin or similar metal enclosure         |1  |$15.00    |https://www.ebay.com/itm/227108602323?_trkparms=itmf%3D1%26aid%3D111001%26rkt%3D20%26algo%3DREC.SEED%26asc%3D20240304162621%26mech%3D1%26algv%3D%26pmt%3D0%26amclksrc%3DITM%26sid%3DAQAKAAAAEAXwxNtvrUxTFaD5DluiPDU%3D%26itm%3D227108602323%26noa%3D1%26ao%3D1%26rk%3D2%26pid%3D102020%26b%3D1%26mehot%3Dnone%26lsid%3D0%26meid%3Dffd0e7c70e6f4f9aa395c1ab6bc12141%26pg%3D2332490&_trksid=p2332490.c102020.m5276                                                                   |$144.72      |
|Toggle Power Switch                   |Supplies power on/off cleanly                  |1  |$6.00     |https://www.amazon.com/Position-Vertical-Available-Electronic-Projects/dp/B0DR2M8B59/ref=sr_1_43_sspa?                                                                                                                                                                                                                                                                                                                                                                             |$150.72      |
|Resistor Kit 1/4 W                    |Resisters to prevent ghost presses from buttons|1  |$5.98     |https://www.amazon.com/Resistor-Resistors-Assortment-Breadboard-Electronics/dp/B0F4P352BB/ref=sr_1_3?dib=eyJ2IjoiMSJ9.51CpWqJSseWX_hEqqJr41AbdsMj3JnUWwQX1kHL7uCPoD1XmRUJZUkOEKaWAuWAIMoSlQ1lVkEW_tdZ41rrbbZqt4EbS3QHCguOPIZySPBdMrLJkvCwZ1_txdbL8PAw_TRjTYwls9fYiINeYinFrncl_q_tHeaGMxbdefJGztPaKf2_vclp2iwA7ZlHbxM_OnNw7k4WVr0SfXXqBM1hoEcPqSt3fE8SrBU_LfdxhjJc.YlEcL16D4I72qS8XC5J566He41yFKOjqTOZOsdVT2kM&dib_tag=se&keywords=10k+ohm+resistor+assortment&qid=1764983133&sr=8-3|$156.70      |
|Shipping                              |                                               |   |$40       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |$196.70      |


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

## Images
![image](https://raw.githubusercontent.com/LowPolyPhosphorus/AltoiDS/main/Altoids%20Images/12-3-25%20%282%29/image%20%282%29.webp)
![image](https://raw.githubusercontent.com/LowPolyPhosphorus/AltoiDS/main/Altoids%20Images/12-5-25/image%20(1).png)
