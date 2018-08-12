import cv2
import numpy as np
 
cascPath = './egg.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
 
# video_capture = cv2.VideoCapture(0)

frame = cv2.imread('../data/IMG_3903.jpg')

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

print('faces')
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    # flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)

print('draw')
# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the resulting frame
cv2.imwrite('egg02.png', frame)
 
# When everything is done, release the capture
cv2.destroyAllWindows()