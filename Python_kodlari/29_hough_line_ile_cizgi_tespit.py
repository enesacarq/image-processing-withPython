import cv2
import numpy as np

img=cv2.imread("resim_ve_videolar//yol_resmi.jpg")
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kenar=cv2.Canny(gri,300,500)
lines = cv2.HoughLinesP(kenar, 1, np.pi/180, threshold=150, minLineLength=100, maxLineGap=300)


for i in lines:
    x1,y1,x2,y2=i[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),5)
    


cv2.imshow("s",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

