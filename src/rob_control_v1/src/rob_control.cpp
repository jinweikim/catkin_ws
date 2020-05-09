#include <rob_control.h>
#include <list>

//#include "armplaning_client.h"

using namespace std;

//定义服务端
typedef actionlib::SimpleActionServer<control_msgs::FollowJointTrajectoryAction> R_TrajectoryServer;

std::list<robotState> r_targetPointList;            

double deg2rad = 3.14159/180.0;
double rad2deg = 180.0/3.14159;


void r_executeTrajectory(const control_msgs::FollowJointTrajectoryGoalConstPtr& r_goal, R_TrajectoryServer* r_as)
{
  //double rad2deg = 180.0 / 3.141;
  robotState rs;
  ROS_INFO("r_executeTrajectory doing");
  float lastDuration = 0.0;

  int nrOfPoints = r_goal->trajectory.points.size();       
  for(int i=0; i<nrOfPoints; i++)
  {
      rs.j[0] = r_goal->trajectory.points[i].positions[3]*rad2deg;   
      rs.j[1] = r_goal->trajectory.points[i].positions[0]*rad2deg;
      rs.j[2] = r_goal->trajectory.points[i].positions[2]*rad2deg;
      rs.j[3] = r_goal->trajectory.points[i].positions[1]*rad2deg;
      rs.j[4] = r_goal->trajectory.points[i].positions[4]*rad2deg;
      rs.j[5] = r_goal->trajectory.points[i].positions[5]*rad2deg;
      
      float dtmp = r_goal->trajectory.points[i].time_from_start.toSec();
      rs.duration = dtmp - lastDuration;
      lastDuration = dtmp;

      r_targetPointList.push_back(rs);//push_back() 在list的末尾添加一个元素 
  }
  r_as->setSucceeded();

 ROS_INFO("right arm recv: %f %f %f %f %f %f,duration: %f", rs.j[0],rs.j[1],rs.j[2],rs.j[3],rs.j[4],rs.j[5],rs.duration);
  
}

//*************************************************************************
void quit(int sig)
{
  ros::shutdown();
  exit(0);
}

//******************** MAIN ************************************************
int main(int argc, char** argv)
{
    ros::init(argc, argv, "chx_arm");
    ros::NodeHandle n2;
    //服务端初始化,当action客户端请求一个动作时，这个动作被认为是一个目标，传递给action服务端，此时就moveit的action客户端而言，这个目标就是机械臂运动轨迹，服务端接收到目标后，会自动回调r_executeTrajectory这个函数，而目标（轨迹）会作为参数传递进来。
    R_TrajectoryServer r_tserver(n2, "chx_arm/follow_joint_trajectory", boost::bind(&r_executeTrajectory, _1, &r_tserver), false);
    ROS_INFO("TrajectoryActionServer: Starting");
    //服务端启动
    r_tserver.start();
    ROS_INFO("1");

   
    rob_robots::rob_control robot;
    robot.init();    
    robot.mainLoop();                   

    signal(SIGINT,quit);    
    return(0);
}

namespace rob_robots{
    //*************************************************************************************
    rob_control::~rob_control(){

    }
    //*************************************************************************************
    void rob_control::init(){
        ROS_INFO("...initing...");

        flag_stop_requested = false;
        //this deside the control msg send frequency 
        cycleTime = 10.0;// in ms
        nrOfJoints = 6;

        r_setPointState.j[0] =  0.0;   
        r_setPointState.j[1] =  0.0;
        r_setPointState.j[2] =  0.0;
        r_setPointState.j[3] =  0.0;
        r_setPointState.j[4] =  0.0;
        r_setPointState.j[5] =  0.0;
        r_setPointState.duration = 0;

        ROS_INFO("2");

        // when starting up (or when reading the HW joint values) the target position has to be aligned with the setPoint position
        for(int i=0; i<nrOfJoints; i++)
        {
            r_targetState.j[i] = r_setPointState.j[i];
        }
            
        r_targetState.duration = 0.0;//init the timeStamp

        for(int j=0;j<6;j++)
        {
            r_controlData[j] = 0;
        }

        r_msgJointsCurrent.header.stamp = ros::Time::now();
        ROS_INFO("3");
        r_msgJointsCurrent.name.resize(6);
        ROS_INFO("4");
        r_msgJointsCurrent.position.resize(6);
        ROS_INFO("5");
        r_msgJointsCurrent.name[0] ="joint0";
        ROS_INFO("6");
        r_msgJointsCurrent.position[0] = 0.0;
        ROS_INFO("7");
        r_msgJointsCurrent.name[1] ="joint1";
        ROS_INFO("8");
        r_msgJointsCurrent.position[1] = 0.0;
        ROS_INFO("9");
        r_msgJointsCurrent.name[2] ="joint2";
        ROS_INFO("10");
        r_msgJointsCurrent.position[2] = 0.0;
        ROS_INFO("11");
        r_msgJointsCurrent.name[3] ="joint3";
        ROS_INFO("12");
        r_msgJointsCurrent.position[3] = 0.0;
        ROS_INFO("13");
        r_msgJointsCurrent.name[4] ="joint4";
        ROS_INFO("14");
        r_msgJointsCurrent.position[4] = 0.0;
        ROS_INFO("15");
        r_msgJointsCurrent.name[5] ="joint5";
        ROS_INFO("16");
        r_msgJointsCurrent.position[5] = 0.0;
        ROS_INFO("17");


        // 发布当前关节信息
        pubJoints = n.advertise<sensor_msgs::JointState>("/joint_states", 1);



    }
    //*************************************************************************************
    void rob_control::mainLoop()
    {
          //ROS_INFO("Starting Mover Main Loop");
        
        //output angle data to a txt file
        int i = 0;
          
          for(;;)
          {
            MotionGeneration();            // Generate the joint motion 
            CommunicationHW();            // Forward the new setpoints to the hardware

            if(flag_stop_requested)
                break;

            ros::spinOnce();
            ros::Duration(cycleTime/1000.0).sleep();        // main loop with 20 Hz.(50/1000=0.05s=50ms)
                        
          }

        ROS_INFO("Closing Mover Main Loop");

    } 
    //************************************************************************************
    //
    void rob_control::MotionGeneration()
    {
    	//ROS_INFO("Starting Motion Generation");
        int i=0;
        int j=0;

        //printf("r_targetPointList.size() = %ld \n",r_targetPointList.size());
       
        if(r_targetPointList.size() > 0)
        {
            r_targetState = r_targetPointList.front();
            r_targetPointList.pop_front();

            for(int i=0; i<nrOfJoints; i++)
            {
                r_setPointState.j[i] = r_targetState.j[i];
            }
            r_setPointState.duration = r_targetState.duration;
            
            for(j=0;j<6;j++)
            {
                r_controlData[j] = r_setPointState.j[j];
            }
            r_controlData[6] = r_setPointState.duration;
        }


    }
    //************************************************************************************
    // Forward the new setpoints to the hardware

    void rob_control::CommunicationHW()
    {
    	//ROS_INFO("Starting CommunicationHW");

        int i = 0;
        for(i=0;i<7;i++)
        {
            r_executeData[i] = r_controlData[i];
        }

        if(r_executeData[0]!=r_executeData_old[0] && r_executeData[1]!=r_executeData_old[1])
        {
            
            

            Comm.SetRightJoints(r_executeData);

           

            ROS_INFO("Right arm MSG [%f][%f][%f][%f][%f][%f][%f]", r_executeData[0],r_executeData[1],r_executeData[2],r_executeData[3],r_executeData[4],r_executeData[5],r_executeData[6]);

            //存储旧数据
            for (int i=0;i<7;i++)
            {
                r_executeData_old[i] = r_executeData[i];
            }

            R_CommunicationROS();            // 发布关节信息
        }

    }


    // 把目前角度信息传给rviz
    void rob_control::R_CommunicationROS()
    {
    	//ROS_INFO("Starting Communication ROS");
        r_msgJointsCurrent.header.stamp = ros::Time::now();
        r_msgJointsCurrent.position[0] = r_executeData[0]*deg2rad;        // Robot SER communication works in degree
        r_msgJointsCurrent.position[1] = r_executeData[1]*deg2rad;
        r_msgJointsCurrent.position[2] = r_executeData[2]*deg2rad;
        r_msgJointsCurrent.position[3] = r_executeData[3]*deg2rad;
        r_msgJointsCurrent.position[4] = r_executeData[4]*deg2rad;
        r_msgJointsCurrent.position[5] = r_executeData[5]*deg2rad;

        pubJoints.publish(r_msgJointsCurrent);    // ROS communication works in Radian

    }

}


