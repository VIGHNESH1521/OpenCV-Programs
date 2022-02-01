import cv2 as cv

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

# read the input image
#img = cv.imread("ABDe.jpg")
cap = cv.VideoCapture("face-demographics-walking-and-pause.mp4")
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#faces = face_cascade.detectMultiScale(gray, 1.1, 4)

while cap.isOpened():
    _, img = cap.read()

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

    # display the image
    cv.imshow("image", img)
    #cv.destroyAllWindows()
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
