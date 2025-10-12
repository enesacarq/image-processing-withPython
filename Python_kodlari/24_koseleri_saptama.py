import cv2
import numpy as np 

img=cv2.imread("resim_ve_videolar//squid_game_sembol.jpg")
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

koseler=cv2.goodFeaturesToTrack(gri,100,0.01,10)

koseler=koseler.astype(np.intp)

for k in koseler:
    x,y=k.ravel()
    cv2.circle(img,(x,y),10,(0,255,0),-1)

img=cv2.resize(img,(720,700))
cv2.imshow("kose tespit",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

