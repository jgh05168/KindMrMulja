import asyncio,socketio,json
import rclpy
from ssafy_msgs.msg import TargetGrid,WorkStatus
from rclpy.node import Node

truct_x=[-61.6042,-53.5767,-45.5926,-37.5455,-37.5455]
truct_y=[-59.33,-59.33,-59.33,-59.33,-59.33]
tutle_id=1

class Client(Node):
    def __init__(self):
        super().__init__('client')
        self.location_publisher=self.create_publisher(TargetGrid,'/target_grid',10)
        self.work_status_subscriber=self.create_subscription(WorkStatus,'/work_status',self.work_status_cb,10)

        self.work_status_msg=WorkStatus()
        
        self.sio = socketio.AsyncClient()
        self.setup_sio()
        
        self.order_detail_id=-99
        
    def work_status_cb(self,msg):
        print("hihih")
        self.work_status_msg=msg
        print(self.work_status_msg.is_start)
        
    def setup_sio(self):
        @self.sio.event
        async def connect():
            print('connection established')
            await self.sio.emit('sendTime','TEST메세지 입니다. 안녕하세요')
        
        @self.sio.event
        async def order(data):
            try:
                json_data=json.loads(data)
                #json 파싱 
                local_num=json_data.get('moving_zone')
                product_x=json_data.get('product_x')  
                product_y=json_data.get('product_y')    
                self.order_detail_id=json_data.get('order_detail_id')    
                turtle_id = json_data.get('turtle_id')
                
                if local_num is not None and product_y is not None and product_x is not None and turtle_id is tutle_id:
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
                    # location_msg.is_done=False
                    self.location_publisher.publish(location_msg)
                    print(location_msg)
                    print("1: ",self.work_status_msg)
    
                else:
                    print('not found num and grid')
                    
                print("2: ",self.work_status_msg)
            
                if self.work_status_msg.is_start:
                    print("is_start")
                    
            except json.JSONDecodeError:
                status_data={"tutle_id":tutle_id,"order_detail_id":self.order_detail_id,"value":1}
                json_status=json.dumps(status_data)
                await self.sio.emit('socketStatus',json_status)
                print('Invalid JSON format:', data)   

        @self.sio.event
        async def disconnect():
            await print('disconnected from server')     
    

        
    async def start_socketio(self):
        await self.sio.connect('http://localhost:12001/')
        await self.sio.wait()
        
    

async def main():
    rclpy.init()
    client_node=Client()
    
    await client_node.start_socketio()
    
    while rclpy.ok():
        rclpy.spin_once(client_node)
    
    rclpy.spin(client_node)
    client_node.destroy_node()
    rclpy.shutdown()
    
    

loop=asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
