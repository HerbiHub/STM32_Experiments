
import zlib
import string

from . import CommBase

class Status(CommBase):
    

    def __init__(self, *args, **kwargs):
        # 1,<DEST>,<SOURCE>,STATUS,<STATUS_CODE>,<CRC_OLD>,<CRC>\n

        super().__init__(*args, **kwargs) 
        self.status_code = int(kwargs.get('status_code',200))
        self.crc_old = kwargs.get('crc_old',0)

    
    def str_stub(self):
        return f"{self.version},{self.destination},{self.source},STATUS,{self.status_code:0>3},{self.crc_old},"
    

    def validate(self):
        super().validate()
        # TODO: Finish validating status code and CRC values

        if self.status_code < 100 or self.status_code >= 600:
            raise ValueError(f"Invalid range of status code: {self.status_code}")

        if self.status_code not in [100,200,400,401,402,404,405,418,429,500]:
            raise ValueError(f"Invalid status code: {self.status_code}")

