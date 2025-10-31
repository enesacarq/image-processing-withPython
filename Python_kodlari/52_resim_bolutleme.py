import cv2
import numpy as np
import matplotlib.pyplot as plt
from ucd_gorsellestirme_53 import visualize3D_RGB as vis3d_rgb
from ucd_gorsellestirme_53 import visualize3D_HSV as vis3d_hsv
from ucd_gorsellestirme_53 import hsv_displayer as hsv_disp


img=cv2.imread(r"resim_ve_videolar\fil.jpg")
if img is None:
    print("Resim okunamadi")
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #plt rgb okur
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# OpenCV HSV aralığında fil rengi
lower_gray = np.array([15, 0, 166])
upper_gray = np.array([156,255, 246])


mask=cv2.inRange(img_hsv,lower_gray,upper_gray)

result=cv2.bitwise_and(img_rgb,img_rgb,mask=mask)

plt.subplot(1,2,1)
plt.imshow(mask,cmap="gray")

plt.subplot(1,2,2)
plt.imshow(result)

plt.show()

