# 1) İndi yuxarıdan quş baxışı görüntü yaratmaq üçün dönüşdürmə matrisinə ehtiyac var. Bunun üçün getPerspectiveTransform() metodundan istifadə edəsiyik. 
import cv2
import imutils  
import numpy as np

top_left     = (230, 399)
bottom_left  = (133, 467)
top_right    = (385, 401)
bottom_right = (455, 462)

# 3)
pts1 = np.float32([top_left, bottom_left, top_right, bottom_right])
pts2 = np.float32([ [0,0], [0,480], [640,0], [640,480] ])  # Bu koordinatlar 640 x 480 ölçülü bir görüntünün künc nöqtələrini təmsil edir.

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

    cv2.circle(frame, top_left,     5, color, -1)
    cv2.circle(frame, bottom_left,  5, color, -1)
    cv2.circle(frame, top_right,    5, color, -1)
    cv2.circle(frame, bottom_right, 5, color, -1)

    # 2) Bu metod 2 arqumnet qəbul edəcək (poin 1 və point 2). Point 1,  yuxarıdakı `top_left, bottom_left, top_right, bottom_right` ROİ -lərini ifadə edir.
    # Point 2 isə, görüntünün ölçüsünü ifadə edir. İndi yuxarıda pts1, və pts2 variable-larını yaradaq. 
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    # 4) funksiyası bir görüntünü (və ya video kadrını) təyin olunmuş koordinatlara uyğun şəkildə yenidən xəritələyir.
    # frame:      Bu, transformasiya ediləcək orijinal görüntüdür (və ya video kadrıdır).
    # matrix:     Bu, perspektiv transformasiya matrisidir. cv2.getPerspectiveTransform() ilə hesablanır və orijinal nöqtələri (məsələn, pts1) yeni nöqtələrə (məsələn, pts2) uyğunlaşdırır.
    # (640, 480): Bu, transformasiya sonrası görüntünün yeni ölçüsünü təyin edir:
    transformed_frame = cv2.warpPerspective(frame, matrix, (640, 480))

    cv2.imshow('Video', frame)
    # 5) Əgər Quş baxışı görüntünü görmək istəyiriksə onuda imshow() metodu ilə göstərə bilərik. NOT: Yaşıl nöqtələrdə görünəsidi. Şəkil 1
    cv2.imshow('Video', transformed_frame)
    if cv2.waitKey(0) == 27:
        break
cv2.destroyAllWindows()
