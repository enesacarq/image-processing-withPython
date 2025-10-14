import cv2
import numpy as np

img=cv2.imread("resim_ve_videolar//moment_icin_altigen.png")
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,binary=cv2.threshold(gri,127,255,cv2.THRESH_BINARY)

contor,_=cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

M=cv2.moments(contor[1])
x=int(M["m10"]/M["m00"])
y=int(M["m01"]/M["m00"])

cv2.circle(img,(x,y),4,(0,0,150),-1)
cv2.imshow("Merkez",img)
cv2.waitKey(0)
cv2.destroyAllWindows()









