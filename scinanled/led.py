from scinanled.btle_connection import BtleConnection
from scinanled.const import BRIGHTNESS_MAX, BRIGHTNESS_MIN, DEFAULT_RETRIES, \
    COMMAND_BRIGHTNESS, COMMAND_EFFECT, COMMAND_SWITCH
from scinanled.effect import Effect


class ScinanLed:

    def __init__(self, mac: str, retries: int = DEFAULT_RETRIES):
        self._connection = BtleConnection(mac, retries)
        self._connection.connect()
        return

    def brightness(self, brightness: int):
        if brightness > BRIGHTNESS_MAX:
            brightness = BRIGHTNESS_MAX

        if brightness < BRIGHTNESS_MIN:
            brightness = BRIGHTNESS_MIN

        command = COMMAND_BRIGHTNESS.copy()
        self._connection.send_command(command.append(brightness))

    def disconnect(self):
        self._connection.disconnect()

    def effect(self, effect: Effect = None, effects: list = None,
               bitmask: int = None):
        e = 0

        if effect is not None:
            e = effect.Value
        elif effects is not None:
            e = Effect.combine_effects(effects)
        elif bitmask is not None:
            e = bitmask

        command = COMMAND_EFFECT.copy()
        self._connection.send_command(command.append(e))

    def turn_on(self):
        command = COMMAND_SWITCH.copy()
        self._connection.send_command(command.append(0x01))

    def turn_off(self):
        command = COMMAND_SWITCH.copy()
        self._connection.send_command(command.append(0x00))

    def __del__(self):
        self.disconnect()
