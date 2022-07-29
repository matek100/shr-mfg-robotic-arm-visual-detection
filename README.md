# shr-mfg-robotic-arm-visual-detection

## General description
Application is used to precisely determine the center of a package when it is loaded/unloaded by HiWonder Jetmax Robotic Arm from the robot car or from the warehouse. Using on-board camera and image detection and recognition methods from opencv library, the application detects the exact position of the package and its distance from the camera / suction hand.

## Visual detection of the package and calculation of its exact center
1. define a new API endpoint for the HTTP server linked below
 * <code>/packageCenter</code>
 * parameters: x, y, z (approximate center of the package)
 * returns: x, y, z (exact center of the package)
2. when a request is received to the above endpoint, move the robotic arm to the location above the approximate center of the package
 * call Robotic Arm HTTP Server API endpoint <code>/basic/moveTo</code> to make an absolute move of the robotic arm
 * consider the offset between the camera and the suction hand
3. calculate the distance of the package from the camera
 * use the definition and measurement of the robotic arm operational area described in https://github.com/fsprojekti/rack-warehouse-jetmax and https://github.com/fsprojekti/plk-blockchain
4. capture an image from the camera
 * subscribe to the <code>/usb_cam/image_rect_color</code> socket and wait for the response
 * when a reponse (message) is received save the image
5. detect the package in the image and calculate its exact center (x, y)
 * use OpenCV JavaScript bindings, for example: https://docs.opencv.org/3.4/d5/d10/tutorial_js_root.html
6. identify the package
 * detect and recognize the tags positioned on the top of the package
 * use AprilTag identification as described here: https://drive.google.com/drive/folders/1lccpQJGc88Jd10sV0wCiwD8eN0oxTAtf
7. a message sent in response to the <code>/packageCenter</code> request must include
 * x, y, z: the coordinates of the exact center of the package
 * ID: package identification number

## Jetmax Robotic Arm
Hiwonder JetMax JETSON NANO Robot Arm ROS Open Source robot, more info: https://www.hiwonder.hk/collections/jetson/products/hiwonder-jetmax-jetson-nano-robot-arm-ros-open-source-vision-recognition-program-robot

## Jetmax Robotic Arm HTTP server
Jetmax robotic arm runs websocket server to which Shared Manufacturing Robotic Arm HTTP Server is connecting. Shared Manufacturing Robotic Arm HTTP Server represents middleware server that enables communication with JetMax robotic arm via specified HTTP API. https://github.com/fsprojekti/shr-mfg-robotic-arm-http-server

## Jetmax Robotic Arm built-in fuctions
Jetmax Robotic Arm functions are written in python. The following link include several examples of the built-in fuctions: https://github.com/JetMaxRoboticArm/jetmax_buildin_funcs

For detailed instructions and video tutorials, check this: https://drive.google.com/drive/folders/1GBiwRRy0NYdtOc2z0U2wGOYut7UGFls6

A useful example, block stacking: https://drive.google.com/drive/folders/1lccpQJGc88Jd10sV0wCiwD8eN0oxTAtf
