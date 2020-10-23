;; Auto-generated. Do not edit!


(when (boundp 'uarm::CoordsWithTime)
  (if (not (find-package "UARM"))
    (make-package "UARM"))
  (shadow 'CoordsWithTime (find-package "UARM")))
(unless (find-package "UARM::COORDSWITHTIME")
  (make-package "UARM::COORDSWITHTIME"))

(in-package "ROS")
;;//! \htmlinclude CoordsWithTime.msg.html


(defclass uarm::CoordsWithTime
  :super ros::object
  :slots (_x _y _z _time ))

(defmethod uarm::CoordsWithTime
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    ((:time __time) 0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
   (setq _time (round __time))
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
  (:time
   (&optional __time)
   (if __time (setq _time __time)) _time)
  (:serialization-length
   ()
   (+
    ;; float32 _x
    4
    ;; float32 _y
    4
    ;; float32 _z
    4
    ;; uint8 _time
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _x
       (sys::poke _x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y
       (sys::poke _y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _z
       (sys::poke _z (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; uint8 _time
       (write-byte _time s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _z
     (setq _z (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; uint8 _time
     (setq _time (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get uarm::CoordsWithTime :md5sum-) "b3627db2ce9496e2653c112694e2c5fa")
(setf (get uarm::CoordsWithTime :datatype-) "uarm/CoordsWithTime")
(setf (get uarm::CoordsWithTime :definition-)
      "float32 x
float32 y
float32 z
uint8 time


")



(provide :uarm/CoordsWithTime "b3627db2ce9496e2653c112694e2c5fa")


