# imutils Python-da OpenCV ilə işləmək üçün hazırlanmış bir kitabxanadır. Bu kitabxana, OpenCV-nin bəzi əsas funksiyalarını 
# daha sadə və istifadəsi asan formada təqdim edir. Əsas məqsədi görüntü işləmə zamanı tez-tez istifadə edilən əməliyyatları asanlaşdırmaqdır.


# Məsələn biz `imutils` kitabxanasını ölçü təyin etmək üçün istifadə edəsiyik. Ancaq CV2 -də istifadə edə bilərdik. 

# imutils ilə cv2 arasındakı ölçü təyin etmə fərqi:
#         a) cv2 ilə ölçü dəyişdirmə:    
#                                     Əl ilə en (width) və hündürlük (height) dəyərlərini təyin etməlisiniz.
#                                     Proportion (nisbət) qorunmur, əgər düzgün hesablama aparmasanız, görüntü deformasiya ola bilər.
#                                     Proportion-u qorumaq üçün nisbəti hesablamaq üçün ayrıca kod yazmalısınız.

#         b) imutils ilə ölçü dəyişdirmə:
#                                     imutils kitabxanası avtomatik olaraq proportion-u (nisbəti) qoruyur.
#                                     Yalnız en (width) dəyərini təyin edirsiniz, hündürlük avtomatik olaraq nisbətə görə hesablanır.


import cv2
import imutils  # 1) Əgər yüklü deyils bu kitabxananı install etmək lazımdır: pip install imutils. Hələ istifadə etməmişik sonra edəsiyik.
import numpy as np

path = "test_videos\\road.mp4"
cap = cv2.VideoCapture(path)

ret, frame = cap.read()

if ret == True:
    # 2) frame.shape OpenCV-də bir görüntünün (və ya video kadrının) ölçülərini və rəng kanallarını təyin edən bir xüsusiyyətdir.
    print("[INFO]... Shape", frame.shape)
else:
    print("[INFO]... The video is not loaded successfully !")

# 3) Geri qayıdan dəyər: [INFO]... Shape (720, 1280, 3)
# Bu dəyər bir tupl şəklindədir və 3 hissədən ibarətdir:
#                                                        720:    Hündürlük (height) - görüntünün şaquli ölçüsü, piksel sayıdır.
#                                                        1280:   En (width) - görüntünün üfüqi ölçüsü, piksel sayıdır.
#                                                        3:      Rəng kanallarının sayı (channels) - rəngli görüntü üçün bu dəyər 3 olur (BGR - Mavi, Yaşıl, Qırmızı).

# Kadrın ölçüsü nə üçün əhəmiyyətlidir?
#               Görüntü işləmə zamanı ölçüləri bilmək, şəkil ölçüsünü dəyişmək (resize), bölgələri seçmək (ROI), və ya fərqli manipulyasiyalar etmək üçün vacibdir.