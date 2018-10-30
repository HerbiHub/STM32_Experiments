
import zlib
import string

from . import CommBase

class Baud(CommBase):
    

    def __init__(self, *args, **kwargs):
        # 1,<DEST>,<SOURCE>,STATUS,<STATUS_CODE>,<CRC_OLD>,<CRC>\n
        # 1,<DEST>,<SOURCE>,BAUD,SET,<BAUD>,<CRC>\n
        # 1,<DEST>,<SOURCE>,BAUD,GET,<CRC>\n
        # 1,<DEST>,<SOURCE>,BAUD,SAY,<BAUD>,<CRC>\n
        # 1,<DEST>,<SOURCE>,BAUD,CLEAR,<CRC>\n

        super().__init__(*args, **kwargs) 
        self.verb = kwargs.get('verb')
        self.baud = kwargs.get('baud')

    
    def str_stub(self):
        ret_str = f"{self.version},{self.destination},{self.source},BAUD,{self.verb}"
        if self.verb in ["SET","SAY"]:
            ret_str += f",{self.baud}"
        return ret_str

    

    def validate(self):
        super().validate()
        # TODO: Finish validating status code and CRC values

        standard_baud_rates = [110, 300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 38400, 57600, 115200, 128000, 256000]

        if self.verb == "SET":
            if self.baud == None:
                raise ValueError(f"Invalid missing argument 'baud'")
            if int(self.baud) not in standard_baud_rates:
                raise ValueError(f"Invalid baud rate: {self.baud}")

        elif self.verb == "GET":
            if self.baud != None:
                raise ValueError(f"Invalid argument 'baud': {self.baud}")

        elif self.verb == "SAY":
            if self.baud == None:
                raise ValueError(f"Invalid missing argument 'baud'")
            if int(self.baud) not in standard_baud_rates:
                raise ValueError(f"Invalid baud rate: {self.baud}")
                
        elif self.verb == "CLEAR":
            if self.baud != None:
                raise ValueError(f"Invalid argument 'baud': {self.baud}")

