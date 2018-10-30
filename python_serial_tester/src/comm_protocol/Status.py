

from . import CommBase

class Status(CommBase):
    

    def __init__(self, *args, **kwargs):
        # 1,<DEST>,<SOURCE>,STATUS,<STATUS_CODE>,<CRC_OLD>,<CRC>\n

        super().__init__(*args, **kwargs) 
        self.status_code = kwargs.get('status_code',200)
        self.old_crc = kwargs.get('old_crc',0)

    def __str__(self):
        return f"{self.version},{self.destination},{self.source},STATUS,{self.status_code:03},{self.old_crc},{self.crc}\n"
