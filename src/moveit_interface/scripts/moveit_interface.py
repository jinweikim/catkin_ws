#!/usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from geometry_msgs.msg import PoseStamped, Pose
from tf.transformations import quaternion_from_euler

def do_execute(group,target_pose,end_effector_link):
    group.set_start_state_to_current_state()
    group.set_pose_target(target_pose,end_effector_link)
    traj = group.plan()
    group.execute(traj,wait=True)


moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial',
                anonymous=True)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()

group_name = "arm"
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

# group.set_named_target('home')
# group.go
# rospy.sleep(1)

# box_pose = geometry_msgs.msg.PoseStamped()
# box_pose.header.frame_id = "base_link"
# box_pose.pose.orientation.w = 1.0
# box_name = 'screen'
# scene.add_box(box_name,box_pose,size=(0.1,0.1,0.1))



# If we exited the while loop without returning then we timed out



# group.set_named_target('home')
# group.go()
# rospy.sleep(1)


target_pose = PoseStamped()


target_pose.header.frame_id = reference_frame
target_pose.header.stamp = rospy.Time.now() 
  
target_pose.pose.position.x = 0.6004
target_pose.pose.position.y = -0.6723
target_pose.pose.position.z = 0.6489

q = quaternion_from_euler(0.78535,0,0)
#(1,5707,0,0) down

# target_pose.pose.orientation.x = -0.3916
# target_pose.pose.orientation.y = 0.61509
# target_pose.pose.orientation.z = 0.68106
# target_pose.pose.orientation.w = 0.06702

target_pose.pose.orientation.x = q[0]
target_pose.pose.orientation.y = q[1]
target_pose.pose.orientation.z = q[2]
target_pose.pose.orientation.w = q[3]

do_execute(group,target_pose,end_effector_link)
print "to the obj"
rospy.sleep(1)



###############################################

# target_pose_down = PoseStamped()

# target_pose_down.header.frame_id = reference_frame
# target_pose_down.header.stamp = rospy.Time.now() 

# target_pose_down.pose.position.x = 0.6004
# target_pose_down.pose.position.y = -0.6723
# target_pose_down.pose.position.z = 0.3489

# q = quaternion_from_euler(1.5707,0,0)

# target_pose_down.pose.orientation.x = q[0]
# target_pose_down.pose.orientation.y = q[1]
# target_pose_down.pose.orientation.z = q[2]
# target_pose_down.pose.orientation.w = q[3]

# do_execute(group,target_pose_down,end_effector_link)
# print "down"
# rospy.sleep(1)

###############################################

# do_execute(group,target_pose,end_effector_link)
# print "back"
# rospy.sleep(1)

# lower
# target_pose.pose.position.z = 0.1279
# group.set_start_state_to_current_state()
# group.set_pose_target(target_pose, end_effector_link)
# traj = group.plan()  


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

joint_goal = group.get_current_joint_values()





# 0.9057; -0.14995; -0.2848; -0.27589
# 0.4219; -0.65066; -0.29486; 0.55831
# 0.39737; -0.58499; -0.14938; 0.69107
# -0.27426; 0.24897; 0.15228; 0.9163
# -0.31699; 0.51515; 0.17757; 0.77628
# -0.0056101; -0.25183; 0.27764; 0.92708


