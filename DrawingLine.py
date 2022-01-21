import cv2

img = cv2.imread('lena.jpg',1)
print(img)
# creating for line
cv2.line(img, (100, 100), (200, 200), (255, 255, 255), 10)
cv2.imshow('image',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()


