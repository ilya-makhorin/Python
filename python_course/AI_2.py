import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as pl

img = cv2.imread('images/w.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_filter = cv2.bilateralFilter(gray, 11, 15, 15)
edges = cv2.Canny(img_filter, 30, 200)
cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cont = imutils.grab_contours(cont)
cont = sorted(cont, key=cv2.contourArea, reverse=True)
pos = None
for c in cont:
    approx = cv2.approxPolyDP(c, 10, True)
    if len(approx) == 4:
        pos = approx
        break
mask = np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask, [pos], 0, 255, -1)
bitwise_img = cv2.bitwise_and(img, img, mask=mask)
(x, y) = np.where(mask==255)
(x1, y1) = np.min(x), np.min(y)
(x2, y2) = np.max(x), np.max(y)
crop = gray[x1:x2, y1:y2]
text = easyocr.Reader(['en'])
text = text.readtext(crop)
res = text[0][-2]
label = cv2.putText(img, res, (x1, y2 + 60), cv2.FONT_ITALIC, 3, (0, 0, 255), 2)
label = cv2.rectangle(img, (x1, x2-50), (y1, y2+30),  (0, 0, 255), 2)
pl.imshow(cv2.cvtColor(label, cv2.COLOR_BGR2RGB))
pl.show()


img = cv2.imread('images/face1.png')
cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = cv2.CascadeClassifier('faces.xml')
results = faces.detectMultiScale(img, scaleFactor=2, minNeighbors=4)
for (x, y, w, h) in results:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)

cv2.imshow('photo', img)
cv2.waitKey(0)



photo = np.zeros((500, 500, 3), dtype='uint8')
photo[100:350, 200:280] = 155, 130, 50
cv2.rectangle(photo, (0, 0), (100, 100), (155, 130, 50), thickness = 10)
cv2.imshow('photo', photo)
cv2.waitKey(0)



img = cv2.imread('images/1.jpg')
cv2.imshow('Result', img)
cv2.waitKey(0)

cap = cv2.VideoCapture('videos/video1.mp4')
while True:
    success, img = cap.read()
    cv2.imshow('Result', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


