import cv2 as cv

cap = cv.VideoCapture("vtest.avi")
# detectShadows by default is True, it will be in gray.
fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=False)

while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)

    cv.imshow("frame", frame)
    cv.imshow("FG FRAME MASK", fgmask)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

cap.release()
cv.destroyAllWindows()
