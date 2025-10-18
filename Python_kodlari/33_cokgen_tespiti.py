import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread("resim_ve_videolar//geometrik_sekil_paint.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,threshold = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)

contours,_ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:

    epsilon = 0.01*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)

    cv2.drawContours(img,[approx],0,(0),5)

    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx)==3:
        cv2.putText(img,"Ucgen",(x,y),font,1,(0))
        
    elif len(approx)==4:
        cv2.putText(img,"Dortgen",(x,y),font,1,(0))
        
    elif len(approx)==5:
        cv2.putText(img,"Besgen",(x,y),font,1,(0))
        
    elif len(approx)==6:
        cv2.putText(img,"Altigen",(x,y),font,4,(0))
        
    else:
        cv2.putText(img,"Elips",(x,y),font,1,(0))

cv2.imshow("IMG",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
        



