# Lane Segmentation mərhələsində 2 texnika vardır. Görəcəyimiz işdən asılı olaraq 1 yaxud bu 2 texniyin ikisinidə istifadə edə bilərik. 

# 1) İmage Processing: 
                    # Image Processing, şəkillərin və ya vizual məlumatların analiz edilməsi, dəyişdirilməsi və 
                    # təhlili üçün istifadə edilən ənənəvi bir texnikadır. Bu texnika əsasən görüntünün müəyyən 
                    # xüsusiyyətlərini vurğulamaq və ya istənməyən hissələri aradan qaldırmaq üçün tətbiq olunur.

                    # Xüsusiyyətləri:
                        # Əsas metodlar:
                            # Filtrləmə (Gaussian, Median, Sobel və s.)
                            # Kənarların aşkarlanması (Edge Detection, məsələn, Canny Edge Detection)
                            # Rəng transformasiyaları (RGB-dən grayscale-ə keçid)
                            # ROI (Region of Interest) seçimi.

                        # Tətbiqi sahələri:
                            # Şəkil keyfiyyətinin artırılması.
                            # Obyektlərin aşkarlanması (nümunə olaraq yol xəttlərinin, zolaqların təyin edilməsi).
                            # Avtomatik nömrə tanıma sistemləri.

                        # Proslar və Konslar:
                            # Proslar:
                                # Daha sadə və daha sürətlidir.
                                # Kiçik resurslarla işləyir.
                            # Konslar:
                                # Dinamik mühitlər üçün yetərsiz ola bilər.
                                # Şəklin mürəkkəbliyi artdıqca performansı azalır.

# 2) Deep Learning: 
                    # Deep Learning süni intellektin bir alt sahəsidir və sinir şəbəkələri vasitəsilə məlumatların 
                    # öyrənilməsi və təhlili ilə məşğuldur. Şəkilləri analiz etmək üçün neyron şəbəkələrdən istifadə 
                    # olunur, bu da maşınların insan kimi öyrənməsinə imkan verir.

                    # Xüsusiyyətləri:
                        # Əsas metodlar:
                            # Konvolyusion Neyron Şəbəkələri (Convolutional Neural Networks - CNN).
                            # Transfer Learning (əvvəldən öyrədilmiş modellərin yenidən istifadəsi).
                            # Fully Convolutional Networks (FCN), U-Net və ya SegNet kimi seqmentasiya modelləri.

                        # Tətbiqi sahələri:
                            # Obyekt tanıma (Object Detection).
                            # Yol zolaqlarının avtomatik seqmentasiyası.
                            # Sürücüsüz avtomobillərdə istifadə.

                        # Proslar və Konslar:
                            # Proslar:
                                # Daha mürəkkəb və dinamik mühitlərdə yüksək performans göstərir.
                                # Əl ilə xüsusiyyət çıxarışına ehtiyac yoxdur (model özü öyrənir).
                            # Konslar:
                                # Daha çox hesablama gücünə ehtiyac duyur.
                                # Böyük miqdarda etiketlənmiş məlumat lazımdır.




# Image Processing: Yol zolaqlarının aşkarlanmasında sadə və ənənəvi üsullara əsaslanır, məsələn, kənarların aşkarlanması və rəng analizi. 
# Daha sürətli, lakin mürəkkəb ssenarilərdə çətinlik çəkə bilər (kölgə, pis hava şəraiti və s.).

# Deep Learning: Yol zolaqlarını daha dəqiq tanıya bilir, hətta mürəkkəb ssenarilərdə (çoxlu zolaqlar, dəyişən işıq şərtləri). Ancaq modelin 
# öyrədilməsi və istifadəsi daha çox resurs tələb edir.

# Hansı texnikanı seçəcəyiniz, layihənizin ehtiyaclarından və mövcud resurslardan asılı olacaq. Ən yaxşı nəticələr üçün bəzən hər iki 
# texnikanı birləşdirərək istifadə etmək olar.