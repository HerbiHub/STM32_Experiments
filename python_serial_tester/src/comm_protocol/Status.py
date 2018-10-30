
import zlib

from . import CommBase

class Status(CommBase):
    

    def __init__(self, *args, **kwargs):
        # 1,<DEST>,<SOURCE>,STATUS,<STATUS_CODE>,<CRC_OLD>,<CRC>\n

        super().__init__(*args, **kwargs) 
        self.status_code = kwargs.get('status_code',200)
        self.crc_old = kwargs.get('crc_old',0)


    def __str__(self):
        return f"{self.__str_stub()},{self.crc}\n"

    
    def __str_stub(self):
        return f"{self.version},{self.destination},{self.source},STATUS,{self.status_code:0>3},{self.crc_old}"


    @property 
    def crc(self):
        return hex(zlib.crc32(self.__str_stub().encode('ASCII')) & 0xFFFFFFFF)


