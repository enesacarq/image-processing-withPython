import cv2
import numpy as np

img=cv2.imread("resim_ve_videolar//rgb_renkler.png")
img=cv2.resize(img,(800,700))

(b,g,r)=cv2.split(img)

cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)

roi=img[100:200,200:300]
img[200:300,100:200]=roi
cv2.imshow("Logo",img)
cv2.imshow("Roi",roi)

cv2.waitKey(0)
cv2.destroyAllWindows()