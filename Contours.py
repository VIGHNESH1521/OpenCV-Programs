import cv2

img = cv2.imread("opencv-logo-white.png")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contour, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("NUMBER OF CONTOURS : " + str(len(contour)))
print(contour[0])

cv2.drawContours(img, contour, 0, (0,255,0), -1)

cv2.imshow("IMAGE", img)
cv2.imshow("GRAY IMAGE", imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()