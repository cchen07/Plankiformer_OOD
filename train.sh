#!/bin/bash -l

# export CUDA_VISIBLE_DEVICES=1

python3 main.py -datapaths /home/EAWAG/chenchen/data/train_data/new/training_zooplankton_new_220823/ -outpath /home/EAWAG/chenchen/out/train_out/densenet/ -classifier multi -aug -datakind image -ttkind image -save_data yes -resize_images 1 -L 128 -valid_set yes -test_set yes -dataset_name zoolake -training_data False -epochs 800 -finetune 2 -finetune_epochs 200 -balance_weight yes -batch_size 8 -init_name Init_0 -run_cnn_or_on_colab yes -use_gpu yes -architecture densenet -last_layer_finetune yes -gpu_id 1 -compute_extrafeat no -resume_from_saved yes