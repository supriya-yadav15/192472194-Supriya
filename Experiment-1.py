import cv2

# Read the image
img = cv2.imread("flower.jpeg")

if img is None:
    print("Error: Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    cv2.imwrite("gray_image.jpg", gray)

    print("Image converted to grayscale successfully!")
    print("Output saved as gray_image.jpg")