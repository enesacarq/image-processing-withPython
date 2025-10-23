import cv2
import numpy as np

img=cv2.imread("resim_ve_videolar//yuz_kahvalti_gunu.jpg")
img=cv2.resize(img,(920,790))
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

frontal_face=cv2.CascadeClassifier(r"haar_cascade_dosyalari/frontal_face.xml")

yuzler=frontal_face.detectMultiScale(gri,1.2,4)
for (x,y,w,h) in yuzler:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


cv2.imshow("Orjinal Resim", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
