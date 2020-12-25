import numpy as np
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    _, image = cap.read()
    image = cv2.resize(image, (1000, 1000))
    imagebg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    height, width = imagebg.shape
    threshold = 170

    for i in np.arange(height):
        for j in np.arange(width):
            a = imagebg[i, j]
            if a > threshold:
                b = 255
            else:
                b = 0
            imagebg.itemset((i, j), b)

    contours, hierachy = cv2.findContours(imagebg, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    contours.sort(key=cv2.contourArea)
    c = contours[-2]
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    roi = imagebg[y-50:y+300, x-50:x + 300]
    cv2.imwrite('image.jpg', roi)
    cv2.imshow("Image", image)
    cv2.waitKey(0)