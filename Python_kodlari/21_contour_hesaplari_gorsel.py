import cv2
import numpy as np

img=cv2.imread("resim_ve_videolar//geometrik_sekiller.jpg")

gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,binary=cv2.threshold(gri,127,255,cv2.THRESH_BINARY)

contour,hierarcy=cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(contour))
cv2.drawContours(img,contour,-1,(255,0,0),3)
cv2.imshow("Normal",img)


cv2.waitKey(0)
cv2.destroyAllWindows()
