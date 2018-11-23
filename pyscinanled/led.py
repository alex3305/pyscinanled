from .btle_connection import BtleConnection
from .const import BRIGHTNESS_MAX, BRIGHTNESS_MIN, DEFAULT_RETRIES, \
    COMMAND_BRIGHTNESS, COMMAND_EFFECT, COMMAND_SWITCH
from .effect import Effect


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
        command.append(brightness)
        self._connection.send_command(command)

    def disconnect(self):
        self._connection.disconnect()

    def effect(self, effect: Effect = None, effects: list = None,
               bitmask: int = None):
        command = COMMAND_EFFECT.copy()

        if effect is not None:
            command.append(effect.Value)
        elif effects is not None:
            command.append(Effect.combine_effects(effects))
        elif bitmask is not None:
            command.append(bitmask)

        self._connection.send_command(command)

    def turn_on(self):
        command = COMMAND_SWITCH.copy()
        command.append(0x01)
        self._connection.send_command(command)

    def turn_off(self):
        command = COMMAND_SWITCH.copy()
        command.append(0x00)
        self._connection.send_command(command)

    def __del__(self):
        self.disconnect()
