import cv2 as cv
import numpy as np

img = cv.imread('../data/IMG_3898.jpg')
print(img.shape)
# exit()
img_resize = cv.resize(img, (img.shape[1] // 5, img.shape[0] // 5))
img_blur = cv.bilateralFilter(img_resize, 5, 50, 35)


img_gray = cv.cvtColor(img_blur, cv.COLOR_BGR2GRAY)

cv.imshow('blur', img_blur)
cv.waitKey(0)
cv.destroyAllWindows()

ret, img_egg = cv.threshold(img_gray, 230, 255, cv.THRESH_BINARY)

strel = cv.getStructuringElement(cv.MORPH_RECT, (20, 20))
img_close = cv.morphologyEx(img_egg, cv.MORPH_CLOSE, strel)

# img_egg = cv.bitwise_and(img_resize, img_resize, mask=mask)

cv.imshow('egg', img_egg)
cv.waitKey(0)
cv.destroyAllWindows()