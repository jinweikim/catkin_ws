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



# group.set_named_target('home')
# group.go()
# rospy.sleep(1)



pos1 = [-0.015027, -0.020196, 0.25845]
pos2 = [0.03236, -0.1192, 0.12815]
pos3 = [-0.022928, 0.13369, 0.18904]
pos4 = [0.054113, -0.18469, 0.028586]
pos5 = [-0.00044815, -0.0034634, 0.33762]
pos6 = [0.023072, -0.075222, 0.29461]
pos7 = [0.13894, -0.19418, 0.039716]
pos8 = [-0.176, -0.11469, 0.17769]
pos9 = [-0.054477, -0.14351, 0.2343]
pos10 = [-0.028901, 0.094254, 0.29455]

pos = [pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9,pos10,]

orient1 =[0.3442, -0.34055, 0.24067, 0.84121]
orient2 =[0.84472, -0.52634, 0.072917, 0.064002]
orient3 =[0.85475, -0.24744, -0.18857, -0.41549 ]
orient4 =[0.61534, 0.76625, -0.1031, 0.1536 ]
orient5 =[0.034062, 0.077439, 0.16892, 0.98199 ]
orient6 =[0.42963, 0.19804, -0.079375, 0.87744 ]
orient7 =[0.88262, -0.020172, 0.28738, 0.37146 ]
orient8 =[-0.46392, -0.032403, 0.76637, -0.44318 ]
orient9 =[-0.1882, -0.113, -0.75252, 0.62091 ]
orient10 =[-0.10915, -0.047213, -0.14436, 0.98235 ]

orient = [orient1,orient2,orient3,orient4,orient5,orient6,orient7,orient8,orient9,orient10]

###############################################

i = 2
i = i-1

target_pose_down = PoseStamped()

target_pose_down.header.frame_id = reference_frame
target_pose_down.header.stamp = rospy.Time.now() 

target_pose_down.pose.position.x = pos[i][0]
target_pose_down.pose.position.y = pos[i][1]
target_pose_down.pose.position.z = pos[i][2]

#target_pose_down.pose.position.x = 0.055
#target_pose_down.pose.position.y = 0.250
#target_pose_down.pose.position.z = 0.226


target_pose_down.pose.orientation.x = orient[i][0]
target_pose_down.pose.orientation.y = orient[i][1]
target_pose_down.pose.orientation.z = orient[i][2]
target_pose_down.pose.orientation.w = orient[i][3]

q = quaternion_from_euler(1.5707,0,0)
#target_pose_down.pose.orientation.x = q[0]
#target_pose_down.pose.orientation.y = q[1]
#target_pose_down.pose.orientation.z = q[2]
#target_pose_down.pose.orientation.w = q[3]

do_execute(group,target_pose_down,end_effector_link)
print "down"
rospy.sleep(1)

group.set_start_state_to_current_state()


target_pose_down.pose.position.x = -0.27
target_pose_down.pose.position.y = 0.0122
target_pose_down.pose.position.z = -0.0183


q = quaternion_from_euler(1.5707,0,0)
target_pose_down.pose.orientation.x = q[0]
target_pose_down.pose.orientation.y = q[1]
target_pose_down.pose.orientation.z = q[2]
target_pose_down.pose.orientation.w = q[3]
# target_pose_down.pose.orientation.x = orient[i][0]
# target_pose_down.pose.orientation.y = orient[i][1]
# target_pose_down.pose.orientation.z = orient[i][2]
# target_pose_down.pose.orientation.w = orient[i][3]

do_execute(group,target_pose_down,end_effector_link)
print "down"
rospy.sleep(1)



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

# joint_goal = group.get_current_joint_values()

# joint_goal[0] = radians(0)
# joint_goal[1] = radians(30)
# joint_goal[2] = radians(-80)
# joint_goal[3] = radians(-90)
# joint_goal[4] = radians(-80)


# group.go(joint_goal,wait=True)

# group.stop()





# 0.9057; -0.14995; -0.2848; -0.27589
# 0.4219; -0.65066; -0.29486; 0.55831
# 0.39737; -0.58499; -0.14938; 0.69107
# -0.27426; 0.24897; 0.15228; 0.9163
# -0.31699; 0.51515; 0.17757; 0.77628
# -0.0056101; -0.25183; 0.27764; 0.92708


