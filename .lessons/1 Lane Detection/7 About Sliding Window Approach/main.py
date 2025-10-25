# İmage Processing texnikasında `Sliding Window Approach` deyilən bir qayda var ki, bizdə bunu istifadə edəcəyik.




# Aşağıdakı `Sliding Window Approach` nədir haqqında yazılmışdır ancaq qarmaşıq olduğu üçün praktikada tətbiq edərək izah etmək məsləhədir. 

# Şəkil 1 -də üst şəkildə,  `Sliding Window Approach` texnikası istifadə edilmişdir. Şəkildə bir yol və həmin yolda isə yol zolağı var və bu yol zolağı pəncərə 
# içinə alınmışdır. Yol hərəkət etdikcə həmin pəncərələrdə hərəkət edərək yol zolağını işarətləyir. 


# Həmin Şəkil 1 -də alt şəkildə isə deep learning piksel texnikası ilə yol zolağı işarələnmişdir. 













# Sliding Window Approach nədir?

# Sliding Window Approach, bir görüntü və ya verilənlərdə lokal xüsusiyyətləri axtarmaq və ya analiz etmək üçün istifadə 
# edilən məşhur bir texnikadır. Bu metod, müəyyən ölçülü pəncərəni (window) verilənlərin və ya görüntünün üzərində sistematik 
# şəkildə "sürüşdürərək" işləyir.

# Bu texnika xüsusilə kompüter görməsi (Computer Vision) və təbii dil emalı (NLP) kimi sahələrdə obyekt aşkarlanması, seqmentasiya 
# və lokal analiz üçün geniş istifadə olunur.

# Prinsip:
#     Pəncərə ölçüsü təyin edilir:
#         Pəncərənin ölçüsü analiz etmək istədiyiniz obyektin və ya hissənin ölçüsünə uyğun seçilir.

#     Sürüşdürmə (Sliding):
#         Pəncərə şəkil və ya verilənlərin üzərində sol üst küncdən başlayaraq müəyyən bir addımla (stride) sağa doğru hərəkət edir.
#         Sonra bir sıra bitdikdə növbəti sıraya keçir və bu proses davam edir.

#     Analiz:
#         Pəncərə hər bir mövqedə dayandıqda, həmin hissədəki verilənləri (məsələn, piksel məlumatlarını) analiz edir.
#         Bu, obyektin aşkarlanması, xüsusiyyətlərin çıxarılması və ya model üçün girişlərin hazırlanması üçün istifadə edilə bilər.

# Sliding Window Approach-un üstünlükləri:
#     Sadə və intuitivdir:
#         Bu metod kompüter görməsində İcra edilməsi və tətbiqi nisbətən asandır.
#     Fərqli ölçülərdə obyektlər üçün uyğunlaşır:
#         Pəncərə ölçüsünü və stride dəyərini tənzimləyərək müxtəlif miqyaslı obyektləri aşkar edə bilərsiniz.
#     Məkanlıq məlumatı saxlayır:
#         Hər bir pəncərənin mövqeyi qeyd olunur, bu da lokal xüsusiyyətlərin öyrənilməsinə imkan yaradır.

# Çatışmazlıqlar:
#     Hesablama baxımından baha başa gəlir:
#         Böyük ölçülü şəkillərdə kiçik pəncərələr və kiçik stride-larla işləmək çox vaxt və resurs tələb edə bilər.
#     Optimal pəncərə ölçüsünü seçmək çətindir:
#         Çox böyük pəncərə ümumiləşdirmə apararkən, çox kiçik pəncərə lazım olmayan detallar çıxara bilər.
#     Dinamizm azdır:
#         Pəncərələr sabit ölçüdə və şəkildədir. Bu, qeyri-adi formalı obyektlərin aşkarlanmasında problemlər yarada bilər.

# Sliding Window Approach-un Tətbiqləri:
#     Kompüter Görməsi:
#         Obyekt Aşkarlanması: Məsələn, yol nişanlarının və ya yol zolaqlarının müəyyən edilməsi.
#         Xüsusiyyət Çıxarışı: Şəklin müəyyən bir hissəsində kənarların, teksturun və ya rənglərin analiz edilməsi.
#     Təbii Dil Emalı (NLP):
#         Mətnlərdə müəyyən naxışların (pattern) və ya söz birləşmələrinin tapılması.
#     Maşın Təlimi:
#         Konvolyusion Neyron Şəbəkələrində (CNN) xüsusilə ənənəvi obyekt aşkarlanması yanaşmalarında əvvəlki addım kimi istifadə olunur.

# Praktik Nümunə: Yol Zolaqlarının Tanınması
#     Pəncərə ölçüsü: Məsələn, 50x50 piksel.
#     Sürüşdürmə addımı: Məsələn, 20 piksel.
#     Prosess:
#       Sliding window hərəkət edərək şəkil üzərindəki yol zolaqlarını axtarır.
#       Hər mövqedə model həmin hissədə yol zolağının olub-olmadığını yoxlayır.


# Bu yanaşma daha sonra Deep Learning modelləri ilə birləşdirilərək obyekt aşkarlanmasını daha effektiv hala gətirə bilər.