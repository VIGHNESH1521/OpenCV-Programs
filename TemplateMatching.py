import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("messi5.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = cv2.imread("messi_face.jpg", 0)
w, h = face.shape[::-1]
print("Value of W : ", w)
print("Value of h : ", h)

result = cv2.matchTemplate(gray, face, cv2.TM_CCORR_NORMED)
print(result)
threshold = 0.99
loc = np.where(result >= threshold)
print(loc)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
