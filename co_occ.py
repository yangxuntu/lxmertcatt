import sys
import csv
import base64
import time
import numpy as np
import json

csv.field_size_limit(sys.maxsize)
FIELDNAMES = ["img_id", "img_h", "img_w", "objects_id", "objects_conf",
              "attrs_id", "attrs_conf", "num_boxes", "boxes", "features"]

data = []
start_time = time.time()
fname = '/data2/yangxu/lxmert/data/mscoco_imgfeat/train2014_obj36.tsv'

print("Start to load Faster-RCNN detected objects from %s" % fname)
n = 0

with open(fname) as f:
    reader = csv.DictReader(f, FIELDNAMES, delimiter="\t")
    for i, item in enumerate(reader):

        for key in ['img_h', 'img_w', 'num_boxes']:
            item[key] = int(item[key])

        boxes = item['num_boxes']
        decode_config = [
            ('objects_id', (boxes,), np.int64),
            ('objects_conf', (boxes,), np.float32),
            ('attrs_id', (boxes,), np.int64),
            ('attrs_conf', (boxes,), np.float32),
        ]
        for key, shape, dtype in decode_config:
            item[key] = np.frombuffer(base64.b64decode(item[key]), dtype=dtype)
            item[key] = item[key].reshape(shape)
            item[key].setflags(write=False)
        data.append(item)
        if len(data) == 10:
            break
with open('co_occ.json', 'w') as outfile:
    json.dump(data, outfile)








