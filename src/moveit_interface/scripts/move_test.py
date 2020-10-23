#!/usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from array import array
from math import pi,radians
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from geometry_msgs.msg import PoseStamped, Pose, Quaternion, PointStamped, Vector3
from tf.transformations import quaternion_from_euler
import tf
from pyquaternion import Quaternion
import numpy as np


# def do_execute(group,target_pose,end_effector_link):
#     print "xyz:"
#     print target_pose_down.pose.position.x
#     print target_pose_down.pose.position.y
#     print target_pose_down.pose.position.z
#     group.set_start_state_to_current_state()
#     group.set_pose_target(target_pose,end_effector_link)
#     traj = group.plan()
#     group.execute(traj,wait=True)

print("start init")
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial',
                anonymous=True)
print("node init finished")
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()

group_name = "manipulator"
group = moveit_commander.MoveGroupCommander(group_name)

end_effector_link = group.get_end_effector_link()

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                               moveit_msgs.msg.DisplayTrajectory,
                                               queue_size=20)

reference_frame = 'base_link'
group.set_pose_reference_frame(reference_frame)
group.allow_replanning(True)


group.set_goal_position_tolerance(0.001)
group.set_goal_orientation_tolerance(0.001)
       

group.set_max_acceleration_scaling_factor(0.5)
group.set_max_velocity_scaling_factor(0.5)

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.w = 1.0
pose_goal.position.x = 0.12
pose_goal.position.y = -0.21
pose_goal.position.z = 0.102
print pose_goal
group.set_pose_target(pose_goal)

plan = group.go(wait=True)
# Calling `stop()` ensures that there is no residual movement
group.stop()
# It is always good to clear your targets after planning with poses.
# Note: there is no equivalent function for clear_joint_value_targets()
group.clear_pose_targets()

# We can get the name of the reference frame for this robot:
planning_frame = group.get_planning_frame()
print "============ Reference frame111: %s" % planning_frame

# We can also print the name of the end-effector link for this group:
eef_link = group.get_end_effector_link()
print "============ End effector111: %s" % eef_link

# We can get a list of all the groups in the robot:
group_names = robot.get_group_names()
print "============ Robot Groups:111", robot.get_group_names()

# Sometimes for debugging it is useful to print the entire state of the
# robot:
print "============ Printing robot state"
print robot.get_current_state()
print ""

# angle = [-23.64,28.02,32.22,-110.81,78.52,152.36]
# joint_goal = group.get_current_joint_values()

# joint_goal[0] = radians(angle[0])
# joint_goal[1] = radians(angle[1])
# joint_goal[2] = radians(angle[2])
# joint_goal[3] = radians(angle[3])
# joint_goal[4] = radians(angle[4])
# joint_goal[5] = radians(angle[5])

# group.go(joint_goal,wait=True)

# group.stop()



