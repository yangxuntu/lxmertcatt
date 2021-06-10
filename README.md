# The Most Important Thing.
## Our code is developed based on:
## LXMERT: Learning Cross-Modality Encoder Representations from Transformers (https://github.com/airsplay/lxmert)
## If you think our work is useful, please also cite their work!

## Introduction
PyTorch code for the CVPR 2021 paper ["Causal Attention for Vision-Language Tasks"](https://arxiv.org/pdf/2103.03493.pdf). 
PyTorch code for the CVPR 2021 paper ["Causal Attention for Vision-Language Tasks"](https://arxiv.org/pdf/2103.03493.pdf). Slides of our EMNLP 2019 talk are avialable [here](http://www.cs.unc.edu/~airsplay/EMNLP_2019_LXMERT_slides.pdf). 
For experiment settings, like the pytorch version and GPU setting, please refer to LXMERT (https://github.com/airsplay/lxmert)

## Results 36 RoI version

| Split            | [VQA](https://visualqa.org/)     | [GQA](https://cs.stanford.edu/people/dorarad/gqa/)     | [NLVR2](http://lil.nlp.cornell.edu/nlvr/)  |
|-----------       |:----:   |:---:    |:------:|
| Local Validation | 70.40%  | 60.90%  | 76.40% |
| Test-Dev         | 72.81%  | 60.84%  | 76.40% (Test-P) |
| Test-Standard    | 73.04%  | 61.17%  | 76.00% (Test-U) |

## Results 64 RoI version 
## Extracting more RoI visual features from an image will largely improve the performances!

| Split            | [VQA](https://visualqa.org/)     | [GQA](https://cs.stanford.edu/people/dorarad/gqa/)     | [NLVR2](http://lil.nlp.cornell.edu/nlvr/)  |
|-----------       |:----:   |:---:    |:------:|
| Test-Dev         | 73.54%  | 61.87%  | 77.27% (Test-P) |
| Test-Standard    | 73.63%  | 62.07%  | 77.23% (Test-U) |

## Pre-training
## Notice that this part is the same as LXMERT: https://github.com/airsplay/lxmert. We put them here for self-containing.

1. Download the aggregated LXMERT dataset from MS COCO, Visual Genome, VQA, and GQA (around 700MB in total). The joint answer labels are saved in `data/lxmert/all_ans.json`.
    ```bash
    mkdir -p data/lxmert
    wget --no-check-certificate https://nlp1.cs.unc.edu/data/lxmert_data/lxmert/mscoco_train.json -P data/lxmert/
    wget --no-check-certificate https://nlp1.cs.unc.edu/data/lxmert_data/lxmert/mscoco_nominival.json -P data/lxmert/
    wget --no-check-certificate https://nlp1.cs.unc.edu/data/lxmert_data/lxmert/vgnococo.json -P data/lxmert/
    wget --no-check-certificate https://nlp1.cs.unc.edu/data/lxmert_data/lxmert/mscoco_minival.json -P data/lxmert/
    ```

2. Download the detection features from MS COCO images from LXMERT.
    ```bash
    mkdir -p data/mscoco_imgfeat
    wget --no-check-certificate https://nlp1.cs.unc.edu/data/lxmert_data/mscoco_imgfeat/train2014_obj36.zip -P data/mscoco_imgfeat
    unzip data/mscoco_imgfeat/train2014_obj36.zip -d data/mscoco_imgfeat && rm data/mscoco_imgfeat/train2014_obj36.zip
    wget --no-check-certificate https://nlp1.cs.unc.edu/data/lxmert_data/mscoco_imgfeat/val2014_obj36.zip -P data/mscoco_imgfeat
    unzip data/mscoco_imgfeat/val2014_obj36.zip -d data && rm data/mscoco_imgfeat/val2014_obj36.zip
    ```

3. Download the detection features for Visual Genome images.
    ```bash
    mkdir -p data/vg_gqa_imgfeat
    wget --no-check-certificate https://nlp1.cs.unc.edu/data/lxmert_data/vg_gqa_imgfeat/vg_gqa_obj36.zip -P data/vg_gqa_imgfeat
    unzip data/vg_gqa_imgfeat/vg_gqa_obj36.zip -d data && rm data/vg_gqa_imgfeat/vg_gqa_obj36.zip
    ```

4. Test on a small split of the MS COCO + Visual Genome datasets:
    ```bash
    bash run/lxmert_pretrain.bash 0,1,2,3 --multiGPU --tiny
    ```

5. Run on the whole [MS COCO](http://cocodataset.org) and [Visual Genome](https://visualgenome.org/) related datasets (i.e., [VQA](https://visualqa.org/), [GQA](https://cs.stanford.edu/people/dorarad/gqa/index.html), [COCO caption](http://cocodataset.org/#captions-2015), [VG Caption](https://visualgenome.org/), [VG QA](https://github.com/yukezhu/visual7w-toolkit)). 

## This part is ours:
The pre-training code is:
```bash
bash run/fsb2.bash 0,1,2,3 --multiGPU
```
After pre-training, the finetuning codes for VQA, GQA, and NLVE2 are:
```bash
bash run/vqa_finetuneft.bash 0 0.00004 0.00004
bash run/gqa_finetuneft.bash 0 0.000001 0.000001
bash run/nlvr2_ft.bash 0 0.00003 0.00003
```

    
