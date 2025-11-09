import os
from cv2 import aruco

# Robot Params #
nuc_ip = "192.168.0.174"
# nuc_ip = "0.0.0.0"
robot_ip = "172.16.0.2"
laptop_ip = "192.168.0.44"
sudo_password = "necl"
robot_type = "panda"  # 'panda' or 'fr3'
robot_serial_number = "289830-1325797"

# Camera ID's #
hand_camera_id = "14452055"
varied_camera_1_id = "23474280"
# varied_camera_2_id = ""

# Charuco Board Params #
CHARUCOBOARD_ROWCOUNT = 9
CHARUCOBOARD_COLCOUNT = 14
CHARUCOBOARD_CHECKER_SIZE = 0.020
CHARUCOBOARD_MARKER_SIZE = 0.015
ARUCO_DICT = aruco.Dictionary_get(aruco.DICT_5X5_100)

# Ubuntu Pro Token (RT PATCH) #
ubuntu_pro_token = "C136Sh44GFGn9m8xSGwPivM62SqNrh"

# Code Version [DONT CHANGE] #
droid_version = "1.3"

