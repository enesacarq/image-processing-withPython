import cv2
import  numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    if ret is False:
        break
    frame=cv2.flip(frame,1)
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,binary=cv2.threshold(gri,125,255,cv2.THRESH_BINARY)

    contours,hierarcy=cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame,contours,-1,(0,255,0),3)
    cv2.imshow("Kenarlar",frame)
    if cv2.waitKey(20) & 0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()    













