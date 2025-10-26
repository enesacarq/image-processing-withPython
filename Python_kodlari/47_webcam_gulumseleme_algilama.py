import cv2
import numpy as np

cap = cv2.VideoCapture(0)

yuz_cascade = cv2.CascadeClassifier(r"haar_cascade_dosyalari\frontal_face.xml")
gulumseme_cascade = cv2.CascadeClassifier(r"haar_cascade_dosyalari\smile.xml")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    yuzler = yuz_cascade.detectMultiScale(gray, 1.15, 3)

    for (x, y, w, h) in yuzler:
        

        roi = frame[y:y+h, x:x+w]
        roig = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        gulumse = gulumseme_cascade.detectMultiScale(roig, 1.5, 4)
        for (ex, ey, ew, eh) in gulumse:
            cv2.rectangle(roi, (ex, ey), (ex+ew, ey+eh), (0, 255, 100), 2)

    cv2.imshow("frame", frame)

    if cv2.waitKey(30) & 0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()
