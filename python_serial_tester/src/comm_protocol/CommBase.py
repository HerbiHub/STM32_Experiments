

import abc
import string
import zlib
from ..crc32 import stm32_crc32

class CommBase(abc.ABC):


    def __init__(self, *args, **kwargs):
        self.version = kwargs.get('version', 1)
        self.source = kwargs.get('source','0000')
        self.destination = kwargs.get('destination','0000')
        if 'crc' in kwargs and kwargs['crc'] is not None:
            self._crc = int(kwargs['crc'], 16)
        else:
            self._crc = None


    def __str__(self):
        if self._crc:
            return f"{self.str_stub()}0x{self._crc:X}"
        else:
            return f"{self.str_stub()}0x{self.crc:X}"


    @property
    def crc(self):
        crc = 0xFFFFFFFF
        for c in self.str_stub().encode('ASCII'):
            crc = stm32_crc32(c, crc)
        return crc
        # return f"0x{(zlib.crc32(self.str_stub().encode('ASCII')) & 0xFFFFFFFF):X}"


    @abc.abstractmethod
    def str_stub(self):
        """Sublcasses will produce a sub string for use in other class methods.
        """


    @abc.abstractmethod
    def validate(self):
        """Validate all current values, raise Value/Type errors when they are detected.
        """
        if int(self.version) != 1:
            raise ValueError(f"Invalid version detected: {self.version}")

        valid_address_chars = string.digits + string.ascii_letters

        for c in self.destination:
            if c not in valid_address_chars:
                raise ValueError(f"Invalid address character in destination: {c} in {self.destination}")
        if len(self.destination) != 4:
            raise ValueError(f"Invalid length of destination: {len(self.destination)}")

        for c in self.source:
            if c not in valid_address_chars:
                raise ValueError(f"Invalid address character in source: {c} in {self.source}")
        if len(self.source) != 4:
            raise ValueError(f"Invalid length of source: {len(self.source)}")

        if self._crc is not None:
            if self._crc != self.crc:
                raise ValueError(f"Invalid manual CRC: 0x{self._crc:X} is not 0x{self.crc:X}")



