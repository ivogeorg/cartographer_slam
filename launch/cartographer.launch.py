#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share_dir = get_package_share_directory('cartographer_slam')
    
    # TODO: there was a preferred way to avoid using os.path.join()
    # Example: https://github.com/ivogeorg/attach_shelf/blob/b511e89921b100bcaad62dd5f4291d8397f8be35/launch/attach_to_shelf.launch.py#L5
    # from launch_ros.substitutions import FindPackageShare
    #     approach_service_launch = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         PathJoinSubstitution([
    #             FindPackageShare(ros2_pkg),
    #             'launch',
    #             'approach_service.launch.py'
    #         ])
    #     ])
    # )

    config_dir_arg = DeclareLaunchArgument("configuration_directory", default_value=os.path.join(pkg_share_dir, 'config'))
    config_basename_arg = DeclareLaunchArgument("configuration_basename", default_value="cartographer.lua")

    cartographer_config_dir = LaunchConfiguration("configuration_directory")
    configuration_basename = LaunchConfiguration("configuration_basename")

    cartographer_node = Node(
            package='cartographer_ros', 
            executable='cartographer_node', 
            name='cartographer_node',
            output='screen',
            parameters=[{'use_sim_time': True}],
            arguments=['-configuration_directory', cartographer_config_dir,
                       '-configuration_basename', configuration_basename]
    )

    resolution_arg = DeclareLaunchArgument('resolution', default_value='0.05')
    publish_period_arg = DeclareLaunchArgument('publish_period_sec', default_value='1.0')

    resolution_f = LaunchConfiguration('resolution')
    publish_period_f = LaunchConfiguration('publish_period_sec')


    ocupancy_grid_node = Node(
            package='cartographer_ros',
            executable='occupancy_grid_node',
            output='screen',
            name='occupancy_grid_node',
            parameters=[{'use_sim_time': True}],
            # arguments=['-resolution', '0.05', '-publish_period_sec', '1.0']    )
            arguments=['-resolution', resolution_f, 
                       '-publish_period_sec', publish_period_f]    
    )
    
    return LaunchDescription([
        config_dir_arg,
        config_basename_arg,
        cartographer_node,
        resolution_arg,
        publish_period_arg,
        ocupancy_grid_node
    ])
