#Image logo identification 
import cv2
import os
import sys
import matplotlib.pyplot as plt

def find_logo(image):
    img = cv2.imread(image)
    # Display the image
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray,(3,3),0)
    canny = cv2.Canny(gray, 50, 150)
    plt.imshow(canny)
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    image_name = "card1.png"
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    file_path = os.path.join(script_directory, image_name)
    find_logo(file_path)