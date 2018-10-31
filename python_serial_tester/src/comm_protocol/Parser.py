
import re

from . import Status
from . import Baud

class Parser:

    def __init__(self, string):
        pass
        self.string = string


    def iparse(self):
        """Attempt to intelligently parse the saved string.
        """
        # Status Code
        regex_object = re.match(r"""
            (?P<version>\d+),
            (?P<destination>[a-zA-Z0-9]{4}),
            (?P<source>[a-zA-Z0-9]{4}),
            STATUS,
            (?P<status_code>[^,\n]+),
            (?P<crc_old>0x[^,\n]+)
            (,(?P<crc>0x[^,\n]+))?
            """,
            self.string,
            re.X)
        if regex_object:
            d = regex_object.groupdict()
            return Status(version = d['version'],
                          destination = d['destination'],
                          source = d['source'],
                          status_code = d['status_code'],
                          crc_old = d['crc_old'],
                          crc = d['crc'],
                          )

        # Baud Rate
        regex_object = re.match(r"""
            (?P<version>\d+),
            (?P<destination>[a-zA-Z0-9]{4}),
            (?P<source>[a-zA-Z0-9]{4}),
            BAUD,
            (?P<verb>GET|SET|SAY|CLEAR)
            (,(?P<baud>[0-9]{2,}))?
            (,(?P<crc>0x[^,\n]+))?
            """,
            self.string,
            re.X)
        if regex_object:
            d = regex_object.groupdict()
            return Baud(version = d['version'],
                          destination = d['destination'],
                          source = d['source'],
                          baud = d['baud'],
                          verb = d['verb'],
                          crc = d['crc'],
                          )

