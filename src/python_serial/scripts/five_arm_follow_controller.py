#!/usr/bin/env python

import rospy, actionlib

from control_msgs.msg import FollowJointTrajectoryAction
from trajectory_msgs.msg import JointTrajectory
from diagnostic_msgs.msg import *
import sensor_msgs.msg
from math import pi as PI, degrees, radians
from joints import Joint 
from listenSerial import Traj

class FollowController:

    def __init__(self,name):

        self.name = name

        rospy.loginfo("controller init")

        print "controller init"

        rospy.init_node(self.name)



        self.rate = 50.0

        self.joint0=Joint('joint0',6,-1.57,1.57,500,2500,False)
        self.joint1=Joint('joint1',5,-1.57,1.57,500,2500,False) 
        self.joint2=Joint('joint2',4,-1.57,1.57,2500,500,False)
        self.joint3=Joint('joint3',3,-1.57,1.57,2500,500,False)
        self.joint4=Joint('joint4',2,-1.57,1.57,2500,500,False)



        self.joints=[self.joint0,
        self.joint1,
        self.joint2,
        self.joint3,
        self.joint4]

        print "ready for register follow_Controller"


        self.server = actionlib.SimpleActionServer('arm_controller/follow_joint_trajectory', FollowJointTrajectoryAction, execute_cb=self.actionCb, auto_start=False)
        self.server.start()
        rospy.spin() 
        rospy.loginfo("Started FollowController")

        print "Started FollowController"
    
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
        
        try: 
            indexs = [traj.joint_names.index(joint.name) for joint in self.joints]

        except ValueError as val:

            msg = "Trajectory invalid"
            rospy.loginfo(msg)
            self.server.set_aborted(text=msg)
            return 

        if self.executeTrajectory(traj):
            self.server.set_succeeded()
        else:
            self.server.set_aborted(text="Execution failed")

        rospy.loginfo(self.name + ":Done")


    def executeTrajectory(self,traj):
        rospy.loginfo("EXecuting trajectory")
        rospy.logdebug(traj)
        pub = rospy.Publisher('/joint_states',sensor_msgs.msg.JointState,queue_size=1)

        jointsCurrent = sensor_msgs.msg.JointState()

        print traj

        try:
            indexes = [traj.joint_names.index(joint.name) for joint in self.joints]

        except ValueError as val:

            rospy.loginfo("invalid joint in trajectory")

            return False

        start = traj.header.stamp

        if start.secs == 0 and start.nsecs == 0:
            start = rospy.Time.now()

        r = rospy.Rate(self.rate)


        for point in traj.points:

            tmp = [point.positions[k] for k in indexes]

            desired = [1500,0,0,0,0,0]
            # desired[0] = 1500
            # desired[1] = tmp[4]
            # desired[2] = tmp[3]
            # desired[3] = tmp[2]
            # desired[4] = tmp[1]
            # desired[5] = tmp[0]

            for i in indexes:
                
                jointsCurrent.header.stamp= rospy.Time.now()
                jointsCurrent.name.append(self.joints[i].name)
                rospy.loginfo('jointsCurrent.name')
                rospy.loginfo(self.joints[i].name)
                jointsCurrent.position.append(tmp[i])
                rospy.loginfo('jointsCurrent.position')
                rospy.loginfo(tmp[i])
                self.joints[i].mapToServoPosition(tmp[i])
                desired[self.joints[i].servoNum-1] = int(self.joints[i].position)
                
                #rospy.loginfo(self.joints[i].servoNum-1)
                #rospy.loginfo(desired[self.joints[i].servoNum-1])
            pub.publish(jointsCurrent)
            rospy.loginfo(desired)
            traj = Traj(1000,desired)
            serial_data = traj.trajToSerial()
            traj.goto(serial_data)


            while rospy.Time.now() + rospy.Duration(0.01) < start:
                rospy.sleep(0.01)

        return True

if __name__=='__main__':

    try:
        
        rospy.loginfo("start FollowController")
        FollowController('follow_Controller')

    except rospy.ROSInterruptException:
        rospy.loginfo('Fialed to start follow_Controller')
 


























