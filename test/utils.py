import numpy as np
import cv2 as cv

def avg_bright(img):
	img = cv.cvtColor(img, cv.COLOR_BGR2HLS)
	avg_brightness = np.sum(img[:,:,1]) / img.shape[0] / img.shape[1]
	return avg_brightness

def maximumBlur(img):
	kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))

	img = cv.erode(img, kernel)
	return img