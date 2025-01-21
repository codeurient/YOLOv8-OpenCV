import cv2
import imutils  
import numpy as np

top_left     = (230, 399)
bottom_left  = (133, 467)
top_right    = (385, 401)
bottom_right = (455, 462)

pts1 = np.float32([top_left, bottom_left, top_right, bottom_right])
pts2 = np.float32([ [0,0], [0,480], [640,0], [640,480] ])  
color = (0, 255, 0)

path = "test_videos\\road.mp4"
cap = cv2.VideoCapture(path)
ret, frame = cap.read()

if ret == True:
    print("[INFO]... Shape", frame.shape)
else:
    print("[INFO]... The video is not loaded successfully !")

def nothing(x):
    pass

cv2.namedWindow("Tracksbars")

cv2.createTrackbar("L-H", "Tracksbars", 0, 255,   nothing) 
cv2.createTrackbar("L-S", "Tracksbars", 0, 255,   nothing) 
cv2.createTrackbar("L-V", "Tracksbars", 200, 255, nothing)
cv2.createTrackbar("U-H", "Tracksbars", 255, 255, nothing) 
cv2.createTrackbar("U-S", "Tracksbars", 50, 255,  nothing) 
cv2.createTrackbar("U-V", "Tracksbars", 255, 255, nothing) 

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    frame_copy = frame.copy()
    
    cv2.circle(frame_copy, top_left,     5, color, -1)
    cv2.circle(frame_copy, bottom_left,  5, color, -1)
    cv2.circle(frame_copy, top_right,    5, color, -1)
    cv2.circle(frame_copy, bottom_right, 5, color, -1)

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    transformed_frame = cv2.warpPerspective(frame, matrix, (640, 480)) 
    
    transformed_frame_hsv = cv2.cvtColor(transformed_frame, cv2.COLOR_BGR2HSV)

    LOWER_H = cv2.getTrackbarPos("L-H", "Tracksbars") 
    LOWER_S = cv2.getTrackbarPos("L-S", "Tracksbars") 
    LOWER_V = cv2.getTrackbarPos("L-V", "Tracksbars") 
    UPPER_H = cv2.getTrackbarPos("U-H", "Tracksbars") 
    UPPER_S = cv2.getTrackbarPos("U-S", "Tracksbars") 
    UPPER_V = cv2.getTrackbarPos("U-V", "Tracksbars") 

    LOWER = np.array([LOWER_H, LOWER_S, LOWER_V])
    UPPER = np.array([UPPER_H, UPPER_S, UPPER_V])

    transformed_frame_mask = cv2.inRange(transformed_frame_hsv, LOWER, UPPER)

    cv2.imshow("Bird's eye view - BGR",  transformed_frame) 
    cv2.imshow("Bird's eye view - HSV",  transformed_frame_hsv) 
    cv2.imshow("Bird's eye view - MASK", transformed_frame_mask) 

    if cv2.waitKey(0) == 27:
        break
cv2.destroyAllWindows()

