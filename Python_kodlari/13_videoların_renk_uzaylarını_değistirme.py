import cv2

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    if ret is False:
        print("video okunamadi")
        break
    else:
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        frame=cv2.flip(frame,1)
        cv2.imshow("Gri görüntü",frame)
        if cv2.waitKey(30) & 0xFF==27:
            break

cap.release()
cv2.destroyAllWindows()
