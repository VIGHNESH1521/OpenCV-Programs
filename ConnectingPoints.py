import cv2
import numpy as np


def click_event(event, x, y, flag, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 50, (255, 0, 0), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 255), 2)
        cv2.imshow("image", img)


img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow("image", img)
points = []
cv2.setMouseCallback("image",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
