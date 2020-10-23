#!/usr/bin/env python
#coding=utf-8
from moveit_interface.srv import RobotControl,RobotControlResponse
import rospy
from Robot import *

class Position:

    x = 0.0
    y = 0.0
    z = 0.0

    #rpy
    roll = 0.0
    pitch = 0.0
    yaw = 0.0

    def __init__(self,x,y,z,roll,pitch,yaw):

        self.x = x
        self.y = y
        self.z = z

        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw

    def setX(self,x):
        self.x = x

    def setY(self,y):
        self.y = y

    def setZ(self,z):
        self.z = z

    def setRoll(self,roll):
        self.roll = roll

    def setPitch(self,pitch):
        self.pitch = pitch

    def setYaw(self,yaw):
        self.yaw = yaw

# 回调函数
def handle_robot_control(req):
    print("handling robot control")
    print("x: %s y: %s,z: %s"%(req.x,req.y,req.z))
    print("roll: %s pitch: %s,yaw: %s"%(req.roll,req.pitch,req.yaw))
    position = Position(req.x,req.y,req.z,req.roll,req.pitch,req.yaw)
    robot.move(position)
    return RobotControlResponse(True);

def robot_control_server():
    print "in server"
    rospy.init_node('robot_control_server')
    s = rospy.Service('robot_control',RobotControl,handle_robot_control)
    print("Ready to control robot")
    rospy.spin()

if __name__ == '__main__':
    print "in main"
    robot_control_server();
robot_control_server()
