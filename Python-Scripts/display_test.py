# display_test.py
import time
import digitalio
import board
import busio
from PIL import Image, ImageDraw

from gpio_map import GPIO_MAP

spi = busio.SPI(board.SCLK, MOSI=board.MOSI)
cs  = digitalio.DigitalInOut(board.CE0)
dc  = digitalio.DigitalInOut(board.D25)
rst = digitalio.DigitalInOut(board.D24)

from adafruit_ili9341 import ILI9341

display = ILI9341(spi, rotation=0, cs=cs, dc=dc, rst=rst)

img = Image.new("RGB", (240, 320), color=(0, 0, 0))
draw = ImageDraw.Draw(img)

draw.text((20, 20), "AltoiDS Display Test", fill=(255, 255, 255))
draw.rectangle((0, 300, 240, 319), fill=(255, 0, 0))

display.image(img)

print("Image displayed. Test finished.")
