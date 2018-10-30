
import zlib

from . import CommBase

class Status(CommBase):
    

    def __init__(self, *args, **kwargs):
        # 1,<DEST>,<SOURCE>,STATUS,<STATUS_CODE>,<CRC_OLD>,<CRC>\n

        super().__init__(*args, **kwargs) 
        self.status_code = kwargs.get('status_code',200)
        self.crc_old = kwargs.get('crc_old',0)

    
    def str_stub(self):
        return f"{self.version},{self.destination},{self.source},STATUS,{self.status_code:0>3},{self.crc_old}"

    


