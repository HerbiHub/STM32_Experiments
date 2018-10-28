#!/usr/bin/env python

# Echo any serial commands recieved 

import serial

# Config pyserial

ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/FIXME' # TODO: Support windows as well
#ser.bytesize = 8
#ser.parity = 'N'
#ser.stopbits = 1
ser.timeout = 0 
