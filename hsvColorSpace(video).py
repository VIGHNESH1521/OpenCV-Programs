import cv2 as cv
import numpy as np


def nothing(x):
    print(x)


cap = cv.VideoCapture(0)

cv.namedWindow("TRACKING")

cv.createTrackbar("lower hue", "TRACKING", 0, 255, nothing)
cv.createTrackbar("lower saturation", "TRACKING", 0, 255, nothing)
cv.createTrackbar("lower value", "TRACKING", 0, 255, nothing)
cv.createTrackbar("upper hue", "TRACKING", 255, 255, nothing)
cv.createTrackbar("upper saturation", "TRACKING", 255, 255, nothing)
cv.createTrackbar("upper value", "TRACKING", 255, 255, nothing)

while True:
    # frame = cv.imread("smarties.png")
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_h = cv.getTrackbarPos("lower hue", "TRACKING")
    l_s = cv.getTrackbarPos("lower saturation", "TRACKING")
    l_v = cv.getTrackbarPos("lower value", "TRACKING")

    u_h = cv.getTrackbarPos("upper hue", "TRACKING")
    u_s = cv.getTrackbarPos("upper saturation", "TRACKING")
    u_v = cv.getTrackbarPos("upper value", "TRACKING")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv.inRange(hsv, l_b, u_b)

    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("res", res)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
