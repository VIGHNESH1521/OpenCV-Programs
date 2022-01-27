import cv2

original = cv2.imread('messi5.jpg', 0)
pyrdown1 = cv2.pyrDown(original)
pyrdown2 = cv2.pyrDown(pyrdown1)

pyrup1 = cv2.pyrUp(pyrdown2)
#pyrup2 = cv2.pyrUp(pyrup1)


cv2.imshow("image", original)
cv2.imshow("Pyramid Down 1", pyrdown1)
cv2.imshow("Pyramid Down 2", pyrdown2)
cv2.imshow("Pyramid Up 1", pyrup1)
#cv2.imshow("Pyramid Up 2", pyrup2)

cv2.waitKey(0)
cv2.destroyAllWindows()