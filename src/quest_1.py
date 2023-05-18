import numpy as np
import cv2 as cv
from config import FRUIT1, FRUIT2


def tam2(img, num: int = 4):
    if num % 2 != 0 or num < 2:
        num += 1

    r, c, ch = img.shape
    nr = r * 2
    nc = c * 2
    img_res = np.zeros((nr, nc, ch), dtype=np.uint8)

    if num > 2:
        img_res = tam2(img_res, int(num / 2))
    else:
        return img_res


img = cv.imread(FRUIT1)
print("\nImagem Original\n")
print(np.array(img))

img_result = tam2(img, 32)
print("\nImagem resultante\n")
print(np.array(img_result))
