import cv2
import numpy as np

canvas=np.zeros((512,512,3),dtype=np.uint8)+255

cv2.imshow("Cizim ekrani",canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()