#!/usr/bin/env python
#coding=utf-8
import serial
import time
import math
class Traj:

    global ser

    def __init__(self,time,desired):
        self.time = time
        self.desired = desired

        portx = "/dev/ttyUSB0"

        bps = 9600

        timex = 5

        global ser
        # ser = serial.Serial(portx, bps, timeout=timex)


    def goto(self,serial_data):

        try:

            #    port = "/dev/ttyUSB0"

            # print(ser.port)  # 获取到当前打开的串口名
            # print(ser.baudrate)  # 获取波特率

            # 55 55 08 03 01 00 00 01 C8 02
            # 55 55 08 03 01 00 00 01 B2 02
            # 55 55 08 03 01 00 00 01 7C 03
            #d = bytes.fromhex(serial_data) python3
            send_data = serial_data.replace(' ','').decode('hex')

            print(send_data)
            result = ser.write(send_data)

            print("写总字节数:", result)


        except Exception as e:
            print("---异常---", e)


    def trajToSerial(self):
        # print("数组长度")
        # print(len(self.desired))

        cmd_length = len(self.desired)*3 + 5#数据长度等于控制舵机个数+5

        cmd_length = self.addZero(cmd_length)

        servoNum = self.addZero(len(self.desired))#控制舵机数量

        #print('舵机数量'+servoNum)


        highTime,lowTime = self.splitData(self.time)
        #print('地位时间' + lowTime)
        #print('高位时间' + highTime)
        serial_data = '55 55 '+ cmd_length + ' 03 ' + servoNum + ' ' + self.addZero(lowTime) + ' ' + self.addZero(highTime)


        for i in range(int(servoNum)):
            highAngle, lowAngle = self.splitData(self.desired[i])
            servoId = self.addZero(i+1)
            serial_data = serial_data + ' ' + servoId + ' ' + self.addZero(lowAngle) + ' ' + self.addZero(highAngle)

        print('发送的数据为: '+serial_data)

        return serial_data



#传入十进制数据，返回十六进制数据的高8位与地8位
    def splitData(self,source):

        #hexData = hex(source)

        #print(hexData)

        hexHigh= hex(source >> 8).lstrip('0x')
        hexLow = hex(source).lstrip('0x')

        hexHigh = self.addZero(hexHigh)

        if(len(hexLow)<2):
            hexLow = '0'+hexLow
        else:
            hexLow = hexLow[-2:]#取倒数两位

        # print("high: ",end="")
        # print(hexHigh)
        # print("low: ",end="")
        # print(hexLow)

        return hexHigh,hexLow

    def addZero(self,source):

        result = str(source)

        if(len(result) < 2):
            result = '0' + result

        return result

    @staticmethod   
    def send_to_sra(startJoints, endJoints):
        
        res = 'go'

        for sj in startJoints:
            res += ' '
            res += str(round(sj*180/math.pi,2))


        for ej in endJoints:
            res += ' '
            res += str(round(ej*180/math.pi,2))

        print(res)

        send_data = res.encode('ascii')

        portx = "/dev/ttyUSB0"

        bps = 9600

        timex = 5

        ser = serial.Serial(portx, bps, timeout=timex)

        bytes_num = ser.write(send_data)
        time.sleep(1)
        bytes_num = ser.write(send_data)
        ser.close()
        
        print("total bytes")
        print(bytes_num)


    def close(self):
        global ser
        ser.close()




#1264,1084,1803,1556,1846,1500
#desried = [1500,1500,1500,1500,1500,1500]
#traj = Traj(200,desried)
#serial_data = traj.trajToSerial()
#traj.goto(serial_data)














