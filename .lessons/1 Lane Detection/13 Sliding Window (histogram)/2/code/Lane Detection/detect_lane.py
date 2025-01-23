# Aşağıdakı kodun əsas məqsədi maska görüntüsündəki müəyyən konturların (məsələn, bir yol və ya xətt) sol və sağ tərəflərini tapmaq və onları izləməkdir. 
# Hər dövrdə konturların mərkəzi koordinatları hesablanır və obyektin sol və sağ tərəfinin yerləşməsi yenilənir. Bu, obyektlərin hərəkətini izləmək üçün istifadə olunur.
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
    print("[INFO]... Check the path !")



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

    histogram = np.sum(transformed_frame_mask[transformed_frame_mask.shape[0]//2:, :], axis=0) 
    middle_point = np.int32(histogram.shape[0]/2)
    # 1) middle_point variable ilə görüntünü iki hissəyə ayırdıqdan sonra aşağıdakı kod ilə soldan başlayaraq sağ yarı ortaya qədər və 
    # ortadan başlayaraq sağ sona qədər olan hissəni scan edirik. 
    left_side = np.argmax(histogram[:middle_point])
    right_side = np.argmax(histogram[middle_point:]) + middle_point
    # 3) Bu iki list  sol və sağ tərəflərin x-koordinatlarını saxlamaq üçün yaradılıb. 
    left_x = []
    right_x = []
    # 4) Maska üzərində dəyişiklik etmək əvəzinə, onun bir nüsxəsi götürülür. Bu, orijinal maska məlumatlarını qoruyub saxlamaq üçündür.
    transformed_frame_mask_copy = transformed_frame_mask.copy()

    # 2) Sliding Window -umuzu While loop-u içində yaradacağıq. Çünki görüntüyə birdən çox kvadrat yerləşdirmək lazımdır. Ancaq ilk öncə pəncərələrin 
    # başlanğıc nöqtələrini təyin etməmiz lazımdır olduğu üçün `starting_y` adlı variable -yə 480 dəyərini veririk. 
    starting_y = 480
    # 5) starting_y dəyəri ilə hər iterasiyada maskanın müəyyən bir sətir aralığı işlənir .
    while starting_y > 0:
        # 6) Left - Maskanın 40 piksel hündürlüyü və sol tərəfdə 50 piksel sağa və sola genişlənmiş hissəsi seçilir.
        img = transformed_frame_mask[starting_y-40:starting_y, left_side-50:left_side+50]
        # 7) cv2.findContours: Seçilmiş maska hissəsində konturlar axtarılır. Konturlar şəkildə obyektlərin kənarlarını tapmağa kömək edir.
        # Python-da altdan xətt (_) bir çox məqsədlə istifadə olunur. Bu kontekstdə, cv2.findContours funksiyasından gələn ikinci qaytarılan dəyəri istifadə etməmək üçün altdan xətt istifadə olunur.
        # Yəni, konturların iyerarxiya məlumatları (hansı kontur hansı konturun içindədir və ya hansı kontur başqası ilə əlaqəlidir). Bu məlumat bizə lazım deyil.
        # Lazımsız bir dəyişən adı təyin etmək əvəzinə (hierarchy kimi), sadəcə _ istifadə olunur.
        contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            # 8) Konturdan momentlər hesablanır.
            M = cv2.moments(contour)
            # 9) M["m00"] - Konturun sahəsi (əgər 0 olarsa, kontur mərkəzi hesablanmır).
            if M["m00"] != 0:
                # 10) center_x və center_y - Mərkəz koordinatları düsturudur.
                center_x = np.int32(M["m10"] / M["m00"])
                center_y = np.int32(M["m01"] / M["m00"])

                print("Left center:", center_x, center_y)
                print("Right center:", center_x, center_y)
                # 11) Bu sətir, tapılan konturun mərkəzini əldə etdikdən sonra sol tərəfin yerini yeniləyir.
                left_side = left_side - 50 + center_x

        # Right - Yuxarıdakı ilə eyni məntiqdədir. 
        img = transformed_frame_mask[starting_y-40:starting_y, right_side-50:right_side+50]
        contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                center_x = np.int32(M["m10"] / M["m00"])
                center_y = np.int32(M["m01"] / M["m00"])
                right_side = right_side - 50 + center_x
        # 12) Son addım olaraq `rectangle()` metodu ilə işarətlərin üzərinə kvadratları çəkmək olacaq. 
        cv2.rectangle(transformed_frame_mask_copy, (left_side-60, starting_y-40), (left_side+60, starting_y-40), (255, 255, 255), 2)


        cv2.rectangle(transformed_frame_mask_copy, (right_side-60, starting_y-40), (right_side+60, starting_y-40), (255, 255, 255), 2)



        starting_y = starting_y - 40    
        print("Histogram:", histogram)

      


    cv2.imshow("Bird's eye view - BGR",             transformed_frame) 
    cv2.imshow("Bird's eye view - HSV",             transformed_frame_hsv) 
    cv2.imshow("Bird's eye view - MASK",            transformed_frame_mask) 
    cv2.imshow("Bird's eye view - Sliding Window",  transformed_frame_mask_copy) 
    if cv2.waitKey(0) == 27:
        break

cv2.destroyAllWindows()