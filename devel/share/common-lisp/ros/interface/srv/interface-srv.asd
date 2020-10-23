
(cl:in-package :asdf)

(defsystem "interface-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "RobotControl" :depends-on ("_package_RobotControl"))
    (:file "_package_RobotControl" :depends-on ("_package"))
  ))