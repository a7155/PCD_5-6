import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def zoom_out(image, factor):

    height, width = image.shape[:2]
    new_height = int(height * factor)
    new_width = int(width * factor)

    zoomed_image = np.zeros((new_height, new_width, 3), dtype=image.dtype)

    for y in range(new_height):
        for x in range(new_width):
            original_y = int(y / factor)
            original_x = int(x / factor)

            original_y = min(original_y, height - 1)  # Clamp y to avoid out-of-bounds
            original_x = min(original_x, width - 1)   # Clamp x to avoid out-of-bounds

            zoomed_image[y, x] = image[original_y, original_x]

    return zoomed_image

image = img.imread("contoh.jpeg")

skala = 2.0
zoomed_image = zoom_out(image, skala)

img.imwrite("zoom_out.jpeg", zoomed_image)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(zoomed_image)
plt.title("Zoomed Out Image (Factor: 0.5)")

plt.show()