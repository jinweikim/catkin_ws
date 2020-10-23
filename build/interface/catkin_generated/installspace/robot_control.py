#!/usr/bin/env python2

from interface.srv import RobotControl,RobotControlResponse
import rospy
from Robot import *
from Rcs3D import *


def handle_robot_control(req):
    print("handling robot control")
    print("x: %s y: %s,z: %s"%(req.x,req.y,req.z))
    # print("roll: %s pitch: %s,yaw: %s"%(req.roll,req.pitch,req.yaw))
    rcs3d = Rcs3D()
    print("after init robot")
    print("after init position")
    if req.type == 'click':
        point = [req.x,req.y,req.z]
        rcs3d.click(point)
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
