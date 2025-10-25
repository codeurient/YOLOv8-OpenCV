# NOT: Aşağıdakı kodların daha ətraflı izahı Qovluq 3 -də qeyd edilmişdir !

# Koordinatları taparaq ROİ çıxarmaq üçün kodlarımızı yazaq. 

# Lane Detection içində `roi_selector.py` adında fayl yaradırıq. 



# Bu faylda yazacağımız kod ilə ( OpenCV istifadə edərək FRAME oxuyasıyıq. ) videonun hər hansısa bir sahəsini seçərək müəyyən yerləri mausla (Yenə OpenCV metodları ilə.
# Bunlara mouse event-ları deyilir) işarətləyəsiyik. İşarətlənin hissələrin də, koordinatlarını əldə edərək variable -lar içinə yaza bilərik. 

# 1) OpenCV - read a frame: cap.read()
# 2) mouse event - define mouse event: cv2.EVENT_LBUTTONDOWN
# 3) Show results.



import cv2
import numpy as np

path = "test_videos\\road.mp4"
cap = cv2.VideoCapture(path)

ret, img = cap.read()

cv2.imshow("Test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()




# Sonra proqramı işə salırıq. Əgər belə bir xəta yaranarsa:        Fatal error in launcher: Unable to create process using '"d:\OpenCV\.venv\Scripts\python.....
# Bu, xətanın səbəbi, pip-in istifadə etdiyi Python mühitinin (virtual environment) düzgün qurulmaması və ya Python icraedici faylının mövcud olmamasıdır. 

# 1) Yeni virtual mühit yaradın:
#                 a) Əvvəlcə mövcud .venv qovluğunu silin:   Remove-Item -Recurse -Force .venv
#                 b) Yeni virtual mühit yaradın:             python -m venv .myenv
#                 c) Virtual mühiti aktivləşdirin:           .\.myenv\Scripts\activate
#                 d) pip-i yenidən yoxlayın:                 pip --version

# 2) Remove-Item -Recurse -Force .venv - bu əmri yazan zaman belə bir xəta olarsa: Remove-Item : Cannot remove item D:\YOLO......
#    Bu problem .venv\Scripts\python.exe faylının başqa bir proses tərəfindən istifadə olunması səbəbindən baş verir.
#                 a) Virtual mühitdən çıxın:                                                        deactivate
#                 b) PowerShell-də aktiv Python proseslərini yoxlayın:                              Get-Process python
#                 c) Əgər aktiv Python prosesləri siyahıda görünürsə, bu əmrlə onları dayandırın:   Stop-Process -Name python -Force


# İndi yenə 1 nömrədə yazılanları terminalda təkrar yazaraq təkrar silmə əmri yerinə yetirə bilərik.

# Şəkil nömrə 1-də bu qurma addımlarını və nəticənin uğurla tamamlandığını görə bilərik. 

# pip install opencv-python - Sonra isə bu əmri yazaraq OPENCV qura və kodumuzu işə salaraq onun işləyib işləmədiyini test edə bilərik. 

# Əmri işə salmazdan əvvəl VScode üzərində, `Lane Detection` qovluğunu ayrıca bir proyekt kimi açın (Şəkil 2). 