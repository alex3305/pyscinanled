import logging
import time

from .const import CHAR_START_HANDLE, CHAR_END_HANDLE, CHAR_UUID
from bluepy.btle import UUID, Peripheral, BTLEException

_LOGGER = logging.getLogger(__name__)


class BtleConnection:

    def __init__(self, mac: str, retries: int):
        self._mac = mac
        self._device = None
        self._characteristic = None
        self._retries = retries
        return

    def connect(self, retry_count: int = 0):
        if retry_count > self._retries:
            raise TimeoutError('Could not reach device ' + self._mac)

        try:
            self._device = Peripheral()
            self._device.connect(self._mac)
            self._characteristic = self._device.getCharacteristics(
                CHAR_START_HANDLE, CHAR_END_HANDLE, UUID(CHAR_UUID))[0]
        except BTLEException:
            _LOGGER.warning("Could not connect to %s, retrying...")
            time.sleep(1)
            self.connect(retry_count + 1)

    def disconnect(self):
        self._device.disconnect()
        self._device = None
        self._characteristic = None

    def send_command(self, command):
        self._characteristic.write(bytearray(command))
