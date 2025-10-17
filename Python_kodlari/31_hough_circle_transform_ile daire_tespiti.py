import cv2
import numpy as np


img=cv2.imread("resim_ve_videolar//geometrik_sekiller.jpg")

gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur=cv2.medianBlur(gri,7)

circles=cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,dp=1,minDist=20,param1=50,param2=100,minRadius=0,maxRadius=0)

if circles is not None:
    circles=np.uint16(np.around(circles))
    for(x,y,r) in circles[0, :]:
        cv2.circle(img,(x,y),r,(0,255,0),2)
        cv2.circle(img,(x,y),2,(0,0,255),2)

cv2.imshow("daire tespit",img)
cv2.waitKey()
cv2.destroyAllWindows()













