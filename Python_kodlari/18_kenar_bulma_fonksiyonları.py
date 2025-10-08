import cv2
import numpy as np

img=cv2.imread("resim_ve_videolar//mustakil_ev.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges=cv2.Canny(img,100,200)

sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
sobelx=cv2.convertScaleAbs(sobelx)
sobely=cv2.convertScaleAbs(sobely)
sobeltotal=cv2.addWeighted(sobelx,0.5,sobely,0.5,0)

laplacian=cv2.Laplacian(img,cv2.CV_64F)

cv2.imshow("Orjinal",img)
cv2.imshow("Canny",edges)
cv2.imshow("Sobel",sobeltotal)
cv2.imshow("Laplacian",laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
