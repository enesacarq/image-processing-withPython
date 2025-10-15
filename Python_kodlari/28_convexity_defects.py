import cv2
import numpy as np

img = cv2.imread('resim_ve_videolar//yildiz.png')
if img is None:
    print("Görüntü yüklenemedi. Dosya yolu doğru mu?")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

if len(contours) == 0:
    print("Kontur bulunamadı.")
    exit()
cnt = contours[1]

hull = cv2.convexHull(cnt)
cv2.drawContours(img, [hull], -1, (0, 0, 255), 2)  # Kırmızı dış hat

hull_indices = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull_indices)


if defects is not None:
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]  # Başlangıç, bitiş, çukur nokta, derinlik

        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        depth = d / 256.0  # Derinlik piksel cinsinden (isteğe bağlı)

        cv2.line(img, start, end, (255, 0, 0), 2)
        cv2.circle(img, far, 5, (255, 0, 255), -1)

cv2.imshow("Convex Hull ve Convexity Defects", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
