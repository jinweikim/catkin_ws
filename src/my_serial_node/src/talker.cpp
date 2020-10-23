#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

int hex2byte(char *, char *);

int main(int argc, char **argv)
{
 ros::init(argc, argv, "talker");
 ros::NodeHandle n;
 //发布主题command
 ros::Publisher command_pub = n.advertise<std_msgs::String>("command", 1000);
 ros::Rate loop_rate(10);
 int count = 0;
 while (ros::ok())
 {
   std_msgs::String msg;
   std::stringstream ss_data;

   // ss_data << "talker publish command " << count;
   // msg.data = ss_data.str();

   char srcBuff[] = "55 55 08 03 01 00 00 01 B2 02";
   char dstBuff[100];
   msg.data = hex2byte(dstBuff,srcBuff);
   ROS_INFO("%s", msg.data);
   command_pub.publish(msg);
   ros::spinOnce();
   loop_rate.sleep();
   ++count;
  }
  return 0;

}

int hex2byte(char *dst, char *src) {
    while(*src) {
        if(' ' == *src) {
            src++;
            continue;
        }
        sscanf(src, "%02X", dst);
        src += 2;
        dst++;
    }
    return 0;
}
