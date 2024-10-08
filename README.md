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

##### Output

Successful output:
```
user:~/ros2_ws/src/warehouse_project/cartographer_slam/config$ ros2 run nav2_map_server map_saver_cli -f warehouse_map_sim[INFO] [1724964361.581900173] [map_saver]:
        map_saver lifecycle node launched.
        Waiting on external lifecycle transitions to activate
        See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [1724964361.582895090] [map_saver]: Creating
[INFO] [1724964361.583029593] [map_saver]: Configuring
[INFO] [1724964361.588110008] [map_saver]: Saving map from 'map' topic to 'warehouse_map_sim' file
[WARN] [1724964361.588149818] [map_saver]: Free threshold unspecified. Setting it to default value: 0.250000
[WARN] [1724964361.588172232] [map_saver]: Occupied threshold unspecified. Setting it to default value: 0.650000
[WARN] [map_io]: Image format unspecified. Setting it to: pgm
[INFO] [map_io]: Received a 154 X 135 map @ 0.05 m/pix
[INFO] [map_io]: Writing map occupancy data to warehouse_map_sim.pgm
[INFO] [map_io]: Writing map metadata to warehouse_map_sim.yaml
[INFO] [map_io]: Map saved
[INFO] [1724964362.482214126] [map_saver]: Map saved successfully
[INFO] [1724964362.483553630] [map_saver]: Destroying
```
