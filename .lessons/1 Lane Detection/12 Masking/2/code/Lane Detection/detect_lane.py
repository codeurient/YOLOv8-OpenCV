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

# 1) TrackBar yaratmaq üçün  `createTrackbar()` metodundan istifadə edəcəyik. Bunun üçün bir metod yaratmaq lazımdır. Çünki `createTrackbar` bizdən tələb edir ki, biz ona
# boş bir metod göndərək. Metodumuzun adı `nothing()` olacaq.  Bu funksiyanın heç bir təsiri yoxdur. Sadəcə məcburi tələb edir deyə boş göndəririk. 
def nothing(x):
    pass

# 2) ilk öncə, TrackBar üçün pəncərə yaratmaq lazımdır. Pəncərəmizin adı, "Tracksbars" olacaq. Həmin pəncərəni yaratmaq üçün də, `namedWindow()` metodundan istifadə edirik.
cv2.namedWindow("Tracksbars")
# 3) Sonra createTrackbar() metodu ilə, `Tracksbar` -larımızı pəncərəyə yerləşdiririk. Bu kod rəng aralığını təyin etmək üçün istifadə olunur və əsasən HSV rəng məkanında rəng filtrasiyası üçün tətbiq edilir.

cv2.createTrackbar("L-H", "Tracksbars", 0, 255,   nothing) # L-H (Lower Hue): Hue üçün aşağı hədd.
cv2.createTrackbar("L-S", "Tracksbars", 0, 255,   nothing) # L-S (Lower Saturation): Saturation üçün aşağı hədd.
cv2.createTrackbar("L-V", "Tracksbars", 200, 255, nothing) # L-V (Lower Value): Value üçün aşağı hədd.

cv2.createTrackbar("U-H", "Tracksbars", 255, 255, nothing) # U-H (Upper Hue): Hue üçün yuxarı hədd.
cv2.createTrackbar("U-S", "Tracksbars", 50, 255,  nothing) # U-S (Upper Saturation): Saturation üçün yuxarı hədd.
cv2.createTrackbar("U-V", "Tracksbars", 255, 255, nothing) # U-V (Upper Value): Value üçün yuxarı hədd.

# 5) Bu L-H, L-S, L-V və U-H, U-S, U-V yazılarının əsas məqsədi, şəkil və ya videoda yalnız müəyyən rəngləri seçərək, digər rəngləri aradan qaldırmaqdır.

# NOT: Proqramı işə saldıqda `Şəkil 1` dəki kimi rəng politrini əks etdirən qrafika görəsiyik. Bu qrafikanı hərəkət etdirdiyimiz zaman, fərqli rəng çalarları əldə etməliyik.
# Aşağıdakı While döngüsünün içində qrafikanı hərəkət etdirdikcə dəyərləri çəkmək lazımdır. 

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

    cv2.imshow("Bird's eye view - BGR", transformed_frame) 
    cv2.imshow("Bird's eye view - HSV", transformed_frame_hsv) 

    if cv2.waitKey(0) == 27:
        break
cv2.destroyAllWindows()

