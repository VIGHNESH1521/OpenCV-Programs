import cv2

img = cv2.imread('messi5.jpg')
layer = img.copy()
gp = [layer]

for i in range(4):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i),layer)

cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
