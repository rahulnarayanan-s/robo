#!/usr/bin/env python3 
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class smartphon(Node):
    def __init__(self):
        super().__init__("smart_phone")
        self.get_logger().info("ready to recive")
        self.subscriber_=self.create_subscription(
            String,"robotnews",self.callback_robot_news,10)
       


    def callback_robot_news(self,msg: String):
        self.get_logger().info(msg.data)

def main(args=None):
    rclpy.init(args=args)
    node= smartphon()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__" :
   main()