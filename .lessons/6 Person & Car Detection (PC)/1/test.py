with open("coco_classes.txt", "r") as f:
    class_names = f.read().strip().split("\n")
    # print(class_names)

print(class_names[4])  # person
print(class_names[5])  # car



# 1) f.read() → Fayldakı bütün məzmunu string kimi oxuyur. 
#    f.read() icra olunduqda bu şəkildə birləşmiş mətn qaytarır:  "person\nbicycle\ncar\nmotorbike"


# 2) .strip() → Mətnin əvvəlində və sonunda olan boşluqları və əlavə \n simvollarını silir.


# 3) .split("\n") → Mətnə əsasən "\n" (sətir sonu simvolu) ilə bölərək onu siyahıya çevirir.
#    Yəni, "person\nbicycle\ncar\nmotorbike" → ["person", "bicycle", "car", "motorbike"] siyahısına çevrilir.