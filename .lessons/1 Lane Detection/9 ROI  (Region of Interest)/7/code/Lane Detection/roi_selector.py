import cv2
import numpy as np

click_points = []  # 1) Kliklənən hər nöqtəni list içində yadda saxlamaq üçün `click_points` variable yaradırıq.
color = (0, 255, 0) 
font = cv2.FONT_HERSHEY_SIMPLEX # 2) OpenCV -nin fontunu istifadə edirik. 

path = "test_videos\\road.mp4"
cap = cv2.VideoCapture(path)

ret, img = cap.read()

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 5, color, -1)
        # 3) Şəklin üzərinə koordinatları yerləşdiririk.
        # (x, y-10) - yazı nöqtənin üstünə düşməsin deyə 10px kənara sürüşdürürük
        # font  - yazının fontunu təyin edirik
        # .5    - yazının ölçüsünü təyin edirik
        # color - yazının rengini təyin edirik
        # 2     - yazının qalınlığını təyin edirik
        cv2.putText(img, f"({x}, {y})", (x, y-10), font, .5, color, 2)  
        cv2.imshow("Test", img)
        click_points.append((x, y))  # 4) Kliklənən hər nöqtəni list içinə əlavə edirik


cv2.imshow("Test", img)
cv2.setMouseCallback("Test", click_event)  

if cv2.waitKey(0) == 27:
    cv2.imwrite("coordinates.png", img) 
    # 5) Esc düyməsi basıldıqdan sonra da, terminala `click_points` variable dəyərlərini yazdırırıq. 
    for point in click_points:
        print(f"Coordinates: {point}")  


cv2.destroyAllWindows()




