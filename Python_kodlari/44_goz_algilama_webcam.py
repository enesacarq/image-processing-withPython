import cv2

cap=cv2.VideoCapture(0)

eyes_cascade=cv2.CascadeClassifier('haar_cascade_dosyalari//eye.xml')
faces_cascade=cv2.CascadeClassifier('haar_cascade_dosyalari//frontal_face.xml')

while 1:
    ret,frame=cap.read()
    if ret is False:
        print("Kameradan veri alinamadi.")
        break

    frame=cv2.resize(frame,(720,720))
    frame=cv2.flip(frame,1)
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    yuzler=faces_cascade.detectMultiScale(gri,1.1,3)
    for (x,y,w,h) in yuzler:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gri=gri[y:y+h,x:x+w]
        roi_renkli=frame[y:y+h,x:x+w]

        gozler=eyes_cascade.detectMultiScale(roi_gri,1.3,5)
        for (ex,ey,ew,eh) in gozler:
            cv2.rectangle(roi_renkli,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
    cv2.imshow('Goz Algilama', frame)
    if cv2.waitKey(1) & 0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()

