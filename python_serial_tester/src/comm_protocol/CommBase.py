

import abc
import zlib

class CommBase(abc.ABC):

    def __init__(self, *args, **kwargs):
        self.version = kwargs.get('version', 1)
        self.source = kwargs.get('source','0000')
        self.destination = kwargs.get('destination','0000')
        self._crc = kwargs.get('crc',None)


    def __str__(self):
        if self._crc:
            return f"{self.str_stub()},{self._crc}"
        else:
            return f"{self.str_stub()},{self.crc}"

    @abc.abstractmethod
    def str_stub(self):
        """Sublcasses will produce a sub string for use in other class methods.
        """
    
    @property
    def crc(self):
        return hex(zlib.crc32(self.str_stub().encode('ASCII')) & 0xFFFFFFFF)

