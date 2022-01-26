import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('RohitSharma.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))
Gblur = cv2.GaussianBlur(img, (5, 5), 0)
Mblur = cv2.medianBlur(img, 5)
bilateralFilter = cv2.bilateralFilter(img, 10, 75, 75)

titles = ['IMAGE', '2D CONVOLUTIONS', 'BLUR', 'Gaussian Blur', 'Median Blur', 'Bilateral filter']
images = [img, dst, blur, Gblur, Mblur, bilateralFilter]

for i in range(6):
    plt.subplot(3, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
