import cv2
import numpy as np

# --- Ayarlar ---
kernel = np.ones((3,3), np.uint8)
cevap_anahtari = ["B", "D", "A", "C","B","C","A","A"]  # Formunuzdaki gerçek cevaplar
esik = 13  # işaretli mi kontrolü için eşik

# --- Görüntüyü oku ve işleme ---
img = cv2.imread("resim_ve_videolar//optik_form.jpg")
gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gri, 200, 255, cv2.THRESH_BINARY)
morf = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# --- Daireleri bul ---
circles = cv2.HoughCircles(binary,
                           cv2.HOUGH_GRADIENT,
                           dp=1.5,
                           minDist=10,
                           param1=50,
                           param2=20,
                           minRadius=7,
                           maxRadius=10)

bosluk = []
if circles is not None:
    circles = np.uint16(np.around(circles))
    circles = circles[0, :]  # shape (N, 3)

    # Önce y sonra x koordinatına göre sırala
    circles = sorted(circles, key=lambda c: (c[1], c[0]))

    # Sadece tam 4 şıklı soruları al, eksikleri at
    bosluk = [circles[i*4:i*4+4] for i in range(len(circles)//4)]

# --- İşaretli mi kontrol fonksiyonu ---
def isaretli_mi(img, x, y, r):
    maske = np.zeros(img.shape, dtype="uint8")
    cv2.circle(maske, (x,y), r//2, 255, -1)
    roi = cv2.bitwise_and(img, img, mask=maske)
    toplam = cv2.countNonZero(roi)
    return toplam > esik

# --- Görselleştirme ---
for soru in bosluk:
    for b in soru:
        x, y, r = b
        if isaretli_mi(binary, x, y, r):
            cv2.circle(img, (x,y), r, (0,255,0), 2)  # Yeşil: işaretli
        else:
            cv2.circle(img, (x,y), r, (0,0,255), 2)  # Kırmızı: işaretsiz

# --- Doğru sayısını hesapla ---
dogru = 0
for i, soru in enumerate(bosluk):
    if i >= len(cevap_anahtari):
        break  # Cevap anahtarı bitti, döngüyü durdur
    if len(soru) != 4:
        continue  # Eksik daire varsa atla

    secim = None
    for j, (x, y, r) in enumerate(soru):
        if isaretli_mi(binary, x, y, r):
            secim = chr(65+j)  # 65 = 'A'
    if secim == cevap_anahtari[i]:
        dogru += 1

print("Toplam Doğru:", dogru, "/", len(bosluk))

# --- Sonuç göster ---
cv2.imshow("Optik Form Sonucu", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
