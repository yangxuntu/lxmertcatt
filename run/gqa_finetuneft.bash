# The name of this experiment.
name=$2

# Save logs and models under snap/gqa; make backup.
output=snap/gqa/fb4/Epoch20/$name
mkdir -p $output/src
cp -r src/* $output/src/
cp $0 $output/run.bash

# See Readme.md for option details.
CUDA_VISIBLE_DEVICES=$1 PYTHONPATH=$PYTHONPATH:./src \
    python src/tasks/gqa.py \
    --train train,valid --valid testdev \
    --llayers 9 --xlayers 5 --rlayers 5 \
    --loadLXMERTQA snap/pretrain/fb4/Epoch20 \
    --MV_size 800 --ML_size 800 \
    --bert_type ft\
    --batchSize 32 --optim bert --lr 5e-6 --epochs 4 \
    --tqdm --output $output ${@:3}
