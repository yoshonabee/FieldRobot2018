import sys
import cv2 as cv
import numpy as np

video_path = sys.argv[1]
output_path = sys.argv[2]

video = cv.VideoCapture(video_path)

image_name, image_num = 0, 0

if video.isOpened() is False:
	print('Invalid Path, exiting...')
	exit()
	
print('Start converting')

while video.isOpened():
	ret, frame = video.read()

	if ret:
		if image_num % 10 == 0:
			cv.imwrite(output_path + str(image_name) + '.jpg', frame)
			image_name += 1
	else:
		break

	image_num += 1

print('Convert complete!')

video.release()