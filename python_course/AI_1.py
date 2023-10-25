import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as pl

cap = cv2.VideoCapture(0)
faces = cv2.CascadeClassifier('faces.xml')
while True:
    ret, img = cap.read()
    f = faces.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5, minSize=(20, 20))
    for (x, y, w, h) in f:
      cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)
    cv2.imshow("camera", img)
    if cv2.waitKey(10) == 27:
        break
cap.release()
cv2.destroyAllWindows()

