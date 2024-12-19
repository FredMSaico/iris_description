from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    iris_description_dir = get_package_share_directory('iris_description')
    urdf_file = os.path.join(iris_description_dir, 'urdf', 'iris.urdf')

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': open(urdf_file, 'r').read()}]
    )

    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        output='screen'
    )

    # Configuración de RViz
    rviz_config_path = os.path.join(iris_description_dir, 'rviz', 'iris.rviz')

    # Nodo para lanzar RViz con la configuración de iris.rviz
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_path]
    )

    return LaunchDescription([
        robot_state_publisher_node,

        rviz_node
    ])
