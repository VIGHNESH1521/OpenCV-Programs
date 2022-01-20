import cv2

print(cv2.__version__)
img = cv2.imread('lena.jpg',-1)
print(img)
cv2.imshow('image',img)
key = cv2.waitKey(0)

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()

