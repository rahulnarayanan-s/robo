#!/usr/bin/env python3

import rclpy   
from rclpy.node import Node
from example_interfaces.msg import Int64 

class MyNode (Node):
   def __init__ (self):
      super().__init__("number_counter")
      self.get_logger().info("counting the number")
      self.subscriper_=self.create_subscription(
         Int64,"number",self.timer_callback,10)
      self.counter = 0
      self.publisher_  = self.create_publisher(
         Int64,"number_counter",10 )
   

   def timer_callback(self,msg):
      self.counter += msg.data
      new_msg = Int64()
      new_msg.data = self.counter
      self.publisher_.publish(new_msg)
      self.get_logger().info(str(new_msg.data))
      self.counter += 1

def main (args = None):
    rclpy.init(args = args )
    node =MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
  main()