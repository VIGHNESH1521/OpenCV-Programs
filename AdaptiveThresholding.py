import cv2

img = cv2.imread("sudoku.png", 0)

_, threshold = cv2.threshold(img, 124, 255, cv2.THRESH_BINARY)
threshold1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 5)

cv2.imshow("IMAGE", img)
cv2.imshow("threshold", threshold)
cv2.imshow("Adpative threshold", threshold1)

cv2.waitKey(0)
cv2.destroyAllWindows()
