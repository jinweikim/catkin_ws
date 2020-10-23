#!/usr/bin/env python
#coding=utf-8
import rospy
import copy
import math
from Robot import Robot


#屏幕类，用于记录屏幕信息
class Screen:

    origin = '' #the 
    width = 0 #屏幕宽度
    height = 0 #屏幕高度
    angle = 0 #屏幕与水平面的夹角

    def __init__(self, origin, width, height, angle):
        self.origin = origin
        self.width = width
        self.height = height
        self.angle = angle

    # #把二维坐标转化为三维坐标
    # def get_3D_position(position):



    # #计算出上一层屏幕中的坐标位置
    # def get_Up_3D_position(position):

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

    def getVerticalPos(self,distance):

        angle = self.roll

        x = self.x
        y = self.y - distance*math.sin(angle)
        z = self.z + distance*math.cos(angle)
        
        newPos = Position(x,y,z,self.roll,self.pitch,self.yaw)

        return newPos
    
    def getSwipePos(self,distance,direction):

        angle = math.pi/2 - self.roll

        if direction == "up":
            x = self.x
            y = self.y - distance*math.cos(angle)
            z = self.z + distance*math.sin(angle)

        if direction == "down":
            x = self.x
            y = self.y + distance*math.cos(angle)
            z = self.z - distance*math.sin(angle)

        if direction == "left":
            x = self.x + distance
            y = self.y
            z = self.z

        if direction == "right":
            x = self.x - distance
            y = self.y
            z = self.z


        newPos = Position(x,y,z,self.roll,self.pitch,self.yaw)

        return newPos

    def __str__(self):

        print "in tostring"

        return 'x: %s, y: %s,z: %s, roll: %s,pitch: %s, yaw: %s' % (self.x,self,y,self,z,self,roll,self,pitch,self.yaw)


class Rcs3D:
    
    #45度: 0.78535
    #screen = Screen(1,1,1,0.78535)

    #90度: 1.5707
    screen = Screen(1,1,1,1.5707)

    robot = Robot()

    def reset(self):
        self.robot.goHome()

    def click(self,point):

        print "in click"

        print "robot will click the point"

        print point

        #position = screen.get_3D_position(position)#获取三维坐标

        #up_position = screen.get_Up_3D_position(position)#获取上层三维坐标

        pos = self.point_to_position(point)

        up_pos = pos.getVerticalPos(0.02)#获取目标点正上方位置处一点

        self.robot.move(up_pos)#移动到目标上方位置

        print "move to up position"

#        old_pos = copy.deepcopy(pos)#深拷贝，避免引用同一对象

        self.robot.move(pos)#移动到目标位置

        print "move to position"

        self.robot.move(up_pos)#返回上方位置

        print "back to position"

    def hide(self):

        self.robot.move('hide')
        

    def double_click(self,position):

        position = screen.get_3D_position(position)#获取三维坐标

        up_position = screen.get_Up_3D_position(position)#获取上层三维坐标

        execute_result = robot.move(position)#移动到目标位置
        
        execute_result = robot.move(up_position)#移动到上一层位置

        execute_result = robot.move(position)#再一次移动到目标位置以实现双击

        robot.move('home')#返回初始位置


    def swipe(self,point,direction):

        pos = self.point_to_position(point)

        up_pos = pos.getVerticalPos(0.2)#获取目标点正上方位置处一点

        swipe_pos = pos.getSwipePos(0.2,direction)#获取滑动目的地坐标

        self.robot.move(up_pos)#移动到目标上方位置
        
        print "move to up position"

        self.robot.move(pos)#移动到目标位置

        print "move to position"

        self.robot.move(swipe_pos)#滑动

        print "start to swipe"

        up_swipe_pose = swipe_pos.getVerticalPos(0.2)#获取滑动目的地的上方位置

        self.robot.move(up_swipe_pose)


    def long_press(self,position,time):

        position = screen.get_3D_position(position)#获取三维坐标
        
        execute_result = robot.move(position)
        
        robot.long_press()

    def drag(self,start,end):

        position = screen.get_3D_position(start)#获取三维坐标
        
        execute_result = robot.move(start)
        
        robot.drag(end)

    def point_to_position(self,point):

        roll =  self.screen.angle#根据屏幕角度值计算roll值

        pos = Position(point[0],point[1],point[2],roll,0,0)#将point点变为带有rpy的position

        return pos

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

# print "in main"

# rcs3D = Rcs3D()

#90度
#pos = Position(0.6004,-0.6723,0.6489,1.5707,0,0)

#45度
#pos = Position(0.6004,-0.6723,0.6489,0.78535,0,0)

# point = [0.6004,-0.90,0.6489]
# point2 = [0,-0.9,0]
# rcs3D.click(point2)
#rcs3D.hide()
#rcs3D.swipe(point,'up')








