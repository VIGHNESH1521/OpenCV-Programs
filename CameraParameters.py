import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1208)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while (cap.isOpened()):

    # Capture the video frame
    # by frame
    ret, frame = cap.read()
    if ret:
        text = "Width : " + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + ", Height : " + str(
            cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        PresentDate = str(datetime.datetime.now())
        DateText = text + " " + PresentDate
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,
                    DateText,
                    (50, 50),
                    font, 1,
                    (255, 0, 0),
                    2,
                    cv2.LINE_4)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
