import os
import cv2
import easyocr
import matplotlib.pyplot as plt

def read_text(img):
    # Initialize the EasyOCR reader
    reader = easyocr.Reader(['en','ja'])

    # Extract text from the image
    result = reader.readtext(img)
    
    """for data in result:
        #print(data[0])
        bbox = data[0]
        # Draw a rectangle on the image
        cv2.rectangle(img, (int(bbox[0][0]), int(bbox[0][1])), (int(bbox[1][0]), int(bbox[1][1])), (0, 255, 0), 1)
       """ 

    # Display the image
    """plt.imshow(img)
    plt.axis('off')  # Turn off the axis labels
    plt.show()"""


    #print(result[0][0])
    return result

if __name__ == "__main__":
    image_name = "card.png"
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, image_name)
    img = cv2.imread(file_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    read_text(img)