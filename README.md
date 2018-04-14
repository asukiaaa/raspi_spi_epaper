# raspi spi epaper
My programs for Raspberry Pi to use e-paper.

# Components
- Raspberry Pi
- [7.5inch e-Paper type B(Red, White and Black)](https://www.aliexpress.com/item/7-5-inch-ink-screen-red-black-and-white-e-paper-screen-compatible-with-Raspberry-Arduino/32853529687.html?ws_ab_test=searchweb0_0,searchweb201602_2_10152_10065_10151_10344_10068_5722815_10342_10343_10340_5722915_10341_10698_10697_5722615_10696_10084_10083_10618_10307_5722715_5711215_10059_5723015_10534_308_100031_10103_441_10624_10623_10622_5711315_5722515_10621_10620,searchweb201603_15,ppcSwitch_4&algo_expid=47e749fc-c01a-489d-958f-4bd7d50bbc7e-1&algo_pvid=47e749fc-c01a-489d-958f-4bd7d50bbc7e&priceBeautifyAB=0)

# Connection

EPD  | Raspberry Pi
---- | ----
VCC  | 3.3
GND  | GND
DIN  | MOSI
CLK  | SCLK
CS   | CE0
D/C  | IO25
RES  | IO17
BUSY | IO24

# Setup
Enable spi

```
sudo raspi-config
```

On raspiconfig, Select Interfaces -> SPI -> OK.

Install dependencies.
```
sudo apt install pip
pip install pillow
```

# Usage
```
python main.py
```

# References
- [7.5inch e-Paper HAT (B)](https://www.waveshare.com/wiki/7.5inch_e-Paper_HAT_(B))
- [File:7.5inch e-paper hat b code.7z](https://www.waveshare.com/wiki/File:7.5inch_e-paper_hat_b_code.7z)
