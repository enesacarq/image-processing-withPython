import cv2
import pytesseract

img=cv2.imread(r"resim_ve_videolar\text_gorseli.png")

text=pytesseract.image_to_string(img,lang="tur")
print(f"sonuc:{text}")





