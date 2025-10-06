import cv2
import  numpy as np
#Görüntüyü binary çevirme
img=cv2.imread("resim_ve_videolar//morfolojik_icin_hello_yazi.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

kernel=np.ones((3,3),np.uint8)
binary=cv2.resize(binary,(500,500))
#Erosion
erosion=cv2.erode(binary,kernel,iterations=1)
#Dilation
dilation=cv2.dilate(binary,kernel,iterations=1)
#Opening
opening=cv2.morphologyEx(binary,cv2.MORPH_OPEN,kernel)
#Closing
closing=cv2.morphologyEx(binary,cv2.MORPH_CLOSE,kernel)
#Gradient
gradient=cv2.morphologyEx(binary,cv2.MORPH_GRADIENT,kernel)
#tophat
tophat=cv2.morphologyEx(binary,cv2.MORPH_TOPHAT,kernel)
#blackhat
blackhat=cv2.morphologyEx(binary,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow("Orijinal",binary)
cv2.imshow("Erosion",erosion)
cv2.imshow("dilation",dilation)
cv2.imshow("opening",opening)
cv2.imshow("gradient",gradient)
cv2.imshow("tophat",tophat)
cv2.imshow("blackhat",blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
