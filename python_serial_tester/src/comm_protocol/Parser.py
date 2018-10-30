
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
            (?P<destination>.{4}),
            (?P<source>.{4}),
            STATUS,
            (?P<status_code>.+),
            (?P<crc_old>.+),
            (?P<crc>.+)
            """,
            self.string,
            re.X)
        if regex_object:
            print("Found a Status message")
            d = regex_object.groupdict()
            print(d)
            return Status(version = d['version'],
                          destination = d['destination'],
                          source = d['source'],
                          status_code = d['status_code'],
                          crc_old = d['crc_old'])

