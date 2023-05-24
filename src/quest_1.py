#######################################
##       Felipe Moura da Silva       ##
##       16/0119740                  ##
##       1/2023                      ##
#######################################

from unittest import result
import numpy as np
import cv2 as cv
from config import FRUIT1, FRUIT2, RESULT_DIR

img = cv.imread(FRUIT1)
img2 = cv.imread(FRUIT2)

########################
##       ITEM 1       ##
########################


def tam2(img, num: int = 8):
    # Verifica se o número de níveis é par e maior ou igual a 2
    if num % 2 != 0 or num < 2:
        num = 2 if num < 2 else num + 1

    r, c, ch = img.shape  # Obtem dimensões da imagem img
    nr = r * 2  # Dobra o número de linhas
    nc = c * 2  # Dobra o número de colunas
    img_res = np.zeros(
        (nr, nc, ch), dtype=np.uint8
    )  # Cria uma matriz de 0's com o dobro das dimensões de img

    # Preenche a imagem resultante duplicando os pixels da imagem original
    for i in range(nr):
        for j in range(nc):
            img_res[i, j] = img[i // 2, j // 2]

    if num <= 2:
        return img_res  # Retorna a imagem resultante se num for igual ou menor que 2
    else:
        return tam2(img_res, num // 2)  # Chama recursivamente a função tam2


img_tam2_8 = tam2(img, 8)  # Aumenta as dimensões de img em 8 vezes
cv.imwrite(
    RESULT_DIR + "q1_1_tam2(img, 8).jpg", img=img_tam2_8
)  # Salva a imagem resultante na pasta de resultados


########################
##       ITEM 2       ##
########################


def tamm(img):
    r, c, ch = img.shape  # Obtem dimensões da imagem img
    nr = r * 2  # Dobra o número de linhas
    nc = c * 2  # Dobra o número de colunas
    img_res = np.zeros(
        (nr, nc, ch), dtype=np.uint8
    )  # Cria uma matriz de 0's com o dobro das dimensões de img

    # Preenche a imagem resultante de acordo com a técnica TAMM
    for i in range(r):
        for j in range(c):
            # Copia o pixel da imagem original para a posição correspondente na imagem resultante
            img_res[2 * i, 2 * j] = img[i, j]
            # Verifica se há uma coluna adjacente à direita
            if j + 1 < c:
                # Calcula a média entre o valor do pixel atual e o valor do pixel à direita
                img_res[2 * i, 2 * j + 1] = (img[i, j] + img[i, j + 1]) // 2
            # Verifica se há uma linha adjacente abaixo
            if i + 1 < r:
                # Calcula a média entre o valor do pixel atual e o valor do pixel abaixo
                img_res[2 * i + 1, 2 * j] = (img[i, j] + img[i + 1, j]) // 2
            # Verifica se há uma linha adjacente abaixo e uma coluna adjacente à direita
            if i + 1 < r and j + 1 < c:
                # Calcula a média entre os quatro pixels adjacentes
                img_res[2 * i + 1, 2 * j + 1] = (
                    img[i, j] + img[i, j + 1] + img[i + 1, j] + img[i + 1, j + 1]
                ) // 4

    return img_res


img_tamm = tamm(img)
cv.imwrite(
    RESULT_DIR + "q1_2_tamm(img).jpg", img=img_tamm
)  # Salva a imagem resultante na pasta de resultados


########################
##       ITEM 3       ##
########################


def superres(img1, img2):
    # Verificar se as imagens têm o mesmo tamanho
    if img1.shape != img2.shape:
        raise ValueError("As imagens devem ter o mesmo tamanho")

    # Obter as dimensões das imagens
    height, width, channels = img1.shape

    # Cria uma matriz vazia com o dobro do tamanho de img1
    img_res = np.zeros((2 * height, 2 * width, channels), dtype=np.uint8)

    # Preencher a imagem com as duas imagens de entrada
    img_res[1::2, 1::2] = img1  # Posições ímpares
    img_res[::2, ::2] = img2  # Posições pares

    # Laços de repetição aninhados que preenchem os pixeis vazios
    for i in range(2 * height):
        for j in range(2 * width):
            if img_res[i, j].all() == 0 or j == 0 or i == 0:
                img_res[i, j] = (img1[i // 2, j // 2] + img2[i // 2, j // 2]) // 2

    return img_res


img_superres = superres(img, img2)
cv.imwrite(
    RESULT_DIR + "q1_3_superres(img, img2).jpg", img=img_superres
)  # Salva a imagem resultante na pasta de resultados
