import sys
import cv2 as cv
import numpy as np

output_path = sys.argv[1]

width = 640
height = 480
fourcc = cv.VideoWriter_fourcc('M', 'J', 'P', 'G')
out = cv.VideoWriter(output_path, fourcc, 20, (width, height))

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
		out.write(frame)

		cv.imshow('frame',frame)
		if cv.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

print('Video writing complete!')

cap.release()
out.release()
cv.destroyAllWindows()

# import numpy as np
# import cv2

# cap = cv2.VideoCapture(0)

# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# out = cv2.VideoWriter('output.mp4',0x00000021, 20.0, (640,480))

# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret==True:
#         frame = cv2.flip(frame,0)

#         # write the flipped frame
#         out.write(frame)

#         cv2.imshow('frame',frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break

# # Release everything if job is finished
# cap.release()
# out.release()
# cv2.destroyAllWindows()
