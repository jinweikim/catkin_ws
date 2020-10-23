;; Auto-generated. Do not edit!


(when (boundp 'interface::RobotControl)
  (if (not (find-package "INTERFACE"))
    (make-package "INTERFACE"))
  (shadow 'RobotControl (find-package "INTERFACE")))
(unless (find-package "INTERFACE::ROBOTCONTROL")
  (make-package "INTERFACE::ROBOTCONTROL"))
(unless (find-package "INTERFACE::ROBOTCONTROLREQUEST")
  (make-package "INTERFACE::ROBOTCONTROLREQUEST"))
(unless (find-package "INTERFACE::ROBOTCONTROLRESPONSE")
  (make-package "INTERFACE::ROBOTCONTROLRESPONSE"))

(in-package "ROS")





(defclass interface::RobotControlRequest
  :super ros::object
  :slots (_type _x _y _z _roll _pitch _yaw _virtual_debug _extra ))

(defmethod interface::RobotControlRequest
  (:init
   (&key
    ((:type __type) "")
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    ((:roll __roll) 0.0)
    ((:pitch __pitch) 0.0)
    ((:yaw __yaw) 0.0)
    ((:virtual_debug __virtual_debug) nil)
    ((:extra __extra) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _type (string __type))
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
   (setq _roll (float __roll))
   (setq _pitch (float __pitch))
   (setq _yaw (float __yaw))
   (setq _virtual_debug __virtual_debug)
   (setq _extra __extra)
   self)
  (:type
   (&optional __type)
   (if __type (setq _type __type)) _type)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:z
   (&optional __z)
   (if __z (setq _z __z)) _z)
  (:roll
   (&optional __roll)
   (if __roll (setq _roll __roll)) _roll)
  (:pitch
   (&optional __pitch)
   (if __pitch (setq _pitch __pitch)) _pitch)
  (:yaw
   (&optional __yaw)
   (if __yaw (setq _yaw __yaw)) _yaw)
  (:virtual_debug
   (&optional __virtual_debug)
   (if __virtual_debug (setq _virtual_debug __virtual_debug)) _virtual_debug)
  (:extra
   (&optional __extra)
   (if __extra (setq _extra __extra)) _extra)
  (:serialization-length
   ()
   (+
    ;; string _type
    4 (length _type)
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _z
    8
    ;; float64 _roll
    8
    ;; float64 _pitch
    8
    ;; float64 _yaw
    8
    ;; bool _virtual_debug
    1
    ;; float64[] _extra
    (* 8    (length _extra)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _type
       (write-long (length _type) s) (princ _type s)
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _z
       (sys::poke _z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _roll
       (sys::poke _roll (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _pitch
       (sys::poke _pitch (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _yaw
       (sys::poke _yaw (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; bool _virtual_debug
       (if _virtual_debug (write-byte -1 s) (write-byte 0 s))
     ;; float64[] _extra
     (write-long (length _extra) s)
     (dotimes (i (length _extra))
       (sys::poke (elt _extra i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _type
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _type (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _z
     (setq _z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _roll
     (setq _roll (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _pitch
     (setq _pitch (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _yaw
     (setq _yaw (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; bool _virtual_debug
     (setq _virtual_debug (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; float64[] _extra
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _extra (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _extra i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(defclass interface::RobotControlResponse
  :super ros::object
  :slots (_execute_result ))

(defmethod interface::RobotControlResponse
  (:init
   (&key
    ((:execute_result __execute_result) nil)
    )
   (send-super :init)
   (setq _execute_result __execute_result)
   self)
  (:execute_result
   (&optional __execute_result)
   (if __execute_result (setq _execute_result __execute_result)) _execute_result)
  (:serialization-length
   ()
   (+
    ;; bool _execute_result
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _execute_result
       (if _execute_result (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _execute_result
     (setq _execute_result (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass interface::RobotControl
  :super ros::object
  :slots ())

(setf (get interface::RobotControl :md5sum-) "06190d94b32e42f9d6491ffb2f6939f0")
(setf (get interface::RobotControl :datatype-) "interface/RobotControl")
(setf (get interface::RobotControl :request) interface::RobotControlRequest)
(setf (get interface::RobotControl :response) interface::RobotControlResponse)

(defmethod interface::RobotControlRequest
  (:response () (instance interface::RobotControlResponse :init)))

(setf (get interface::RobotControlRequest :md5sum-) "06190d94b32e42f9d6491ffb2f6939f0")
(setf (get interface::RobotControlRequest :datatype-) "interface/RobotControlRequest")
(setf (get interface::RobotControlRequest :definition-)
      "string type
float64 x
float64 y
float64 z
float64 roll
float64 pitch
float64 yaw
bool virtual_debug
float64[] extra
---
bool execute_result

")

(setf (get interface::RobotControlResponse :md5sum-) "06190d94b32e42f9d6491ffb2f6939f0")
(setf (get interface::RobotControlResponse :datatype-) "interface/RobotControlResponse")
(setf (get interface::RobotControlResponse :definition-)
      "string type
float64 x
float64 y
float64 z
float64 roll
float64 pitch
float64 yaw
bool virtual_debug
float64[] extra
---
bool execute_result

")



(provide :interface/RobotControl "06190d94b32e42f9d6491ffb2f6939f0")


