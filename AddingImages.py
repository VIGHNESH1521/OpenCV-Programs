import cv2

img = cv2.imread("messi5.jpg")
img1 = cv2.imread("opencv-logo.png")

img = cv2.resize(img, (512, 512))
img1 = cv2.resize(img1, (512, 512))

AddImage = cv2.add(img, img1)
Subimage = cv2.subtract(img,img1)

cv2.imshow("Addition of the IMAGE",AddImage)
cv2.imshow("Subtraction of the IMAGE", Subimage)
cv2.waitKey(0)
cv2.destroyAllWindows()