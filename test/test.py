import cv2 as cv
import numpy as np
from utils import *

img = cv.imread('../data/IMG_3898.jpg')

# avg_light = avg_bright(img)
# print(avg_bright(img))

# img_hsl = cv.cvtColor(img, cv.COLOR_BGR2HLS)

# for i in range(img_hsl.shape[0]):
# 	for j in range(img_hsl.shape[1]):
# 		img_hsl[i][j][1] //= avg_light / 123

# img_relight = cv.cvtColor(img_hsl, cv.COLOR_HLS2BGR)
# print(avg_bright(img_relight))

# cv.imshow('img_relight', img_relight)
# cv.waitKey(0)
# cv.destroyAllWindows()
# img_gray = cv.cvtColor()
print(avg_bright(img))
img = np.uint8(np.clip((1.2 * img + 10), 0, 255))
print(avg_bright(img))
cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()
