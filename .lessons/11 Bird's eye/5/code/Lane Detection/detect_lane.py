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

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    # 1) frame -in kopyasını yaradırıq. Kopyasını normal görüntü üçün istifadə edirik. Orginalını Quş baxışı üçün istifadə edirik.  
    frame_copy = frame.copy()
    
    cv2.circle(frame_copy, top_left,     5, color, -1) # 2) 
    cv2.circle(frame_copy, bottom_left,  5, color, -1) # 2) 
    cv2.circle(frame_copy, top_right,    5, color, -1) # 2) 
    cv2.circle(frame_copy, bottom_right, 5, color, -1) # 2) 

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    transformed_frame = cv2.warpPerspective(frame, matrix, (640, 480)) 
    
    cv2.imshow('Video 1', frame_copy) # 3) Və hər frame üçün fərqli ad veririk: Video 1
    cv2.imshow('Video 2', transformed_frame) # 4) Video 2

    if cv2.waitKey(0) == 27:
        break
cv2.destroyAllWindows()

# 5) Şəkil 1
