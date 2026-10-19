from pathlib import Path
from ultralytics.engine.results import Results


import cv2
from ultralytics import YOLO
# Run this file from the FootBallTrack project root.
output_folder = Path("outputs/detection/yolo11n/every_30")
output_folder.mkdir(parents=True, exist_ok=True)




model = YOLO("models/yolo11n.pt")
folder = Path("outputs/frames/every_30")
image_paths = sorted(
    folder.glob("*_frame.jpg"),
    key=lambda p: int(p.stem.split("_")[0])
)

index = 0
while index < len(image_paths):
    image_path = image_paths[index]
    index += 1

for image_path in image_paths:
    if not image_path.is_file():
        raise FileNotFoundError(f"Input image not found: {image_path}")
    output_path = output_folder / image_path.name
    if output_path.exists():
        continue
    results = list(model.predict(
        source=str(image_path),
        conf=0.25,
        imgsz=640,
        classes=[0],
        device="cpu",
        save=False,
        stream=False
    ))

    result = results[0]
    if not isinstance(result, Results):
        raise TypeError("Expected an Ultralytics Results object")
    print(type(result))

    annotated_img = result.plot()

    cv2.namedWindow("Detection",cv2.WINDOW_NORMAL)

    cv2.resizeWindow("Detection", 960, 540)

    cv2.imshow("Detection", annotated_img)
    k = cv2.waitKey(0)
    if k & 0xFF == ord("q"):
        break
    saved = cv2.imwrite(str(output_path), annotated_img)
    if saved:
        print(f"Save: {output_path}")
    else:
        print(f"Failed to save: {output_path}")



cv2.destroyAllWindows()