import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/unknown/ros2_setup_scripts/ros2_ws/src/mypkg/install/mypkg'
