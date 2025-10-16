import cv2
import numpy as np

cap=cv2.VideoCapture("resim_ve_videolar//aksaray_yol.mp4")

while True:
    ret,frame=cap.read()
    if ret is False:
        print("Video okunamadi.")
        break
    frame=cv2.resize(frame,(600,500))
    
    alt=np.array([0,0,0],np.uint8)
    ust=np.array([180,255,80],np.uint8)

    mask=cv2.inRange(frame,alt,ust)
    kernel=np.ones((4,4),np.uint8)
    morf=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    cizgi=cv2.Canny(morf,700,800)
    cizgiler=cv2.HoughLinesP(cizgi,1,np.pi/180,threshold=100,maxLineGap=30)

    for i in cizgiler:
        x1,y1,x2,y2=i[0]
        if y1<100:
            y1=100
        if y2<100:
            y2=100
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)
            
   

    cv2.imshow("morf",frame)
    if cv2.waitKey(1)&0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()
