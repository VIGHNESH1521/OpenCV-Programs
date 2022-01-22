import cv2
import numpy as np


def click_event(event, x, y, flag, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x ,',', y)
        font = cv2.FONT_HERSHEY_PLAIN
        strxy = str(x) + ',' + str(y)
        cv2.putText(img, strxy, (x, y), font, 2, (255, 255, 0), 2, cv2.LINE_4)
        cv2.imshow("IMAGE", img)


img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow("IMAGE", img)
cv2.setMouseCallback("IMAGE", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()

