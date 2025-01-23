import cv2
import imutils  
import numpy as np

path = "test_videos\\road.mp4"
cap = cv2.VideoCapture(path)

ret, frame = cap.read()

if ret == True:
    print("[INFO]... Shape", frame.shape)
else:
    print("[INFO]... The video is not loaded successfully !")


while True:
    # 1) cv2 -nin resize metodu ilə aşağıdakı kimi formalaşdırırıq. 
    frame = cv2.resize(frame, (640, 480))

    cv2.imshow('Video', frame)

    if cv2.waitKey(0) == 27:
        break

cv2.destroyAllWindows()