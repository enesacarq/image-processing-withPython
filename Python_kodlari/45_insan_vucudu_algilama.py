import cv2
import numpy as np

img=cv2.imread(r"resim_ve_videolar\uc_kisi.jpg")
img=cv2.resize(img,(600,400))
body_cascade=cv2.CascadeClassifier(r"haar_cascade_dosyalari\full_body.xml")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

bodies=body_cascade.detectMultiScale(gray,1.1,1)

for (x,y,w,h) in bodies:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("vucut",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


##Bu metot çok iyi değil
