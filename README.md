# Soil moisture sensor + Raspberry Pi

> Python script for reading value of an analog soil moisture sensor via an
> MCP3008 and Raspberry Pi

### Breadboard layout

![Breadboard](schematic_bb.png)

### Script dependencies

```bash
pip install adafruit-mcp3008
```

### MCP3008

The MCP3008 allows the digital-only Raspberry Pi GPIO pins to read up to eight
analog signals. Details on how to configure and use this with Python can be
found at
[this link](https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008)
from the Adafruit website.
