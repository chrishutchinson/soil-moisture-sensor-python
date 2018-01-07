import time
import RPi.GPIO as GPIO

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_MCP3008

# Setup the GPIO board
GPIO.setmode(GPIO.BCM)

# Setup the switch pin
SWITCH = 20
GPIO.setup(SWITCH, GPIO.OUT)

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

print('Reading MCP3008 value on channel 0, press Ctrl-C to quit...')

try:
    # Main program loop.
    while True:
        GPIO.output(SWITCH, GPIO.HIGH)
        time.sleep(0.1)
        value = float(mcp.read_adc(0))
        print("The soil moisture reading is currently at {:.2f}%").format(value / 1023 * 100)
        GPIO.output(SWITCH, GPIO.LOW)
        time.sleep(10)
except KeyboardInterrupt:
    GPIO.output(SWITCH, GPIO.LOW)
    GPIO.cleanup()