import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def rotate_image(image, degree, pivot=(0, 0)):


    radian = np.radians(degree)

    height, width, channels = image.shape

    max_dim = int(np.sqrt(height**2 + width**2))

    output_image = np.zeros((max_dim, max_dim, channels), dtype=image.dtype)

    for y in range(height):
        for x in range(width):
            x_orig = x  
            y_orig = y

            new_x = int(x_orig * np.cos(radian) - y_orig * np.sin(radian))
            new_y = int(x_orig * np.sin(radian) + y_orig * np.cos(radian))

            if 0 <= new_x < max_dim and 0 <= new_y < max_dim:
                output_image[new_y, new_x] = image[y, x]

    return output_image


image = img.imread("contoh.jpeg")

rotated_image = rotate_image(image, 45)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(rotated_image)
plt.title("Rotated Image (45 degrees)")

plt.show()