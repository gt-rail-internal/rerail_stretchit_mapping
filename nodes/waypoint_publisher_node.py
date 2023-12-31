#!/usr/bin/env python
from stretchit_mapping.waypoint_map import WayPointMap
import rospy
import rospkg

log_lvls = {
   'DEBUG': rospy.DEBUG,
   'INFO': rospy.INFO,
   'WARN': rospy.WARN,
   'ERROR': rospy.ERROR,
   'FATAL': rospy.FATAL,
   'debug': rospy.DEBUG,
   'info': rospy.INFO,
   'warn': rospy.WARN,
   'error': rospy.ERROR,
   'fatal': rospy.FATAL,
}

if __name__ == "__main__":
   """
   Initialize the node
   """
   log_lvl = rospy.get_param("/logger_lvl", 'INFO')
   rospy.init_node('waypoint_publisher_node', log_level=log_lvls[log_lvl])

   # gets the roslaunch params. die if this very important param is not
   # specified
   waypoint_map_fp = rospy.get_param("~waypoint_map_filepath")

   # load map and publish
   wp_map_pub = WayPointMap(waypoint_map_fp)
   wp_map_pub.run_broadcaster()