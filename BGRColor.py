import cv2
import numpy as np


def click_event(event, x, y, flag, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        myColorImage = np.zeros((512, 512, 3), np.uint8)
        myColorImage[:] = [blue, green, red]
        cv2.imshow("ColorImage", myColorImage)


img = cv2.imread('lena.jpg')
cv2.imshow("image", img)
points = []
cv2.setMouseCallback("image",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
