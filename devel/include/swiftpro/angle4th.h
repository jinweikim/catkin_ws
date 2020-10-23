// Generated by gencpp from file swiftpro/angle4th.msg
// DO NOT EDIT!


#ifndef SWIFTPRO_MESSAGE_ANGLE4TH_H
#define SWIFTPRO_MESSAGE_ANGLE4TH_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace swiftpro
{
template <class ContainerAllocator>
struct angle4th_
{
  typedef angle4th_<ContainerAllocator> Type;

  angle4th_()
    : angle4th(0.0)  {
    }
  angle4th_(const ContainerAllocator& _alloc)
    : angle4th(0.0)  {
  (void)_alloc;
    }



   typedef double _angle4th_type;
  _angle4th_type angle4th;





  typedef boost::shared_ptr< ::swiftpro::angle4th_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::swiftpro::angle4th_<ContainerAllocator> const> ConstPtr;

}; // struct angle4th_

typedef ::swiftpro::angle4th_<std::allocator<void> > angle4th;

typedef boost::shared_ptr< ::swiftpro::angle4th > angle4thPtr;
typedef boost::shared_ptr< ::swiftpro::angle4th const> angle4thConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::swiftpro::angle4th_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::swiftpro::angle4th_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace swiftpro

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'swiftpro': ['/home/jinwei/catkin_ws/src/RosForSwiftAndSwiftPro-master/swiftpro/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::swiftpro::angle4th_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::swiftpro::angle4th_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::swiftpro::angle4th_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::swiftpro::angle4th_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::swiftpro::angle4th_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::swiftpro::angle4th_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::swiftpro::angle4th_<ContainerAllocator> >
{
  static const char* value()
  {
    return "8eecd591854543ff5e9cf583de2d05e6";
  }

  static const char* value(const ::swiftpro::angle4th_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x8eecd591854543ffULL;
  static const uint64_t static_value2 = 0x5e9cf583de2d05e6ULL;
};

template<class ContainerAllocator>
struct DataType< ::swiftpro::angle4th_<ContainerAllocator> >
{
  static const char* value()
  {
    return "swiftpro/angle4th";
  }

  static const char* value(const ::swiftpro::angle4th_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::swiftpro::angle4th_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 angle4th\n\
";
  }

  static const char* value(const ::swiftpro::angle4th_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::swiftpro::angle4th_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.angle4th);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct angle4th_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::swiftpro::angle4th_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::swiftpro::angle4th_<ContainerAllocator>& v)
  {
    s << indent << "angle4th: ";
    Printer<double>::stream(s, indent + "  ", v.angle4th);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SWIFTPRO_MESSAGE_ANGLE4TH_H