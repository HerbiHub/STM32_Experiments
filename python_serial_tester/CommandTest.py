#!/usr/bin/env python

import src.comm_protocol.Status as Status

from src.comm_protocol import Status, Parser

x = Parser("1,SLAV,HOST,STATUS,200,0x12345678,0x6ed95d53\n").iparse()
x.validate()
print(x)



print()
y = Parser("1,SLAV,HOST,STATUS,200,0x12345678\n").iparse()
y.validate()
print(y)

