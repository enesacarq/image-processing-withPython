import cv2
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
fileName=r"iki_isareti.avi"
codec = cv2.VideoWriter_fourcc(*'MJPG')  # veya MJPG
frameRate=30
resolution=(640,480)
videoFileOutput=cv2.VideoWriter(fileName,codec,frameRate,resolution)

while True:
    ret,frame=cap.read()
    if not ret:
        print("Kare alinamadi. cikiyor...")
        break
    frame=cv2.flip(frame,1)
    videoFileOutput.write(frame)
    cv2.imshow("Ekrancanli",frame)
    if cv2.waitKey(33) & 0xFF ==ord("q"):
        break

videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()
