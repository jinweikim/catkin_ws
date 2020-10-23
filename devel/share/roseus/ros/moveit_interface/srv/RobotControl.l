;; Auto-generated. Do not edit!


(when (boundp 'moveit_interface::RobotControl)
  (if (not (find-package "MOVEIT_INTERFACE"))
    (make-package "MOVEIT_INTERFACE"))
  (shadow 'RobotControl (find-package "MOVEIT_INTERFACE")))
(unless (find-package "MOVEIT_INTERFACE::ROBOTCONTROL")
  (make-package "MOVEIT_INTERFACE::ROBOTCONTROL"))
(unless (find-package "MOVEIT_INTERFACE::ROBOTCONTROLREQUEST")
  (make-package "MOVEIT_INTERFACE::ROBOTCONTROLREQUEST"))
(unless (find-package "MOVEIT_INTERFACE::ROBOTCONTROLRESPONSE")
  (make-package "MOVEIT_INTERFACE::ROBOTCONTROLRESPONSE"))

(in-package "ROS")





(defclass moveit_interface::RobotControlRequest
  :super ros::object
  :slots (_type _x _y _z _roll _pitch _yaw _extra ))

(defmethod moveit_interface::RobotControlRequest
  (:init
   (&key
    ((:type __type) "")
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    ((:roll __roll) 0.0)
    ((:pitch __pitch) 0.0)
    ((:yaw __yaw) 0.0)
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

(defclass moveit_interface::RobotControlResponse
  :super ros::object
  :slots (_execute_result ))

(defmethod moveit_interface::RobotControlResponse
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

(defclass moveit_interface::RobotControl
  :super ros::object
  :slots ())

(setf (get moveit_interface::RobotControl :md5sum-) "f4178e569aa36a63f67d15ee7547eaac")
(setf (get moveit_interface::RobotControl :datatype-) "moveit_interface/RobotControl")
(setf (get moveit_interface::RobotControl :request) moveit_interface::RobotControlRequest)
(setf (get moveit_interface::RobotControl :response) moveit_interface::RobotControlResponse)

(defmethod moveit_interface::RobotControlRequest
  (:response () (instance moveit_interface::RobotControlResponse :init)))

(setf (get moveit_interface::RobotControlRequest :md5sum-) "f4178e569aa36a63f67d15ee7547eaac")
(setf (get moveit_interface::RobotControlRequest :datatype-) "moveit_interface/RobotControlRequest")
(setf (get moveit_interface::RobotControlRequest :definition-)
      "string type
float64 x
float64 y
float64 z
float64 roll
float64 pitch
float64 yaw
float64[] extra
---
bool execute_result

")

(setf (get moveit_interface::RobotControlResponse :md5sum-) "f4178e569aa36a63f67d15ee7547eaac")
(setf (get moveit_interface::RobotControlResponse :datatype-) "moveit_interface/RobotControlResponse")
(setf (get moveit_interface::RobotControlResponse :definition-)
      "string type
float64 x
float64 y
float64 z
float64 roll
float64 pitch
float64 yaw
float64[] extra
---
bool execute_result

")



(provide :moveit_interface/RobotControl "f4178e569aa36a63f67d15ee7547eaac")


