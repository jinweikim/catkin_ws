#!/usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

from math import pi,radians
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from geometry_msgs.msg import PoseStamped, Pose
from tf.transformations import quaternion_from_euler

def do_execute(group,target_pose,end_effector_link):
    print "xyz:"
    print target_pose_down.pose.position.x
    print target_pose_down.pose.position.y
    print target_pose_down.pose.position.z
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


joint_goal = group.get_current_joint_values()

joint_goal[0] = 0.33045
joint_goal[1] = 0.88154
joint_goal[2] = 0.61874
joint_goal[3] = 1.52274
joint_goal[4] = 0.99258


group.go(joint_goal,wait=True)

group.stop()

print "============ Printing robot state"
print robot.get_current_state()
print ""



# 0.9057; -0.14995; -0.2848; -0.27589
# 0.4219; -0.65066; -0.29486; 0.55831
# 0.39737; -0.58499; -0.14938; 0.69107
# -0.27426; 0.24897; 0.15228; 0.9163
# -0.31699; 0.51515; 0.17757; 0.77628
# -0.0056101; -0.25183; 0.27764; 0.92708

