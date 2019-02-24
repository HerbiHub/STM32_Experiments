#!/usr/bin/env python

# import src.comm_protocol.Status as Status

from src.comm_protocol import Parser

cmd_strings = [
    "1,SLAV,HOST,STATUS,200,0x12345678,0x34F01C3C",
    "1,SLAV,HOST,BAUD,SET,9600,0x927C442",
    "1,SLAV,HOST,BAUD,GET,0xB0FFF347",
    "1,SLAV,HOST,RTC,GET,0x17B1EA77",
    "1,HOST,SLAV,BAUD,SAY,9600,0xBA7CC691",
    "1,SLAV,HOST,BAUD,CLEAR,0x42D736CE",
    "1,HOST,SLAV,RTC,SAY,0,0,0,0,0,0,0xA36E2DB2",
    ]

for cmd_str in cmd_strings:
    print()
    x = Parser(cmd_str).iparse()
    print(x,hex(x.crc))
    x.validate()
    print(cmd_str)
    print(x)
    print(type(x))
exit()
