import cv2
import imutils  
import numpy as np

# 1) koordinatlarımızı köçürdük. 
top_left     = (230, 399)
bottom_left  = (133, 467)
top_right    = (385, 401)
bottom_right = (455, 462)
# 2) rəngimizi yaratdıq.
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
    # 5)
    frame = cv2.resize(frame, (640, 480))
    # 3) Koordinatlarımızı şəklin üzərinə yerləşdiririk. 
    cv2.circle(frame, top_left,     5, color, -1)
    cv2.circle(frame, bottom_left,  5, color, -1)
    cv2.circle(frame, top_right,    5, color, -1)
    cv2.circle(frame, bottom_right, 5, color, -1)

    cv2.imshow('Video', frame)

    # 4) Dərsə başlayanda demişdik ki, video-dan sabit bir görüntü əldə edəcəyik. Bu şəklin sabit qalmasının səbəbi `waitKey(0)` metoduna 0 (sıfır) verməyimizdir.
    # Videonun hərəkətə gəlməsi üçün bu dəyəri 10 edirik. Dəyər nə qədər yüksək olarsa video o qədər yavaş hərəkət edər. Sonra isə:  frame = cv2.resize(frame, (640, 480))
    # bu kodu WHILE loopuna yerləşdiririk ki, READ() metodu təkrar-təkrar oxusun videonu. Video sona çatanda frame qapanır və WHILE dayanır. 
    if cv2.waitKey(0) == 27:
        break

cv2.destroyAllWindows()