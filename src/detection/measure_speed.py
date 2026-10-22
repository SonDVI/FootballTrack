"""Measure YOLO processing time on saved frames, without GUI or image saving."""

import argparse
import csv
from pathlib import Path
from statistics import mean

from ultralytics import YOLO
from ultralytics.engine.results import Results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", choices=["yolo11n", "yolo11s"], default="yolo11n")
    parser.add_argument("--interval", type=int, choices=[15, 30, 60], default=60)
    args = parser.parse_args()

    # Resolve paths from this script so the working directory does not matter.
    project_root = Path(__file__).resolve().parents[2]
    weights_path = project_root / "models" / f"{args.model}.pt"
    input_folder = project_root / "outputs/frames" / f"every_{args.interval}"
    output_folder = (
        project_root / "outputs/speed" / args.model / f"every_{args.interval}"
    )
    image_paths = sorted(
        input_folder.glob("*_frame.jpg"),
        key=lambda path: int(path.stem.split("_")[0]),
    )
    if not weights_path.is_file():
        raise FileNotFoundError(f"Model weights not found: {weights_path}")
    if not image_paths:
        raise FileNotFoundError(f"No frame images found in: {input_folder}")

    model = YOLO(str(weights_path))

    def predict(image_path):
        predictions = list(model.predict(
            source=str(image_path),
            conf=0.25,
            imgsz=640,
            classes=[0],
            device="cpu",
            save=False,
            stream=False,
            verbose=False,
        ))
        result = predictions[0]
        if not isinstance(result, Results):
            raise TypeError("Expected an Ultralytics Results object")
        return result

    # One warm-up prediction; its timings are excluded from the report.
    print(f"Warm-up: {args.model} on CPU")
    predict(image_paths[0])

    rows = []
    for image_path in image_paths:
        result = predict(image_path)
        timings = {}
        for stage in ("preprocess", "inference", "postprocess"):
            value = result.speed.get(stage)
            if value is None:
                raise ValueError(f"Missing {stage} timing for {image_path.name}")
            timings[f"{stage}_ms"] = float(value)

        row = {"frame": image_path.name, **timings}
        row["total_ms"] = sum(timings.values())
        rows.append(row)
        print(
            f"{image_path.name}: inference={row['inference_ms']:.2f} ms, "
            f"total={row['total_ms']:.2f} ms"
        )

    # These CSV files are replaced when rerunning the same model and interval.
    output_folder.mkdir(parents=True, exist_ok=True)
    with (output_folder / "per_frame.csv").open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    summary = {
        "model": args.model,
        "interval": args.interval,
        "device": "cpu",
        "conf": 0.25,
        "imgsz": 640,
        "classes": "person (0)",
        "frame_count": len(rows),
        "warmup_runs": 1,
    }
    for column in ("preprocess_ms", "inference_ms", "postprocess_ms", "total_ms"):
        summary[f"mean_{column}"] = mean(row[column] for row in rows)

    with (output_folder / "summary.csv").open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(summary))
        writer.writeheader()
        writer.writerow(summary)

    print(f"Mean total processing: {summary['mean_total_ms']:.2f} ms/image")
    print(f"Reports saved in: {output_folder}")
    print("Timings exclude disk image loading, plotting, display and output saving.")


if __name__ == "__main__":
    main()
