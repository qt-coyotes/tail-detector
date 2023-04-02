#!/usr/bin/env python3
import os
import json
import itertools
import cv2 as cv
from pathlib import Path

input_file = "RowlandF.json"
image_dir = "mvzip"
is_half = True

for json_file in filter(lambda x: x.endswith('json'), os.listdir('json_files')):
    print(f"==== {json_file} ====")
    with open(f"json_files/{json_file}", "r") as f:
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

    with open(f"filtered_jsons/{json_file}", 'w') as f:
        json.dump(bboxes, f, indent=4, sort_keys=True)

    print("Success")
