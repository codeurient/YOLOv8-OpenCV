import cv2
import numpy as np

path = "test_videos\\road.mp4"
cap = cv2.VideoCapture(path)

ret, img = cap.read()

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # print("Coordinates({}, {})".format(x, y))
        pass


cv2.imshow("Test", img)
cv2.setMouseCallback("Test", click_event)  

# 1) 
# cv2.waitKey: OpenCV-də klaviatura düymələrini tutmaq (yəni gözləmək və oxumaq) üçün istifadə olunur.
# Parametr: 0  - 0 verildikdə, proqram sonsuz müddətə klaviatura girişini gözləyir. İstənilən düymə basıldıqda, proqram həmin düymənin ASCII kodunu qaytarır. Məsələn: 27 ESC (Escape) düyməsinin ASCII kodudur.
# Əgər ESC düyməsi basılıbsa (cv2.waitKey(0) geri 27 qaytararsa), aşağıdakı kod blokunu icra edir.
if cv2.waitKey(0) == 27:
    # cv2.imwrite: Şəkili fayl kimi yadda saxlamaq üçün istifadə olunur. Proqram img dəyişənindəki görüntünü coordinates.png adlı fayl kimi saxlayır.
    cv2.imwrite("coordinates.png", img) # Şəkil 1


cv2.destroyAllWindows()