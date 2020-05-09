#!/usr/bin/env python
#coding=utf-8
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

from math import pi
import math
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from geometry_msgs.msg import PoseStamped, Pose
from tf.transformations import quaternion_from_euler

class Robot:

    r = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()

    group_name = "arm"
    group = moveit_commander.MoveGroupCommander(group_name)#规划组group

    # gripper_name = "gripper"
    # gripper = moveit_commander.MoveGroupCommander(gripper_name)#规划组gripper

    end_effector_link = group.get_end_effector_link()

    reference_frame = 'base_link'

    box_name = ''

    def __init__(self):

        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('move_group_python_interface_tutorial',
                            anonymous=True)
        

        display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                           moveit_msgs.msg.DisplayTrajectory,
                                                           queue_size=20)
        
        self.group.set_pose_reference_frame(self.reference_frame)#参考坐标系
        self.group.allow_replanning(True)#是否尝试重新规划

        #误差容忍度
        self.group.set_goal_position_tolerance(0.001)
        self.group.set_goal_orientation_tolerance(0.001)
                   
        #移动速率
        self.group.set_max_acceleration_scaling_factor(0.5)
        self.group.set_max_velocity_scaling_factor(0.5)

        add_result = self.add_box()

        print "if add box: %s" % add_result

    def go(self,target_pose):

        self.group.set_start_state_to_current_state()
        self.group.set_pose_target(target_pose,self.end_effector_link)
        traj = self.group.plan()
        self.group.execute(traj,wait=True)

    def pos_to_target_pose(self,pos):

        target_pose = PoseStamped()

        target_pose.header.frame_id = self.reference_frame
        target_pose.header.stamp = rospy.Time.now() 

        target_pose.pose.position.x = pos.x
        target_pose.pose.position.y = pos.y
        target_pose.pose.position.z = pos.z

        #print "roll: %s, pitch: %s, yaw: %s" % (pos.roll,pos.pitch,pos.yaw)

        q = quaternion_from_euler(pos.roll,pos.pitch,pos.yaw)

        target_pose.pose.orientation.x = q[0]
        target_pose.pose.orientation.y = q[1]
        target_pose.pose.orientation.z = q[2]
        target_pose.pose.orientation.w = q[3]

        return target_pose

    def move(self,position):    

        # group.set_named_target('home')
        # group.go
        # rospy.sleep(1)

        group = self.group

        print "in move"

        if position == 'home':
            group.set_named_target('home')
            group.go()
            rospy.sleep(1)


        #规避
        if position == 'hide':
            # We can get the joint values from the group and adjust some of the values:
            joint_goal = group.get_current_joint_values()
            joint_goal[0] =  -1.686
            joint_goal[1] = 2.173
            joint_goal[2] = -1.50
            joint_goal[3] = -1.700
            joint_goal[4] = -1.531
            joint_goal[5] = -0.785

            #-1.68602366327 2.1734413774 -1.49991589924 -1.70095518518 -1.53124549999 -0.785432329752]     

            # The go command can be called with joint values, poses, or without any
            # parameters if you have already set the pose or joint target for the group
            group.go(joint_goal, wait=True)

            # Calling ``stop()`` ensures that there is no residual movement
            group.stop()

            return 1

        print 'x: %s, y: %s,z: %s, roll: %s,pitch: %s, yaw: %s' % (position.x,position.y,position.z,position.roll,position.pitch,position.yaw)

        target_pose = self.pos_to_target_pose(position)

        self.go(target_pose)
        
        rospy.sleep(1)

        #joint_goal = self.group.get_current_joint_values()

        return 1

    def add_box(self, timeout=4):
        # Copy class variables to local variables to make the web tutorials more clear.
        # In practice, you should use the class variables directly unless you have a good
        # reason not to.
        box_name = self.box_name
        scene = self.scene

        rospy.sleep(2)

        ## BEGIN_SUB_TUTORIAL add_box
        ##
        ## Adding Objects to the Planning Scene
        ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ## First, we will create a box in the planning scene at the location of the left finger:

        roll = math.pi/2 - 1.5707

        q = quaternion_from_euler(roll,0,0)

        box_pose = geometry_msgs.msg.PoseStamped()
        box_pose.header.frame_id = self.r.get_planning_frame()

        box_pose.pose.orientation.x = q[0]
        box_pose.pose.orientation.y = q[1]
        box_pose.pose.orientation.z = q[2]
        box_pose.pose.orientation.w = q[3]

        box_pose.pose.position.y = -1.0
        box_pose.pose.position.z = 0.75

        box_name = "box"
        scene.add_box(box_name, box_pose, size=(1.5, 0.1, 1.5))

        ## END_SUB_TUTORIAL
        # Copy local variables back to class variables. In practice, you should use the class
        # variables directly unless you have a good reason not to.
        self.box_name=box_name
        return self.wait_for_state_update(box_is_known=True, timeout=timeout)

    def wait_for_state_update(self, box_is_known=False, box_is_attached=False, timeout=4):
        # Copy class variables to local variables to make the web tutorials more clear.
        # In practice, you should use the class variables directly unless you have a good
        # reason not to.
        box_name = self.box_name
        scene = self.scene

        ## BEGIN_SUB_TUTORIAL wait_for_scene_update
        ##
        ## Ensuring Collision Updates Are Receieved
        ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ## If the Python node dies before publishing a collision object update message, the message
        ## could get lost and the box will not appear. To ensure that the updates are
        ## made, we wait until we see the changes reflected in the
        ## ``get_known_object_names()`` and ``get_known_object_names()`` lists.
        ## For the purpose of this tutorial, we call this function after adding,
        ## removing, attaching or detaching an object in the planning scene. We then wait
        ## until the updates have been made or ``timeout`` seconds have passed
        start = rospy.get_time()
        seconds = rospy.get_time()
        while (seconds - start < timeout) and not rospy.is_shutdown():

            # Test if the box is in attached objects
            attached_objects = scene.get_attached_objects([box_name])
            is_attached = len(attached_objects.keys()) > 0

            # Test if the box is in the scene.
            # Note that attaching the box will remove it from known_objects
            is_known = box_name in scene.get_known_object_names()

            print "is known:%s" % is_known

            # Test if we are in the expected state
            if (box_is_attached == is_attached) and (box_is_known == is_known):
                return True

            # Sleep so that we give other threads time on the processor
            rospy.sleep(0.1)
            seconds = rospy.get_time()

        # If we exited the while loop without returning then we timed out
        return False
        ## END_SUB_TUTORIAL






    # def swipe(self,direction):
    #     joint_goal_new = adaptAngle()
    #     self.gripper.go()


    # def long_press(self,position)：

    #     joint_goal_new = adaptAngle()


    # def hide(self):
    #     self.move()




