# shr-mfg-robotic-arm-visual-detection

## General description
Application is used to precisely determine the center of a package when it is loaded/unloaded by HiWonder Jetmax Robotic Arm from the robot car or from the warehouse. Using on-board camera and image detection and recognition methods from opencv library, the application detects the exact position of the package and its distance from the camera / suction hand.

## Jetmax Robotic Arm
Hiwonder JetMax JETSON NANO Robot Arm ROS Open Source robot, more info: https://www.hiwonder.hk/collections/jetson/products/hiwonder-jetmax-jetson-nano-robot-arm-ros-open-source-vision-recognition-program-robot

## Jetmax Robotic Arm HTTP server
Jetmax robotic arm runs websocket server to which Shared Manufacturing Robotic Arm HTTP Server is connecting. Shared Manufacturing Robotic Arm HTTP Server represents middleware server that enables communication with JetMax robotic arm via specified HTTP API. https://github.com/fsprojekti/shr-mfg-robotic-arm-http-server

## Functionalities for visual detection of the package and robotic arm position correction
* move the robotic arm above the approximate position of a package
* measure the distance of the package from the camera
* using the camera capture an image of the package
* detect the package and its exact center
* calculate the offset (x, y) of the center of the package from the center of the image
* move the robotic arm to the correct position = the suction hand must be exactly at the center of the package and at the correct height
* **NOTE**: when moving the arm consider the distance between the suction hand and the camera
