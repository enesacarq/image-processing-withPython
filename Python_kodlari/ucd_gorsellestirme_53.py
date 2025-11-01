import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors
from matplotlib.colors import hsv_to_rgb

# --- 1) RGB 3D Görselleştirme ---
def visualize3D_RGB(img_rgb):
    r, g, b = cv2.split(img_rgb)
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1, projection="3d")

    pixel_colors = img_rgb.reshape((-1, 3))
    norm = colors.Normalize(vmin=-1., vmax=1.)
    norm.autoscale(pixel_colors)
    pixel_colors = norm(pixel_colors).tolist()

    axis.scatter(r.flatten(), g.flatten(), b.flatten(),
                 facecolors=pixel_colors, marker=".")
    axis.set_xlabel("Red")
    axis.set_ylabel("Green")
    axis.set_zlabel("Blue")
    plt.show()

# --- 2) HSV 3D Görselleştirme ---
def visualize3D_HSV(img_rgb):
    img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(img_hsv)

    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1, projection="3d")

    pixel_colors = img_hsv.reshape((-1, 3)).astype(np.float32) / 255.0
    pixel_colors_rgb = hsv_to_rgb(pixel_colors)

    axis.scatter(h.flatten(), s.flatten(), v.flatten(),
                 facecolors=pixel_colors_rgb, marker=".")
    axis.set_xlabel("Hue")
    axis.set_ylabel("Saturation")
    axis.set_zlabel("Value")
    plt.show()

# --- 3) HSV Renk Aralığı Maskeleme ---
def hsv_displayer(img_rgb, light_black, dark_black):
    # RGB -> HSV
    hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
    # Maske
    mask = cv2.inRange(hsv, light_black, dark_black)
    result = cv2.bitwise_and(img_rgb, img_rgb, mask=mask)

    # Görselleştirme
    plt.subplot(1, 3, 1)
    plt.imshow(img_rgb)
    plt.title("Orijinal")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(mask, cmap="gray")
    plt.title("Maske")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(result)
    plt.title("Sonuç")
    plt.axis("off")

    plt.show()
