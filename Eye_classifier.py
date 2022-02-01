import cv2 as cv

from FaceClassifier import face_cascade

eye_cascade = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")

cap = cv.VideoCapture("head-pose-face-detection-male.mp4")

while cap.isOpened():
    _, img = cap.read()

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 5)

    # display the image
    cv.imshow("image", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
