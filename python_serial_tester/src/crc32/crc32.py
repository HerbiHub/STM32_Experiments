#!/usr/bin/env python

def stm32_crc32(data, crc):
    crc = crc ^ data
    for i in range(0, 32):
        if crc & 0x80000000:
            crc = ((crc << 1) ^ 0x04C11DB7) & 0xFFFFFFFF  # Polynomial used in STM32
        else:
            crc = (crc << 1) & 0xFFFFFFFF
    return crc
