import cv2 
import numpy as np

img=cv2.imread("resim_ve_videolar//yildiz.png")
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,binary=cv2.threshold(gri,127,255,cv2.THRESH_BINARY)

contours,hierarcy=cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

hull=cv2.convexHull(contours[1])
cv2.drawContours(img,[hull],0,(255,0,0),2)

cv2.imshow("Dis bukey cizim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()