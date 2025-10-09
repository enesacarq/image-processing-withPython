import cv2
import numpy as np

img=cv2.imread("resim_ve_videolar//mantar_dugme.jpg",0)

ret,threshol=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

cv2.imshow("Binary",threshol)

cv2.waitKey(0)
cv2.destroyAllWindows()
