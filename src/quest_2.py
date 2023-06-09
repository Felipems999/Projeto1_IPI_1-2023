#######################################
##       Felipe Moura da Silva       ##
##       16/0119740                  ##
##       1/2023                      ##
#######################################

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
    img = img / 255.0  # Normaliza a imagem para o intervalo entre 0 e 1

    # Aplica power-law para cada valor de gamma
    img_g1 = np.power(img, g1)
    img_g2 = np.power(img, g2)
    img_g3 = np.power(img, g3)

    # Salva as imagens resultantes
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


# Aplica a função compare_powerlaw() em car.png, crowd.png e university.png com nomes personalizados
compare_powerlaw(img_car, name="car")
compare_powerlaw(img_car, name="car")
compare_powerlaw(img_crowd, name="crowd")
compare_powerlaw(img_uni, name="university")

########################
##       ITEM 2       ##
########################

# Aplica a equalização de histograma em car.png, crowd.png e university.png, convertidas para escala de cinza
car_equ = cv.equalizeHist(cv.cvtColor(img_car, cv.COLOR_BGR2GRAY))
crowd_equ = cv.equalizeHist(cv.cvtColor(img_crowd, cv.COLOR_BGR2GRAY))
uni_equ = cv.equalizeHist(cv.cvtColor(img_uni, cv.COLOR_BGR2GRAY))

# Salva as imagens resultantes na pasta de resultados
cv.imwrite(RESULT_DIR + "q2_1_car_equalize.png", car_equ)
cv.imwrite(RESULT_DIR + "q2_1_crowd_equalize.png", crowd_equ)
cv.imwrite(RESULT_DIR + "q2_1_university_equalize.png", uni_equ)
