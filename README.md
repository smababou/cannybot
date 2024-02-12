# CannyBot

## :package: Packages Overview

- [`cannybot_description`](./cannybot_description): URDF description of CannyOne including its sensors
- [`cannybot_maps`](./cannybot_maps): Saved Maps and mapserver launch for CannyBot
- [`cannybot_navigation`](./cannybot_navigation): Full Automated Navigation for CannyBot
- [`cannybot_simulation`](./cannybot_simulation): Simulation specific launch and configuration files for CannyBot
- [`cannybot_slam`](./cannybot_slam): SLAM including gmapping for CannyBot worlds
- [`cannybot_teleop`](./cannybot_teleop): Generic Keyboard Teleop for CannyBot


## CannyBot Navigation Launch

### 1st Terminal
```console
roslaunch cannybot_simulation cannybot_house.launch 
```

### 2nd Terminal
```console
roslaunch cannybot_navigation cannybot_navigation.launch 
```