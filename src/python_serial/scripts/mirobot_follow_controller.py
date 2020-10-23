#!/usr/bin/env python3
#coding=utf-8

import rospy, actionlib

from control_msgs.msg import FollowJointTrajectoryAction
from trajectory_msgs.msg import JointTrajectory
from diagnostic_msgs.msg import *
import sensor_msgs.msg
from math import pi as PI, degrees, radians
from joints import Joint 
from listenSerial import Traj
import serial
import time
import os
from mirobot import Mirobot

class FollowController:

    def __init__(self,name):

        self.name = name

        rospy.loginfo("controller init")

        print("controller init")

        rospy.init_node(self.name)

        portx = "/dev/ttyUSB0"

        bps = 115200

        timex = 5

        self.ser = serial.Serial(portx, bps, timeout=timex)

        # self.ser.open()

        self.rate = 50.0

        time.sleep(0.1)

        m = Mirobot(portname="/dev/ttyUSB0",debug=True)

        m.home_simultaneous()

        # self.homing()

        print("ready for register follow_Controller")


        self.server = actionlib.SimpleActionServer('arm_controller/follow_joint_trajectory', FollowJointTrajectoryAction, execute_cb=self.actionCb, auto_start=False)
        self.server.start()
        rospy.spin() 
        rospy.loginfo("Started FollowController")

        

        print("Started FollowController")
    
    def actionCb(self,goal):

        print("**************actionCb**************")

        rospy.loginfo(self.name + ":Action goal received")
        traj = goal.trajectory

        # if set(self.joints) != set(traj.joint_names):
        #     print set(self.joints)
        #     print set(traj.joint_names)
        #     print "self.joints"
        #     for j in self.joints:
        #         print j.name
        #         if j.name not in traj.joint_names:
        #             msg = "Trajectory joint names does not match action controlled joints." + str(traj.joint_names)
        #             rospy.logerr(msg)
        #             self.server.set_aborted(text=msg)
        #             return
            
        #     print "traj.joint_names"    
        #     print traj.joint_names

        #     rospy.logwarn("Extra joints in trajectory")

        if not traj.points:
            msg = "Trajectory empty"
            rospy.loginfo(msg)
            self.server.set_aborted(text=msg)
            return 
        
        # try: 
        #     indexs = [traj.joint_names.index(joint.name) for joint in self.joints]

        # except ValueError as val:

        #     msg = "Trajectory invalid"
        #     rospy.loginfo(msg)
        #     self.server.set_aborted(text=msg)
        #     return 

        if self.executeTrajectory(traj):
            self.server.set_succeeded()
        else:
            self.server.set_aborted(text="Execution failed")

        rospy.loginfo(self.name + ":Done")


    def executeTrajectory(self,traj):
        rospy.loginfo("Executing trajectory")
        rospy.logdebug(traj)

        pub = rospy.Publisher('/joint_states',sensor_msgs.msg.JointState,queue_size=1)

        jointsCurrent = sensor_msgs.msg.JointState()

        print(traj)

        start = traj.header.stamp

        if start.secs == 0 and start.nsecs == 0:
            start = rospy.Time.now()

        r = rospy.Rate(self.rate)

        # points_len = len(traj.points)

        # start_point = traj.points[0] #get the start point
        # end_point = traj.points[points_len-1] # get the end point

        # start_joints = [start_point.positions[k] for k in indexes] # get the start joints
        # end_joints = [end_point.positions[k] for k in indexes] # get the end joints


        for point in traj.points:

            pos = point.positions

            # construct the joint_state to publish 
            for i in range(6):
                
                jointsCurrent.header.stamp= rospy.Time.now()
                jointsCurrent.name.append(traj.joint_names[i])
                rospy.loginfo('jointsCurrent.name')
                rospy.loginfo(traj.joint_names[i])
                jointsCurrent.position.append(pos[i])
                rospy.loginfo('jointsCurrent.position')
                rospy.loginfo(pos[i])

            pub.publish(jointsCurrent)

            self.send_data(pos)

            while rospy.Time.now() + rospy.Duration(0.01) < start:
                rospy.sleep(0.01)
        
        return True

    def send_data(self,positions):

        # the data to send
        data = 'M21 G90 G01'

        flag = ['X','Y','Z','A','B','C','F2000']
        
        for i in range(6):
            data = data + ' ' + flag[i]
            data += str(round(positions[i] * 57.296,2))

        data += ' ' + flag[6] + '\r\n'
        
        print(data)

        send_data = data.encode('ascii')      

        bytes_num = self.ser.write(send_data)
        #time.sleep(1)
        #bytes_num = self.ser.write(send_data)
        
        print("total bytes")
        print(bytes_num)

        #time.sleep(2)
        # count = self.ser.inWaiting()
        # if count > 0:
        #     data = self.ser.read(count)
        #     print data

    def homing(self):

        msg = '$H'
        msg = msg.strip()
        msg += os.linesep

        #data_m50 = 'M50\n'

        self.ser.write(msg.encode('utf-8'))

        send_data = data.encode('utf-8')      

        bytes_num = self.ser.write(send_data)
        # time.sleep(0.1)
        # bytes_num = self.ser.write(send_data)

        # bytes_num = self.ser.write(send_data)

        print("homing")
        print(bytes_num)

        print(self.ser.read())
        # try:
        #     message += terminator
        #     self.serialport.write(message.encode('utf-8'))
        # except Exception as e:
        #     print(e)
        #     print("Error sending message: ", sys.exc_info()[0])


if __name__=='__main__':

    try:
        
        rospy.loginfo("start FollowController")
        FollowController('follow_Controller')

    except rospy.ROSInterruptException:
        rospy.loginfo('Fialed to start follow_Controller')
 

