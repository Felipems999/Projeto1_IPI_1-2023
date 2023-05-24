import cv2 as cv
import numpy as np
from config import CAR, CROWD, UNIVERSITY, RESULT_DIR

img_car = cv.imread(CAR)
img_crowd = cv.imread(CROWD)
img_uni = cv.imread(UNIVERSITY)

########################
##       ITEM 1       ##
########################


def compare_powerlaw(
    img, g1: float = 0.5, g2: float = 0.3, g3: float = 1.5, name: str = "none"
):
    img = img / 255.0
    img_g1 = np.power(img, g1)
    img_g2 = np.power(img, g2)
    img_g3 = np.power(img, g3)

    cv.imwrite(
        RESULT_DIR + f"q2_1_powerlaw_gamma_0,5_{name}.png",
        (img_g1 * 255).astype(np.uint8),
    )
    cv.imwrite(
        RESULT_DIR + f"q2_1_powerlaw_gamma_0,3_{name}.png",
        (img_g2 * 255).astype(np.uint8),
    )
    cv.imwrite(
        RESULT_DIR + f"q2_1_powerlaw_gamma_1,5_{name}.png",
        (img_g3 * 255).astype(np.uint8),
    )


compare_powerlaw(img_car, name="car")
compare_powerlaw(img_crowd, name="crowd")
compare_powerlaw(img_uni, name="university")
