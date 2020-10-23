/***********************************************************************
Copyright 2019 Wuhan PS-Micro Technology Co., Itd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
***********************************************************************/

#ifndef PROBOT_GRASPING_DEMO
#define PROBOT_GRASPING_DEMO

#include <ros/ros.h>

#include <tf/transform_listener.h>



class GraspingDemo
{
  private:
	/**
 	 * @brief NodeHandle of the current node
 	 */
	ros::NodeHandle nh_;


	tf::StampedTransform camera_to_robot_;
	/**
	 * @brief tf_camera_to_robot is an instance of tf_listener
	 */

	tf::TransformListener tf_camera_to_robot;
	/**
	 * @brief obj_camera_frame, obj_robot_frame are instance of tf::Vector
	 */

	tf::Vector3 obj_camera_frame, obj_robot_frame;
	/**
	 * @brief homePose is StampedPose keeping Home position of arm
	 */

	
};
	
#endif
