#!/user/bin/python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
n=0
def cd():
    global n
    msg=Int16()
    msd.data = n
    pub.publish(meg)
    n+=1

node.create_timer(0.5,cb)
rclpy.spin(node)
