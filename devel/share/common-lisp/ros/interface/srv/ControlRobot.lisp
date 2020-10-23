; Auto-generated. Do not edit!


(cl:in-package interface-srv)


;//! \htmlinclude ControlRobot-request.msg.html

(cl:defclass <ControlRobot-request> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0)
   (z
    :reader z
    :initarg :z
    :type cl:float
    :initform 0.0))
)

(cl:defclass ControlRobot-request (<ControlRobot-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ControlRobot-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ControlRobot-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name interface-srv:<ControlRobot-request> is deprecated: use interface-srv:ControlRobot-request instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <ControlRobot-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader interface-srv:x-val is deprecated.  Use interface-srv:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <ControlRobot-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader interface-srv:y-val is deprecated.  Use interface-srv:y instead.")
  (y m))

(cl:ensure-generic-function 'z-val :lambda-list '(m))
(cl:defmethod z-val ((m <ControlRobot-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader interface-srv:z-val is deprecated.  Use interface-srv:z instead.")
  (z m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ControlRobot-request>) ostream)
  "Serializes a message object of type '<ControlRobot-request>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ControlRobot-request>) istream)
  "Deserializes a message object of type '<ControlRobot-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'z) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ControlRobot-request>)))
  "Returns string type for a service object of type '<ControlRobot-request>"
  "interface/ControlRobotRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ControlRobot-request)))
  "Returns string type for a service object of type 'ControlRobot-request"
  "interface/ControlRobotRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ControlRobot-request>)))
  "Returns md5sum for a message object of type '<ControlRobot-request>"
  "681989edb1f8dcc80f4d6c0444e90e5f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ControlRobot-request)))
  "Returns md5sum for a message object of type 'ControlRobot-request"
  "681989edb1f8dcc80f4d6c0444e90e5f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ControlRobot-request>)))
  "Returns full string definition for message of type '<ControlRobot-request>"
  (cl:format cl:nil "float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ControlRobot-request)))
  "Returns full string definition for message of type 'ControlRobot-request"
  (cl:format cl:nil "float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ControlRobot-request>))
  (cl:+ 0
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ControlRobot-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ControlRobot-request
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':z (z msg))
))
;//! \htmlinclude ControlRobot-response.msg.html

(cl:defclass <ControlRobot-response> (roslisp-msg-protocol:ros-message)
  ((execute_result
    :reader execute_result
    :initarg :execute_result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass ControlRobot-response (<ControlRobot-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ControlRobot-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ControlRobot-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name interface-srv:<ControlRobot-response> is deprecated: use interface-srv:ControlRobot-response instead.")))

(cl:ensure-generic-function 'execute_result-val :lambda-list '(m))
(cl:defmethod execute_result-val ((m <ControlRobot-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader interface-srv:execute_result-val is deprecated.  Use interface-srv:execute_result instead.")
  (execute_result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ControlRobot-response>) ostream)
  "Serializes a message object of type '<ControlRobot-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'execute_result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ControlRobot-response>) istream)
  "Deserializes a message object of type '<ControlRobot-response>"
    (cl:setf (cl:slot-value msg 'execute_result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ControlRobot-response>)))
  "Returns string type for a service object of type '<ControlRobot-response>"
  "interface/ControlRobotResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ControlRobot-response)))
  "Returns string type for a service object of type 'ControlRobot-response"
  "interface/ControlRobotResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ControlRobot-response>)))
  "Returns md5sum for a message object of type '<ControlRobot-response>"
  "681989edb1f8dcc80f4d6c0444e90e5f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ControlRobot-response)))
  "Returns md5sum for a message object of type 'ControlRobot-response"
  "681989edb1f8dcc80f4d6c0444e90e5f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ControlRobot-response>)))
  "Returns full string definition for message of type '<ControlRobot-response>"
  (cl:format cl:nil "bool execute_result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ControlRobot-response)))
  "Returns full string definition for message of type 'ControlRobot-response"
  (cl:format cl:nil "bool execute_result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ControlRobot-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ControlRobot-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ControlRobot-response
    (cl:cons ':execute_result (execute_result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ControlRobot)))
  'ControlRobot-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ControlRobot)))
  'ControlRobot-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ControlRobot)))
  "Returns string type for a service object of type '<ControlRobot>"
  "interface/ControlRobot")