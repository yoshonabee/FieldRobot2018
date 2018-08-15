import cv2 as cv
import numpy as np
from time import sleep
from utils import *

img = cv.imread('../data/IMG_3913.jpg')
print(img.shape)
# exit()
img_resize = cv.resize(img, (img.shape[1] // 5, img.shape[0] // 5))
# img_blur = cv.blur(img_resize, (5, 5))
# img_blur = cv.bilateralFilter(img_resize, 5, 200, 200)
img_blur = maximumBlur(img_resize)
cv.imshow('blur', img_blur)
cv.waitKey(0)

for i in range(3):
	img_blur = maximumBlur(img_blur)
	cv.imshow('blur', img_blur)
	cv.waitKey(0)

img_hsv = cv.cvtColor(img_blur, cv.COLOR_BGR2HSV)
# print(img_hsv)
# sleep(3)


# cv.destroyAllWindows()
# exit()
# ret, img_egg = cv.threshold(img_gray, 230, 255, cv.THRESH_BINARY)

# for g in range(50, 120):
lower_range_brown = np.array([0, 0, 100])
upper_range_brown = np.array([180, 40, 255])

img_egg_brown = cv.inRange(img_hsv, lower_range_brown, upper_range_brown)
# print(img_egg_brown)



cv.imshow('img_egg_brown', img_egg_brown)
cv.waitKey(0)

	# if (g - 99) % 10 == 0:
	# 	cv.destroyAllWindows()
cv.destroyAllWindows()

# lower_range_white = np.array([0, 0, 100])
# upper_range_white = np.array([360, 80, 255])

# img_egg_white = cv.inRange(img_hsv, lower_range_white, upper_range_white)

# cv.imshow('img_egg_white', img_egg_white)
# cv.waitKey(0)

# img_egg = cv.bitwise_or(img_egg_brown, img_egg_white)
# cv.imshow('img_egg', img_egg)
# cv.waitKey(0)
# cv.destroyAllWindows()

# strel = cv.getStructuringElement(cv.MORPH_RECT, (10, 10))
# img_egg_close = cv.morphologyEx(img_egg, cv.MORPH_CLOSE, strel)

# cv.imshow('img_egg_close', img_egg_close)
# cv.waitKey(0)
# cv.destroyAllWindows()