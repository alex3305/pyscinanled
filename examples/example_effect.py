# Hack to allow relative import above top level package
import sys
import os
folder = os.path.dirname(os.path.abspath(__file__))  # noqa
sys.path.insert(0, os.path.normpath("%s/.." % folder))  # noqa

import argparse
import time

from pyscinanled import ScinanLed, Effect, EFFECT_LIST


parser = argparse.ArgumentParser()
parser.add_argument('-m', dest='mac', type=str,
                    help='MAC address of bluetooth device')

args = parser.parse_args()

if args.mac is None:
    print('A MAC address is required to run this example')
    exit(1)

print('Connecting to your led strip...')
dev = ScinanLed(args.mac)

print('Activating a random effect')
dev.effect(Effect.get_random_effect(EFFECT_LIST))
time.sleep(5)

print('Activating all effects')
dev.effect(Effect.combine_effects(EFFECT_LIST))
time.sleep(5)

print('Returning to constant effect')
dev.effect(Effect.get_effect(EFFECT_LIST, name='Stay on'))

dev.disconnect()
