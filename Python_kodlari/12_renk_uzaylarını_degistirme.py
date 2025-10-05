import cv2

img=cv2.imread("resim_ve_videolar//esas67.jpg")

img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("BGR",img)
cv2.imshow("RGB",img1)
cv2.imshow("HSV",img2)
cv2.imshow("GRAY",img3)

cv2.waitKey(0)
cv2.destroyAllWindows()


