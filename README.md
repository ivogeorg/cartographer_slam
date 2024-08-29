### cartographer_slam

Simultaneous mapping and localization in ROS. 

#### Notes

1. [Cartographer](https://github.com/cartographer-project/cartographer?tab=readme-ov-file#a-note-for-ros-users) is no longer developed or maintained, except for occasional pull requests and bug fixes. 
2. The ROS integration [cartographer_ros](https://github.com/ros2/cartographer_ros) is also getting stale. Last contribution was 2 years ago. [Documentation](https://google-cartographer-ros.readthedocs.io/en/latest/).
3. The currently supported ROS2-SLAM library is [slam_toolbox](https://github.com/SteveMacenski/slam_toolbox?tab=readme-ov-file#slam-toolbox). The author leads the [Navigation Working Group](https://github.com/ros-navigation). That seems to be what underlies [nav2](https://docs.nav2.org/index.html).

#### Saving the map

```
ros2 run nav2_map_server map_saver_cli -f warehouse_map_sim
```  
##### Notes

1. The cartographer node should still be running, as the saver requires the `/map` topic to save from.
2. **Don't specify a file extension!!!** The saver creates an occupancy `pgm` data file and a `yaml` file with metadata, including the name of the `pgm` file.
3. No way to specify target directory. Saves to the `.` directory.
