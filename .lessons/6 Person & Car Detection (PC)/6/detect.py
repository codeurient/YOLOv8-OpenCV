import cv2
import time
import random
import numpy as np
from ultralytics import YOLO

confidence_score = 0.5

text_color_b = (0,0,0)
text_color_w = (255,255,255)
# 1) Arxan fon üçündə bir variable yaradırıq. 
background_color = (0,255,0)

font = cv2.FONT_HERSHEY_SIMPLEX

class_ids = [0, 1, 2, 3, 5, 6, 7, 8]

total_fps = 0
average_fps = 0
num_of_frame = 0
video_frames = [] 

model = YOLO("models/yolov8n.pt")
labels = model.names
colors = [[random.randint(0, 255) for _ in range(0,3)] for _ in labels]

video_path = "inference/test.mp4"
cap = cv2.VideoCapture(video_path)

width = int(cap.get(3))
height = int(cap.get(4))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

while True:
    start = time.time()

    ret, frame = cap.read()
    if ret == False:
        break

    results = model(frame, verbose=False)[0]
    boxes = np.array(results.boxes.data.tolist())

    for box in boxes:
        x1, y1, x2, y2, score, class_id = box
        x1, y1, x2, y2, class_id = int(x1), int(y1), int(x2), int(y2), int(class_id)

        box_color = colors[class_id]

        if score > confidence_score and class_id in class_ids:
            cv2.rectangle(frame, (x1, y1), (x2, y2), box_color, 2)

            score = score * 100
            class_name = results.names[class_id]
            text = f"{class_name}: %{score:.2f}"

            labelSize, baseLine = cv2.getTextSize(text, font, 1, 1)
            cv2.rectangle(frame, 
                          (x1, y1 - 10 - labelSize[1]), 
                          (x1 + labelSize[0], int(y1 + baseLine-10)), 
                          box_color, 
                          cv2.FILLED)
            cv2.putText(frame, text, (x1, y1-10), font, 1, text_color_w, thickness=1)

    
    # 2) Aşağıdakı hissə videoda FPS hesablamaları və ekranda FPS-in göstərilməsi üçün istifadə olunur. Hissə-hissə izah edək:
    # start = time.time() ilə dövrün əvvəlində vaxt qeyd edilir.
    # end = time.time() ilə dövrün sonunda vaxt yenidən ölçülür.
    # Bu iki ölçü arasındakı fərq bir kadrın işlənmə müddətini (saniyədə) müəyyən edir.
    end           = time.time()

    # 3) FPS – saniyədə neçə kadrın işlənildiyini göstərir. Bunun üçün xüsusi formul fardır:    FPS 1 / bir kadrın işlənmə müddəti (saniyə)
    # Misal: Əgər bir kadrın işlənmə müddəti 0.05 saniyədirsə:   FPS 1 / 0.05 = 20 .    Yəni saniyədə 20 kadr işlənir.
    # num_of_frame  += 1                                    → Hər işlənmiş kadr üçün say artırılır.
    # total_fps     += fps                                  → FPS dəyərləri cəmlənir.
    # average_fps   = total_fps / num_of_frame              → Ümumi FPS sayına bölünərək orta FPS hesablanır.
    # avg_fps       = float("{:.2f}".format(average_fps))   → Orta FPS 2 onluq rəqəmlə formatlanır (məsələn: 23.56 FPS).
    num_of_frame  += 1
    fps           = 1 / (end - start)
    total_fps     = total_fps + fps
    average_fps   = total_fps / num_of_frame
    avg_fps       = float("{:.2f}".format(average_fps))

    # 4) FPS göstəricisi üçün fon yaradılır:
    # (10,2)             → Sol yuxarı küncdəki başlanğıc nöqtə.
    # (280,50)           → Sağ aşağı küncdəki bitiş nöqtə.
    # background_color   → FPS-in göstəriləcəyi fondur (yaşıl (0,255,0)).
    # -1                 → Düzbucaqlı tam doldurulur.
    cv2.rectangle(frame, (10,2), (280,50), background_color, -1)

    # 5) FPS mətni ekrana yazılır:
    # "FPS: "+str(avg_fps)   → FPS dəyəri mətnə çevrilir və göstərilir.
    # (20,40)                → Mətnin yerləşdiyi koordinat.
    # 1.5                    → Mətnin ölçüsü.
    # text_color_b (0,0,0)   → Mətnin rəngi (qara).
    # thickness=3            → Mətnin qalınlığı.
    cv2.putText(frame, "FPS: "+str(avg_fps), (20,40), font, 1.5, text_color_b, thickness=3)

    # 6) Hər işlənmiş kadr `video_frames` massivinə əlavə olunur (sonradan video kimi saxlanması üçün).
    video_frames.append(frame)


    cv2.imshow("Test", frame)
    if cv2.waitKey(20) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()