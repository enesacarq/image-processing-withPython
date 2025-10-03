import cv2

img1=cv2.imread("resim_ve_videolar//toplama1.jpg")
img2=cv2.imread("resim_ve_videolar//toplama2.jpg")
img1=cv2.resize(img1,(700,600))
img2=cv2.resize(img2,(700,600))

add=cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow("Agirlikli toplam",add)

cv2.waitKey(0)
cv2.destroyAllWindows()

