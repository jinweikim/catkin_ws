#!/usr/bin/env python
#coding=utf-8
from Robot import Robot
import time

class RobotTest:

    robot = Robot()

    # def repeatMoveTest(self,position,times):

    #     for i in range(times):
    #         self.robot.goHome()
    #         time.sleep(3)
    #         posUp = Position(position.x,position.y,position.z,0,0,0)
    #         self.robot.move(posUp)
    #         time.sleep(3)
    #         self.robot.move(position)
    #         time.sleep(3)
    #         self.robot.move(posUp)
    #     self.robot.goHome()


from Rcs3D import Position,Rcs3D

rt = RobotTest()
point = [0.198,0.06,0.18]
rcs3d = Rcs3D()
rcs3d.reset()
rcs3d.click(point)
rcs3d.reset()
#rt.repeatMoveTest(pos,1)

