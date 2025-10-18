import cv2
import numpy as np

cap=cv2.VideoCapture("resim_ve_videolar//trafik_china.mp4")
ret,frame1=cap.read()
frame1=cv2.resize(frame1,(600,720))
gri1=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
blur1=cv2.GaussianBlur(gri1,(5,5),0)


while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(600,720))
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gri,(5,5),0)

    diff=cv2.absdiff(gri1,gri)
    ret,binary=cv2.threshold(diff,80,255,cv2.THRESH_BINARY)
    cv2.imshow("Arka plansiz",binary)
    if cv2.waitKey(1)&0xFF==27:
        break
    frame1=frame


cap.release()
cv2.destroyAllWindows()
    
