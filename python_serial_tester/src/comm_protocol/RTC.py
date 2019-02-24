
import zlib
import string

from . import CommBase

class RTC(CommBase):
    

    def __init__(self, *args, **kwargs):
        # 1,<DEST>,<SOURCE>,RTC,<VERB>,<CRC>\n
        super().__init__(*args, **kwargs) 
        self.verb = kwargs.get('verb')
        self.year = kwargs.get('year',0)
        self.month = kwargs.get('month',0)
        self.day = kwargs.get('day',0)
        self.hour = kwargs.get('hour',0)
        self.minute = kwargs.get('minute',0)
        self.second = kwargs.get('second',0)

    
    def str_stub(self):
        if self.verb in ['SET','SAY']:
            return f"{self.version},{self.destination},{self.source},RTC,{self.verb},{self.year},{self.month},{self.day},{self.hour},{self.minute},{self.second},"
        elif self.verb in ['GET','CLEAR']:
            return f"{self.version},{self.destination},{self.source},RTC,{self.verb},"
        else:
            raise ValueError()


    def validate(self):
        super().validate()
        # TODO: Finish validating status code and CRC values
        return True
