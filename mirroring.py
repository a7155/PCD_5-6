import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt


# Load the image
image = img.imread("contoh.jpeg")

height, width = image.shape[:2]
horizontal = np.zeros_like(image)
vertikal = np.zeros_like(image)
img_mirrored = np.flip(image, axis=(0, 1))

for y in range(height):
    for x in range(width):
        horizontal[y,x] = image[y, width -1 -x]
for y in range(height):
    for x in range(width):
        vertikal[y,x] = image[height -1 -y ,x]
plt.figure(figsize=(10,5))
plt.subplot(1, 4, 1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(1, 4, 2)
plt.imshow(horizontal)
plt.title("Horizontal Flip")

plt.subplot(1, 4, 3)
plt.imshow(vertikal)
plt.title("Vertical Flip")

plt.subplot(1, 4, 4)
plt.imshow(img_mirrored)
plt.title("Mirrored")
plt.show()