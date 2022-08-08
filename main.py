import numpy as np
import cv2 as cv

img = cv.imread('test.jph', 0)
img = cv.medainBlur(img, 5)
cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

circles = c