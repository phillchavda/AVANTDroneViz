import rclpy
from rclpy.node import Node
import csv
from geometry_msgs.msg import Twist
import datetime

class SubscriberClass(Node):

    def __init__(self):
        super().__init__('subscriber_node')

        self.fieldnames = ['velocidade_linear', 'velocidade_angular',  'tempo']
        with open('velocidade.csv', 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            csv_writer.writeheader()

        self.subscription = self.create_subscription(Twist,'turtle1/cmd_vel',self.subscriber_callback,1)
        self.subscription 
        


    def subscriber_callback(self, msg): 
        self.get_logger().info('Recieved - Linear Velocity: %f, Angualr Velocity: %f' % (msg.linear.x, msg.angular.z))
        now = datetime.datetime.now()

        with open('velocidade.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames= self.fieldnames)
            
            info = {'velocidade_linear': msg.linear.x, 'velocidade_angular': msg.angular.z, 'tempo': now.strftime("%H:%M:%S")}

            csv_writer.writerow(info)
            csv_file.close()

            

def main():
    rclpy.init()

    node = SubscriberClass()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
