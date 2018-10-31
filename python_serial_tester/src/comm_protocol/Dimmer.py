
import zlib
import string

from . import CommBase

class Dimmer(CommBase):
    

    def __init__(self, *args, **kwargs):
        # 1,<DEST>,<SOURCE>,DIMMER,<VERB>,<CHANNEL>,<SETTING>,<CRC>\n

        super().__init__(*args, **kwargs) 
        self.verb = kwargs.get('verb')
        self.channel = kwargs.get('channel')
        self.setting = kwargs.get('setting')

    
    def str_stub(self):
        ret_str = f"{self.version},{self.destination},{self.source},DIMMER,{self.verb},"
        if self.verb == 'SAY':
        elif self.verb == 'SAY':
        elif self.verb == 'SAY':
        elif self.verb == 'SAY':


    def validate(self):
        super().validate()
        # TODO: Finish validating status code and CRC values

        if self.status_code < 100 or self.status_code >= 600:
            raise ValueError(f"Invalid range of status code: {self.status_code}")

        if self.status_code not in [100,200,400,401,402,404,405,418,429,500]:
            raise ValueError(f"Invalid status code: {self.status_code}")

