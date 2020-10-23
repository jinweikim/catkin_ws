;; Auto-generated. Do not edit!


(when (boundp 'interface::ControlRobot)
  (if (not (find-package "INTERFACE"))
    (make-package "INTERFACE"))
  (shadow 'ControlRobot (find-package "INTERFACE")))
(unless (find-package "INTERFACE::CONTROLROBOT")
  (make-package "INTERFACE::CONTROLROBOT"))
(unless (find-package "INTERFACE::CONTROLROBOTREQUEST")
  (make-package "INTERFACE::CONTROLROBOTREQUEST"))
(unless (find-package "INTERFACE::CONTROLROBOTRESPONSE")
  (make-package "INTERFACE::CONTROLROBOTRESPONSE"))

(in-package "ROS")





(defclass interface::ControlRobotRequest
  :super ros::object
  :slots (_x _y _z ))

(defmethod interface::ControlRobotRequest
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:z
   (&optional __z)
   (if __z (setq _z __z)) _z)
  (:serialization-length
   ()
   (+
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _z
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _z
       (sys::poke _z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _z
     (setq _z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass interface::ControlRobotResponse
  :super ros::object
  :slots (_execute_result ))

(defmethod interface::ControlRobotResponse
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

(defclass interface::ControlRobot
  :super ros::object
  :slots ())

(setf (get interface::ControlRobot :md5sum-) "681989edb1f8dcc80f4d6c0444e90e5f")
(setf (get interface::ControlRobot :datatype-) "interface/ControlRobot")
(setf (get interface::ControlRobot :request) interface::ControlRobotRequest)
(setf (get interface::ControlRobot :response) interface::ControlRobotResponse)

(defmethod interface::ControlRobotRequest
  (:response () (instance interface::ControlRobotResponse :init)))

(setf (get interface::ControlRobotRequest :md5sum-) "681989edb1f8dcc80f4d6c0444e90e5f")
(setf (get interface::ControlRobotRequest :datatype-) "interface/ControlRobotRequest")
(setf (get interface::ControlRobotRequest :definition-)
      "float64 x
float64 y
float64 z
---
bool execute_result

")

(setf (get interface::ControlRobotResponse :md5sum-) "681989edb1f8dcc80f4d6c0444e90e5f")
(setf (get interface::ControlRobotResponse :datatype-) "interface/ControlRobotResponse")
(setf (get interface::ControlRobotResponse :definition-)
      "float64 x
float64 y
float64 z
---
bool execute_result

")



(provide :interface/ControlRobot "681989edb1f8dcc80f4d6c0444e90e5f")


