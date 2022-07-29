# shr-mfg-robotic-arm-visual-detection

## General description
Application is used to precisely determine the center of a package when it is loaded/unloaded by HiWonder Jetmax Robotic Arm from the robot car or from the warehouse. Using on-board camera and image detection and recognition methods from opencv library, the application detects the exact position of the package and its distance from the camera / suction hand.

## Functionalities for visual detection of the package and robotic arm position correction
* move the robotic arm above the approximate position of a package (for communication with the robot use the HTTP server linked below)
* measure the distance of the package from the camera
* using the camera capture an image of the package (call HTTP API endpoint /image)
* detect the package and its exact center
* calculate the offset (x, y) of the center of the package from the center of the image
* move the robotic arm to the correct position = the suction hand must be exactly at the center of the package and at the correct height
* **NOTE**: when moving the arm consider the offset from the suction hand to the camera

## Jetmax Robotic Arm
Hiwonder JetMax JETSON NANO Robot Arm ROS Open Source robot, more info: https://www.hiwonder.hk/collections/jetson/products/hiwonder-jetmax-jetson-nano-robot-arm-ros-open-source-vision-recognition-program-robot

## Jetmax Robotic Arm HTTP server
Jetmax robotic arm runs websocket server to which Shared Manufacturing Robotic Arm HTTP Server is connecting. Shared Manufacturing Robotic Arm HTTP Server represents middleware server that enables communication with JetMax robotic arm via specified HTTP API. https://github.com/fsprojekti/shr-mfg-robotic-arm-http-server

## Jetmax Robotic Arm built-in fuctions
Jetmax Robotic Arm functions are written in python. The following link include several examples of the built-in fuctions: https://github.com/JetMaxRoboticArm/jetmax_buildin_funcs

For detailed instructions and video tutorials, check this: https://drive.google.com/drive/folders/1GBiwRRy0NYdtOc2z0U2wGOYut7UGFls6

