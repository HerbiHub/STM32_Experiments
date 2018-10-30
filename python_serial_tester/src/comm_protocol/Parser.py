
import re

from . import Status

class Parser:

    def __init__(self, string):
        pass
        self.string = string


    def iparse(self):
        """Attempt to intelligently parse the saved string.
        """

        # 1,<DEST>,<SOURCE>,STATUS,<STATUS_CODE>,<CRC_OLD>,<CRC>\n
        regex_object = re.match(r"""
            (?P<version>\d+),
            (?P<destination>[a-zA-Z0-9]{4}),
            (?P<source>[a-zA-Z0-9]{4}),
            STATUS,
            (?P<status_code>[^,\n]+),
            (?P<crc_old>[^,\n]+)
            (,(?P<crc>[^,\n]+))?
            """,
            self.string,
            re.X)
        if regex_object:
            d = regex_object.groupdict()
            print(d)
            return Status(version = d['version'],
                          destination = d['destination'],
                          source = d['source'],
                          status_code = d['status_code'],
                          crc_old = d['crc_old'],
                          crc = d['crc'],
                          )

