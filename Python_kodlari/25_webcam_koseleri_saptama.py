import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    framegri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    koseler=cv2.goodFeaturesToTrack(framegri,99999999,0.01,1)
    koseler=koseler.astype(np.intp)

    for k in koseler:
        x,y=k.ravel()
        cv2.circle(frame,(x,y),1,(0,255,0),-1)
        
    cv2.imshow("Koseler",frame)
    if cv2.waitKey(10)&0xFF==27:
            break
cap.release()
cv2.destroyAllWindows()




