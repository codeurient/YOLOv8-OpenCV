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
    # 1) Bu kod dövrün başlanğıc vaxtını ölçür. time.time() → cari vaxtı saniyə cinsindən qaytarır.
    # Bu, FPS hesablamaları üçün lazımdır, çünki hər kadrın işləmə vaxtını hesablamaq üçün istifadə olunur.
    start = time.time()

    ret, frame = cap.read()
    if ret == False:
        break


    # 2) Bu sətr YOLO modelini frame üzərində işlədərək obyekt axtarır. 
    # verbose=False → hər xırda detalların ekrana yazılmasının qarşısını alır (konsolu lazımsız məlumatlarla doldurmamaq üçün).
    # [0]           → YOLO modeli bir neçə nəticə qaytara bilər, amma biz yalnız birinci nəticəni (results) alırıq. YOLO dokumentasiyasında, bu cür yazmaq tələb edilibdir. 
    #! Bu addımdan sonra results dəyişəni içərisində aşkarlanan obyektlərin məlumatları olur. 
    results = model(frame, verbose=False)[0]
    # 3) Bu sətr YOLO modelinin çıxışını numpy arrayına çevirir.
    # results.boxes.data → YOLO modelinin tapdığı obyektlərin sərhəd qutularını (bounding boxes) saxlayır.
    # .tolist() → YOLO çıxışını siyahıya çevirir (çünki numpy.array() funksiyası siyahını daha yaxşı emal edə bilir).
    # np.array(...) → Siyahını numpy massivinə çevirir, çünki numpy ilə işləmək sürətlidir və asandır.
    #! Bu addımdan sonra boxes dəyişəni içərisində hər obyektin `koordinatları`, `sinif ID`-si və `etibar dərəcəsi` (confidence score) olur. 
    boxes = np.array(results.boxes.data.tolist())

    # 4) Bu dövr boxes massivindəki hər bir obyektin koordinatlarını və sinif məlumatlarını götürür.
    for box in boxes:
        # print("[INFO].. Box:", box)
        # (x1, y1) → Sərhəd qutusunun sol yuxarı küncü.
        # (x2, y2) → Sərhəd qutusunun sağ aşağı küncü.
        x1, y1, x2, y2, score, class_id = box
        x1, y1, x2, y2, class_id = int(x1), int(y1), int(x2), int(y2), int(class_id)

        # print("[INFO].. Box:", x1, y1, x2, y2)
        # print("[INFO].. Class:", class_id)
        # print("[INFO].. Score:", score)


        # 5) Burada obyektin sinifinə (class_id) uyğun rəng (box_color) təyin edilir.
        # colors → Əvvəldə random rənglər yaradılmışdı. colors içində listlər var idi. class id-yə uyğun list seçilir. Həmin list içində də, 3 dənə 
        # dəyər var idi. Bu dəyərlər birlikdə rəngi təmsil edirlər. 
        box_color = colors[class_id]

        # 6) score > confidence_score → Aşkarlanan obyektin etibarlılıq səviyyəsi (score) müəyyən edilmiş həddən (confidence_score) böyükdürsə, 
        # AND aşkarlanan obyektin sinif ID-si icazə verilmiş obyektlər siyahısında (class_ids) varsa, davam et.
        if score > confidence_score and class_id in class_ids:
            # 7) Bu funksiya cv2.rectangle(), obyektin koordinatlarına (x1, y1, x2, y2) əsasən çərçivə çəkir.
            cv2.rectangle(frame, (x1, y1), (x2, y2), box_color, 2)

            # 8) Obyektin adını və etibarlılıq faizini mətn şəklində hazırlamaq. 
            # score = score * 100                           -  score faiz şəklinə çevrilir.
            # class_name = results.names[class_id]          - Obyektin adı müəyyən edilir.
            # text = f"{class_name}: %{score:.2f}"          - Məsələn, "person: %87.53" formatında mətn yaradılır.
            score = score * 100
            class_name = results.names[class_id]
            text = f"{class_name}: %{score:.2f}"

            # 9) cv2.getTextSize(text, font, 1, 1) → Mətni göstərmək üçün lazım olan ölçünü əldə edir.
            labelSize, baseLine = cv2.getTextSize(text, font, 1, 1)
            # 10) Obyektin üstündə mətni oxumaq üçün bir fon çəkir.
            cv2.rectangle(frame, 
                          (x1, y1 - 10 - labelSize[1]), 
                          (x1 + labelSize[0], int(y1 + baseLine-10)), 
                          box_color, 
                          cv2.FILLED)
            # 11) Çərçivəyə daxil edilmiş obyektin üzərində onun adını və etibarlılıq səviyyəsini göstərir.
            cv2.putText(frame, text, (x1, y1-10), font, 1, text_color_w, thickness=1)

    # 12) Nəticəni göstərmək üçün    imshow()   metodundan istifadə edirik. 
    cv2.imshow("Test", frame)
    if cv2.waitKey(20) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()