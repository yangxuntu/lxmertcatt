import json

import numpy as np
from torch.utils.data import Dataset

import csv
import sys
csv.field_size_limit(sys.maxsize)

FIELDNAMES = ["img_id", "img_h", "img_w", "objects_id", "objects_conf",
              "attrs_id", "attrs_conf", "num_boxes", "boxes", "features"]

id_file = 'data/vg_gqa_imgfeat/gqa_testdev_obj36.tsv'
coco_file = 'data/mscoco_imgfeat/test2015_obj64.tsv'
outfile = 'data/vg_gqa_imgfeat/gqa_testdev_obj64.tsv'
all_id = []
all_id_number = []
coco_data = []

with open(coco_file) as f:
    coco_reader = csv.DictReader(f, FIELDNAMES, delimiter="\t")
    for i, item in enumerate(coco_reader):
        if i % 1000 == 0:
            print(i)
        coco_data.append(item)
        all_id_number.append(int(item['img_id'][14:]))

with open(outfile, 'w') as tsvfile:
    writer = csv.DictWriter(tsvfile, delimiter='\t', fieldnames=FIELDNAMES)
    with open(id_file) as f:
        id_reader = csv.DictReader(f, FIELDNAMES, delimiter="\t")
        for i, item in enumerate(id_reader):
            nlvr2_id = item['img_id']
            nlvr2_id_number=int(nlvr2_id[1:])
            index_id = all_id_number.index(nlvr2_id_number)
            coco_datum=coco_data[index_id]
            coco_datum['img_id'] = item['img_id']
            writer.writerow(coco_datum)
