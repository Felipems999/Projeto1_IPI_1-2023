import numpy
import cv2
from config import IMG_DIR


def tam2():
    img = cv2.imread(IMG_DIR + "car.png")
    cv2.imshow(img, 1)
