import cv2

img = cv2.imread("gradient.png")

_, threshold = cv2.threshold(img, 124, 255, cv2.THRESH_BINARY)
_, threshold_2 = cv2.threshold(img, 124, 255, cv2.THRESH_BINARY_INV)
_, threshold_3 = cv2.threshold(img, 124, 255, cv2.THRESH_MASK)
_, threshold_4 = cv2.threshold(img, 200, 255, cv2.THRESH_TRUNC)
_, threshold_5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, threshold_6 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow("IMAGE", img)
cv2.imshow("THRESHOLD BINARY", threshold)
cv2.imshow("THRESHOLD BINARY INVERSE", threshold_2)
cv2.imshow("THRESHOLD MASK", threshold_3)
cv2.imshow("THRESHOLD TRUNK", threshold_4)
cv2.imshow("THRESHOLD TO ZERO", threshold_5)
cv2.imshow("THRESHOLD TO ZERO INVERSE", threshold_6)

cv2.waitKey(0)
cv2.destroyAllWindows()
