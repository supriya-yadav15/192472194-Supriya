import cv2

# Read the image
img = cv2.imread("flower.jpeg")

# Check if the image exists
if img is None:
    print("Error: Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect edges using the Canny function
    edges = cv2.Canny(blur, 100, 200)

    # Save the output image
    cv2.imwrite("canny_output.jpg", edges)

    print("Outline detected successfully!")
    print("Output saved as: canny_output.jpg")