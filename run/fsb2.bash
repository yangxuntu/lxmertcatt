# The name of experiment
name=fsb2

# Create dirs and make backup
output=snap/pretrain/$name
mkdir -p $output/src
cp -r src/* $output/src/
cp $0 $output/run.bash

# Pre-training
CUDA_VISIBLE_DEVICES=$1 PYTHONPATH=$PYTHONPATH:./src \
    python src/pretrain/lxmert_pretrain2.py \
    --taskMaskLM --taskObjPredict --taskMatched --taskQA \
    --visualLosses obj,attr,feat \
    --wordMaskRate 0.15 --objMaskRate 0.15 \
    --train mscoco_train,mscoco_nominival,vgnococo --valid mscoco_minival \
    --llayers 9 --xlayers 5 --rlayers 5 \
    --batchSize 196 --optim bert --lr 5e-5 --epochs 20 \
    --MV_size 500 --ML_size 500 \
    --tqdm --output $output --bert_type ft_same --multiGPU ${@:2}

