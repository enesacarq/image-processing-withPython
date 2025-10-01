import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Trackbar Window")

cv2.createTrackbar("B","Trackbar Window",0,255,nothing)
cv2.createTrackbar("G","Trackbar Window",0,255,nothing)
cv2.createTrackbar("R","Trackbar Window",0,255,nothing)

cv2.createTrackbar("On/Off","Trackbar Window",0,1,nothing)

while True:
    img=np.zeros((512,512,3),np.uint8)

    b=cv2.getTrackbarPos("B","Trackbar Window")
    g=cv2.getTrackbarPos("G","Trackbar Window")
    r=cv2.getTrackbarPos("R","Trackbar Window")
    s=cv2.getTrackbarPos("On/Off","Trackbar Window")

    if s==1:
        img[:]=[b,g,r]

    cv2.imshow("Trackbar Window",img)

    if cv2.waitKey(1) & 0xFF==27:
        break


cv2.destroyAllWindows()    