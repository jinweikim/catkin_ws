# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from visp_hand2eye_calibration/compute_effector_camera_quickRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import visp_hand2eye_calibration.msg
import std_msgs.msg

class compute_effector_camera_quickRequest(genpy.Message):
  _md5sum = "4ce42b1236ce32724031d598c2a332bf"
  _type = "visp_hand2eye_calibration/compute_effector_camera_quickRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """


visp_hand2eye_calibration/TransformArray camera_object
visp_hand2eye_calibration/TransformArray world_effector

================================================================================
MSG: visp_hand2eye_calibration/TransformArray
# An array of transforms with a header for global reference.

Header header

geometry_msgs/Transform[] transforms
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Transform
# This represents the transform between two coordinate frames in free space.

Vector3 translation
Quaternion rotation

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['camera_object','world_effector']
  _slot_types = ['visp_hand2eye_calibration/TransformArray','visp_hand2eye_calibration/TransformArray']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       camera_object,world_effector

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(compute_effector_camera_quickRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.camera_object is None:
        self.camera_object = visp_hand2eye_calibration.msg.TransformArray()
      if self.world_effector is None:
        self.world_effector = visp_hand2eye_calibration.msg.TransformArray()
    else:
      self.camera_object = visp_hand2eye_calibration.msg.TransformArray()
      self.world_effector = visp_hand2eye_calibration.msg.TransformArray()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.camera_object.header.seq, _x.camera_object.header.stamp.secs, _x.camera_object.header.stamp.nsecs))
      _x = self.camera_object.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.camera_object.transforms)
      buff.write(_struct_I.pack(length))
      for val1 in self.camera_object.transforms:
        _v1 = val1.translation
        _x = _v1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v2 = val1.rotation
        _x = _v2
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      _x = self
      buff.write(_get_struct_3I().pack(_x.world_effector.header.seq, _x.world_effector.header.stamp.secs, _x.world_effector.header.stamp.nsecs))
      _x = self.world_effector.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.world_effector.transforms)
      buff.write(_struct_I.pack(length))
      for val1 in self.world_effector.transforms:
        _v3 = val1.translation
        _x = _v3
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v4 = val1.rotation
        _x = _v4
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.camera_object is None:
        self.camera_object = visp_hand2eye_calibration.msg.TransformArray()
      if self.world_effector is None:
        self.world_effector = visp_hand2eye_calibration.msg.TransformArray()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.camera_object.header.seq, _x.camera_object.header.stamp.secs, _x.camera_object.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.camera_object.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.camera_object.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.camera_object.transforms = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Transform()
        _v5 = val1.translation
        _x = _v5
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v6 = val1.rotation
        _x = _v6
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.camera_object.transforms.append(val1)
      _x = self
      start = end
      end += 12
      (_x.world_effector.header.seq, _x.world_effector.header.stamp.secs, _x.world_effector.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.world_effector.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.world_effector.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.world_effector.transforms = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Transform()
        _v7 = val1.translation
        _x = _v7
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v8 = val1.rotation
        _x = _v8
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.world_effector.transforms.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.camera_object.header.seq, _x.camera_object.header.stamp.secs, _x.camera_object.header.stamp.nsecs))
      _x = self.camera_object.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.camera_object.transforms)
      buff.write(_struct_I.pack(length))
      for val1 in self.camera_object.transforms:
        _v9 = val1.translation
        _x = _v9
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v10 = val1.rotation
        _x = _v10
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      _x = self
      buff.write(_get_struct_3I().pack(_x.world_effector.header.seq, _x.world_effector.header.stamp.secs, _x.world_effector.header.stamp.nsecs))
      _x = self.world_effector.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.world_effector.transforms)
      buff.write(_struct_I.pack(length))
      for val1 in self.world_effector.transforms:
        _v11 = val1.translation
        _x = _v11
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v12 = val1.rotation
        _x = _v12
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.camera_object is None:
        self.camera_object = visp_hand2eye_calibration.msg.TransformArray()
      if self.world_effector is None:
        self.world_effector = visp_hand2eye_calibration.msg.TransformArray()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.camera_object.header.seq, _x.camera_object.header.stamp.secs, _x.camera_object.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.camera_object.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.camera_object.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.camera_object.transforms = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Transform()
        _v13 = val1.translation
        _x = _v13
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v14 = val1.rotation
        _x = _v14
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.camera_object.transforms.append(val1)
      _x = self
      start = end
      end += 12
      (_x.world_effector.header.seq, _x.world_effector.header.stamp.secs, _x.world_effector.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.world_effector.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.world_effector.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.world_effector.transforms = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Transform()
        _v15 = val1.translation
        _x = _v15
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v16 = val1.rotation
        _x = _v16
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.world_effector.transforms.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_4d = None
def _get_struct_4d():
    global _struct_4d
    if _struct_4d is None:
        _struct_4d = struct.Struct("<4d")
    return _struct_4d
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from visp_hand2eye_calibration/compute_effector_camera_quickResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class compute_effector_camera_quickResponse(genpy.Message):
  _md5sum = "e28a9ea34e6e135a6309cbdf6fb0ad0d"
  _type = "visp_hand2eye_calibration/compute_effector_camera_quickResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """geometry_msgs/Transform effector_camera

================================================================================
MSG: geometry_msgs/Transform
# This represents the transform between two coordinate frames in free space.

Vector3 translation
Quaternion rotation

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['effector_camera']
  _slot_types = ['geometry_msgs/Transform']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       effector_camera

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(compute_effector_camera_quickResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.effector_camera is None:
        self.effector_camera = geometry_msgs.msg.Transform()
    else:
      self.effector_camera = geometry_msgs.msg.Transform()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_7d().pack(_x.effector_camera.translation.x, _x.effector_camera.translation.y, _x.effector_camera.translation.z, _x.effector_camera.rotation.x, _x.effector_camera.rotation.y, _x.effector_camera.rotation.z, _x.effector_camera.rotation.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.effector_camera is None:
        self.effector_camera = geometry_msgs.msg.Transform()
      end = 0
      _x = self
      start = end
      end += 56
      (_x.effector_camera.translation.x, _x.effector_camera.translation.y, _x.effector_camera.translation.z, _x.effector_camera.rotation.x, _x.effector_camera.rotation.y, _x.effector_camera.rotation.z, _x.effector_camera.rotation.w,) = _get_struct_7d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_7d().pack(_x.effector_camera.translation.x, _x.effector_camera.translation.y, _x.effector_camera.translation.z, _x.effector_camera.rotation.x, _x.effector_camera.rotation.y, _x.effector_camera.rotation.z, _x.effector_camera.rotation.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.effector_camera is None:
        self.effector_camera = geometry_msgs.msg.Transform()
      end = 0
      _x = self
      start = end
      end += 56
      (_x.effector_camera.translation.x, _x.effector_camera.translation.y, _x.effector_camera.translation.z, _x.effector_camera.rotation.x, _x.effector_camera.rotation.y, _x.effector_camera.rotation.z, _x.effector_camera.rotation.w,) = _get_struct_7d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_7d = None
def _get_struct_7d():
    global _struct_7d
    if _struct_7d is None:
        _struct_7d = struct.Struct("<7d")
    return _struct_7d
class compute_effector_camera_quick(object):
  _type          = 'visp_hand2eye_calibration/compute_effector_camera_quick'
  _md5sum = 'ac7e8b661c5bfedda75b54410a11cf73'
  _request_class  = compute_effector_camera_quickRequest
  _response_class = compute_effector_camera_quickResponse
