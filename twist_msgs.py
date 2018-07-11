from geometry_msgs.msg import Twist

velocity_pub = rospy.Publisher('/pioneer/cmd_vel', Twist, queue_size=1)

def move(msg):
    vel_msg = Twist()

    vel_msg.linear.x = msg.get('linear_x', 0)
    vel_msg.linear.y = msg.get('linear_y', 0)
    vel_msg.linear.z = msg.get('linear_z', 0)
    vel_msg.angular.x = msg.get('angular_x', 0)
    vel_msg.angular.y = msg.get('angular_y', 0)
    vel_msg.angular.z = msg.get('angular_z', 0)

    velocity_pub.publish(vel_msg)
