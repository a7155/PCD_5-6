import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def Translasi(image, shiftX, shiftY):
    rows, cols = image.shape[:2]  # Get image dimensions
    imgTranslasi = np.roll(image, shift=shiftY, axis=0)  # Vertical shift
    imgTranslasi = np.roll(imgTranslasi, shift=shiftX, axis=1)  # Horizontal shift


    if shiftY > 0:
        imgTranslasi[:shiftY, :] = 0
    elif shiftY < 0:
        imgTranslasi[rows + shiftY:, :] = 0
    if shiftX > 0:
        imgTranslasi[:shiftX, :] = 0
    elif shiftX < 0:
        imgTranslasi[:, cols + shiftX:] = 0

    return imgTranslasi

# Load the image
image = img.imread("contoh.jpeg")

# Perform translation
imgResult = Translasi(image, shiftX=50, shiftY=-300)

# Display the results
plt.figure(figsize=(10, 10))
plt.subplot(2, 1, 1)
plt.imshow(image)
plt.title("Original Image")
plt.subplot(2, 1, 2)
plt.imshow(imgResult)
plt.title("Translated Image")
plt.show()