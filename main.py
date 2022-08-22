import numpy as np
import cv2 as cv

cap = cv.VideoCapture("http://192.168.220.167:8080/stream?topic=/usb_cam/image_rect_color")
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't recieve from. Exiting ....")
        break
    
    frame = cv.medianBlur(frame, 5)
    gray = cv.cvtColor(frame, cv.COLOR_BR2GRAY)
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    
    circles = np.unit16(np.around(circles))
    for i in circles[0,:]:
        cv.circle(gray,(i[0],i[1]),i[2],(0,255,0),2)
        cv.circle(gray,(i[0],i[1]),2,(0,0,255),3)
        org = (i[0], i[1])
        cv.putText(gray, "x: " + i[0] + " y: " + i[1] + " radius: " + i[2], org, cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255, 0, 0), 2, cv.LINE_AA)

    cv.imshow("frame", gray)
    if cv.waitKey(1) == ord('q'):
        break


cap.relase()
cv.destroyAllWindows()
