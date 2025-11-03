import cv2
import imutils

cap=cv2.VideoCapture("resim_ve_videolar\kosu_yarisi.mp4")

hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:
    ret,frame=cap.read()
    if ret is False:
        break
    
    frame=imutils.resize(frame,400)

    (cordinate,_)=hog.detectMultiScale(frame,winStride=(4,4),padding=(20,20),scale=1.05)

    for (x,y,w,h) in cordinate:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,222,0),2)

    cv2.imshow("s",frame)
    if cv2.waitKey(1) & 0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()
