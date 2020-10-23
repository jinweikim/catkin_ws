#!/usr/bin/env python
import rospy
import tf
import geometry_msgs.msg 

t = tf.TransformListener()
camera_to_robot = t.lookupTransform("link1","camera_link",rospy.Time(0))
rospy.loginfo(camera_to_robot)


