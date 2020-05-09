// Generated by gencpp from file ros_arduino_msgs/ArduinoConstants.msg
// DO NOT EDIT!


#ifndef ROS_ARDUINO_MSGS_MESSAGE_ARDUINOCONSTANTS_H
#define ROS_ARDUINO_MSGS_MESSAGE_ARDUINOCONSTANTS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ros_arduino_msgs
{
template <class ContainerAllocator>
struct ArduinoConstants_
{
  typedef ArduinoConstants_<ContainerAllocator> Type;

  ArduinoConstants_()
    {
    }
  ArduinoConstants_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }





  enum {
    LOW = 0u,
    HIGH = 1u,
    INPUT = 0u,
    OUTPUT = 1u,
  };


  typedef boost::shared_ptr< ::ros_arduino_msgs::ArduinoConstants_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ros_arduino_msgs::ArduinoConstants_<ContainerAllocator> const> ConstPtr;

}; // struct ArduinoConstants_

typedef ::ros_arduino_msgs::ArduinoConstants_<std::allocator<void> > ArduinoConstants;

typedef boost::shared_ptr< ::ros_arduino_msgs::ArduinoConstants > ArduinoConstantsPtr;
typedef boost::shared_ptr< ::ros_arduino_msgs::ArduinoConstants const> ArduinoConstantsConstPtr;

// constants requiring out of line definition

   

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ros_arduino_msgs::ArduinoConstants_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ros_arduino_msgs::ArduinoConstants_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ros_arduino_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'ros_arduino_msgs': ['/home/jinwei/catkin_ws/src/ros_arduino_bridge/ros_arduino_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ros_arduino_msgs::ArduinoConstants_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ros_arduino_msgs::ArduinoConstants_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ros_arduino_msgs::ArduinoConstants_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ros_arduino_msgs::ArduinoConstants_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_arduino_msgs::ArduinoConstants_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_arduino_msgs::ArduinoConstants_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ros_arduino_msgs::ArduinoConstants_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6ca092be59914d9e8dd11612f0a5c895";
  }

  static const char* value(const ::ros_arduino_msgs::ArduinoConstants_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6ca092be59914d9eULL;
  static const uint64_t static_value2 = 0x8dd11612f0a5c895ULL;
};

template<class ContainerAllocator>
struct DataType< ::ros_arduino_msgs::ArduinoConstants_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ros_arduino_msgs/ArduinoConstants";
  }

  static const char* value(const ::ros_arduino_msgs::ArduinoConstants_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ros_arduino_msgs::ArduinoConstants_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Arduino-style constants\n\
uint8 LOW=0\n\
uint8 HIGH=1\n\
uint8 INPUT=0\n\
uint8 OUTPUT=1\n\
";
  }

  static const char* value(const ::ros_arduino_msgs::ArduinoConstants_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ros_arduino_msgs::ArduinoConstants_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ArduinoConstants_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ros_arduino_msgs::ArduinoConstants_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::ros_arduino_msgs::ArduinoConstants_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // ROS_ARDUINO_MSGS_MESSAGE_ARDUINOCONSTANTS_H
