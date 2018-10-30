#!/usr/bin/env python

import src.comm_protocol.Status as Status


x = Status(destination="YOUa", source="MEME", old_crc = "0x12345678", status_code = 45)
print(x,end="")

