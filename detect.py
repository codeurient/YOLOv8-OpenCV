import cv2
import time
import random
import numpy as np
from ultralytics import YOLO

confidence_score = 0.5

text_color_b = (0,0,0)
text_color_w = (255,255,255)

font = cv2.FONT_HERSHEY_SIMPLEX

class_ids = [0, 1, 2, 3, 5, 6, 7]

total_fps = 0
average_fps = 0
num_of_frames = 0


# Bu kod hissəsi YOLO modelini yükləyir, obyekt kateqoriyalarını (labels) alır və hər bir obyekt üçün təsadüfi rənglər təyin edir. Hissə-hissə izah edək:
# 1️⃣ YOLO Modelinin Yüklənməsi:
#                               YOLO("models/yolov8n.pt")   → yolov8n.pt adlı YOLOv8 Nano modelini yükləyir.
#                               YOLOv8 Nano (yolov8n.pt)    → YOLO modelinin ən yüngül versiyasıdır, daha sürətli işləyir, amma daha az dəqiq nəticələr verə bilər.
#                               Əgər `yolov8n.pt` modeli `models` qovluğunda mövcud deyilsə onda bu fayl həmin qovluq içinə endiriləcək. 
model = YOLO("models/yolov8n.pt")



# 2️⃣ Modelin Kateqoriyalarını Almaq
# model.names → YOLO modelinin tanıya biləcəyi obyekt kateqoriyalarını (labels) siyahı (list) şəklində qaytarır.
labels = model.names
# Coco Dataset istifadə edilirsə, bu kateqoriyalar 80 müxtəlif obyekt ola bilər (məsələn, person, car, bus, dog, cat və s.).
# Bütün dataları görmək yaxud sayısını görmək üçün `labels` variable -ının dəyərini ekrana çap edə bilərik. 
print("Labels:\n", labels)                              # Mövcud kateqoriyaların adlarını ekrana çıxarır.
print("[INFO].. Number of Class: ", len(labels))        # Ümumi kateqoriya sayını çap edir: 80 dənə label var. 



# 3️⃣ Hər Bir Obyekt Üçün Təsadüfi Rənglər. Bu kod iki səviyyəli List Comprehension istifadə edir. Onu parçalayaq:
# [random.randint(0, 255) for _ in range(0,3)]      - Daxili Dövr (Inner Loop)
# for _ in labels                                   - Siyahıda neçə obyekt varsa, hər biri üçün bir dənə RGB rəngi yaradılır.
colors = [[random.randint(0, 255) for _ in range(0,3)] for _ in labels]
print(colors)
print("[INFO].. Number of Class: ", len(colors))


# _ Simvolunun Mənası:  Python-da _ (alt xətt, underscore) dəyişən adı kimi istifadə edilə bilər, amma xüsusi mənaları var.
# 🚀 Bu kodda _ sadəcə olaraq bir iterasiya dəyişənidir, lakin biz onu istifadə etmədiyimiz üçün _ qoymuşuq.
# 🟢 Əgər _ yerinə `i` yazsaydıqda, kod işləyərdi:


# Biz sadəcə `i`  ona görə yazmamışıq ki, `labels` içindən gələnləri istifadə etmək istəmirik. Bizə sadəcə həmin `labels` içində olan dəyərlərin sayı əsasdır. Bu say 80 olduğu 
# üçün FOR döngüsü 80 dəfə təkrarlanacaq. FOR əgər 80 dəfə təkrarlanarsa onda həmin FOR -un solunda dayanan və içində random ilə əlaqəli kodlar olan list-də [...] 80 dəfə təkrarlanacaq. 
# Həmin LİST içində olan FOR döngüsü isə onun sağında yazılan `RANDİT`-in qaytardığı dəyərləri 3 dəfə təkrarlayacaq. Beləliklə 80 dənə [33, 76, 122] bu cür fərqli LİST əldə etmiş olacağıq.
# [  [33, 76, 122],   [53, 86, 23],   [42, 2, 74],   [77, 22, 52],   [5, 6, 233]  ...  ]







#! Tək-tək kodun hissələrini `a` və `b` adlı variable içinə yerləşdirərək, onların nə qaytardığına baxa bilərik. Belə etsək yuxarıdakı kodu daha rahat başa düşərik.
# a = random.randint(0, 255)                              #! R,G,B (Red, Green, Blue) üçün təsadüfi 0-255 arasında dəyərlər seçir.
# print(a)                                                #! Hər dəfə random bir ədəd verir. Məsələn: 46
# b = [random.randint(0, 255) for _ in range(0,3)]        #! 3 təsadüfi rəng dəyəri (R, G, B) seçilir.
# print(b)                                                #! Hər dəfə random 3 ədəd verir. Məsələn: [33, 76, 122]