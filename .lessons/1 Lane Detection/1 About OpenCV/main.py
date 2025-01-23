# OpenCV (Open Source Computer Vision Library) – görüntü işləmə, kompüter görmə və maşın öyrənmə tətbiqləri üçün istifadə olunan 
# açıq mənbəli bir kitabxanadır. Python-da OpenCV kitabxanası, kompüter görməsi və video işləmə ilə əlaqəli bir çox 
# funksiyanı təmin edir və çoxsaylı şəkil və video formatları ilə işləməyə imkan verir.



# OpenCV, çoxsaylı görüntü işləmə və analiz metodlarını, o cümlədən obyekt tanıma, üz tanıma, hərəkət izləmə, şəkil və video emalı, 
# optik simvolların tanınması (OCR) və daha çoxunu dəstəkləyir. Python ilə OpenCV istifadə edərək görüntü və video üzərində müxtəlif 
# əməliyyatlar həyata keçirə


# Python-da OpenCV-nin istifadəsi üçün opencv-python kitabxanasını quraşdırmaq lazımdır: pip install opencv-python

# Ən sadə istifadə nümunəsi:
import cv2

# Şəkil oxuma
image = cv2.imread('bbb.jpg')

# Şəkili göstərmək
cv2.imshow('Image', image)

# Şəkil üzərində əməliyyatlar (məsələn, şəkli boz rəngə çevirmək)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Yenidən göstərmək
cv2.imshow('Gray Image', gray_image)

# Pəncərəni bağlamaq üçün istifadə olunur
cv2.waitKey(0)
cv2.destroyAllWindows()
