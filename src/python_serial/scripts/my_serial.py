#!/usr/bin/env python
import serial
import time

port = "/dev/ttyUSB0"
bps = 9600
timex = 0.5

ser = serial.Serial(port,bps,timeout=timex)

send_data = '5555080301000001C802'.decode('hex')
ser.write(send_data)
time.sleep(0.1)
