
import zlib
import string

from . import CommBase

class Dimmer(CommBase):
    

    def __init__(self, *args, **kwargs):
        # 1,<DEST>,<SOURCE>,DIMMER,CLEAR,<CHANNEL>,<CRC>\n
        # 1,<DEST>,<SOURCE>,DIMMER,GET,<CHANNEL>,<CRC>\n
        # 1,<DEST>,<SOURCE>,DIMMER,SAY,<CHANNEL>,<SETTING>,<CRC>\n
        # 1,<DEST>,<SOURCE>,DIMMER,SET,<CHANNEL>,<SETTING>,<CRC>\n

        super().__init__(*args, **kwargs) 
        self.verb = kwargs.get('verb')

        try:
            self.channel = int(kwargs.get('channel'))
        except TypeError:
            self.channel = None

        try:
            self.setting = int(kwargs.get('setting'))
        except TypeError:
            self.setting = None

    
    def str_stub(self):
        ret_str = f"{self.version},{self.destination},{self.source},DIMMER,{self.verb}"
        if self.verb == 'CLEAR':
            pass
        elif self.verb == 'GET':
            pass
        elif self.verb == 'SAY':
            ret_str += f",{self.channel},{self.setting}"
        elif self.verb == 'SET':
            ret_str += f",{self.channel},{self.setting}"
        return ret_str


    def validate(self):
        super().validate()
        # TODO: Finish validating status code and CRC values

        if self.channel != None:
            if self.channel < 0 or self.channel > 16:
                raise ValueError(f"Invalid channel range: {self.channel}")

        if self.setting != None:
            if self.setting < 0 or self.setting > 255:
                raise ValueError(f"Invalid setting range: {self.setting}")


        if self.verb == 'CLEAR':
            if self.setting is not None:
                raise ValueError(f"Invalid setting {self.setting} for verb CLEAR")
        elif self.verb == 'GET':
            if self.setting is not None:
                raise ValueError(f"Invalid setting {self.setting} for verb GET")
        elif self.verb == 'SAY':
            if self.setting is None:
                raise ValueError(f"Invalid setting {self.setting} for verb SAY")
            if self.channel is None:
                raise ValueError(f"Invalid channel {self.channel} for verb SAY")
        elif self.verb == 'SET':
            if self.setting is None:
                raise ValueError(f"Invalid setting {self.setting} for verb SET")
            if self.channel is None:
                raise ValueError(f"Invalid channel {self.channel} for verb SET")
