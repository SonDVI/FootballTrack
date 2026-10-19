import cv2
import numpy
from pathlib import Path
#Open video
cap = cv2.VideoCapture("raw/data/test.mp4")

#Open = True
if cap.isOpened():
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    #Counter increase when save each frame
    frame_count = 0
    cv2.namedWindow("FootballTrack", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("FootballTrack", 640, 360)
    #Choose frame interval
    frame_interval = 60
    while True:
        #Take img each frame, success for check if is it success or not
        success, img = cap.read()

        if not success:
            break

        #Display img(frame)
        cv2.imshow("FootballTrack", img)

        #WaitKey updated to 15 means 1 frame will stop 15 ms then move to next one
        key = cv2.waitKey(15)

        #Logic saves Img but not duplicated
        frame_count += 1
        if frame_count % frame_interval == 0:
            file_path = Path(f"outputs/frames/every_{frame_interval}/{frame_count}_frame.jpg")

            if not file_path.exists():
                
                #cv2.imwrite() return True/False so saved is checked variable and also saved img in folder
                saved = cv2.imwrite(str(file_path), img)
                #if img is saved in folder
                if saved:
                    print(f"Saved: {file_path.name}")
                #if not
                else:
                    print(f"Failed To Save: {file_path.name}")
        if frame_count >= 300:
            break
        #Quit the display
        if key & 0xFF == ord("q"):
            break
    cap.release() #Close Video
    cv2.destroyAllWindows() # Release Memory
    