import cv2
import numpy as np

click_points = [] 
color = (0, 255, 0) 
font = cv2.FONT_HERSHEY_SIMPLEX 

path = "test_videos\\road.mp4"
cap = cv2.VideoCapture(path)

ret, img = cap.read()

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 5, color, -1)
        cv2.putText(img, f"({x}, {y})", (x, y-10), font, .5, color, 2)  
        cv2.imshow("Test", img)
        click_points.append((x, y)) 


cv2.imshow("Test", img)
cv2.setMouseCallback("Test", click_event)  

if cv2.waitKey(0) == 27:
    cv2.imwrite("coordinates.png", img) 
    for point in click_points:
        print(f"Coordinates: {point}")  


cv2.destroyAllWindows()