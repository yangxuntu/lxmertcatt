# The name of this experiment.
name=$2

# Save logs and models under snap/vqa; make backup.
output=snap/vqa/fb3/Epoch20/$name
mkdir -p $output/src
cp -r src/* $output/src/
cp $0 $output/run.bash

# See Readme.md for option details.
CUDA_VISIBLE_DEVICES=$1 PYTHONPATH=$PYTHONPATH:./src \
    python src/tasks/vqa.py \
    --train train,nominival --valid minival  \
    --llayers 9 --xlayers 5 --rlayers 5 \
    --loadLXMERTQA snap/pretrain/fb3/Epoch20 \
    --batchSize 32 --optim bert  \
    --MV_size 800 --ML_size 800 \
    --lr_schedule warmup_linear_yx --lr 5e-5 --lr_min 0 --epochs 4 \
    --tqdm --output $output --bert_type ft ${@:3}

# output=snap/vqa/ft20/$name
#--loadLXMERTQA snap/pretrain/ftlxmert/Epoch20 \
