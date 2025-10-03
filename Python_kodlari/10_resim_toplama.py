import cv2
import numpy as np

img1=cv2.imread("resim_ve_videolar//toplama1.jpg")
img2=cv2.imread("resim_ve_videolar//toplama2.jpg")

img1=cv2.resize(img1,(480,480))
img2=cv2.resize(img2,(480,480))

add=cv2.add(img1,img2)
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)

cv2.imshow("total",add)
cv2.waitKey(0)
cv2.destroyAllWindows()
