import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)

print("Image Size: %d x %d" % (width, height))

if cap.isOpened():
	for i in range(100):
		ret, frame = cap.read()

	if ret:
		cv.imwrite('yenshuo.jpg', frame)
	else:
		print('Read Fail...')

	cap.release()
	cv.destroyAllWindows()
else:
	print('Camera not open')

print('Exit')
