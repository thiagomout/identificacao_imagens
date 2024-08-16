import cv2
import numpy as np

def preprocessing(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224,224))
    image = image / 255.0
    return image

def indentifybases():

    return 0

vid = cv2.VideoCapture(0)
while(True):
    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()