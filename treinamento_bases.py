import cv2
import numpy as np

def preprocessing(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224,224))
    image = image / 255.0
    return image