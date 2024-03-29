import rclpy
import numpy as np
from rclpy.node import Node
from geometry_msgs.msg import Pose, PoseStamped
from ssafy_msgs.msg import Col
from squaternion import Quaternion
from nav_msgs.msg import Odometry, OccupancyGrid, Path
from math import pi, cos, sin, sqrt
from collections import deque
import heapq

class a_star(Node):

    def __init__(self):
        super().__init__('a_Star')
        self.map_sub = self.create_subscription(OccupancyGrid, 'map', self.map_callback, 10)
        self.local_map_sub = self.create_subscription(OccupancyGrid, 'local_grid_map', self.local_map_callback, 10)
        self.odom_sub = self.create_subscription(Odometry, 'odom', self.odom_callback, 10)
        self.goal_sub = self.create_subscription(PoseStamped, 'goal_pose', self.goal_callback, 10)
        self.a_star_pub = self.create_publisher(Path, 'global_path', 10)
        self.col_sub = self.create_subscription(Col, 'col', self.col_callback, 10)

        self.map_msg = OccupancyGrid()
        self.odom_msg = Odometry()
        self.col_msg = Col()
        self.is_map = False
        self.is_odom = False
        self.is_found_path = False
        self.is_grid_update = False

        self.goal = [184, 224]
        self.map_size_x = 250
        self.map_size_y = 250
        self.map_resolution = 0.2
        self.map_offset_x = -50-25.0
        self.map_offset_y = -50-25.0
        self.GRIDSIZE = 250 

        self.dx = [-1, 0, 0, 1]
        self.dy = [0, 1, -1, 0]
        self.dCost = [1, 1, 1, 1]

    def grid_update(self):
        self.is_grid_update = True
        map_to_grid = self.map_msg.data
        rotated_grid = np.rot90(np.array(map_to_grid).reshape((self.map_size_x, self.map_size_y)), 1)
        self.grid = np.flipud(rotated_grid)  # 좌우반전과 상하반전을 수행합니다.

    def pose_to_grid_cell(self, x, y):
        map_point_x = (x - self.map_offset_x) / self.map_resolution
        map_point_y = (y - self.map_offset_y) / self.map_resolution
        return int(map_point_x), int(map_point_y)

    def grid_cell_to_pose(self, grid_cell):
        x = (grid_cell[0] * self.map_resolution) + self.map_offset_x
        y = (grid_cell[1] * self.map_resolution) + self.map_offset_y
        return x, y
    
    def col_callback(self, msg):
        self.is_col = True
        self.col_msg = msg
        if msg.col:
            self.generate_global_path()

    def local_map_callback(self, msg):
        self.is_local_map = True
        self.local_map_msg = msg

    def odom_callback(self, msg):
        self.is_odom = True
        self.odom_msg = msg

    def map_callback(self, msg):
        self.is_map = True
        self.map_msg = msg

    def goal_callback(self, msg):
        if msg.header.frame_id == 'map':
            goal_x, goal_y = msg.pose.position.x, msg.pose.position.y
            self.goal = self.pose_to_grid_cell(goal_x, goal_y)
            self.generate_global_path()

    def generate_global_path(self):
        if self.is_map and self.is_odom:
            if not self.is_grid_update:
                self.grid_update()
            
            if self.col_msg.col and self.is_local_map:  # col_msg.col이 True이면 로컬 그리드와 전역 그리드를 합칩니다.
                merged_grid = np.copy(self.grid)
    
                # Assuming local_map_msg contains local occupancy grid map data
                local_map_data = np.array(self.local_map_msg.data).reshape((30, 30))

                local_map_data = np.rot90(local_map_data, 1)
                local_map_data = np.flipud(local_map_data)
                print(local_map_data)
                # Adjust local grid position to match robot position
                robot_pose_x, robot_pose_y = self.pose_to_grid_cell(self.odom_msg.pose.pose.position.x, self.odom_msg.pose.pose.position.y)
                robot_pose_x -= 15
                robot_pose_y -= 15
                print(robot_pose_x, robot_pose_y)
                # Merge grids
                for i in range(30):
                    for j in range(30):
                        global_x = robot_pose_x + i
                        global_y = robot_pose_y + j
                        print(local_map_data[i][j])
                        if 0 <= global_x < self.GRIDSIZE and 0 <= global_y < self.GRIDSIZE:
                            if local_map_data[i][j] == 100:
                                print(global_x, global_y)
                                merged_grid[global_x][global_y] = 100
                print(merged_grid)
            else:
                merged_grid = np.copy(self.grid)

            self.final_path = []

            x, y = self.odom_msg.pose.pose.position.x, self.odom_msg.pose.pose.position.y
            start_grid_cell = self.pose_to_grid_cell(x, y)

            self.path = [[0] * self.GRIDSIZE for _ in range(self.GRIDSIZE)]
            self.cost = np.full((self.GRIDSIZE, self.GRIDSIZE), self.GRIDSIZE * self.GRIDSIZE)
            self.f_func = np.full((self.GRIDSIZE, self.GRIDSIZE), self.GRIDSIZE * self.GRIDSIZE)

            if 0 <= start_grid_cell[0] < self.GRIDSIZE and 0 <= start_grid_cell[1] < self.GRIDSIZE and 0 <= self.goal[0] < self.GRIDSIZE and 0 <= self.goal[1] < self.GRIDSIZE and start_grid_cell != self.goal:
                self.dijkstra(start_grid_cell, merged_grid)

            self.global_path_msg = Path()
            self.global_path_msg.header.frame_id = 'map'
            print(self.final_path)
            for grid_cell in reversed(self.final_path):
                tmp_pose = PoseStamped()
                waypoint_x, waypoint_y = self.grid_cell_to_pose(grid_cell)
                tmp_pose.pose.position.x = waypoint_x
                tmp_pose.pose.position.y = waypoint_y
                tmp_pose.pose.orientation.w = 1.0
                self.global_path_msg.poses.append(tmp_pose)

            if len(self.final_path) != 0:
                self.a_star_pub.publish(self.global_path_msg)

        
    def heuristic(self, a, b):
        #유클리디안 거리 함수
        return abs(b[0] - a[0]) + abs(b[1] - a[1])

    def dijkstra(self, start, grid):
        pq = []
        heapq.heappush(pq,(0, start))
        self.cost[start[0]][start[1]] = 1
        self.f_func[start[0]][start[1]] = 1
        found = False


        while pq:
            if found:
                self.get_logger().info(f"found")
                break

            current = heapq.heappop(pq)[1]

            

            for i in range(4):
                next_node = (current[0] + self.dx[i], current[1] + self.dy[i])
                # if self.grid[next_node[0]][next_node[1]] >= 50:
                #     continue

                # 다음 노드가 맵 범위 내에 있는지 확인
                if 0 <= next_node[0] < self.GRIDSIZE and 0 <= next_node[1] < self.GRIDSIZE:
                    if grid[next_node[0]][next_node[1]] < 50:
                        
                        new_cost = self.cost[current[0]][current[1]] + self.dCost[i]
                        f_func = new_cost + self.heuristic(next_node, self.goal)

                        # 다음 노드의 현재까지의 최소 비용보다 작은 경우 업데이트
                        if f_func < self.f_func[next_node[0]][next_node[1]]:
                            self.cost[next_node[0]][next_node[1]] = new_cost
                            self.f_func[next_node[0]][next_node[1]] = f_func

                            heapq.heappush(pq, (f_func, next_node))
                            self.path[next_node[0]][next_node[1]] = current

                            if next_node == self.goal:
                                found = True
                                break


        node = self.goal
        while node != start:
            if isinstance(node, int):
                break
            self.final_path.append(node)
            node = self.path[node[0]][node[1]]
        if not isinstance(node, int):
            self.final_path.append(node)

def main(args=None):
    rclpy.init(args=args)

    global_planner = a_star()

    try:
        rclpy.spin(global_planner)
    except KeyboardInterrupt:
        pass

    global_planner.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()