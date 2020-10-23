// Generated by gencpp from file uarm/Angles.msg
// DO NOT EDIT!


#ifndef UARM_MESSAGE_ANGLES_H
#define UARM_MESSAGE_ANGLES_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace uarm
{
template <class ContainerAllocator>
struct Angles_
{
  typedef Angles_<ContainerAllocator> Type;

  Angles_()
    : servo_1(0)
    , servo_2(0)
    , servo_3(0)
    , servo_4(0)  {
    }
  Angles_(const ContainerAllocator& _alloc)
    : servo_1(0)
    , servo_2(0)
    , servo_3(0)
    , servo_4(0)  {
  (void)_alloc;
    }



   typedef uint8_t _servo_1_type;
  _servo_1_type servo_1;

   typedef uint8_t _servo_2_type;
  _servo_2_type servo_2;

   typedef uint8_t _servo_3_type;
  _servo_3_type servo_3;

   typedef uint8_t _servo_4_type;
  _servo_4_type servo_4;





  typedef boost::shared_ptr< ::uarm::Angles_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::uarm::Angles_<ContainerAllocator> const> ConstPtr;

}; // struct Angles_

typedef ::uarm::Angles_<std::allocator<void> > Angles;

typedef boost::shared_ptr< ::uarm::Angles > AnglesPtr;
typedef boost::shared_ptr< ::uarm::Angles const> AnglesConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::uarm::Angles_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::uarm::Angles_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace uarm

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'uarm': ['/home/jinwei/catkin_ws/src/UArmForROS-master/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::uarm::Angles_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::uarm::Angles_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::uarm::Angles_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::uarm::Angles_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::uarm::Angles_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::uarm::Angles_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::uarm::Angles_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c365f7c0f52d109b4b516ca588b94bd3";
  }

  static const char* value(const ::uarm::Angles_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc365f7c0f52d109bULL;
  static const uint64_t static_value2 = 0x4b516ca588b94bd3ULL;
};

template<class ContainerAllocator>
struct DataType< ::uarm::Angles_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uarm/Angles";
  }

  static const char* value(const ::uarm::Angles_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::uarm::Angles_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint8 servo_1\n\
uint8 servo_2\n\
uint8 servo_3\n\
uint8 servo_4\n\
";
  }

  static const char* value(const ::uarm::Angles_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::uarm::Angles_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.servo_1);
      stream.next(m.servo_2);
      stream.next(m.servo_3);
      stream.next(m.servo_4);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Angles_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::uarm::Angles_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::uarm::Angles_<ContainerAllocator>& v)
  {
    s << indent << "servo_1: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.servo_1);
    s << indent << "servo_2: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.servo_2);
    s << indent << "servo_3: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.servo_3);
    s << indent << "servo_4: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.servo_4);
  }
};

} // namespace message_operations
} // namespace ros

#endif // UARM_MESSAGE_ANGLES_H