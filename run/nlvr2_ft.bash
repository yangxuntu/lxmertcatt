# The name of this experiment.
name=$2

# Save logs and models under snap/nlvr2; Make backup.
output=snap/nlvr2/nfsb2/Epoch20/$name
mkdir -p $output/src
cp -r src/* $output/src/
cp $0 $output/run.bash

# See run/Readme.md for option details.
CUDA_VISIBLE_DEVICES=$1 PYTHONPATH=$PYTHONPATH:./src \
    python src/tasks/nlvr2.py \
    --train train --valid valid \
    --llayers 9 --xlayers 5 --rlayers 5 \
    --loadLXMERT snap/pretrain/nfsb2/Epoch20 \
    --MV_size 500 --ML_size 500 \
    --bert_type ft_same \
    --batchSize 32 --optim bert --lr $3 --epochs 4 \
    --tqdm --multiGPU --output $output ${@:4}

