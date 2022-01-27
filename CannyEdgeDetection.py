import matplotlib.pyplot as plt
import cv2

img = cv2.imread('messi5.jpg', 0)
canny = cv2.Canny(img, 75, 200)

titles = ['image','canny']
images = [img, canny]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
