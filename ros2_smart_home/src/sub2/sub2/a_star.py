import rclpy
import numpy as np
from rclpy.node import Node
from geometry_msgs.msg import Pose, PoseStamped
from squaternion import Quaternion
from nav_msgs.msg import Odometry, OccupancyGrid, Path
from math import pi, cos, sin
from collections import deque
from ssafy_msgs.msg import TargetGrid

class a_star(Node):

    def __init__(self):
        super().__init__('a_Star')
        self.map_sub = self.create_subscription(OccupancyGrid, 'map', self.map_callback, 1)
        self.odom_sub = self.create_subscription(Odometry, 'odom', self.odom_callback, 1)
        # self.goal_sub = self.create_subscription(PoseStamped, 'target_grid', self.goal_callback, 1)
        self.goal_sub = self.create_subscription(PoseStamped, 'goal_pose', self.goal_callback, 1)
        # self.target_sub = self.create_subscription(TargetGrid, 'target_grid', self.goal_callback, 1)
        self.a_star_pub = self.create_publisher(Path, 'global_path', 1)
        
        self.map_msg = OccupancyGrid()
        self.odom_msg = Odometry()
        self.is_map = False
        self.is_odom = False
        self.is_found_path = False
        self.is_grid_update = False

        self.goal = [184, 224]
        self.map_size_x = 350
        self.map_size_y = 350
        self.map_resolution = 0.05
        self.map_offset_x = -8-8.75
        self.map_offset_y = -4-8.75
        self.GRIDSIZE = 350 

        self.dx = [-1, 0, 0, 1, -1, -1, 1, 1]
        self.dy = [0, 1, -1, 0, -1, 1, -1, 1]
        self.dCost = [1, 1, 1, 1, 1.414, 1.414, 1.414, 1.414]

    def grid_update(self):
        self.is_grid_update = True
        map_to_grid = self.map_msg.data
        self.grid = np.array(map_to_grid).reshape((self.map_size_x, self.map_size_y))

    def pose_to_grid_cell(self, x, y):
        map_point_x = (x - self.map_offset_x) / self.map_resolution
        map_point_y = (y - self.map_offset_y) / self.map_resolution
        return int(map_point_x), int(map_point_y)

    def grid_cell_to_pose(self, grid_cell):
        x = (grid_cell[0] * self.map_resolution) + self.map_offset_x
        y = (grid_cell[1] * self.map_resolution) + self.map_offset_y
        return x, y

    def odom_callback(self, msg):
        self.is_odom = True
        self.odom_msg = msg

    def map_callback(self, msg):
        self.is_map = True
        self.map_msg = msg
        
    def target_callback(self, msg):
        self.is_target = True
        self.target_msg = msg

    def goal_callback(self, msg):
        if msg.header.frame_id == 'map':
            # goal_x, goal_y =msg.x, msg.y
            goal_x, goal_y = msg.pose.position.x, msg.pose.position.y
            goal_cell = self.pose_to_grid_cell(goal_x, goal_y)
            self.goal = goal_cell
            self.get_logger().info("Goal pose: {}, {}".format(goal_x, goal_y))
            self.get_logger().info(f"{msg}")  # 수정된 부분

            if self.is_map and self.is_odom:
                self.get_logger().info(f"{self.goal}")
                if not self.is_grid_update:
                    self.grid_update()

                self.final_path = []

                x, y = self.odom_msg.pose.pose.position.x, self.odom_msg.pose.pose.position.y
                start_grid_cell = self.pose_to_grid_cell(x, y)
                start_grid_cell = (int(start_grid_cell[0]), int(start_grid_cell[1]))

                self.path = [[0] * self.GRIDSIZE for _ in range(self.GRIDSIZE)]
                self.cost = np.full((self.GRIDSIZE, self.GRIDSIZE), self.GRIDSIZE * self.GRIDSIZE)

                if 0 <= start_grid_cell[0] < self.GRIDSIZE and 0 <= start_grid_cell[1] < self.GRIDSIZE and 0 <= self.goal[0] < self.GRIDSIZE and 0 <= self.goal[1] < self.GRIDSIZE and self.grid[start_grid_cell[0]][start_grid_cell[1]] == 0 and self.grid[int(self.goal[0])][int(self.goal[1])] == 0 and start_grid_cell != self.goal:
                    self.dijkstra(start_grid_cell)

                self.global_path_msg = Path()
                self.global_path_msg.header.frame_id = 'map'
                for grid_cell in reversed(self.final_path):
                    tmp_pose = PoseStamped()
                    waypoint_x, waypoint_y = self.grid_cell_to_pose(grid_cell)
                    tmp_pose.pose.position.x = waypoint_x
                    tmp_pose.pose.position.y = waypoint_y
                    tmp_pose.pose.orientation.w = 1.0
                    self.global_path_msg.poses.append(tmp_pose)
                
                self.get_logger().info("final path: {}".format(self.final_path)) 
                if len(self.final_path) != 0:
                    self.a_star_pub.publish(self.global_path_msg)

    def dijkstra(self, start):
        Q = deque()
        Q.append(start)
        self.cost[start[0]][start[1]] = 1
        found = False

        while Q:
            if found:
                break

            current = Q.popleft()

            for i in range(8):
                next_node = (current[0] + self.dx[i], current[1] + self.dy[i])
                if 0 <= next_node[0] < self.GRIDSIZE and 0 <= next_node[1] < self.GRIDSIZE:
                    if self.grid[next_node[0]][next_node[1]] < 51:
                        if self.cost[current[0]][current[1]] + self.dCost[i] < self.cost[next_node[0]][next_node[1]]:
                            Q.append(next_node)
                            self.path[next_node[0]][next_node[1]] = current
                            self.cost[next_node[0]][next_node[1]] = self.cost[current[0]][current[1]] + self.dCost[i]

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
            self.final_path.append((int(node[0]), int(node[1])))

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
