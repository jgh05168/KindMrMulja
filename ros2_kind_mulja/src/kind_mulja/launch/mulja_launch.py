from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
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
      
    ])