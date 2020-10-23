#!/usr/bin/env python
#coding=utf-8
from Robot import Robot 
import time
   


class RcsTest:


    robot = Robot()
    def __init__(self):
        print("init Rcs Test")


rt = RcsTest()
point = [0.035,0.074,0.435]
print("import")

from Rcs3D import Rcs3D
print("init Rcs3D")
rcs3d = Rcs3D()
rcs3d.click(point)
#rcs3d.reset()
# rcs3d.click(point)
# rcs3d.reset()
#rt.repeatMoveTest(pos,1)

