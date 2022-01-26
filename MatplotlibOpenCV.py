import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread("RohitSharma.png")
cv.imshow("IMAGE", img)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)


plt.imshow(img)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()