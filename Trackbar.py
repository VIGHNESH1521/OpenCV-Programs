import cv2 as cv
import numpy as np


def nothing(x):
    print(x)


img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow("IMAGE")

cv.createTrackbar("B", "IMAGE", 0, 255, nothing)
cv.createTrackbar("G", "IMAGE", 0, 255, nothing)
cv.createTrackbar("R", "IMAGE", 0, 255, nothing)
switch = '0 : OFF\n 1 : ON'
cv.createTrackbar(switch, "IMAGE",0,1,nothing)

while True:
    cv.imshow("IMAGE", img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    b = cv.getTrackbarPos("B", "IMAGE")
    g = cv.getTrackbarPos("G", "IMAGE")
    r = cv.getTrackbarPos("R", "IMAGE")
    s = cv.getTrackbarPos(switch, "IMAGE")

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]


cv.destroyAllWindows()
