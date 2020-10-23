;; Auto-generated. Do not edit!


(when (boundp 'uarm::CoordsWithTS4)
  (if (not (find-package "UARM"))
    (make-package "UARM"))
  (shadow 'CoordsWithTS4 (find-package "UARM")))
(unless (find-package "UARM::COORDSWITHTS4")
  (make-package "UARM::COORDSWITHTS4"))

(in-package "ROS")
;;//! \htmlinclude CoordsWithTS4.msg.html


(defclass uarm::CoordsWithTS4
  :super ros::object
  :slots (_x _y _z _time _servo_4 ))

(defmethod uarm::CoordsWithTS4
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    ((:time __time) 0)
    ((:servo_4 __servo_4) 0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
   (setq _time (round __time))
   (setq _servo_4 (round __servo_4))
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
  (:servo_4
   (&optional __servo_4)
   (if __servo_4 (setq _servo_4 __servo_4)) _servo_4)
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
    ;; uint8 _servo_4
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
     ;; uint8 _servo_4
       (write-byte _servo_4 s)
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
   ;; uint8 _servo_4
     (setq _servo_4 (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get uarm::CoordsWithTS4 :md5sum-) "d591a4c1754daa954bee92aa3a0cadd7")
(setf (get uarm::CoordsWithTS4 :datatype-) "uarm/CoordsWithTS4")
(setf (get uarm::CoordsWithTS4 :definition-)
      "float32 x
float32 y
float32 z
uint8 time
uint8 servo_4

")



(provide :uarm/CoordsWithTS4 "d591a4c1754daa954bee92aa3a0cadd7")


