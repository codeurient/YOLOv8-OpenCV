# Bu kod YOLO modelindən istifadə edərək müəyyən obyektləri (class_ids siyahısındakı obyektlər) aşkar 
# edir və onların tanınması prosesində FPS (Frames Per Second - kadr sürəti) ölçmələri aparır.

# cv2 (OpenCV)      → Görüntüləri oxumaq, üzərində işləmək və vizuallaşdırmaq üçün.
# time              → FPS ölçmək üçün vaxt hesablamalarında istifadə edilir.
# random            → Obyektlərin rənglərini təsadüfi seçmək üçün istifadə oluna bilər.
# numpy             → Matris və riyazi əməliyyatlar üçün.
# ultralytics       → YOLO modelini yükləmək və obyekt tanımaq üçün.

import cv2
import time
import random
import numpy as np
from ultralytics import YOLO

# confidence_score  → 50% və yuxarı etibarlılığı olan obyektlər tanınacaq. Yəni, modelin aşkar etdiyi 
# obyektin güvən səviyyəsi 0.5-dən aşağıdırsa, o obyekt vizuallaşdırılmayacaq.
confidence_score = 0.5

# Mətn rəngləri     → Qara (0,0,0) və ağ (255,255,255) rənglərində mətnlər göstərmək üçün təyin edilir.
text_color_b = (0,0,0)
text_color_w = (255,255,255)

# Şrift             → OpenCV-də mətni görüntü üzərində göstərmək üçün Hershey Simplex şrifti seçilir.
font = cv2.FONT_HERSHEY_SIMPLEX

# YOLO modelinin istifadə edəcəyi obyekt ID-ləri:
# 0 → person (İnsan)
# 1 → bicycle (Velosiped)
# 2 → car (Avtomobil)
# 3 → motorbike (Motosiklet)
# 5 → bus (Avtobus)
# 6 → train (Qatar)
# 7 → truck (Yük maşını)
class_ids = [0, 1, 2, 3, 5, 6, 7]


# total_fps     → Bütün kadrların FPS dəyərlərinin cəmini saxlayır.
total_fps = 0
# average_fps   → FPS-in ortalama dəyəri hesablanacaq.
average_fps = 0
# num_of_frames → Neçə kadrın emal edildiyini izləmək üçün istifadə edilir.
num_of_frames = 0