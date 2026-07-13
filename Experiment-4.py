import cv2
import numpy as np

# Read the image
img = cv2.imread("flower.jpeg")

# Check if the image exists
if img is None:
    print("Error: Image not found!")
else:
    # Create a 5x5 kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply dilation
    dilated = cv2.dilate(img, kernel, iterations=1)

    # Save the dilated image
    cv2.imwrite("dilated_image.jpg", dilated)

    print("Image dilated successfully!")
    print("Output saved as: dilated_image.jpg")