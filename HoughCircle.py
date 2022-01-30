import cv2 as cv
import numpy as np

img = cv.imread("shapes.png")
output = img.copy()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, ksize=5)
circles = cv.HoughCircles(
    gray,
    cv.HOUGH_GRADIENT,
    dp=1,
    minDist=20,
    param1=50,
    param2=30,
    minRadius=0,
    maxRadius=0
)
detected_circles = np.uint16(np.around(circles))
for (x, y, r) in detected_circles[0, :]:
    cv.circle(output, (x, y), r, (0, 255, 0), 3)
    cv.circle(output, (x, y), 2, (255, 255, 0), 3)

cv.imshow("image", output)
cv.waitKey(0)
cv.destroyAllWindows()