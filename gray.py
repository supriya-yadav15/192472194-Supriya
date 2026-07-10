import cv2

# Enter the image filename
image_path = input("Enter image filename (e.g., flower.jpg): ")

# Read the image
img = cv2.imread(image_path)

if img is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    cv2.imwrite("grayscale_output.jpg", gray)

    print("Image converted successfully!")
    print("Saved as: grayscale_output.jpg")
