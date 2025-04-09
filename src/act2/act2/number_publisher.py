import rclpy   
from rclpy.node import Node
from example_interfaces.msg import String
from std_msgs.msg import Int32

class numpublisher (Node):
   def __init__ (self):
      super().__init__("number_pub")
      self.get_logger().info("sart_publishing")
      self.counter_ = 2
      self.publisher_= self.create_publisher(Int32,"number",10) 
      self.timer_= self.create_timer(0.5,self.publisher_num)


   def publisher_num(self):
      msg = Int32()
      msg.data = self.counter_
      self.publisher_.publish(msg)
      self.get_logger().info(str(msg.data))
      # self. counter_ +=1


class counternode (Node):
   def __init__ (self):
      super().__init__("counter_pub")
      self.get_logger().info("sart_publishing")
      self.counter = 0
      self.subscriber_= self.create_subscription(
         Int32,"number",self.callback_timer,10)  
      self.publisher_= self.create_publisher(
         Int32,"number_counter",10)

   def callback_timer(self,msg):
      self.counter += msg.data
      new_msg = Int32()
      new_msg.data = self.counter
      self.publisher_.publish(new_msg)
      self.get_logger().info(str(new_msg.data))


def main (args = None):
      rclpy.init(args = args )
      num_node = numpublisher()
      counter_node = counternode()
      executor = rclpy.executors.MultiThreadedExecutor()
      executor.add_node(num_node)
      executor.add_node(counter_node)
      
      try:
         executor.spin()
      except KeyboardInterrupt:
         pass
      finally:
         num_node.destroy_node()
         counter_node.destroy_node()
         rclpy.shutdown()


if __name__ == "__main__":
  main()