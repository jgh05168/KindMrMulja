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
        self.map_size_x=500 
        self.map_size_y=500
        self.map_resolution=0.1
        self.map_offset_x=-50-25.0
        self.map_offset_y=-50-25.0
        self.map_data = [0 for i in range(self.map_size_x*self.map_size_y)]
        grid=np.array(self.map_data)
        grid=np.reshape(grid,(500, 500))

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
            if num < 500*500:
                self.map_data[num]=int(data)
   
        
        map_to_grid=np.array(self.map_data)
        grid=np.reshape(map_to_grid,(500, 500))


        for y in range(500):
            for x in range(500):

                if grid[x][y]==100 :
                    '''
                    로직 3. 점유영역 근처 필터처리
                    '''
                    for box_x in range(-10,11):
                        for box_y in range(-10,11):
                            if  0< x+box_x < 500 and 0 < y+box_y <500 and grid[x+box_x][y+box_y]<80 :
                                grid[x+box_x][y+box_y]=127
        
        # for i in range(5):
        #     grid[85][74+i]=0
        #     grid[53][60-i]=0
        #     grid[72][91-i]=0
        #     grid[12-i][97]=0
        #     grid[47][91-i]=0

        # for j in range(3, 100):
        #     if j != 11 and j != 31 and j != 51 and j != 71 and j != 91:
        #         grid[j][49]=127
        #     else:
        #         grid[j][49]=0

        # for j in range(57, 109):
        #         grid[63][j]=0

        # for j in range(24, 31):
        #         grid[j][61]=127

        # for j in range(32, 92):
        #     if j != 62 and j != 63 and j != 85:
        #         grid[j][78]=127
        #     else:
        #         grid[j][78]=0

        # for i in range(95,98):
        #     for j in range(87,109):
        #         grid[i][j]=0
        
        # for i in range(5):
        #     grid[112+i][108]=0
        #     grid[112+i][78]=0
        #     grid[112+i][26]=0
                                
        for i in range(11):
            for w in range(-1,2):
                if i==9 and w!=0:
                    continue
                else:
                    grid[170+w][149+i]=0
                    grid[107+w][123-i]=0
                    grid[144+w][183-i]=0
                    grid[24-i][194+w]=0
                    grid[94+w][183-i]=0
        
        for i in range(10,12):
            grid[106][123-i]=127
            grid[108][123-i]=127
                                
        for i in range(109,112):
            for j in range(190,213):
                grid[j][i]=0

        for i in range(113,130):
            for j in range(15,60):
                grid[j][i]=127

        for i in range(112,132):
            for j in range(213,234):
                grid[j][i]=127

        for i in range(79,99):
            for j in range(213,234):
                grid[j][i]=127

        for i in range(28,79):
            for j in range(205,234):
                if (i == 52 or i == 53 or i == 54) and j >= 224 and j != 233:
                    grid[j][i]=0
                elif j == 233 and i == 53:
                    grid[233][53]=0
                else:
                    grid[j][i]=127
        
        for i in range(132,182):
            for j in range(205,234):
                if (i == 156 or i == 157 or i == 158) and j >= 224 and j != 233:
                    grid[j][i]=0
                elif j == 233 and i == 157:
                    grid[233][157]=0
                else:
                    grid[j][i]=127

        for i in range(192,242):
            for j in range(205,234):
                if (i== 215 or i == 216 or i == 217) and j >= 223 and j != 233:
                    grid[j][i]=0
                elif j == 233 and i == 216:
                    grid[233][216]=0
                else:
                    grid[j][i]=127


        for j in range(11, 190):
            if j != 22 and j != 62 and j != 102 and j != 142 and j != 182:
                grid[j][98]=127
            else:
                grid[j][98]=0

        for j in range(113, 236):
            grid[189][j]=0

        for j in range(15, 185):
            if j == 60  or j == 61 or j == 62 or j == 63  or j == 107  or j == 123 or j == 124 or j == 125 or j == 126:
                grid[j][112]=0
            else:
                grid[j][112]=127

        for i in range(124, 158):
            grid[126][i]=0

        for i in range(114, 123):
            grid[i][113]=127

        for i in range(6):
            for w in range(-1,2):
                if i==5 and w!=0:
                    continue
                else:
                    grid[195-i][177+w]=0
                    grid[195-i][190+w]=0
                    grid[195-i][203+w]=0
                    grid[195-i][215+w]=0
            
        arr=[[113,127], [158,127], [158, 122], [174,64], [158,64], [113,64], [219,15]]
        for i in range(7):
            grid[arr[i][1]][arr[i][0]]=127


        np_map_data=grid.reshape(1,500*500) 
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




       
   
