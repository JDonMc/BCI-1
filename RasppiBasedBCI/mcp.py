import time
# https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

NetworkOutput = ['Please', 'Phone', 'Computer', 'Headtop', 'Up', 'Down', 'Left', 'Right', 'In', 'Out', 'Click',
                 'Search', 'Add', 'Remove', 'Cancel', 'Thanks']

CLK = 23
MISO = 21
MOSI = 19
CS = 24
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
readings = 100000
rate = 0.00001  # readings*rate = 1
switch_pin = 11  # refer to pinout.xyz


def write_to_file(filename, array):
    actual_file_name = filename + '.txt'
    writefile = open(actual_file_name, 'w+')
    writefile.write('nextLearning')
    writefile.write(str(len(array)))
    writefile.writelines(array)
    writefile.close()

# make a switch control this. 3.3V with pull up / down
counter = 0
value = [0]*readings
while True:
    switch = GPIO.input(switch_pin)  # read GPIO pin input for switch.
    if switch:
        for r in range(0, readings, 1):
            value[r] = mcp.read_adc(1)
            time.sleep(rate)  # 100k X 24 bits... 2.4 MHz, should be ok...
        write_to_file(NetworkOutput[counter], value)
        counter += 1
        switch = False
