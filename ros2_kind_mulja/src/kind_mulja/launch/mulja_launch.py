from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # package_name : ssafy_bridge
        Node(
            package='ssafy_bridge',
            node_executable='udp_to_pub',
            node_name='udp_to_pub'
        ),
        Node(
            package='ssafy_bridge',
            node_executable='sub_to_udp',
            node_name='sub_to_udp'
        ),
        Node(
            package='ssafy_bridge',
            node_executable='udp_to_cam',
            node_name='udp_to_cam'
        ),

        Node(
            package='ssafy_bridge',
            node_executable='udp_to_laser',
            node_name='udp_to_laser'
        ),
        
        # package_name : kind_mulja
        Node(
            package='kind_mulja',
            node_executable='odom',
            node_name='odom'
        ),
        Node(
            package='kind_mulja',
            node_executable='path_tracking',
            node_name='path_tracking'
        ),
        Node(
            package='kind_mulja',
            node_executable='lidar_trans',
            node_name='lidar_trans'
            # output='screen' 
        ),
        Node(
            package='kind_mulja',
            node_executable='load_map',
            node_name='load_map'
            # output='screen' 
        ),
        Node(
            package='kind_mulja',
            node_executable='a_star',
            node_name='a_star',
            output='screen'
        ), 
        Node(
            package='kind_mulja',
            node_executable='a_star_local_path',
            node_name='a_star_local_path'
        ),
        Node(
            package='kind_mulja',
            node_executable='auto_handcontrol',
            node_name='auto_handcontrol'
        ),
        Node(
            package='kind_mulja',
            node_executable='request_handcontrol',
            node_name='request_handcontrol'
        ),
        Node(
            package='kind_mulja',
            node_executable='client',
            node_name='client'
        ),
        Node(
            package='kind_mulja',
            node_executable='local_grid_map',
            node_name='local_grid_map'
        ),
        Node(
            package='kind_mulja',
            node_executable='send_turtlebot_loc',
            node_name='send_turtlebot_loc'
        ),
        # Node(
        #     package='kind_mulja',
        #     node_executable='camera',
        #     node_name='camera'
        # ),
    ])