import argparse
import time

from pyscinanled.led import ScinanLed

parser = argparse.ArgumentParser()
parser.add_argument('mac', metavar='Mac', type=str,
                    help='MAC address of bluetooth device')

args = parser.parse_args()

if args.mac is None:
    print('A MAC address is required to run this example')
    exit(1)

print('Connecting to your led strip...')
dev = ScinanLed(args.mac)

print('Turning on your led strip')
dev.turn_on()
time.sleep(5)

print('Set the brightness to 20%')
dev.brightness(20)
time.sleep(5)

print('Set the brightness to 100%')
dev.brightness(100)
time.sleep(5)

print('Turning off the led strip and disconnect')
dev.turn_off()
dev.disconnect()
