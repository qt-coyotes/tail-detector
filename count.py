#!/usr/bin/env python3
import os
import json

ann_count = 0
image_count = 0

for json_file in filter(lambda x: x.endswith('.json'), os.listdir('json_files')):
    with open(f"json_files/{json_file}", 'r') as f:
        js = json.load(f)

    area_name = json_file.split('.')[0]

    ann_c = len(js['annotations'])
    image_c = len(js['images'])

    print(f"{area_name}: {ann_c}/{image_c}")
    ann_count += ann_c
    image_count += image_c

print(f"====\nTotal annotations: {ann_count}/{image_count}")
