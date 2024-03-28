import socketio
import json
import asyncio
import rclpy
from rclpy.node import Node
from ssafy_msgs.msg import TargetGrid,WorkStatus


# client 는 socketio의 기본 API로 구성된 노드입니다. 서버와 연결을 시도해서 서버와 통신을 합니다.

# 각자의 서버 주소에 맞게 connect 함수 안을 바꿔주고, server 스켈레톤코드를 이용해 서비스를 하고 있다면, 연결이 됩니다.
# 버튼을 누르면 해당 키값에 맞는 함수들이 호출이 됩니다. 연결이 된 후에는 emit 함수를 이용해 서버로 키값과 데이터를 보냅니다.
# 이 노드는 AWS EC2에 구축한 서버와 통신만 하는 노드이고, ROS2와 연동하여 사용하면 스마트홈에서 얻은 데이터들을 서버로 보내고, 웹서버로부터의 명령을 ROS2로 전달할 수 있습니다.

# 노드 로직 순서
# 1. 클라이언트 소켓 생성
# 2. 데이터 수신 콜백함수
# 3. 서버 연결
# 4. 데이터 송신

# 트럭 위치 배열 
truct_x=[-61.6042,-53.5767,-45.5926,-37.5455,-37.5455]
truct_y=[-59.33,-59.33,-59.33,-59.33,-59.33]

# 터틀봇 충전소 위치 
charge_x=-49.0
charge_y=-28.0

# 로직 1. 클라이언트 소켓 생성
# sio = socketio.AsyncClient()
# sio = socketio.Client()

# rclpy.init()
tutle_id=1

class client(Node):
    def __init__(self):
        super().__init__('client')
        self.location_publisher=self.create_publisher(TargetGrid,'/target_grid',10)
        
        self.work_status_subscriber=self.create_subscription(WorkStatus,'/work_status',self.work_status_cb,10)

        self.sio = socketio.AsyncClient()
        self.setup_sio()
        
        self.work_status_msg=WorkStatus()
        
        self.order_detail_id=-99
# location_node=rclpy.create_node('socket_to_location_publisher')

# location_publisher=location_node.create_publisher(TargetGrid,'/target_grid',10)



        
    def setup_sio(self):
        # 서버 연결 
        @self.sio.event
        async def connect():
            print('connection established')
            
            await self.sio.emit('sendTime','TEST메세지 입니다. 안녕하세요')


        # 로직 2. 데이터 수신 콜백함수
        # 1. json 파싱
        # 2. TargetGrid msg 작성
        # 3. msg Publish
        
        @self.sio.event
        async def order(data):
            print('recevied massage from server : ',data)
            # json 받기 
            try:
                json_data=json.loads(data)
                #json 파싱 
                local_num=json_data.get('moving_zone')
                product_x=json_data.get('product_x')  
                product_y=json_data.get('product_y')    
                self.order_detail_id=json_data.get('order_detail_id')    
                                                                       
                
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
                    # location_msg.is_done=False
                    self.location_publisher.publish(location_msg)
                    print(location_msg)
                    
                    
                    # 상품 위치까지 msg를 전달했다면 서버에 start 메세지 보내기 
                    # status_data={"tutle_id":tutle_id,"order_detail_id":self.order_detail_id,"work_status":"start"}
                    # json_status=json.dumps(status_data)
                    # print("status data: ", json_status)
                    # await self.sio.emit('tutleStatus',json_status)
                    
                else:
                    print('not found num and grid')
            except json.JSONDecodeError:
                status_data={"tutle_id":tutle_id,"order_detail_id":self.order_detail_id,"value":1}
                json_status=json.dumps(status_data)
                await self.sio.emit('socketStatus',json_status)
                print('Invalid JSON format:', data)
            
        @self.sio.event
        async def disconnect():
            await print('disconnected from server')
            
    async def work_status_cb(self,msg):
        self.work_status_msg=msg
        print(self.work_status_msg.is_start)

        # if self.work_status_msg.is_start==True:
        #     self.send_work_tutle_status("start")
        # elif self.work_status_msg.is_done==True:
        #     self.send_work_tutle_status("done")
            
        
    async def send_work_tutle_status(self,str):
        status_data={"tutle_id":tutle_id,"order_detail_id":self.order_detail_id,"work_status":str}
        json_status=json.dumps(status_data)
        print("status data: ", json_status)
        await self.sio.emit('tutleStatus',json_status)
        
    
    async def start_socketio(self):
        await self.sio.connect('http://localhost:12001/')
        await self.sio.wait()

async def main():
    # rclpy.init()
    
    # socket_to_location_publisher = client()  
    # asyncio.get_event_loop().run_until_complete(socket_to_location_publisher.start_socketio())
    # rclpy.spin(socket_to_location_publisher)
    # socket_to_location_publisher.destroy_node()
    # rclpy.shutdown()
    rclpy.init()
    client_node = client()
    # await client_node.start_socketio()
    try:
        asyncio.run(client_node.start_socketio())
        while rclpy.ok():
            rclpy.spin_once(client_node, timeout_sec=0.1)
            # 추가적인 작업 수행 가능
    finally:
        client_node.destroy_node()
        rclpy.shutdown()
    

if __name__ == '__main__':
    main()

# 로직 3. 서버 연결
# sio.connect('http://ec2-3-34-134-166.ap-northeast-2.compute.amazonaws.com:12001/')
# sio.connect('http://localhost:12001/')

# 로직 4. 데이터 송신


# sio.wait()
# sio.disconnect()
