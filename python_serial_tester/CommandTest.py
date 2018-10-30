#!/usr/bin/env python

# import src.comm_protocol.Status as Status

from src.comm_protocol import Status, Parser, Baud

x = Parser("1,SLAV,HOST,STATUS,200,0x12345678,0x6ed95d53\n").iparse()
x.validate()
print(x)



print()
y = Parser("1,SLAV,HOST,BAUD,GET,0xbd05806e\n").iparse()
y.validate()
print(y)
print()
y = Parser("1,SLAV,HOST,BAUD,SET,9600,0xf2434f96\n").iparse()
y.validate()
print(y)

print()
y = Parser("1,SLAV,HOST,BAUD,SAY,9600,0xba92785b\n").iparse()
y.validate()
print(y)

print()
y = Parser("1,SLAV,HOST,BAUD,CLEAR,0xae740462\n").iparse()
y.validate()
print(y)


