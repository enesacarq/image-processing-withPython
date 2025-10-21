import cv2
import numpy as np
img=cv2.imread("resim_ve_videolar//ceviz.jpg")
img=cv2.resize(img,(640,480))

rotated1=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
rotated2=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
rotated3=cv2.rotate(img,cv2.ROTATE_180)

(h,w)=img.shape[:2]
center=(w//2,h//2)
M=cv2.getRotationMatrix2D(center,27,0.4)
rotated4=cv2.warpAffine(img,M,(w,h))

cv2.imshow("1",rotated1)
cv2.imshow("2",rotated2)
cv2.imshow("3",rotated3)
cv2.imshow("4",rotated4)

cv2.waitKey(0)
cv2.destroyAllWindows()
