import sys
import cv2 as cv
import numpy as np

output_path = sys.argv[1]

width = 1280
height = 720
fourcc = cv.VideoWriter_fourcc('M', 'J', 'P', 'G')
#out = cv.VideoWriter(output_path, fourcc, 20, (width, height))

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)

if cap.isOpened() is False:
	print('Cannot open camera, exiting...')
	exit()

print('Start writing')
while(cap.isOpened()):
	ret, frame = cap.read()

	if ret:
		# frame = cv.flip(frame,0)
		#out.write(frame)

		#cv.imshow('frame',frame)
		if cv.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

print('Video writing complete!')

cap.release()
#out.release()
cv.destroyAllWindows()
