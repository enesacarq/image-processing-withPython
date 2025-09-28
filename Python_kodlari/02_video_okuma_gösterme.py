import cv2

cap=cv2.VideoCapture("resim_ve_videolar//corlu_yol.mp4")

while True:
    ret,frame=cap.read()

    if ret== 0:
        print("Basarisiz")
        break
    frame=cv2.resize(frame,(720,750))
    cv2.imshow("Çorlu Yolu",frame)
    if cv2.waitKey(10) & 0xFF== ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


