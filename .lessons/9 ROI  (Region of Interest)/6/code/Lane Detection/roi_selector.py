import cv2
import numpy as np

color = (0, 255, 0) # 1) color adında variable yaradaraq yaşıl rəngin dəyərlərini tuple tipində yazırıq. OpenCV-də rənglər BGR (Blue, Green, Red) formatında verilir.

path = "test_videos\\road.mp4"
cap = cv2.VideoCapture(path)

ret, img = cap.read()

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # 2) Bu funksiya OpenCV-də bir görüntünün üzərinə dairə çəkmək üçün istifadə olunur.
        #       img:      Dairənin çəkiləcəyi görüntü (bu halda img dəyişəni).
        #       (x, y):   Dairənin mərkəz koordinatları.
        #       5:        Dairənin radiusu (5 piksel).
        #       color:    Dairənin rəngi (bu halda yaşıl: (0, 255, 0)).
        #       -1:       Dairənin içini doldurmaq üçün istifadə olunur. Əgər -1 əvəzinə müsbət bir rəqəm verilsəydi, dairə həmin qalınlıqla çəkilərdi (içi boş olardı).
        cv2.circle(img, (x, y), 5, color, -1)
        
        # 3) Hər klikdən sonra şəklin üzərində nöqtələr olacaq və yeni nöqtə ilə şəkli təkrar göstərmək lazımdır deyər imshow() metodunu funksiya içində yenidən yazırıq. 
        cv2.imshow("Test", img)


cv2.imshow("Test", img)
cv2.setMouseCallback("Test", click_event)  

if cv2.waitKey(0) == 27:
    cv2.imwrite("coordinates.png", img) 


cv2.destroyAllWindows()




