import socketio
import json
import asyncio

class ClientSocket:
    def __init__(self):
        self.sio = socketio.AsyncClient()
        self.setup_sio()

    def setup_sio(self):
        @self.sio.event
        async def connect():
            print('connection established')
            await self.sio.emit('sendTime', 'TEST메세지 입니다. 안녕하세요')

        @self.sio.event
        async def order(data):
            print('received message from server:', data)
            try:
                json_data = json.loads(data)
                order_detail_id = json_data.get('order_detail_id')
                #target_grid = json_data.get('target_grid')
                
                print(order_detail_id)
            except json.JSONDecodeError:
                print('Invalid JSON format:', data)
            
        @self.sio.event
        async def disconnect():
            print('disconnected from server')
    
    async def start_socketio(self):
        await self.sio.connect('http://localhost:12001/')
        await self.sio.wait()

def main():
    client_socket = ClientSocket()  
    asyncio.get_event_loop().run_until_complete(client_socket.start_socketio())

if __name__ == '__main__':
    main()
