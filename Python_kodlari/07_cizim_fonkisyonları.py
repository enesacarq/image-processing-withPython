import cv2
import numpy as np

canvas=np.zeros((512,512,3),dtype=np.uint8)+255

#Düz çizgi
cv2.line(canvas,(10,10),(100,10),(0,0,100),10)

#Dikdörtgen
cv2.rectangle(canvas,(12,20),(150,300),(255,0,0),3)

#Daire
cv2.circle(canvas,(250,250),60,(0,220,0),-1)

#Çokgen
points = np.array([[120,100],[150,150],[200,200],[230,230],[300,300],[150,250]], dtype=np.int32)
points = points.reshape((-1, 1, 2))
cv2.polylines(canvas,[points],True,(0,0,255),3)

#Yazı yazma
cv2.putText(canvas,"yusuf hiyar midir",(0,400),cv2.FONT_HERSHEY_DUPLEX,2,(20,200,400),1)


cv2.imshow("Cizimler",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()