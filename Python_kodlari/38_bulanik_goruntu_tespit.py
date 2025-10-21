import cv2
import numpy as np

img=cv2.imread("resim_ve_videolar//futbolcu.jpg")

img_blur=cv2.GaussianBlur(img,(5,5),0)

laplacian=cv2.Laplacian(img,cv2.CV_64F).var()

if laplacian <100:
    print("blurludur.")
else:
    print("degildir.")

