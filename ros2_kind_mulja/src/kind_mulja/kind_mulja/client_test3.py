import asyncio,socketio,json
import threading
import rclpy
from ssafy_msgs.msg import TargetGrid,WorkStatus
from rclpy.node import Node

truct_x=[-66.1336,-66.1336,-66.1336,-66.1336,-66.1336,-53.3041,-59.2474,-69.6383]
truct_y=[-56.8071,-60.8233,-64.8082,-68.8176,-72.8231,-52.488,-52.488,-52.488]
# truct_x=[-61.64,-53.581,-45.569,-37.532,-29.518]
# truct_y=[-58.0,-58.0,-58.0,-58.0,-58.0]

turtle_id_about_me=2
turtle_charge_x= -50.0
turtle_charge_y= -50.0
### float 형태로 해주세요 !!!!!!!
# turtle_charge_x= -50.0
# turtle_charge_y= -50.0

class Client(Node):
    def __init__(self):
        super().__init__('client')
        self.location_publisher=self.create_publisher(TargetGrid,'/target_grid',10)
        self.work_status_subscriber=self.create_subscription(WorkStatus,'/work_status',self.work_status_cb,10)

        self.work_status_msg=WorkStatus()
        
        # self.sio = socketio.AsyncClient()
        # self.setup_sio()
        self.sio = socketio.Client()
        
        self.order_detail_id=-99
        
        @self.sio.event
        def connect():
            print('connection established')
            self.sio.emit('sendTime','TEST메세지 입니다. 안녕하세요')
        
        @self.sio.event
        def order(data):
            try:
                json_data=json.loads(data)
                #json 파싱 
                print(data)
                local_num=json_data.get('moving_zone')
                product_x=json_data.get('product_x')  
                product_y=json_data.get('product_y')    
                self.order_detail_id=json_data.get('order_detail_id')   
                order_turtle_id=json_data.get('turtle_id')
                
                if order_turtle_id==turtle_id_about_me:                                                                      
                    if local_num is not None and product_y is not None and product_x is not None:
                            product_x = float(product_x)
                            product_y = float(product_y)
                            
                            #target_grid msg 작성 및 publish
                            moving_zone_x=truct_x[int(local_num)-1]
                            moving_zone_y=truct_y[int(local_num)-1]
                            
                            location_msg=TargetGrid()
                            location_msg.product_x=product_x
                            location_msg.product_y=product_y
                            location_msg.moving_zone_x=moving_zone_x
                            location_msg.moving_zone_y=moving_zone_y
                            location_msg.charge_x=turtle_charge_x
                            location_msg.charge_y=turtle_charge_y
                            
                            # location_msg.is_done=False
                            self.location_publisher.publish(location_msg)
                            # print(location_msg)
                            # print("1: ",self.work_status_msg)
            
                    else:
                        print('not found num and grid')
                else:
                    print("It's not my work") 
                        
            except json.JSONDecodeError:
                status_data={"turtle_id":order_turtle_id,"order_detail_id":self.order_detail_id,"value":1}
                json_status=json.dumps(status_data)
                self.sio.emit('socketStatus',json_status)
                print('Invalid JSON format:', data)
        
        @self.sio.event
        def disconnect():
            print('disconnected from server')
        
    def work_status_cb(self,msg):
        # print("3: ",msg)
        self.work_status_msg=msg
        # print(self.work_status_msg.is_start)
        
        if self.work_status_msg.is_start:
            self.send_work_turtle_status("start")
        else:
            self.send_work_turtle_status("done")

            
    def send_work_turtle_status(self,str):
        status_data={"turtle_id":turtle_id_about_me,"order_detail_id":self.order_detail_id,"work_status":str}
        json_status=json.dumps(status_data)
        print("status data: ", json_status)
        self.sio.emit('turtleStatus',json_status)
        
    
    def start_socketio(self):
        self.sio.connect('http://localhost:12001/')
        self.sio.wait()

    
 
   
def main():
    rclpy.init()
    client_node=Client()
    
    # loop=asyncio.get_event_loop()
    
    socket_thread=threading.Thread(target=client_node.start_socketio)
    socket_thread.start()
    
    rclpy.spin(client_node)
    client_node.destroy_node()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()

# loop.run_until_complete(main())
# loop.close()
    

# async def main():
#     rclpy.init()
#     client_node=Client()
    
#     # await client_node.start_socketio()
#     socket_thread=threading.Thread(target=client_node.start_socketio)
#     socket_thread.start()
    
#     while rclpy.ok():
#         rclpy.spin_once(client_node)
    
#     rclpy.spin(client_node)
#     client_node.destroy_node()
#     rclpy.shutdown()
    
    

# loop=asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()
