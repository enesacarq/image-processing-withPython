import cv2

img=cv2.imread("resim_ve_videolar//yuz_kahvalti_gunu.jpg")
img=cv2.resize(img,(800,600))
eyes_cascade=cv2.CascadeClassifier('haar_cascade_dosyalari//eye.xml')
faces_cascade=cv2.CascadeClassifier('haar_cascade_dosyalari//frontal_face.xml')

gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

yuzler=faces_cascade.detectMultiScale(gri,1.1,3)

for (x,y,w,h) in yuzler:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gri = gri[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]

    gozler = eyes_cascade.detectMultiScale(roi_gri, 1.3, 1)

    for (gx, gy, gw, gh) in gozler:
        cv2.rectangle(roi_color, (gx, gy), (gx + gw, gy + gh), (0, 255, 0), 2)


cv2.imshow('Goz Algilama', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
