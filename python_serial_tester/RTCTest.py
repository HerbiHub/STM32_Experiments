#!/usr/bin/env python

from serial import Serial, rs485
import serial
import time
import datetime

from src.comm_protocol import Status, Parser, Baud, RTC

cmd_strings = [
    "1,SLAV,HOST,STATUS,200,0x12345678,0x34F01C3C",
    "1,SLAV,HOST,BAUD,SET,9600,0x927C442",
    "1,SLAV,HOST,BAUD,GET,0xB0FFF347",
    "1,SLAV,HOST,RTC,GET,0x17B1EA77",
    "1,HOST,SLAV,BAUD,SAY,9600,0xBA7CC691",
    "1,SLAV,HOST,BAUD,CLEAR,0x42D736CE",
    ]

#ser = Serial('/dev/ttyUSB0', baudrate=9600, parity = serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE)
#ser.rs485_mod = rs485.RS485Settings()
ser = rs485.RS485('/dev/ttyUSB0', baudrate=9600, parity = serial.PARITY_EVEN)
ser.timeout = 0.1

now = datetime.datetime.now()

cmd = RTC(verb='SET',year=now.year%100, month=now.month, day=now.day, hour=now.hour, minute=now.minute, second=now.second)
print(cmd)
ser.write((str(cmd)+"\n").encode("ASCII"))
while 1:
    data = ser.read(200)
    if len(data) == 0:
        break
    print(data.decode('UTF8'), end='')


cmd = RTC(verb='GET')
print(cmd)
ser.write((str(cmd)+"\n").encode("ASCII"))
while 1:
    data = ser.read(200)
    if len(data) == 0:
        break
    print(data.decode('UTF8'), end='')