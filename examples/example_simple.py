# Hack to allow relative import above top level package
import sys
import os
folder = os.path.dirname(os.path.abspath(__file__))  # noqa
sys.path.insert(0, os.path.normpath("%s/.." % folder))  # noqa

import argparse
import time

from pyscinanled import ScinanLed

parser = argparse.ArgumentParser()
parser.add_argument('mac', dest='mac', type=str,
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
