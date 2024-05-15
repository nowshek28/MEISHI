import cv2
import matplotlib.pyplot as plt
import os
import easyocr
from DATA_Seprator import DATA_Seperator

def find_card(image):
    img = cv2.imread(image)
    # Display the image
    Card_data = []
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    canny = cv2.Canny(gray, 50, 150)
    cany = cv2.resize(canny, (1920, 1080))
    #cv2.imshow('Canny', cany)
    contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter rectangles
    rectangles = []
    for contour in contours:
        # Approximate the contour to a polygon
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        # Check if the contour has 4 vertices (rectangle)
        if len(approx) == 4:
            # Get the bounding box of the contour
            rectangles.append(approx)
    
    for rect in rectangles:
        cv2.drawContours(img, [rect], -1, (255, 0, 0), 2)

    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)  #for the threshold
    # Initialize the EasyOCR reader
    reader = easyocr.Reader(['en','ja'])

    # Extract text from the image
    result = reader.readtext(thresh)
    for data in result:
        #print(data[0])
        bbox = data[0]
        # Draw a rectangle on the image
        cv2.rectangle(img, (int(bbox[0][0]), int(bbox[0][1])), (int(bbox[2][0]), int(bbox[2][1])), (255,0, 0), 1)
        #print(data[1:])
        if data[2]>=0.6:
            Card_data.append(data[1])
        
    #print(Card_data)
    DATA_Seperator(Card_data)
    # Display the image
    plt.imshow(img)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    image_name = "card.jpg"
    script_directory = 'C:\\Users\\abhishek\\Desktop'
    file_path = os.path.join(script_directory, image_name)
    find_card(file_path)