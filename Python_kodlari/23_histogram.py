import cv2
from matplotlib import pyplot as plt

img = cv2.imread("resim_ve_videolar//esas67.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Görüntü yüklenemedi!")
else:
    plt.hist(img.ravel(), bins=256, range=[0, 256])
    plt.title("Histogram")
    plt.show()
