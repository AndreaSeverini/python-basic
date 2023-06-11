# Import necessary libraries
import cv2, glob

# Retrieve all .png files in the current directory
glob_img = glob.glob('*.png')

# Initialize the Haar cascade face detector provided by OpenCV
detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Define maximum size for the largest dimension (width or height) of the image
max_size = 1000

# Iterate through each .png file
for actual_img in glob_img:

    # Read the image file
    img = cv2.imread(actual_img)

    # If an image's width or height is larger than max_size,
    # scale it down to max_size while maintaining its aspect ratio.
    if max(img.shape) > max_size:
        scale = max_size / max(img.shape)
        img = cv2.resize(img, None, fx=scale, fy=scale)

    # Convert the color image to grayscale, as the Haar cascade
    # face detector uses grayscale images.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization on the grayscale image to improve the contrast,
    # which can help the face detection process.
    gray = cv2.equalizeHist(gray)

    # Apply Gaussian blur on the grayscale image to reduce noise,
    # which can improve the face detection process.
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform face detection using the Haar cascade face detector.
    # Adjust the scaleFactor and minNeighbors parameters according to your needs.
    face = detect.detectMultiScale(gray, scaleFactor=1.20, minNeighbors=5)

    # Draw a rectangle around each detected face on the original (color) image.
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the image with detected faces.
    cv2.imshow('Detect Multiple Faces in Images', img)

    # Wait for 2000 ms before displaying the next image.
    cv2.waitKey(2000)

    # Close the image window.
    cv2.destroyAllWindows()
