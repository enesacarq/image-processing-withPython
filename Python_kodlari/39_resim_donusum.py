import cv2
import numpy as np

def nothing(x):
    pass

img1=cv2.imread("resim_ve_videolar//dunya_uzerinde_turkiye.jpg")
img1=cv2.resize(img1,(1080,800))
img2=cv2.imread("resim_ve_videolar//ayasofya_cami.jpg")
img2=cv2.resize(img2,(1080,800))

output=cv2.addWeighted(img1,1,img2,0,0)

namewindow="Donusum"
cv2.namedWindow(namewindow)

cv2.createTrackbar("Alpha-Beta",namewindow,0,3000,nothing)

while True:
    
    cv2.imshow(namewindow,output)
    beta=cv2.getTrackbarPos("Alpha-Beta",namewindow)/3000
    alpha=1-beta
    output=cv2.addWeighted(img1,alpha,img2,beta,0)
    print(alpha,beta)
    if cv2.waitKey(1)==27:
        break