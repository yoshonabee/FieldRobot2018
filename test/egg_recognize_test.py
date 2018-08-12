import cv2 as cv
import numpy as np

img = cv.imread('../data/IMG_3913.jpg')
print(img.shape)
# exit()
img_resize = cv.resize(img, (img.shape[1] // 5, img.shape[0] // 5))
img_blur = cv.blur(img_resize, (5, 5))
# cv.imshow('blur', img_blur)
# cv.waitKey(0)
# cv.destroyAllWindows()

img_gray = cv.cvtColor(img_blur, cv.COLOR_BGR2GRAY)
ret, img_egg = cv.threshold(img_gray, 230, 255, cv.THRESH_BINARY)
# img_egg = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv.THRESH_BINARY,3,2)

strel = cv.getStructuringElement(cv.MORPH_RECT, (20, 20))
img_close = cv.morphologyEx(img_egg, cv.MORPH_CLOSE, strel)

cv.imshow('egg', img_close)
cv.waitKey(0)
cv.destroyAllWindows()