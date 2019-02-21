#!/usr/bin/env python

import zlib
from src.crc32 import stm32_crc32


x = b'1'

crc = 0xFFFFFFFF

for b in x:
    #crc = zlib.crc32(b,crc)
    crc = stm32_crc32(b, crc)
crc = crc & 0xFFFFFFFF
print( f"0x{crc:X}" ) 

x = b'1'
crc = 0xFFFFFFFF
for b in x:
    print(b, crc)
    crc = ~zlib.crc32(bytes([b]), crc)
    #crc = stm32_crc32(b, crc)
crc = crc & 0xFFFFFFFF
print( f"0x{crc:X}" ) 

