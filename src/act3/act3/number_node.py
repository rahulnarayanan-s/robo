#!/usr/bin/env python3

import rclpy   
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberNode (Node):
   def __init__ (self):
      super().__init__("number_node")
      self.publisher_= self.create_publisher(
         Int64,"number",10)
      self.get_logger().info("printing number")
      self.counter = 2
      self.timer_= self.create_timer(1.0,self.publisher)

   def publisher(self):
      msg =  Int64()
      msg.data = self.counter
      self.publisher_.publish(msg)
      


def main (args = None):
    rclpy.init(args = args )
    node =NumberNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
  main()