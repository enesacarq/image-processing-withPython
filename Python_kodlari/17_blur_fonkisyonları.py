import cv2
import numpy as np

img=cv2.imread("resim_ve_videolar//futbolcu.jpg")
img=cv2.resize(img,(400,500))

blurred1=cv2.blur(img,(9,9))

blurred2=cv2.GaussianBlur(img,(5,5),0)

blurred3=cv2.medianBlur(img,33)

blurred4=cv2.bilateralFilter(img,9,75,75)

cv2.imshow("Orijinal",img)
cv2.imshow("Blur",img)
cv2.imshow("GaussianBlur",img)
cv2.imshow("MedianBlur",img)
cv2.imshow("bilateralFilter",img)

cv2.waitKey(0)
cv2.destroyAllWindows()











