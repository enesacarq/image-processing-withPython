import cv2
import numpy as np

cap=cv2.VideoCapture("resim_ve_videolar//trafik_china.mp4")
subtractor=cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=80)

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    mask=subtractor.apply(frame)

    cv2.imshow("Arka plansiz",mask)

    if cv2.waitKey(1)&0xFF==27:
        break


cap.release()
cv2.destroyAllWindows()