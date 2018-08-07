import cv2
import numpy as np

cap = cv2.VideoCapture(0)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("Image Size: %d x %d" % (width, height))

if cap.isOpened():
	ret, frame = cap.read()

	if ret:
		cv2.imwrite('example.png', frame)
	else:
		print('Read Fail...')

	cap.release()
	cv2.destroyAllWindows()
else:
	print('Camera not open')

print('Exit')