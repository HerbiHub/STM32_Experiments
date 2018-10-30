
import zlib

class CommBase:

    def __init__(self, *args, **kwargs):
        self.version = kwargs.get('version', 1)
        self.source = kwargs.get('source','0000')
        self.destination = kwargs.get('destination','0000')
        self._crc = kwargs.get('crc',None)


    def __str__(self):
        raise NotImplementedError

    
    def __str_stub(self):
        raise NotImplementedError

    
    @property
    def crc(self):
        raise NotImplementedError

