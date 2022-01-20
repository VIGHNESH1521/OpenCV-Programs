# import the opencv library
import cv2

# define a video capture object
video = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
print(video.isOpened())

while (video.isOpened()):

    # Capture the video frame
    # by frame
    ret, frame = video.read()
    print(ret)
    print(frame)
    print(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(video.get(cv2.CAP_PROP_FPS))

    out.write(frame
              )
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame', gray)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
video.release()
out.release()
# Destroy all the windows
cv2.destroyAllWindows()