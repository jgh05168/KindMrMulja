import rclpy
import numpy as np
from rclpy.node import Node

import os
from geometry_msgs.msg import Pose
from squaternion import Quaternion
from nav_msgs.msg import Odometry,OccupancyGrid,MapMetaData
from math import pi

# load_map 노드는 맵 데이터를 읽어서, 맵 상에서 점유영역(장애물) 근처에 로봇이 움직일 수 없는 영역을 설정하고 맵 데이터로 publish 해주는 노드입니다.
# 추 후 a_star 알고리즘에서 맵 데이터를 subscribe 해서 사용합니다.

# 노드 로직 순서
# 1. 맵 파라미터 설정
# 2. 맵 데이터 읽고, 2차원 행렬로 변환
# 3. 점유영역 근처 필터처리

class loadMap(Node):

    def __init__(self):
        super().__init__('load_map')
        self.map_pub = self.create_publisher(OccupancyGrid, 'map', 1)
        
        time_period=1  
        self.timer = self.create_timer(time_period, self.timer_callback)
       
        # 로직 1. 맵 파라미터 설정
        # 제공한 맵 데이터의 파라미터입니다. size_x,y는 x,y 방향으로 grid의 개수이고, resolution은 grid 하나당 0.05m라는 것을 의미합니다.
        # offset_x,y 의 -8, -4 는 맵 데이터가 기준 좌표계(map)로 부터 떨어진 거리를 의미합니다. 
        # 각 항에 -25를 뺀이유는 ros에서 occupancygrid의 offset이라는 데이터는 맵의 중앙에서 기준좌표계까지 거리가 아니라 맵의 우측하단에서 부터 기준좌표계까지의 거리를 의미합니다.
        # 따라서 (250*0.05)/2를 해준 값을 빼줍니다.
        self.map_msg=OccupancyGrid()
        self.map_size_x=250 
        self.map_size_y=250
        self.map_resolution=0.2
        self.map_offset_x=-50-25.0
        self.map_offset_y=-50-25.0
        self.map_data = [0 for i in range(self.map_size_x*self.map_size_y)]
        grid=np.array(self.map_data)
        grid=np.reshape(grid,(250, 250))

        self.map_msg.header.frame_id="map"

        #int((robot_pose_y - self.map_offset_y) / self.map_resolution)

        m = MapMetaData()
        m.resolution = self.map_resolution
        m.width = self.map_size_x
        m.height = self.map_size_y
        m.origin = Pose()
        m.origin.position.x = self.map_offset_x
        m.origin.position.y = self.map_offset_y

        self.map_meta_data = m
        self.map_msg.info=self.map_meta_data
        


        '''
        로직 2. 맵 데이터 읽고, 2차원 행렬로 변환
        '''
        pkg_path =os.getcwd()
        back_folder='..'
        folder_name='map'
        file_name='map.txt'
        full_path=os.path.join(pkg_path,back_folder,folder_name,file_name)

        self.f=open(full_path,'r')

        line=self.f.readlines()
        line_data=line[0].split()
        for num,data in enumerate(line_data) :
            if num < 250*250:
                self.map_data[num]=int(data)
   
        
        map_to_grid=np.array(self.map_data)
        grid=np.reshape(map_to_grid,(250, 250))


        for y in range(250):
            for x in range(250):

                if grid[x][y]==100 :
                    '''
                    로직 3. 점유영역 근처 필터처리
                    '''
                    for box_x in range(-5,6):
                        for box_y in range(-5,6):
                            if  0< x+box_x < 250 and 0 < y+box_y <250 and grid[x+box_x][y+box_y]<80 :
                                grid[x+box_x][y+box_y]=127
        
        for i in range(5):
            grid[85][74+i]=0
            grid[53][60-i]=0
            grid[72][91-i]=0
            grid[12-i][97]=0
            grid[47][91-i]=0

        for j in range(3, 100):
            if j != 11 and j != 31 and j != 51 and j != 71 and j != 91:
                grid[j][49]=127
            else:
                grid[j][49]=0

        for j in range(57, 109):
                grid[63][j]=0

        for j in range(24, 31):
                grid[j][61]=127

        for j in range(32, 92):
            if j != 62 and j != 63 and j != 85:
                grid[j][78]=127
            else:
                grid[j][78]=0

        for i in range(95,98):
            for j in range(87,109):
                grid[i][j]=0
        
        for i in range(5):
            grid[112+i][108]=0
            grid[112+i][78]=0
            grid[112+i][26]=0

        np_map_data=grid.reshape(1,250*250) 
        list_map_data=np_map_data.tolist()
   
   
        self.f.close()
        print('read_complete')
        self.map_msg.data=list_map_data[0]



    def timer_callback(self):
        self.map_msg.header.stamp =rclpy.clock.Clock().now().to_msg()
        self.map_pub.publish(self.map_msg)


def main(args=None):
    rclpy.init(args=args)
    load_map = loadMap()
    rclpy.spin(load_map)
    load_map.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()




       
   
