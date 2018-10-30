#!/usr/bin/env python

import src.comm_protocol.Status as Status

from src.comm_protocol import Status, Parser

x = Parser("1,YOUa,MEME,STATUS,045,0x12345678,0xf70da055\n").iparse()
x.validate()
print(x)
print(type(x))




