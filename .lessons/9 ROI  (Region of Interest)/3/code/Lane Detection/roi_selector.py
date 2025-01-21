# Kitabxanaların import edilməsi
import cv2
import numpy as np

# path: Videonun yerləşdiyi yol və fayl adı. İkiqat \\ işarəsi Windows mühitində fayl yollarını düzgün göstərmək üçün istifadə olunur.
path = "test_videos\\road.mp4"
# cv2.VideoCapture(path): cap obyektini yaradır və verilmiş path faylından video oxumağa çalışır. Əgər video düzgün yüklənibsə, bu obyekt videonu oxumaq üçün istifadə olunacaq.
cap = cv2.VideoCapture(path)

# 1) cap.read():    Videodan növbəti kadrı oxumaq üçün istifadə olunur.
# 2) ret (boolean): Oxuma əməliyyatının uğurlu olub-olmadığını göstərir.   True → Əgər kadr uğurla oxunubsa.      False → Əgər video bitibsə və ya hər hansı bir problem baş veribsə.
# 3) img (array):   Oxunan kadrın (frame) piksel məlumatlarını üçölçülü numpy massivində saxlayır (BGR rəng formatında). `print(img)` - yazaraq terminalda qayıdan dəyərə baxa bilərsiz. 
ret, img = cap.read()

# cv2.imshow: Verilən görüntünü ekranda göstərir.           a) "Test": Pəncərənin adı.           b) img: Göstəriləcək görüntü (numpy massivində olan məlumat).
cv2.imshow("Test", img)

# cv2.waitKey(0): Proqramın durması və pəncərənin bağlı qalmaması üçün istifadə olunur.  Parametr olaraq 0 verilməsi, proqramın hər hansı bir düymə basılana qədər gözləməsi deməkdir.
cv2.waitKey(0)

# cv2.destroyAllWindows(): Açılmış bütün OpenCV pəncərələrini bağlayır.
cv2.destroyAllWindows()