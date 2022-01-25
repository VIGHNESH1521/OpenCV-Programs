import cv2
import numpy as np

img1 = cv2.imread("1bit1.png")
img2 = cv2.imread("2bit2.png")

bitand = cv2.bitwise_and(img2, img1)
bitor = cv2.bitwise_or(img2, img1)
bitxor = cv2.bitwise_xor(img2, img1)
bitnot = cv2.bitwise_not(img2, img1)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("Bitwise AND", bitand)
cv2.imshow("Bitwise OR", bitor)
cv2.imshow("Bitwise XOR", bitxor)
cv2.imshow("Bitwise NOT", bitnot)


cv2.waitKey(0)
cv2.destroyAllWindows()