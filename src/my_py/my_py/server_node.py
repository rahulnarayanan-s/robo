#!/usr/bin/env python3 
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class addtwoint(Node):
    def __init__(self):
        super().__init__("add_two_int")
      
        self.server_=self.create_service(
            AddTwoInts,"add_two_int",self.callback_add_two_inits
        )
        self.get_logger().info("give imput for sum")

    def callback_add_two_inits(
            self,request: AddTwoInts.Request,response: AddTwoInts.Response):
        response.sum = request.a +request.b
        
        self.get_logger().info(str(request.a)+" + "+
                               str(request.b)+ " = " + str(response.sum))
        return response

def main(args=None):
    rclpy.init(args=args)
    node= addtwoint()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__" :
   main()