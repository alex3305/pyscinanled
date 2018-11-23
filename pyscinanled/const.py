from .effect import Effect

BRIGHTNESS_MIN = 10
BRIGHTNESS_MAX = 110

CHAR_START_HANDLE = 0x0024
CHAR_END_HANDLE = 0x0024
CHAR_UUID = "0000fff1-0000-1000-8000-00805f9b34fb"

COMMAND_BRIGHTNESS = [0x03, 0x01, 0x01]
COMMAND_EFFECT = [0x05, 0x01, 0x02, 0x03]
COMMAND_SWITCH = [0x01, 0x01, 0x01]

DEFAULT_RETRIES = 5

EFFECT_LIST = [
    Effect('Wave', 1),
    Effect('Phasing', 2),
    Effect('Fade away in phase', 4),
    Effect('Twinkling in phase', 8),
    Effect('Fade away', 16),
    Effect('Fast twinkling', 32),
    Effect('Stay on', 64)
]
