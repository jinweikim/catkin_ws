// Generated by gencpp from file easy_handeye/TakeSampleRequest.msg
// DO NOT EDIT!


#ifndef EASY_HANDEYE_MESSAGE_TAKESAMPLEREQUEST_H
#define EASY_HANDEYE_MESSAGE_TAKESAMPLEREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace easy_handeye
{
template <class ContainerAllocator>
struct TakeSampleRequest_
{
  typedef TakeSampleRequest_<ContainerAllocator> Type;

  TakeSampleRequest_()
    {
    }
  TakeSampleRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::easy_handeye::TakeSampleRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::easy_handeye::TakeSampleRequest_<ContainerAllocator> const> ConstPtr;

}; // struct TakeSampleRequest_

typedef ::easy_handeye::TakeSampleRequest_<std::allocator<void> > TakeSampleRequest;

typedef boost::shared_ptr< ::easy_handeye::TakeSampleRequest > TakeSampleRequestPtr;
typedef boost::shared_ptr< ::easy_handeye::TakeSampleRequest const> TakeSampleRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::easy_handeye::TakeSampleRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::easy_handeye::TakeSampleRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace easy_handeye

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'visp_hand2eye_calibration': ['/home/jinwei/catkin_ws/src/vision_visp/visp_hand2eye_calibration/msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'easy_handeye': ['/home/jinwei/catkin_ws/src/easy_handeye/easy_handeye/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::easy_handeye::TakeSampleRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::easy_handeye::TakeSampleRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::easy_handeye::TakeSampleRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::easy_handeye::TakeSampleRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::easy_handeye::TakeSampleRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::easy_handeye::TakeSampleRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::easy_handeye::TakeSampleRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::easy_handeye::TakeSampleRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::easy_handeye::TakeSampleRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "easy_handeye/TakeSampleRequest";
  }

  static const char* value(const ::easy_handeye::TakeSampleRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::easy_handeye::TakeSampleRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
";
  }

  static const char* value(const ::easy_handeye::TakeSampleRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::easy_handeye::TakeSampleRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct TakeSampleRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::easy_handeye::TakeSampleRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::easy_handeye::TakeSampleRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // EASY_HANDEYE_MESSAGE_TAKESAMPLEREQUEST_H
