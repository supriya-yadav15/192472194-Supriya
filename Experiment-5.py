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

    # Apply erosion
    eroded = cv2.erode(img, kernel, iterations=1)

    # Save the eroded image
    cv2.imwrite("eroded_image.jpg", eroded)

    print("Image eroded successfully!")
    print("Output saved as: eroded_image.jpg")