#!/usr/bin/env python
#coding=utf-8

import roslib
import rospy
from ros_arduino_msgs.srv import *
from math import pi as PI, degrees, radians

class Joint:

    def __init__(self,name,servoNum,max,min,servo_max,servo_min,inverse):
        self.name = name#关节名称
        self.servoNum = servoNum#对应舵机编号
        self.max = max#舵机做大角度
        self.min = min#舵机做小角度
        self.servo_max = servo_max
        self.servo_min = servo_min
        self.inverse = inverse

        self.position = 0.0
        self.velocity = 0.0
    
    def setCurrentPosition(self):

        rospy.wait_for_service('/arduino/servo_write')

        try:
            servo_write = rospy.ServiceProxy('arduino/servo_write',ServoWrite)
            servo_write(self.servoNum,self.position)
        except rospy.ServiceException as e:
            print("Service call failed:%s" % e)

    def setCurrentPosition(self,position):
        rospy.loginfo("wait for servo_write")
        rospy.wait_for_service('/arduino/servo_write')
        rospy.loginfo("start servo_write")

        try:
            #if self.servoNum == 2:
            servo_write = rospy.ServiceProxy('arduino/servo_write',ServoWrite)
            rospy.loginfo("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            rospy.loginfo("before mapping--- the servo id:"+str(self.servoNum)+" position is "+str(position))
            self.mapToServoPosition(position)
            rospy.loginfo("after mapping---- the servo id:"+str(self.servoNum)+" self.position is "+str(self.position))             
            servo_write(self.servoNum,radians(self.position))
            print("servo_write(" + self.servoNum + "," + radians(self.position) + ")")

        except rospy.ServiceException as e:
            print("Service call failed:%s" % e)

#将moveit中的角度转化为舵机实际控制的角度
    def mapToServoPosition(self,position):
        #rospy.loginfo("position before map")
        per=(position-self.min)/(self.max-self.min)
        if not self.inverse:            
            self.position=self.servo_min+per*(self.servo_max-self.servo_min)
        else:
            self.position=self.servo_max-per*(self.servo_max-self.servo_min)



