import cv2
import matplotlib.pyplot as plt
import os
from MEISHI import read_text

def find_card(image):
    img = cv2.imread(image)
    # Display the image
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    canny = cv2.Canny(gray, 50, 150)
    cany = cv2.resize(canny, (1920, 1080))
    #cv2.imshow('Canny', cany)
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter rectangles
    rectangles = []
    for i,contour in enumerate(contours):
        # Approximate the contour to a polygon
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        # Check if the contour has 4 vertices (rectangle)
        if len(approx) == 4:
                # Get the bounding box of the contour
            x, y, w, h = cv2.boundingRect(contour)
            
            # Crop the rectangle from the original image
            cropped_rectangle = img[y:y+h, x:x+w]
            
            
            rectangles.append(approx)
    # Draw rectangles on the original image
    # Display the result (optional)
    cropped_rectangle = cv2.resize(cropped_rectangle, (1080, 920))
    cv2.imshow('Cropped Rectangle', cropped_rectangle)
    for rect in rectangles:
        cv2.drawContours(img, [rect], -1, (0, 255, 0), 2)

    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)  #for the threshold

    img2= read_text(thresh)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    image_name = "card.jpg"
    script_directory = ''
    file_path = os.path.join(script_directory, image_name)
    find_card(file_path)