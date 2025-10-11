import cv2
import numpy as np

canvas1=np.zeros((512,512),dtype=np.uint8)

canvas2=np.zeros((512,512),dtype=np.uint8)

circle=cv2.circle(canvas1,(350,300),100,(255,255,255),-1)

dikdörtgen=cv2.rectangle(canvas2,(100,100),(300,280),(255,255,255),-1)

ve=cv2.bitwise_and(circle,dikdörtgen)
veya=cv2.bitwise_or(circle,dikdörtgen)
yada=cv2.bitwise_xor(circle,dikdörtgen)
degili1=cv2.bitwise_not(circle)
degili2=cv2.bitwise_not(dikdörtgen)

cv2.imshow("daire",circle)
cv2.imshow("dikgdortgen",dikdörtgen)
cv2.imshow("ve",ve)
cv2.imshow("veya",veya)
cv2.imshow("yada",yada)
cv2.imshow("degil1",degili1)
cv2.imshow("degil2",degili2)

cv2.waitKey(0)
cv2.destroyAllWindows()






