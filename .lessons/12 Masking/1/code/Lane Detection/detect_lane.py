# Quş baxışı görüntü aldıqdan sonra yol işarətlərini çıxartmaq, əldə etmək lazımdır. Buna maskalama əməliyyatı deyilir. Maskalamamı rəng üzərindən gərçəkləşdirə 
# bilərik. Rəng üzərində maskalama etmək üçün isə, rənglər arasında keçidlər etmək lazımdır. Yəni, loru dildə deəsək məsələn, qırmıza çevirmək sonra o qırmızını 
# sarıya çevirmək kimi. Əslində qırmızıya çevirmirik bu sadəcə bir misaldır.
#  
# Rəngə əsaslanan maskalama əməliyyatlarında, HSV (hue, value, saturation) adlanan rəng orqanizasiyasından ( RGB, ARGB, CMYK kimi fərqli rəng orqanizasiyaları mövcuddur ) 
# istifadə edilir. Yəni ilk öncə HSV rəng orqanizasiyasına keçid etməliyik sonra isə istədiyimiz işarətləri maskalıya bilərik. Bəs düzgün HSV dəyərlərini necə əldə edə bilərik ? 
# Bunun üçün fərqli qaydalardan istifadə edə bilərik: Məsələn, ağ rəngin HSV dəyərlərini əldə edə bilərik. Ancaq ən yaxşı yanaşma TRACKBAR istifadə etməkdir. 

#  trackbar, bir görüntünün spesifik rəng aralığını təyin etmək və həmin rəngləri interaktiv şəkildə ayırmaq üçün istifadə olunur. Bunun üçün `createTrackbar()` metodu 
# istifadə edilir.

# Qısaca, 1) görüntünü HSV formatına çevirəsiyik.
#         2) Sonra trackbar ilə uyğun HSV dəyərlərini tapıb, yol işarətlərini maskalayacağıq.

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
    frame_copy = frame.copy()
    
    cv2.circle(frame_copy, top_left,     5, color, -1)
    cv2.circle(frame_copy, bottom_left,  5, color, -1)
    cv2.circle(frame_copy, top_right,    5, color, -1)
    cv2.circle(frame_copy, bottom_right, 5, color, -1)

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    transformed_frame = cv2.warpPerspective(frame, matrix, (640, 480)) 
    
    # 1) Bu kod, transformed_frame adlı bir görüntünü RGB rəng modelindən (OpenCV-də BGR olaraq istifadə olunur) HSV (Hue, Saturation, Value) rəng modelinə çevirir.
    # cv2.cvtColor() funksiyası: rəng məkanını çevirmək üçün istifadə olunur.
    #       İlk parametr: Çevirmək istədiyiniz görüntü
    #       İkinci parametr: Hədəf rəng məkanını təyin edir (burada: cv2.COLOR_BGR2HSV).
    transformed_frame_hsv = cv2.cvtColor(transformed_frame, cv2.COLOR_BGR2HSV) # hsv variable adını transformed_frame_hsv adı ilə əvəz elədim ki, məntiqli olsun. 

    # cv2.imshow('Frame', frame_copy) 
    # 2) Aradakı fərqə baxa bilərik. Şəkil 1
    cv2.imshow("Bird's eye view - BGR", transformed_frame) 
    cv2.imshow("Bird's eye view - HSV", transformed_frame_hsv) # hsv variable adını transformed_frame_hsv adı ilə əvəz elədim ki, məntiqli olsun. 

    if cv2.waitKey(0) == 27:
        break
cv2.destroyAllWindows()

