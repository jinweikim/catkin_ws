;; Auto-generated. Do not edit!


(when (boundp 'uarm::Angles)
  (if (not (find-package "UARM"))
    (make-package "UARM"))
  (shadow 'Angles (find-package "UARM")))
(unless (find-package "UARM::ANGLES")
  (make-package "UARM::ANGLES"))

(in-package "ROS")
;;//! \htmlinclude Angles.msg.html


(defclass uarm::Angles
  :super ros::object
  :slots (_servo_1 _servo_2 _servo_3 _servo_4 ))

(defmethod uarm::Angles
  (:init
   (&key
    ((:servo_1 __servo_1) 0)
    ((:servo_2 __servo_2) 0)
    ((:servo_3 __servo_3) 0)
    ((:servo_4 __servo_4) 0)
    )
   (send-super :init)
   (setq _servo_1 (round __servo_1))
   (setq _servo_2 (round __servo_2))
   (setq _servo_3 (round __servo_3))
   (setq _servo_4 (round __servo_4))
   self)
  (:servo_1
   (&optional __servo_1)
   (if __servo_1 (setq _servo_1 __servo_1)) _servo_1)
  (:servo_2
   (&optional __servo_2)
   (if __servo_2 (setq _servo_2 __servo_2)) _servo_2)
  (:servo_3
   (&optional __servo_3)
   (if __servo_3 (setq _servo_3 __servo_3)) _servo_3)
  (:servo_4
   (&optional __servo_4)
   (if __servo_4 (setq _servo_4 __servo_4)) _servo_4)
  (:serialization-length
   ()
   (+
    ;; uint8 _servo_1
    1
    ;; uint8 _servo_2
    1
    ;; uint8 _servo_3
    1
    ;; uint8 _servo_4
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _servo_1
       (write-byte _servo_1 s)
     ;; uint8 _servo_2
       (write-byte _servo_2 s)
     ;; uint8 _servo_3
       (write-byte _servo_3 s)
     ;; uint8 _servo_4
       (write-byte _servo_4 s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _servo_1
     (setq _servo_1 (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _servo_2
     (setq _servo_2 (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _servo_3
     (setq _servo_3 (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _servo_4
     (setq _servo_4 (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get uarm::Angles :md5sum-) "c365f7c0f52d109b4b516ca588b94bd3")
(setf (get uarm::Angles :datatype-) "uarm/Angles")
(setf (get uarm::Angles :definition-)
      "uint8 servo_1
uint8 servo_2
uint8 servo_3
uint8 servo_4

")



(provide :uarm/Angles "c365f7c0f52d109b4b516ca588b94bd3")


