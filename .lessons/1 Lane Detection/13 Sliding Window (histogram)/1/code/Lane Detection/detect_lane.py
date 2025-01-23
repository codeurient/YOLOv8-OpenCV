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

    

    # 1) Yol işarətlərinin üzərinə `window` qoymaq üçün görüntünü ilk öncə ortadan ikiyə bölmək lazımdır. Sonra bölgünün soluna və sağına düşən işarətləri seçə bilərik. 
    # Aşağıdakı iki sətrlik kod (histogram və middle_point), bir şəklin xüsusiyyətlərini analiz etmək üçün histogram çıxarır və bir mərkəz nöqtə təyin edir.

    # 1ci sətrdəki kodda olan cüt nöqtələr İNDEXİNG qaydasıdır:              :,: 
    # Tutaq ki, bir massiviniz var: array = np.array([10, 20, 30, 40, 50])
    #       array[:] - Bütün elementləri seçir: [10, 20, 30, 40, 50]
    #       array[1:] - İlk indeksdən başlayaraq qalanları seçir: [20, 30, 40, 50]
    #       array[:3] - İlk 3 elementi seçir: [10, 20, 30]

    # [0]//2:,: - Bu nədir?
    # [0]       - Matrisanın ilk ölçüsünün dəyərini alır. Məsələn, transformed_frame_mask.shape[0] matrisanın hündürlüyünü verir.
    # böl  //2  - Hündürlüyü 2-yə bölərək yarısını alır. Bu, şəkilin alt yarısına baxmaq üçündür.
    # :         - İki nöqtə göstərir ki, bütün aralıq seçilsin. Birinci iki nöqtə (sətir seçimi): transformed_frame_mask.shape[0]//2: sətirlərin 
    #             yarısından sonrasını seçir. İkinci iki nöqtə (sütun seçimi): : bütün sütunları seçir.
    histogram = np.sum(transformed_frame_mask[transformed_frame_mask.shape[0]//2:,:], axis=0) # axis=0: Sətirlər üzrə toplama aparılır (vertikal cəmləmə). Yəni, hər bir sütun üçün sətirlərin toplamını verir.
    middle_point = np.int32(histogram[0]/2)

    # Qayıdan dəyərləri görmək üçün onları terminala çap edə bilərik. 
    print("transformed_frame_mask: ",                                        transformed_frame_mask)
    print("transformed_frame_mask.shape: ",                                  transformed_frame_mask.shape)                                   # [hündürlük (480) və eni verir (640)]
    print("transformed_frame_mask.shape[0]: ",                               transformed_frame_mask.shape[0])                                # maskanın təkcə hündürlüyünü verir (480).
    print("transformed_frame_mask.shape[0]//2: ",                            transformed_frame_mask.shape[0]//2)                             # maskanın yalnız alt yarısına fokuslanır (240). Bu, ümumiyyətlə yolda zolaq xətlərini axtarmaq üçün edilir, çünki yol xəttləri adətən görüntünün alt hissəsində yerləşir.
    print("transformed_frame_mask[transformed_frame_mask.shape[0]//2:,:]: ", transformed_frame_mask[transformed_frame_mask.shape[0]//2:,:])  # Bu hissə maskanın alt yarısını seçir.
    print("histogram: ",                                                     histogram)                                                      # sum() -hündürlük boyunca toplama əməliyyatını yerinə yetirir. Bu, hər bir sütundakı ağ piksellərin sayını hesablayır.
    print("histogram[0]: ",                                                  histogram[0])                                                   # Histogramın ilk sütunundakı dəyəri verir. Burada ən sol sütundakı piksellərin sayını göstərir.
    print("histogram[0]/2: ",                                                histogram[0]/2)                                                 # İlk sütundakı dəyəri 2-yə bölür. Bu, bəzi analizlər üçün referans nöqtəsi kimi istifadə oluna bilər.
    print("middle_point: ",                                                  middle_point)                                                   # int32() - Alınan dəyəri tam ədədə (integer) çevirir.



    cv2.imshow("Bird's eye view - BGR",  transformed_frame) 
    cv2.imshow("Bird's eye view - HSV",  transformed_frame_hsv) 
    cv2.imshow("Bird's eye view - MASK", transformed_frame_mask) 

    if cv2.waitKey(0) == 27:
        break
cv2.destroyAllWindows()

