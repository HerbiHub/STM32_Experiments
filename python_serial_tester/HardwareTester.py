#!/usr/bin/env python

from serial import Serial, rs485
import serial
import time

from src.comm_protocol import Status, Parser, Baud

cmd_strings = [
    #"1,SLAV,HOST,STATUS,200,0x12345678,0x34F01C3C",
    "1,SLAV,HOST,BAUD,SET,9600,0x927C442",
    "1,SLAV,HOST,BAUD,GET,0xB0FFF347",
    "1,SLAV,HOST,RTC,GET,0x17B1EA77",
    #"1,HOST,SLAV,BAUD,SAY,9600,0xBA7CC691",
    "1,SLAV,HOST,BAUD,CLEAR,0x42D736CE",
    ]

#ser = Serial('/dev/ttyUSB0', baudrate=9600, parity = serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE)
#ser.rs485_mod = rs485.RS485Settings()
ser = rs485.RS485('/dev/ttyUSB0', baudrate=9600, parity = serial.PARITY_EVEN)
ser.timeout = 1

for cmd_str in cmd_strings:
    print()
    x = Parser(cmd_str).iparse()
    x.validate()
    print(x)
    ser.write((str(x)+"\n").encode("ASCII"))
    while 1:
        data = ser.read(200).decode('UTF-8','replace')
        if len(data) == 0:
            break
        for line in data.split("\n"):
            if len(line) == 0:
                break
            try:
                x = Parser(line).iparse()
                x.validate()
                #print("Data:",line)
                print(x)
            except:
                print("RAW:", line.encode('ASCII'))



exit()

#!/usr/bin/env python



commands = [
    "1,STM3,RASP,STATUS,SAY,0x12345678"
        ]

cur_command = 0

while 1:
    print(commands[cur_command])
    ser.write((commands[cur_command]+"\n").encode("ASCII"))
    data = ser.read(200)
    cur_command += 1
    cur_command %= len(commands)
    time.sleep(1)


print(ser.read(100))
exit()
