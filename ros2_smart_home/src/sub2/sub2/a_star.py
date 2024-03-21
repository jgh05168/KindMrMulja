import rclpy
import numpy as np
from rclpy.node import Node
from geometry_msgs.msg import Pose, PoseStamped
from squaternion import Quaternion
from nav_msgs.msg import Odometry, OccupancyGrid, Path
from math import pi, cos, sin, sqrt
from collections import deque
import heapq

class a_star(Node):

    def __init__(self):
        super().__init__('a_Star')
        self.map_sub = self.create_subscription(OccupancyGrid, 'map', self.map_callback, 1)
        self.odom_sub = self.create_subscription(Odometry, 'odom', self.odom_callback, 1)
        self.goal_sub = self.create_subscription(PoseStamped, 'goal_pose', self.goal_callback, 1)
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
        self.dCost = [10, 10, 10, 10, 14, 14, 14, 14]

    def grid_update(self):
        self.is_grid_update = True
        map_to_grid = self.map_msg.data
        #self.grid = np.array(map_to_grid).reshape((self.map_size_x, self.map_size_y))
        #self.grid = np.array(map_to_grid).reshape((self.map_size_x, self.map_size_y)).T[:, ::-1]
        rotated_grid = np.rot90(np.array(map_to_grid).reshape((self.map_size_x, self.map_size_y)), 1)
        self.grid = np.flipud(rotated_grid)

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

    def goal_callback(self, msg):
        if msg.header.frame_id == 'map':
            goal_x, goal_y = msg.pose.position.x, msg.pose.position.y
            goal_cell = self.pose_to_grid_cell(goal_x, goal_y)
            self.goal = goal_cell
            self.get_logger().info("Goal pose: {}, {}".format(goal_x, goal_y))
            self.get_logger().info(f"{msg}")  # 수정된 부분
            # self.get_logger().info(f"{start_grid_cell}")
            # self.get_logger().info(f"{self.grid[start_grid_cell[0]][start_grid_cell[1]]}")
            # self.get_logger().info(f"{self.grid[int(self.goal[0])][int(self.goal[1])]}")

            if self.is_map and self.is_odom:
                if not self.is_grid_update:
                    self.grid_update()

                self.final_path = []

                x, y = self.odom_msg.pose.pose.position.x, self.odom_msg.pose.pose.position.y
                start_grid_cell = self.pose_to_grid_cell(x, y)
                # start_grid_cell = (int(start_grid_cell[0]), int(start_grid_cell[1]))

                self.path = [[0] * self.GRIDSIZE for _ in range(self.GRIDSIZE)]
                self.cost = np.full((self.GRIDSIZE, self.GRIDSIZE), self.GRIDSIZE * self.GRIDSIZE)
                self.f_func = np.full((self.GRIDSIZE, self.GRIDSIZE), self.GRIDSIZE * self.GRIDSIZE)
                
                #if 0 <= start_grid_cell[0] < self.GRIDSIZE and 0 <= start_grid_cell[1] < self.GRIDSIZE and 0 <= self.goal[0] < self.GRIDSIZE and 0 <= self.goal[1] < self.GRIDSIZE and self.grid[start_grid_cell[0]][start_grid_cell[1]] == 0 and self.grid[int(self.goal[0])][int(self.goal[1])] == 0 and start_grid_cell != self.goal:
                #self.get_logger().info(f"start: {start_grid_cell}")
                #self.get_logger().info(f"target: {self.goal}")
                if 0 <= start_grid_cell[0] < self.GRIDSIZE and 0 <= start_grid_cell[1] < self.GRIDSIZE and 0 <= self.goal[0] < self.GRIDSIZE and 0 <= self.goal[1] < self.GRIDSIZE and start_grid_cell != self.goal:
                    #self.get_logger().info(f"start: {start_grid_cell}")
                    #self.get_logger().info(f"target: {self.goal}")
                    #self.get_logger().info(f"target cell: {goal_cell}")
                    self.get_logger().info(f"grid: {self.grid}")
                    self.dijkstra(start_grid_cell)
                    self.get_logger().info(f"path: {self.final_path}")

                self.global_path_msg = Path()
                self.global_path_msg.header.frame_id = 'map'
                for grid_cell in reversed(self.final_path):
                    tmp_pose = PoseStamped()
                    waypoint_x, waypoint_y = self.grid_cell_to_pose(grid_cell)
                    tmp_pose.pose.position.x = waypoint_x
                    tmp_pose.pose.position.y = waypoint_y
                    tmp_pose.pose.orientation.w = 1.0
                    self.global_path_msg.poses.append(tmp_pose)

                #self.get_logger().info(f"final_path: {self.final_path}")
                if len(self.final_path) != 0:
                    self.get_logger().info(f"pub final_path")
                    self.a_star_pub.publish(self.global_path_msg)

    def heuristic(self, a, b):
        #유클리디안 거리 함수
        return ((b[0] - a[0])**2 + (b[1] - a[1])**2)

    def dijkstra(self, start):
        #self.get_logger().info(f"dijkstra start")
        #Q = deque()
        pq = []
        #Q.append(start)
        heapq.heappush(pq,(0, start))
        self.cost[start[0]][start[1]] = 1
        self.f_func[start[0]][start[1]] = 1
        found = False
        self.get_logger().info(f"start: {start}")
        self.get_logger().info(f"start_grid: {self.grid[start[0]][start[1]]}")
        self.get_logger().info(f"goal: {self.goal}")
        self.get_logger().info(f"goal_grid: {self.grid[self.goal[0]][self.goal[1]]}")

        while pq:
            if found:
                self.get_logger().info(f"found")
                break

            current = heapq.heappop(pq)[1]
            #self.get_logger().info(f"      ")
            #self.get_logger().info(f"current: {current}")
            

            for i in range(8):
                #self.get_logger().info(f"             ")
                next_node = (current[0] + self.dx[i], current[1] + self.dy[i])
                # if self.grid[next_node[0]][next_node[1]] >= 50:
                #     continue

                # 다음 노드가 맵 범위 내에 있는지 확인
                if 0 <= next_node[0] < self.GRIDSIZE and 0 <= next_node[1] < self.GRIDSIZE:
                    #self.get_logger().info(f"next_node: {next_node}")
                    #self.get_logger().info(f"grid: {self.grid[next_node[0]][next_node[1]]}")
                    if self.grid[next_node[0]][next_node[1]] < 50:
                        new_cost = self.cost[current[0]][current[1]] + self.dCost[i]
                        f_func = new_cost + self.heuristic(next_node, self.goal)

                        # 다음 노드의 현재까지의 최소 비용보다 작은 경우 업데이트
                        #self.get_logger().info(f"nextnode: {next_node}")
                        if f_func < self.f_func[next_node[0]][next_node[1]]:
                            self.cost[next_node[0]][next_node[1]] = new_cost
                            self.f_func[next_node[0]][next_node[1]] = f_func

                            heapq.heappush(pq, (f_func, next_node))
                            self.path[next_node[0]][next_node[1]] = current

                            if next_node == self.goal:
                                self.get_logger().info(f"goal!!!!!!!!!!")
                                found = True
                                break


        node = self.goal
        while node != start:
            if isinstance(node, int):
                break
            self.final_path.append(node)
            #self.get_logger().info(f"endpath: {self.path[node[0]][node[1]]}")
            node = self.path[node[0]][node[1]]

        if not isinstance(node, int):
            self.final_path.append(node)

    def aStar(self, start):
        # startNode와 endNode 초기화
        startNode = Node(None, start)
        endNode = Node(None, self.goal)

        # openList, closedList 초기화
        openList = []
        closedList = []

        # openList에 시작 노드 추가
        openList.append(startNode)

        # endNode를 찾을 때까지 실행
        while openList:

            # 현재 노드 지정
            currentNode = openList[0]
            currentIdx = 0

            # 이미 같은 노드가 openList에 있고, f 값이 더 크면
            # currentNode를 openList안에 있는 값으로 교체
            for index, item in enumerate(openList):
                if item.f < currentNode.f:
                    currentNode = item
                    currentIdx = index

            # openList에서 제거하고 closedList에 추가
            openList.pop(currentIdx)
            closedList.append(currentNode)

            # 현재 노드가 목적지면 current.position 추가하고
            # current의 부모로 이동
            if currentNode == endNode:
                path = []
                current = currentNode
                while current is not None:
                    # maze 길을 표시하려면 주석 해제
                    # x, y = current.position
                    # maze[x][y] = 7 
                    path.append(current.position)
                    current = current.parent
                return path[::-1]  # reverse

            children = []
            # 인접한 xy좌표 전부
            for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

                # 노드 위치 업데이트
                nodePosition = (
                    currentNode.position[0] + newPosition[0],  # X
                    currentNode.position[1] + newPosition[1])  # Y
                    
                # 미로 maze index 범위 안에 있어야함
                within_range_criteria = [
                    nodePosition[0] > (len(maze) - 1),
                    nodePosition[0] < 0,
                    nodePosition[1] > (len(maze[len(maze) - 1]) - 1),
                    nodePosition[1] < 0,
                ]

                if any(within_range_criteria):  # 하나라도 true면 범위 밖임
                    continue

            # 장애물이 있으면 다른 위치 불러오기
                if maze[nodePosition[0]][nodePosition[1]] != 0:
                    continue

                new_node = Node(currentNode, nodePosition)
                children.append(new_node)

            # 자식들 모두 loop
            for child in children:

                # 자식이 closedList에 있으면 continue
                if child in closedList:
                    continue

                # f, g, h값 업데이트
                child.g = currentNode.g + 1
                child.h = ((child.position[0] - endNode.position[0]) **
                        2) + ((child.position[1] - endNode.position[1]) ** 2)
                # child.h = heuristic(child, endNode) 다른 휴리스틱
                # print("position:", child.position) 거리 추정 값 보기
                # print("from child to goal:", child.h)
                
                child.f = child.g + child.h

                # 자식이 openList에 있으고, g값이 더 크면 continue
                if len([openNode for openNode in openList
                        if child == openNode and child.g > openNode.g]) > 0:
                    continue
                        
                openList.append(child)

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
