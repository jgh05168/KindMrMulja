import socketio
import json
import asyncio
import rclpy
from ssafy_msgs.msg import TargetGrid


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
truct_x=[-45.0,20.0,30.0,40.0,50.0]
truct_y=[-58.0,50.0,50.0,50.0,50.0]

# 터틀봇 충전소 위치 
charge_x=-49.0
charge_y=-28.0

# 로직 1. 클라이언트 소켓 생성
sio = socketio.AsyncClient()
# sio = socketio.Client()

rclpy.init()

location_node=rclpy.create_node('socket_to_location_publisher')

location_publisher=location_node.create_publisher(TargetGrid,'/target_grid',10)


# 서버 연결 
@sio.event
async def connect():
    print('connection established')
    
    await sio.emit('sendTime','TEST메세지 입니다. 안녕하세요')


# 로직 2. 데이터 수신 콜백함수
# 1. json 파싱
# 2. TargetGrid msg 작성
# 3. msg Publish
 
@sio.event
async def order(data):
    print('recevied massage from server : ',data)
    # json 받기 
    try:
        json_data=json.loads(data)
        #json 파싱 
        local_num=json_data.get('num')
        target_grid=json_data.get('grid')
        
        if local_num is not None and target_grid is not None:
            product_x = float(target_grid.get('x'))
            product_y = float(target_grid.get('y'))
            
            #target_grid msg 작성 및 publish
            moving_zone_x=truct_x[int(local_num)-1]
            moving_zone_y=truct_y[int(local_num)-1]
            
            location_msg=TargetGrid()
            location_msg.product_x=product_x
            location_msg.product_y=product_y
            location_msg.moving_zone_x=moving_zone_x
            location_msg.moving_zone_y=moving_zone_y
            location_msg.is_done=False
            location_publisher.publish(location_msg)
            print(location_msg)
            
        else:
            print('not found num and grid')
    except json.JSONDecodeError:
        print('Invalid JSON format:', data)
    
@sio.event
async def disconnect():
    await print('disconnected from server')
    
async def start_socketio():
    await sio.connect('http://localhost:12001/')
    await sio.wait()

async def main():
    await start_socketio()

if __name__ == '__main__':
    asyncio.run(main())


# 로직 3. 서버 연결
# sio.connect('http://ec2-3-34-134-166.ap-northeast-2.compute.amazonaws.com:12001/')
# sio.connect('http://localhost:12001/')

# 로직 4. 데이터 송신


sio.wait()
sio.disconnect()
