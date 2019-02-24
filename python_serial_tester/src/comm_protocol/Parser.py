
import re

from . import Baud, Dimmer, Status, RTC

class Parser:

    def __init__(self, string):
        pass
        self.string = string


    def iparse(self):
        """Attempt to intelligently parse the saved string.
        """

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

        # Dimmer Rate
        regex_object = re.match(r"""
            (?P<version>\d+),
            (?P<destination>[a-zA-Z0-9]{4}),
            (?P<source>[a-zA-Z0-9]{4}),
            DIMMER,
            (?P<verb>GET|SET|SAY|CLEAR)
            (,(?P<channel>[0-9]{1,3}(?!x)))? # Checkout that negative lookahead!
            (,(?P<setting>[0-9]{1,3}(?!x)))?
            (,(?P<crc>0x[^,\n]+))?
            """,
            self.string,
            re.X)
        if regex_object:
            d = regex_object.groupdict()
            return Dimmer(version = d['version'],
                          destination = d['destination'],
                          source = d['source'],
                          verb = d['verb'],
                          channel = d['channel'],
                          setting = d['setting'],
                          crc = d['crc'],
                          )

        # Status Code
        regex_object = re.match(r"""
            (?P<version>\d+),
            (?P<destination>[a-zA-Z0-9]{4}),
            (?P<source>[a-zA-Z0-9]{4}),
            STATUS,
            (?P<status_code>[^,\n]+),
            (?P<crc_old>0x[^,\n]+),
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

        # RTC Code
        regex_object = re.match(r"""
            (?P<version>\d+),
            (?P<destination>[a-zA-Z0-9]{4}),
            (?P<source>[a-zA-Z0-9]{4}),
            RTC,
            (?P<verb>GET|SET|SAY|CLEAR)
            (,(?P<year>[^,\n]+))?
            (,(?P<month>[^,\n]+))?
            (,(?P<day>[^,\n]+))?
            (,(?P<hour>[^,\n]+))?
            (,(?P<minute>[^,\n]+))?
            (,(?P<second>[^,\n]+))?
            (,(?P<crc>0x[^,\n]+))?
            """,
            self.string,
            re.X)
        if regex_object:
            d = regex_object.groupdict()
            return RTC(version = d['version'],
                       destination = d['destination'],
                       source = d['source'],
                       verb = d['verb'],
                       year = d['year'],
                       month = d['month'],
                       day = d['day'],
                       hour = d['hour'],
                       minute = d['minute'],
                       second = d['second'],
                       crc = d['crc'],
                       )

