import cv2
import numpy
cap = cv2.VideoCapture("raw/data/test.mp4")
if cap.isOpened():
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    while True:
        success, img = cap.read()
        if not success:
            break
        cv2.imshow("FootballTrack", img)
        key = cv2.waitKey(0)
        if key & 0xFF == ord("q"):
            break

    

    