#!/usr/bin/env python3
import json
import itertools
import cv2 as cv
from pathlib import Path

input_file = "RowlandF.json"
image_dir = "mvzip"

with open(input_file, "r") as f:
    js = json.load(f)

bboxes = dict()
# Looks like the below, where images withou an annotation are None
# image_path (str): bbox[]

for image in js["images"]:
    image_id = image["id"]

    for annotation in js["annotations"]:
        if annotation["image_id"] == image_id:
            bboxes[image["file_name"]] = annotation["bbox"]
            break

i = iter(bboxes.items())

for i, (key, bbox) in enumerate(itertools.islice(bboxes.items(), 3, 33, 3)):
    p = Path(image_dir) / input_file.split(".")[0] / key

    bbox = [int(b)//2 for b in bbox]
    image = cv.imread(str(p))
    image = cv.resize(image, (image.shape[1]//2, image.shape[0]//2))
    print(bbox)

    image = cv.rectangle(
        image,
        (bbox[0], bbox[1]),
        (bbox[0] + bbox[2], bbox[1] + bbox[3]),
        (0, 0, 255),
        3,
    )

    cv.imshow(f"coyote{i}", image)

    print(p)

while cv.waitKey(0) != ord("q"):
    pass
