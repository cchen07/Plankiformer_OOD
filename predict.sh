#!/bin/bash -l

python predict_labeled.py -test_path /home/EAWAG/chenchen/data/train_data/new/new_split_CNN/0_test/ -test_outpath /home/EAWAG/chenchen/out/predict_out/Zoo_CNN_01/ -main_param_path /home/EAWAG/kyathasr/DEPLOY/Zoo_Nov2022_OUT/ -model_path /home/EAWAG/kyathasr/DEPLOY/Zoo_Nov2022_OUT/trained_models/CNN_zoo_01/ -ensemble 0 -finetuned 2 -threshold 0.0 -use_gpu yes