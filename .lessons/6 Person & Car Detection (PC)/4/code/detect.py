import cv2
import time
import random
import numpy as np
from ultralytics import YOLO

confidence_score = 0.5

text_color_b = (0,0,0)
text_color_w = (255,255,255)

font = cv2.FONT_HERSHEY_SIMPLEX

class_ids = [0, 1, 2, 3, 5, 6, 7, 8]

total_fps = 0
average_fps = 0
num_of_frame = 0
# 1) Bu, boş bir siyahı (list) yaradır və videonun kadrlarını (frames) saxlamaq üçün nəzərdə tutulub.
# Kadrlar (frame) — videonun hər bir ayrı-ayrı şəkilləridir.
video_frames = []

model = YOLO("models/yolov8n.pt")
labels = model.names
colors = [[random.randint(0, 255) for _ in range(0,3)] for _ in labels]

# 2) Videonu çağıraraq görüntünü əldə edirik.
video_path = "inference/test.mp4"
cap = cv2.VideoCapture(video_path)

# 3) videonun enini və uzunluğunu müəyyən edirik.
width = int(cap.get(3))
height = int(cap.get(4))
# 4) Bu kod videonun ümumi çərçivə (frame) sayını tapır. total_frames dəyəri, videonun neçə çərçivədən (frame) 
# ibarət olduğunu göstərir və videonu analiz edərkən "harada dayanaq" sualına cavab verməyə kömək edir.
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# 5) Ekrana çap ədərək dəyərləri görə bilərik
print("[INFO].. Width:", width)
print("[INFO].. Height:", height)
print("[INFO].. Total Frames:", total_frames)

# 6) Bu kod OpenCV (cv2) kitabxanasından istifadə edərək videonu oxuyur və göstərir. Sonsuz dövr yaradırıq ki, video 
# tam oxunana qədər və ya biz "q" düyməsinə basana qədər işləsin.
while True:
    # 7) Bu kod hər dəfə cap.read() funksiyasını çağırır və növbəti kadrı (frame) oxuyur.
    # ret   — True və ya False qaytarır: True → əgər kadr düzgün oxunubsa. False → əgər artıq video bitibsə (və ya səhv baş veribsə).
    # frame — videodan oxunan cari çərçivədir (şəkildir).
    ret, frame = cap.read()
    # 6) Bu kod videonun bitib-bitmədiyini yoxlayır. Əgər video artıq oxunmursa (ret == False), dövr dayandırılır (break).
    if ret == False:
        break

    # 7) Bu kod hazırda oxunan çərçivəni (frame) ekranda göstərir. 
    cv2.imshow("Test", frame)
    # 8) 20 millisaniyə gözləyir (bu, videonun sürətini tənzimləməyə kömək edir).
    #    & 0xFF     → OpenCV-nin waitKey() funksiyasının düzgün işləməsi üçün əlavə edilir.
    #    ord("q")   → "q" düyməsinin ASCII kodu ilə müqayisə edilir. Əgər istifadəçi "q" düyməsinə basarsa, break əmri icra olunur və dövr dayanır.
    if cv2.waitKey(20) & 0xFF==ord("q"):
        break

# 9) Bu kod videonu oxuyan obyektin (cap) yaddaşdan çıxarılmasını təmin edir. Əgər cap.release() çağırılmazsa, bəzi sistemlərdə videofayl açıq qalır 
# və digər proqramlar tərəfindən istifadə edilə bilmir.
cap.release()
# 10) Bu kod bütün açıq OpenCV pəncərələrini bağlayır. Əgər bu kod olmasa, pəncərələr açıq qala bilər və proqram tam bağlanmaz.
cv2.destroyAllWindows()