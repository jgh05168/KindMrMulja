import socketio
import json
import asyncio

class ClientSocket:
    def __init__(self):
        self.sio = socketio.AsyncClient()
        self.setup_sio()

    def setup_sio(self):
        
        @self.sio.event
        async def order(data):
            print('received message from server:', data)
            try:
                json_data = json.loads(data)
                turtle_id = json_data.get('turtle_id')
                order_detail_id = json_data.get('order_detail_id')
                product_x = json_data.get('product_x')
                product_y = json_data.get('product_y')
                moving_zone = json_data.get('moving_zone')

                # 받은 데이터를 기반으로 새로운 데이터 생성
                new_data = {
                    "turtle_id": turtle_id,
                    "order_detail_id": order_detail_id,
                    "work_status": "done"  # 새로운 데이터의 work_status를 설정
                }
                new_json_data = json.dumps(new_data)

                # 생성한 새로운 데이터를 turtleStatus로 보냄
                await self.sio.emit('turtleStatus', new_json_data)

            except json.JSONDecodeError:
                print('Invalid JSON format:', data)

        # @self.sio.event
        # async def connect():
        #     data = {
        #         "turtle_id": 1,
        #         "order_detail_id": 93,
        #         "work_status": "start"
        #     }
        #     jsonData = json.dumps(data)
        #     print('connection established')
        #     await self.sio.emit('turtleStatus', jsonData)
            
        @self.sio.event
        async def disconnect():
            print('disconnected from server')
    
    async def start_socketio(self):
        await self.sio.connect('http://localhost:12001/')
        await self.sio.wait()

    # async def start_socketio(self):
    #     await self.sio.connect('http://localhost:12002/')
    #     await self.sio.wait()

def main():
    client_socket = ClientSocket()  
    asyncio.get_event_loop().run_until_complete(client_socket.start_socketio())

if __name__ == '__main__':
    main()
