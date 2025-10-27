import cv2
import numpy as np
import pytesseract
import imutils
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img=cv2.imread(r"resim_ve_videolar\plaka_bjk.jpg")
img=cv2.resize(img,(600,600))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.bilateralFilter(gray,17,100,150)
kenar=cv2.Canny(blur,50,200)


kontur=cv2.findContours(kenar,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
 
cnt=imutils.grab_contours(kontur)
cnt=sorted(cnt,key=cv2.contourArea,reverse=True)[:10]

ekran=0 
for i in cnt:
    eps=0.018*cv2.arcLength(i,True)
    aprx=cv2.approxPolyDP(i,eps,True)
    if len(aprx)==4:
        ekran=aprx
        break


maske=np.zeros(gray.shape,np.uint8)
yeni_maske=cv2.drawContours(maske,[ekran],0,255,-1)

yazi=cv2.bitwise_and(img,img,mask=yeni_maske)
(x,y)=np.where(maske==255)
(x1,y1)=(np.min(x),np.min(y))  
(x2,y2)=(np.max(x),np.max(y))
kirp=gray[x1:x2+1,y1:y2+1]

config = "--psm 7 --oem 3"  
text = pytesseract.image_to_string(kirp, config=config, lang="eng")

print("Plaka : ",text)

cv2.imshow("a",kirp)
cv2.waitKey(0)
cv2.destroyAllWindows()

