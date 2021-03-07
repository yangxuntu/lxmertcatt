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

submit_data = json.load(open('/home/yangxu/data/lxmert/data/gqa/submit.json'))
fsb2_submit = json.load(open('/home/yangxu/data/lxmert/data/gqa/fsb2ep204.json'))
nfsb2_submit = json.load(open('/home/yangxu/data/lxmert/data/gqa/gqa_submit.json'))



test_file = 'data/vg_gqa_imgfeat/vg_gqa_obj36.tsv'
for item in submit_data:
    all_id.append(item['img_id'])


with open(test_file) as f:
    test_reader = csv.DictReader(f, FIELDNAMES, delimiter="\t")
    for i, item in enumerate(test_reader):
        if i % 1000 == 0:
            print(i)
        index = (item['img_id'] in all_id)
        if index == False:
            print('missing image:{0}'.format(item['img_id']))

