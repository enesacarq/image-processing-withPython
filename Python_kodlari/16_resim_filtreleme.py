import cv2
import numpy as np

img=cv2.imread("resim_ve_videolar//montain.jpg")
img=cv2.resize(img,(400,500))

kernel1=np.array([[0,-1,0],  #keskinleştirme
                  [-1,5,-1],
                  [0,-1,0]])

kernel2=np.array([[0,1,0],   #kenar belirleme
                 [1,-4,1],
                 [0,1,0]])

kernel3=np.ones((3,3),np.float32)/9   #bulanıklaştırma

filtered1=cv2.filter2D(img,-1,kernel1)
filtered2=cv2.filter2D(img,-1,kernel2)
filtered3=cv2.filter2D(img,-1,kernel3)

cv2.imshow("orijinal",img)
cv2.imshow("Keskinlestirme",filtered1)
cv2.imshow("Kenar belirleme",filtered2)
cv2.imshow("Bulaniklastirma",filtered3)

cv2.waitKey(0)
cv2.destroyAllWindows()



