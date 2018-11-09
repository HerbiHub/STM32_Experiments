#!/usr/bin/env python

# Echo any serial commands recieved 

import serial
from serial import rs485

# Config pyserial

# ser = serial.Serial('/dev/ttyUSB0',
# 	230400,
# 	bytesize=serial.EIGHTBITS,
# 	# parity = serial.PARITY_EVEN,
# 	stopbits = serial.STOPBITS_ONE)
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0,
                    parity='N', stopbits=2)
# ser.rs485_mode=serial.rs485.RS485Settings()
ser.write(b'hello')
# print(ser)
