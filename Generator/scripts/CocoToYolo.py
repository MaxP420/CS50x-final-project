from pathlib import Path
import json

import paths


def load_coco(coco_file_path):
    with open(coco_file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_category_mapping(coco_data):
    image_map = {}

    for image in coco_data["images"]:
        image_map[image["id"]] = {
            "file_name": image["file_name"],
            "width": image["width"],
            "height": image["height"],
        }

    return image_map


def group_annotations_by_image(coco_data):
    annotations_by_image = {}

    for annotation in coco_data["annotations"]:
        image_id = annotation["image_id"]
        annotations_by_image.setdefault(image_id, []).append(annotation)

    return annotations_by_image


def convert_coco_to_yolo(annotation, image_width, image_height):
    x_min, y_min, box_width, box_height = annotation["bbox"]

    center_x = x_min + box_width / 2
    center_y = y_min + box_height / 2

    x_norm = center_x / image_width
    y_norm = center_y / image_height
    w_norm = box_width / image_width
    h_norm = box_height / image_height

    return [x_norm, y_norm, w_norm, h_norm]


def norm_classes(annotations_by_image, category_id_to_index):
    for annotations in annotations_by_image.values():
        for annotation in annotations:
            class_id = int(annotation["category_id"])
            annotation["category_id"] = category_id_to_index[class_id]


def write_yolo_labels(image_map, annotations_by_image):
    paths.YOLO_LABELS_DIR.mkdir(parents=True, exist_ok=True)

    for image_id, image_info in image_map.items():
        image_file_stem = Path(image_info["file_name"]).stem
        label_path = paths.YOLO_LABELS_DIR / f"{image_file_stem}.txt"

        lines = []
        for annotation in annotations_by_image.get(image_id, []):
            class_id = int(annotation["category_id"])
            bbox = convert_coco_to_yolo(annotation, image_info["width"], image_info["height"])
            lines.append(f"{class_id} {bbox[0]:.6f} {bbox[1]:.6f} {bbox[2]:.6f} {bbox[3]:.6f}")

        label_path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def main():
    category_id_to_index = {
        1: 0,
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
    }

    coco_file_path = paths.COCO_PATH
    coco_data = load_coco(coco_file_path)
    image_map = build_category_mapping(coco_data)
    annotations_by_image = group_annotations_by_image(coco_data)

    norm_classes(annotations_by_image, category_id_to_index)
    write_yolo_labels(image_map, annotations_by_image)

    with open(paths.OUTPUT_DIR / "yolo.json", "w", encoding="utf-8") as output:
        json.dump(annotations_by_image, output, indent=4)


if __name__ == "__main__":
    main()
