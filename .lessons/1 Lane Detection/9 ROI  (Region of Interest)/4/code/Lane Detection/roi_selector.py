import cv2
import numpy as np

path = "test_videos\\road.mp4"
cap = cv2.VideoCapture(path)

ret, img = cap.read()

# 1) click_event: OpenCV pəncərəsində siçan hadisələrini (mouse events) işləmək üçün yazılmış istifadəçi təyinli funksiyadır.
# event: Hər hansı bir siçan hadisəsini təmsil edən dəyişən
# x, y: Siçanın pəncərə içindəki klik etdiyi yerin koordinatları.
# flags: Siçan ilə bağlı xüsusi əlavə məlumatları saxlayan parametr. Bu kodda istifadə olunmayıb.
# param: İstifadəçi tərəfindən əlavə məlumat ötürmək üçün nəzərdə tutulmuş parametr. Bu da burada istifadə olunmayıb.
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # print("Coordinates(x, y): ", x, y)  # Şəkil 1
        print("Coordinates({}, {})".format(x, y))  # Yaxud Belə yaza bilərik. 


cv2.imshow("Test", img)

# 2) cv2.setMouseCallback: Verilən bir OpenCV pəncərəsinə (window) siçan hadisələrini bağlamaq üçün istifadə olunur.
# "Test": Siçan hadisələrini izləmək üçün nəzərdə tutulmuş OpenCV pəncərəsinin adı. Bu ad daha əvvəl yaradılmış bir pəncərənin adı olmalıdır, məsələn, cv2.imshow("Test", img).
# click_event: Siçan hadisələrini işləmək üçün çağırılacaq funksiyanın adı. Bu halda, click_event funksiyası.
cv2.setMouseCallback("Test", click_event)  

cv2.waitKey(0)

cv2.destroyAllWindows()