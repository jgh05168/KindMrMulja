import rclpy
import numpy as np
from rclpy.node import Node
import os
from geometry_msgs.msg import Pose,PoseStamped
from squaternion import Quaternion
from nav_msgs.msg import Odometry,OccupancyGrid,MapMetaData,Path
from math import pi,cos,sin, sqrt
from collections import deque

class a_star(Node):

    def __init__(self):
        super().__init__('a_Star')
        self.map_sub = self.create_subscription(OccupancyGrid,'map',self.map_callback,1)
        self.odom_sub = self.create_subscription(Odometry,'odom',self.odom_callback,1)
        self.goal_sub = self.create_subscription(PoseStamped,'goal_pose',self.goal_callback,1)
        self.a_star_pub= self.create_publisher(Path, 'global_path', 1)
        
        self.map_msg=OccupancyGrid()
        self.odom_msg=Odometry()
        self.is_map=False
        self.is_odom=False
        self.is_found_path=False
        self.is_grid_update=False

        self.goal = [184,224] 
        self.map_size_x=350
        self.map_size_y=350
        self.map_resolution=0.05
        self.map_offset_x=-8-8.75
        self.map_offset_y=-4-8.75
    
        self.GRIDSIZE=350 
 
        self.dx = [-1,0,0,1,-1,-1,1,1]
        self.dy = [0,1,-1,0,-1,1,-1,1]
        self.dCost = [1, 1, 1, 1, 1.414, 1.414, 1.414, 1.414]

    def grid_update(self):
        self.is_grid_update=True
        map_to_grid = self.map_msg.data
        self.grid = np.array(map_to_grid).reshape((self.map_size_x, self.map_size_y))

    def pose_to_grid_cell(self,x,y):
        map_point_x = (x - self.map_offset_x) / self.map_resolution
        map_point_y = (y - self.map_offset_y) / self.map_resolution
        return map_point_x,map_point_y

    def grid_cell_to_pose(self,grid_cell):
        x = (grid_cell[0] * self.map_resolution) + self.map_offset_x
        y = (grid_cell[1] * self.map_resolution) + self.map_offset_y
        return [x,y]

    def odom_callback(self,msg):
        self.is_odom=True
        self.odom_msg=msg

    def map_callback(self,msg):
        self.is_map=True
        self.map_msg=msg

    def goal_callback(self,msg):
        
        if msg.header.frame_id=='map':
            goal_x = msg.pose.position.x
            goal_y = msg.pose.position.y
            goal_cell = self.pose_to_grid_cell(goal_x, goal_y)
            self.goal = goal_cell

            if self.is_map ==True and self.is_odom==True  :
                if self.is_grid_update==False :
                    self.grid_update()

                self.final_path=[]

                x=self.odom_msg.pose.pose.position.x
                y=self.odom_msg.pose.pose.position.y
                start_grid_cell=self.pose_to_grid_cell(x,y)

                self.path = {}
                self.cost_so_far = {}
                self.path[start_grid_cell] = None
                self.cost_so_far[start_grid_cell] = 0

                if self.grid[start_grid_cell[0]][start_grid_cell[1]] ==0  and self.grid[self.goal[0]][self.goal[1]] ==0  and start_grid_cell != self.goal :
                    self.astar(start_grid_cell)

                self.global_path_msg=Path()
                self.global_path_msg.header.frame_id='map'
                for grid_cell in reversed(self.final_path) :
                    tmp_pose=PoseStamped()
                    waypoint_x,waypoint_y=self.grid_cell_to_pose(grid_cell)
                    tmp_pose.pose.position.x=waypoint_x
                    tmp_pose.pose.position.y=waypoint_y
                    tmp_pose.pose.orientation.w=1.0
                    self.global_path_msg.poses.append(tmp_pose)
            
                if len(self.final_path)!=0 :
                    self.a_star_pub.publish(self.global_path_msg)

    def heuristic(self, a, b):
        #유클리디안 거리 함수 사용
        return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

    def astar(self, start):
        open_list = deque([start])

        while open_list:
            current = open_list.popleft()

            if current == self.goal:
                break

            for i in range(8):
                next_cell = (current[0] + self.dx[i], current[1] + self.dy[i])
                
                if 0 <= next_cell[0] < self.GRIDSIZE and 0 <= next_cell[1] < self.GRIDSIZE and self.grid[next_cell[0]][next_cell[1]] < 51:
                    new_cost = self.cost_so_far[current] + self.dCost[i]
                    if next_cell not in self.cost_so_far or new_cost < self.cost_so_far[next_cell]:
                        self.cost_so_far[next_cell] = new_cost
                        priority = new_cost + self.heuristic(self.goal, next_cell)
                        open_list.append(next_cell)
                        self.path[next_cell] = current

        node = self.goal

        while node:
            self.final_path.append(node)
            node = self.path[node]
            
def main(args=None):
    rclpy.init(args=args)

    global_planner = a_star()

    rclpy.spin(global_planner)

    global_planner.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
