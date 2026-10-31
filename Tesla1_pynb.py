# Tesla nasıl uçar?
# Roket sistemleri arabaları uçurabilir mi?

# 1. KÜTÜPHANELER:
# math matematiksel işlemler, numpy sayısal hesaplamalar,
# matplotlib ise grafik çizmek için kullanılır.

import math
import numpy as np
import matplotlib.pyplot as plt

print("Tüm kütüphaneler başarıyla çalışıyor!")

# 2. DEĞİŞKENLER:
# DRY_MASS aracın boş kütlesini, INITIAL_FUEL yakıt miktarını,
# GRAVITY yerçekimi ivmesini temsil eder.

# 3. KUVVET VE BİRİMLER:
# Ağırlık, kütle ile yerçekimi ivmesinin çarpılmasıyla hesaplanır.
# Ağırlık ve itki kuvveti Newton (N) ile ifade edilir.

# 4. HAVA DİRENCİ:
# CD_DRAG hava sürükleme katsayısını, AIR_DENSITY hava yoğunluğunu,
# FRONTAL_AREA ise aracın önden görünen alanını belirtir.

# 5. MOTOR İTKİSİ:
# T_MAX_TOTAL toplam motor itki kuvvetini temsil eder.
# ISP_MAIN motorun özgül itki değeridir ve saniye cinsindendir.

# 6. TWR (İTKİ-AĞIRLIK ORANI):
# Motor itkisinin aracın ağırlığına bölünmesiyle bulunur.
# TWR 1'den büyükse itki ağırlıktan büyüktür.
# Gerçek uçuş için hava direnci, yakıt, denge ve diğer etkenler
# de değerlendirilmelidir.

DRY_MASS = 1800.0       # kg: Aracın yakıt hariç boş kütlesi
INITIAL_FUEL = 45.0     # kg: Başlangıçtaki yakıt miktarı
GRAVITY = 9.81          # m/s²: Dünya yüzeyindeki yerçekimi ivmesi
T_MAX_TOTAL = 38847.6   # N: Toplam motor itki kuvveti
ISP_MAIN = 260.0        # s: Ana motorun özgül itki değeri
G0 = 9.80665            # m/s²: Standart yerçekimi ivmesi
CD_DRAG = 0.38          # Boyutsuz: Hava sürükleme katsayısı
AIR_DENSITY = 1.225     # kg/m³: Deniz seviyesindeki havanın yoğunluğu
FRONTAL_AREA = 2.4      # m²: Aracın önden görünen yüzey alanı
DT = 1.0 / 120.0        #120Hz Zaman Adımı (0.0033 Saniye)

# 7. F-STRING VE SAYI BİÇİMLENDİRME:
# f"..." değişkenleri yazı içine yerleştirmeyi sağlar.
# :.1f sayıyı virgülden sonra 1 basamakla,
# :.2f ise 2 basamakla gösterir.

print(f"araç Ağırlığı: {DRY_MASS * GRAVITY:.1f} N")
print(f"Maksimum Motor İtkisi: {T_MAX_TOTAL:.1f} N")
print(f"İtki-Ağırlık Oranı (TWR). {T_MAX_TOTAL / (DRY_MASS * GRAVITY):.2f} (1'den büyük olduğu için uçar.")

# SONUÇ:
# Bu çalışmada Python değişkenlerini, yorum satırlarını,
# fiziksel büyüklükleri, kuvvet hesaplamalarını ve sonuçları
# ekrana yazdırmayı öğrendik.
