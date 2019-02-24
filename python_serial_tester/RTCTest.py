#!/usr/bin/env python

from serial import Serial, rs485
import serial
import time
import datetime
import re

from src.comm_protocol import Status, Parser, Baud, RTC

SynchPrediv = 625

ser = Serial('/dev/ttyUSB0', baudrate=9600, parity = serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE)
#ser.rs485_mod = rs485.RS485Settings()
#ser = rs485.RS485('/dev/ttyUSB0', baudrate=9600, parity = serial.PARITY_EVEN)
ser.timeout = 1

now = datetime.datetime.now()
start =  datetime.datetime.now()

cmd = RTC(verb='SET',year=now.year%100, month=now.month, day=now.day, hour=now.hour, minute=now.minute, second=now.second)
print(cmd)
ser.write((str(cmd)+"\n").encode("ASCII"))
while 1:
    data = ser.read(200)
    if len(data) == 0:
        break
    print(data.decode('UTF8'), end='')


while 1:
    cmd = RTC(verb='GET')
    ser.write((str(cmd)+"\n").encode("ASCII"))
    now = datetime.datetime.now().replace(microsecond=0)
    t0 = time.time()
    data = ser.read(200)
    t1 = time.time()
    print(t1-t0)
    for line in data.split(b'\n'):
        response = Parser(line.decode('UTF-8')).iparse()
        print("Line:", line)
        print(response)
    time.sleep(1)




while 1:
    cmd = RTC(verb='GET')
    ser.write((str(cmd)+"\n").encode("ASCII"))
    now = datetime.datetime.now().replace(microsecond=0)
    data = ser.read(200)
    match_obj = re.search(b"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})",data)
    if match_obj:
        #print(match_obj.group(0))
        stm32 = datetime.datetime.strptime(match_obj.group(0).decode('UTF-8'), "%Y-%m-%d %H:%M:%S")
        duration = (now - start).total_seconds()
        offset = (now - stm32).total_seconds()
        mul_ratio = offset/duration
        print(f"{-mul_ratio*1e6:.20f} ({(1-mul_ratio) * SynchPrediv:.1f})  {offset:.0f} {duration:,.0f} stm: {stm32} sys: {now}")
    #print(data.decode('UTF8'), end='')
    #print(datetime.datetime.now())
    time.sleep(10)
