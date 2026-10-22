from ultralytics import YOLO
import cv2
from pathlib import Path
from ultralytics.engine.results import Results
import numpy


model_name = "yolo11n"
frame_choose = 30
input_video = Path(f"raw/data/test.mp4")
output_folder = Path(f"outputs/detection/{model_name}/video_frame_{frame_choose}")
model = YOLO(f"models/{model_name}.pt")
output_folder.mkdir(parents=True, exist_ok=True)


def predict(img):
    predictions = list(model.predict(
        source=img,
        conf=0.25,
        imgsz=640,
        classes=[0],
        device="cpu",
        save=False,
        stream=False,
        verbose=False
    ))

    result = predictions[0]
    if not isinstance(result, Results):
        raise TypeError("Expected an Ultralytics Results object")

    annotated_img = result.plot()
    return annotated_img

def main():
    
    cap = cv2.VideoCapture(str(input_video))

    if cap.isOpened():
        print(f"Ready to process video : {input_video}  With model :  {model_name}")
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        cv2.namedWindow("DetectionFootBallVideo", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("DetectionFootBallVideo", 900, 640)
    while True:
        success, img = cap.read()

        if not success:
            break
        detect_img = predict(img)

        cv2.imshow("DetectionFootBallVideo", detect_img)

        key = cv2.waitKey(frame_choose)


        if key & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


