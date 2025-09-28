import cv2
import numpy
import matplotlib

img=cv2.imread("resim_ve_videolar//oturan_yasli_adam.jpg",0)
cv2.namedWindow("fotograf",cv2.WINDOW_NORMAL)
cv2.imshow("fotograf",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(r"C:\\Users\\enesc\\OneDrive\\Resimler\\griyasli.png", img)

