import cv2

cap=cv2.VideoCapture(r"resim_ve_videolar\yuruyen_insanlar.mp4")

body_cascade=cv2.CascadeClassifier(r"haar_cascade_dosyalari\full_body.xml")

while True:
    ret,frame=cap.read()
    if ret==False:
        break

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    bodies=body_cascade.detectMultiScale(gray,1.1,3)
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("vudud",frame)
    if cv2.waitKey(25) & 0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()